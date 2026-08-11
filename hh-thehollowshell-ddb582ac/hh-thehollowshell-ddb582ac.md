![The Hollow Shell Banner](https://cdn-images.tryhackme.com/room-icons/5dbea226085ab6182a2ee0f7-1785251767201)

<p align="center">
   <img src="https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/hh-thehollowshell-ddb582ac/The_Hollow_Shell_Cover.png" alt="The Hollow Shell Logo">
</p>

# <img src="https://cdn-images.tryhackme.com/room-icons/5dbea226085ab6182a2ee0f7-1785251823751" alt="image" style="vertical-align: middle;height: 50px;" /> The Hollow Shell

This guide contains the answer and steps necessary to get to them for the [The Hollow Shell](https://tryhackme.com/room/hh-thehollowshell-ddb582ac) room.

<h2>Table of contents</h2>

- [Task 1 - Hacker Holidays: Day 10](#task-1---hacker-holidays-day-10)

### Task 1 - Hacker Holidays: Day 10

1.  What is the flag?

    First lets perform some basic enumeration with `nmap` and `gobuster`.

    ```console
    nmap -sV -sC 10.113.128.148
    gobuster dir -u http://10.113.128.148:5000 -w /usr/share/wordlists/SecLists/Discovery/Web-Content/common.txt 
    ```

    ![Nmap](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/hh-thehollowshell-ddb582ac/The_Hollow_Shell_Nmap.png)

    ![Gobuster](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/hh-thehollowshell-ddb582ac/The_Hollow_Shell_Gobuster.png)

    Looks like we have a webserver on port 5000 redirecting to a login page. The upload endpoint cannot be used through the browser. So this is likely used in the upload process itself.

    ![Login](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/hh-thehollowshell-ddb582ac/The_Hollow_Shell_Login.png)

    Looks like they forgot to remove some credentials on the page source! Never underestimate the importance of looking through the page source.

    ![Display](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/hh-thehollowshell-ddb582ac/The_Hollow_Shell_Display.png)

    Looks like we can upload a file here. It must be a zip file. But maybe we can trick the system into accepting a php file instead.

    Unfortunately, we cannot upload a reverse shell as 'shell.zip.php'. So we must create the archive as it is requesting.

    

    ><details><summary>Click for answer</summary></details>





![](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/hh-thehollowshell-ddb582ac/The_Hollow_Shell_.png)
![](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/hh-thehollowshell-ddb582ac/The_Hollow_Shell_.png)
![](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/hh-thehollowshell-ddb582ac/The_Hollow_Shell_.png)
![](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/hh-thehollowshell-ddb582ac/The_Hollow_Shell_.png)
