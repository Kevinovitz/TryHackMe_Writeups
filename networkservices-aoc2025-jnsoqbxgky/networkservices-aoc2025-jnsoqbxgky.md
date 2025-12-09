![Network Discovery - Scan-ta Clause Banner](https://tryhackme-images.s3.eu-west-1.amazonaws.com/room-icons/678ecc92c80aa206339f0f23-1762176251102)

<p align="center">
   <img src="https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/networkservices-aoc2025-jnsoqbxgky/Network_Discovery_-_Scan-ta_Clause_Cover.png" alt="Network Discovery - Scan-ta Clause Logo">
</p>

# <img src="https://tryhackme-images.s3.amazonaws.com/room-icons/678ecc92c80aa206339f0f23-1761778821176" alt="image" style="vertical-align: middle;height: 50px;" /> Network Discovery - Scan-ta Clause | Advent of Cyber 2025 - Day 7

This guide contains the answer and steps necessary to get to them for the [Network Discovery - Scan-ta Clause](https://tryhackme.com/room/networkservices-aoc2025-jnsoqbxgky) room.

## Table of contents

- [Discover Network Services](#discover-network-services)

### Discover Network Services

1.  What evil message do you see on top of the website?

    We can do an nmap scan of the server to find any exposed applications.

    ```cmd
    nmap -sV -p- 10.82.172.20 --script=banner
    ```

    This will run a stealth scan on all ports and display some more information about any exposed servies.

    ![Scan](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/networkservices-aoc2025-jnsoqbxgky/Network_Discovery_-_Scan-ta_Clause_Scan.png)

    We can see there is a webserver active on port 80. This should be viewable in the browser.

    The answer can be found by navigating to the application hosted on the compromised server '10.82.172.20'.

    ![Message](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/networkservices-aoc2025-jnsoqbxgky/Network_Discovery_-_Scan-ta_Clause_Message.png)

    ><details><summary>Click for answer</summary>Pwned by HopSec</details>

2.  What is the first key part found on the FTP server?

    Another service we found to be of interest is an FTP server on port 21212.

    We can connect to the server using `ftp 10.82.172.20 21212`. Use 'anonymous' as login name.

    We can now look through the directory and download any interesting files.

    ```cmd
    ls
    get tbfc_qa_key1 - 
    ```

    ![Key1](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/networkservices-aoc2025-jnsoqbxgky/Network_Discovery_-_Scan-ta_Clause_Key1.png)

    ><details><summary>Click for answer</summary>3aster_</details>

3.  What is the second key part found in the TBFC app?

    The app can be found on port 25251. Our best bet is to use netcat `nc` to connect to it. Doing so we can use the help command to find any handy commands.

    Looks like there is a simple command to get the key. Lets use that!

    ```cmd
    nc 10.82.172.20 25251
    HELP
    GET KEY
    ```

    ![Key2](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/networkservices-aoc2025-jnsoqbxgky/Network_Discovery_-_Scan-ta_Clause_Key2.png)

    ><details><summary>Click for answer</summary>15_th3_</details>

4.  What is the third key part found in the DNS records?

    For this key we will take a look at any open ports using UDP.

    ```cmd
    nmap -sU 10.82.172.20
    ```

    ![Scan2](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/networkservices-aoc2025-jnsoqbxgky/Network_Discovery_-_Scan-ta_Clause_Scan2.png)

    We can see there is a service on port 53, which is usually used by DNS. Lets query it with the given command.

    ```cmd
    dig @10.81.184.96 TXT key3.tbfc.local +short
    ```

    ![Key3](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/networkservices-aoc2025-jnsoqbxgky/Network_Discovery_-_Scan-ta_Clause_Key3.png)

    Here we are given our third key in return.

    ><details><summary>Click for answer</summary>n3w_xm45</details>

5.  Which port was the MySQL database running on?

    Now that we have our three keys we can unlock the dashboard.

    ![Website](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/networkservices-aoc2025-jnsoqbxgky/Network_Discovery_-_Scan-ta_Clause_Website.png)

    Combine all three keys and add them to the box. Now we should get access to the secret terminal.

    ![Unlock](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/networkservices-aoc2025-jnsoqbxgky/Network_Discovery_-_Scan-ta_Clause_Unlock.png)

    Here we can run `ss -tulnp` to list its open ports.

    ![Console](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/networkservices-aoc2025-jnsoqbxgky/Network_Discovery_-_Scan-ta_Clause_Console.png)

    We can see the default MySQL port is open.

    ><details><summary>Click for answer</summary>3306</details>

6.  Finally, what's the flag you found in the database?

    To enumerate the database, we will use `mysql`. Since we are logged into the host, we shouldn't need to autheticate to the database and can directly access it. We are given the database name to use.

    ```cmd
    mysql -D tbfcqa01
    show tables;
    select * from flags;
    ```

    ![Flag](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/networkservices-aoc2025-jnsoqbxgky/Network_Discovery_-_Scan-ta_Clause_Flag.png)

    ><details><summary>Click for answer</summary>THM{4ll_s3rvice5_d1sc0vered}</details>

7.  If you enjoyed today's room, feel free to check out theNmap: The Basicsroom.
