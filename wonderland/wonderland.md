![Wonderland Banner](https://i.imgur.com/q9N2UUs.png)

<p align="center">
   <img src="https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/wonderland/Wonderland_Cover.png" alt="Wonderland Logo">
</p>

# Wonderland

This guide contains the answer and steps necessary to get to them for the [Wonderland](https://tryhackme.com/room/wonderland) room.

### Capture the Flags

1. Obtain the flag in user.txt

   Lets start with an nmap scan to enumerate the machine.

   ```cmd
   sudo nmap -sS -sV 10.10.249.20 -O
   ```

   NMAP

   This gives us two open ports, 22 for SSH and 80 for a webserver. This we can see when accessing the IP in our browser.

   HOMEPAGE

   Now we can also enumerate the directories of the webserver with `gobuster`.

   ```cmd
   gobuster dir -u http://10.10.249.20/ -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -x php,html,txt
   ```

   GOBUSTER

   We have three directories which are of interest. /r, /img, and /poem.

   /img we also found looking at the source code of the webpage. It links us to a page with the stored images.

   SOURCECODE

   IMAGES

   Lets download these images and see if we can find anything usefull hidden inside them. For this, I will be using `binwalk`, `strings`, `exiftool`, and `steghide`.

   None of these came up with anything interesting except for `steghide`. Apparently, there is something hidden inside the rabbit image.

   ```cmd
   steghide extract -sf white_rabbit_1.jpg 
   ```

   RABBIT HINT

   It tells us to follow the "r a b b i t". This was also placed on the webpage, but not with the spacing. That might be something of use. /r was namely a directory found by gobuster. My guess is that it would have found the other, single character, directories. And trying them manually didn't give us anything.

   So it must be something else. Using "/r a b b i t" didn't work either. But /r (as found by `gobuster` gives us some text.

   R

   What if we add the characters as a subfolder?

   RA

   This seems to be working. Navigating all the way down to "/r/a/b/b/i/t" we are greeted with more text and an image.

   RABBIT

   Looking at the source code again, we find some hidden message.

   RABBIT SOURCE

   Looking at the wording, this might be credentials. Maybe for an SSH user? Sure enough that seems to work!

   SSH

   Looking through our folder, we don't see a `user.txt` file, rather a `root.txt` file. This is quite odd. We also have a python file. 

   Furthermore, we have three different user folder that could be of interest.

   We can also see that we have execute permissions for the /root folder, which is strange. This means we can look at files/folders within /root if we have permission.

   PERMISSIONS

   Usually, the user.txt file would be in the user folder and the root.txt file in the root folder. Although not clear, the hint might give us a clue here. Perhaps the user.txt file can be found (and read) in the root folder.

   ```cmd
   ls -lh /root/user.txt
   ```

   It appears the file is indeed located in the root folder and we infact do have permission to read it.

   FLAG   

   ><details><summary>Click for answer</summary>thm{"Curiouser and curiouser!"}</details>

3. + 20 - Escalate your privileges, what is the flag in root.txt?



   PEAS CVE

   PEAS CAPABILITIES

   SUDO_L

   PYTHON_SCRIPT

   RANDOM

   TEAPARTY

   PATH

   HATTER

   PERL

   ROOT




sudo -u rabbit /usr/bin/python3.6 /home/alice/walrus_and_the_carpenter.py 

import os
os.system("/bin/bash")


#!/bin/bash
/bin/bash


chmod +x date



  
   ><details><summary>Click for answer</summary>thm{Twinkle, twinkle, little bat! How I wonder what you’re at!}</details>
