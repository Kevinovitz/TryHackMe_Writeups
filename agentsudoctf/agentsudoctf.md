![Agent Sudo Banner](https://tryhackme.com/img/banners/default_tryhackme.png)

<p align="center">
   <img src="https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/agentsudoctf/Agent_Sudo_Cover.png" alt="Agent Sudo Logo">
</p>

# Agent Sudo

This guide contains the answer and steps necessary to get to them for the [Agent Sudo](https://tryhackme.com/room/agentsudoctf) room.

## Table of contents

- [Enumerate](#enumerate)
- [Hash cracking and brute-force](#hash-cracking-and-brute-force)
- [Capture the user flag](#capture-the-user-flag)
- [Privilege escalation ](#privilege-escalation)

### Enumerate

**IP Adress:** 10.10.203.242

1. How many open ports?

   nmap -sV 10.10.203.242


   ><details><summary>Click for answer</summary>3</details>

2. How you redirect yourself to a secret page?

   Another way is to use curl -A "User-agent"

   ><details><summary>Click for answer</summary>user-agent</details>

3. What is the agent name?



   ><details><summary>Click for answer</summary>chris</details>

### Hash cracking and brute-force



1. FTP password

   hydra -l chris -P /usr/share/wordlists/rockyou.txt ftp://10.10.203.242 -t 4


   ><details><summary>Click for answer</summary>crystal</details>

2. Zip file password



   ><details><summary>Click for answer</summary></details>

3. steg password



   ><details><summary>Click for answer</summary></details>

4. Who is the other agent (in full name)?



   ><details><summary>Click for answer</summary></details>

5. SSH password



   ><details><summary>Click for answer</summary></details>

### Capture the user flag



1. What is the user flag?



   ><details><summary>Click for answer</summary></details>

2. What is the incident of the photo called?



   ><details><summary>Click for answer</summary></details>

### Privilege escalation 



1. CVE number for the escalation 



   ><details><summary>Click for answer</summary></details>

2. What is the root flag?



   ><details><summary>Click for answer</summary></details>

3. (Bonus) Who is Agent R?



   ><details><summary>Click for answer</summary></details>
