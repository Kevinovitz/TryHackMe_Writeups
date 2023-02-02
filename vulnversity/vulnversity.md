<p align="center">
   <img src="https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/vulnversity/Vulnversity_Logo.png" alt="Vulnversity Logo">
</p>

# Vulnversity

This guide contains the answer and steps necessary to get to them for the [Vulnversity](https://tryhackme.com/room/vulnversity) room.

## Table of contents

- [Reconnaissance](#reconnaissance)
- [Locating directories using GoBuster](#locating-directories-using-gobuster)
- [Compromise the webserver](#compromise-the-webserver)
- [Privilege Escalation](#privilege-escalation)

## [Reconnaissance]()


2. Scan the box, how many ports are open?
   
   
   
   ><details><summary>Click for answer</summary>6</details>
   
3. What version of the squid proxy is running on the machine?



   ><details><summary>Click for answer</summary>3.5.12</details>

4. How many ports will nmap scan if the flag -p-400 was used?



   ><details><summary>Click for answer</summary>400</details>

5. Using the nmap flag -n what will it not resolve?



   ><details><summary>Click for answer</summary>DNS</details>

6. What is the most likely operating system this machine is running?



   ><details><summary>Click for answer</summary>Ubuntu</details>

7. What port is the web server running on?



   ><details><summary>Click for answer</summary>3333</details>
   
## [Locating directories using GoBuster]()


2. What is the directory that has an upload form page?



   ><details><summary>Click for answer</summary>/internal/</details>

## [Compromise the webserver]()


1. What common file type, which you'd want to upload to exploit the server, is blocked? Try a couple to find out.



   ><details><summary>Click for answer</summary>.php</details>

3. Run this attack, what extension is allowed?



   ><details><summary>Click for answer</summary>.phtml</details>

5. What is the name of the user who manages the webserver?



   ><details><summary>Click for answer</summary>bill</details>

6. What is the user flag?



   ><details><summary>Click for answer</summary>8bd7992fbe8a6ad22a63361004cfcedb</details>

## [Privilege Escalation]

1. On the system, search for all SUID files. What file stands out?



   ><details><summary>Click for answer</summary>/bin/systemctl</details>

2. Become root and get the last flag (/root/root.txt)



   ><details><summary>Click for answer</summary>a58ff8579f0a9270368d33a9966c7fd5</details>
