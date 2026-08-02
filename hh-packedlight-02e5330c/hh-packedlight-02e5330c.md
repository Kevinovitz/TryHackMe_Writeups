![Packed Light Banner](https://cdn-images.tryhackme.com/room-icons/5dbea226085ab6182a2ee0f7-1785251384272)

<p align="center">
   <img src="https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/hh-packedlight-02e5330c/Packed_Light_Cover.png" alt="Packed Light Logo">
</p>

# <img src="https://cdn-images.tryhackme.com/room-icons/5dbea226085ab6182a2ee0f7-1785251388851" alt="image" style="vertical-align: middle;height: 50px;" /> Packed Light

This guide contains the answer and steps necessary to get to them for the [Packed Light](https://tryhackme.com/room/hh-packedlight-02e5330c) room.

## Table of contents

- [Task 1 - Hacker Holidays: Day 4](#task-1---hacker-holidays-day-4)

### Task 1 - Hacker Holidays: Day 4

1.  What is the flag?

    First we look at the statistics listed in Wireshark to find any low hanging fruit. We don’t get much, but we do see a couple of ip addresses that have been sending more data than others. 
 
    ![Statistics](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/hh-packedlight-02e5330c/Packed_Light_Statistics.png)
 
    Next thing to do, is looking at the objects we can export. In this file we only find http objects. File -> Export Objects -> HTTP.
 
    ![Objects](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/hh-packedlight-02e5330c/Packed_Light_Objects.png)
 
    Two items stand out. One is the python file and the other is a recurring file. Let’s download both of them. 
 
    The first file is an HTML file of the Byte Lotus Resort. 
 
    ![Page](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/hh-packedlight-02e5330c/Packed_Light_Page.png)
 
    This doesn’t give us much so we will look at the python file next. 
 
    ![Script](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/hh-packedlight-02e5330c/Packed_Light_Script.png)
 
    Looks like we struck gold. This script gives us a lot of information about what has been going on and how the data is encoded. Let’s look at each part. 
 
    This script seems to behave like a keylogger. Sending each keystroke to a remote server. 
    This is the remote server, data is being sent to. 
    This looks like a secret key that is used to encode the data. 
    Here we can see the process that is used to encode the data. Each keystroke is processed individually. This is important to remember when decoding. Data is first XOR encoded, then base 64 encoded. 
    The XOR encoding process used. 
    The data is added to the request header as part of the cookie. 
    The actual request with the headers and url. 
 
    This also tells us what we need to look for in the capture file. Let’s identify any traffic with “byte-lotus-resort” in the user-agent. 
 
    ```bash
    tcp.user-agent contains “byte-lotus-resort”
    ```
 
    ![Traffic](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/hh-packedlight-02e5330c/Packed_Light_Traffic.png)
 
    Here we indeed see that the cookie contains the data we are after. 
 
    Lets us use ‘Tshark’ to extract all these parts. 
 
    ```bash
    tshark -r traffic.pcapng -Y 'http.user_agent contains "ByteLotusClient"' -T fields -e http.cookie
    ```
 
    ![Output](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/hh-packedlight-02e5330c/Packed_Light_Output.png) 
 
    This works, but lets remove the padding and new lines to give us a single string
 
    ```bash
    tshark -r traffic.pcapng -Y 'http.user_agent contains "ByteLotusClient"' -T fields -e http.cookie | grep -oP 'hotel_sess_state=\K[^;]+' | sed 's/=*$//' | tr -d '\n'
    ```
       
    ![String](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/hh-packedlight-02e5330c/Packed_Light_String.png)
 
    Now is the time to remember that each keystroke is processed and sent individually. So we can’t create a single string and decode that. So let’s change the command to output all pieces including the padding. 
 
    ```bash
    tshark -r traffic.pcapng -Y 'http.user_agent contains "ByteLotusClient"' -T fields -e http.cookie | grep -oP 'hotel_sess_state=\K[^;]+'
    ```
 
    ![Data](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/hh-packedlight-02e5330c/Packed_Light_Data.png)
 
    Now we can create a python script that will decode each piece individually and then combine them into a single string. Each piece must first be base 64 decoded and then XOR decoded. 
 
    ```python
 
    ```
 
    ![Flag](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/hh-packedlight-02e5330c/Packed_Light_Flag.png)
 
    Success! We found our flag!

    ><details><summary>Click for answer</summary>THM{V3r4_1s_w4tch1ng_0veR_y0u}</details>

