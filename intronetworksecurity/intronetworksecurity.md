![Network Security Banner](https://assets.tryhackme.com/room-banners/intro-to-offensive-security.png)

<p align="center">
   <img src="https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/intronetworksecurity/Network_Security_Cover.png" alt="Network Security Logo">
</p>

# Network Security

This guide contains the answer and steps necessary to get to them for the [Network Security](https://tryhackme.com/room/intronetworksecurity) room.

## Table of contents

- [Introduction](#introduction)
- [Methodology](#methodology)
- [Practical Example of Network Security](#practical-example-of-network-security)

### Introduction

1. What type of firewall is Windows Defender Firewall?

   As the Windows Defender Firewall is a software tool, it is a host firewall as the text suggests.

   ><details><summary>Click for answer</summary>Host firewall</details>

### Methodology

1. During which step of the Cyber Kill Chain does the attacker gather information about the target? 

   This would be during the first step. The name can be found in the text.

   ><details><summary>Click for answer</summary>Recon</details>

### Practical Example of Network Security

In this task, we will look at a practical example of the Cyber Kill Chain.

1. What is the password in the secret.txt file?

   After an nmap scan with `nmap -sV 10.10.39.25`, we find various services that are open.
   
   ![Nmap](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/intronetworksecurity/Network_Security_Nmap.png)
   
   One of them is FTP. We can try to log in with anonymous credentials.
   
   ```cmd
   ftp anonymous@10.10.39.25
   ```
   
   ![FTP Login](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/intronetworksecurity/Network_Security_FTP_Login.png)
   
   Looks like anonymous login was indeed enabled. We can now download the file we find using `get`. However, downloading multiple files can be down easier.
   
   ```cmd
   wget *.*
   ```
   
   ![FTP Download](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/intronetworksecurity/Network_Security_FTP_Download.png)
   
   The txt and epub files didn't contain anything interesting for us. The secret.txt file, however, seems to have a passwordt.
   
   ![Secret Files](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/intronetworksecurity/Network_Security_Secret_Files.png)

   ><details><summary>Click for answer</summary>ABC789xyz123</details>

2. What is the content of the flag.txt in the /root directory?

   Maybe the password we found belongs to the root user. We can try and login through SSH.
   
   ```cmd
   ssh root@10.10.39.25
   ```
   
   ![SSH Root](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/intronetworksecurity/Network_Security_SSH_Root.png)
   
   Success! Now lets find the flag in the root folder.
   
   ![Root Flag](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/intronetworksecurity/Network_Security_Root_Flag.png)

   ><details><summary>Click for answer</summary>THM{FTP_SERVER_OWNED}</details>

3. What is the content of the flag.txt in the /home/librarian directory?

   Eventhough we known the username, we can look up the available accounts using `ls -lh /home`. Then we can navigate to that account and find the flag.
   
   ![User Flag](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/intronetworksecurity/Network_Security_User_Flag.png)

   ><details><summary>Click for answer</summary>THM{LIBRARIAN_ACCOUNT_COMPROMISED}</details>
