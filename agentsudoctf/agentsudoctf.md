![Agent Sudo Banner](https://tryhackme.com/img/banners/default_tryhackme.png)

<p align="center">
   <img src="https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/agentsudoctf/Agent_Sudo_Cover.png" alt="Agent Sudo Logo">
</p>

# Agent Sudo

This guide contains the answer and steps necessary to get to them for the [Agent Sudo](https://tryhackme.com/room/agentsudoctf) room.

## Table of contents

- [Enumerate](#enumerate)
- [Hash cracking and brute-force](#hash-cracking-and-brute-force)
- [Capture the user flag](#capture-the-user-flag)
- [Privilege escalation ](#privilege-escalation)

### Enumerate

In this task, we will find more information about the machine and see if we can access the hidden page.

**IP Adress:** 10.10.203.242

1. How many open ports?

   To find the open ports on the machine we can use nmap.
   
   ```cmd
   nmap -sV 10.10.203.242
   ```
   
   ![Nmap Scan](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/agentsudoctf/Agent_Sudo_Nmap_Scan.png)

   ><details><summary>Click for answer</summary>3</details>

2. How you redirect yourself to a secret page?

   When we visit the website on port 80, we see the following page:
   
   ![Webpage](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/agentsudoctf/Agent_Sudo_Web_Page.png)
   
   Apparently we can visit this secret page by using the correct codename as the 'user-agent' value in our browser. Judging from the Agent R codename, this might be single letter from the alphabet. Instead of trying each one by one, we can use Burpsuite. We can use the build-in browser from Burpsuite or we can use the FoxyProxy plugin to use Firefox.
   
   ![Foxy Proxy](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/agentsudoctf/Agent_Sudo_Foxy_Proxy.png)
   
   Then we need to make sure 'intercept' is turned on in the Burpsuite Proxy tool.
   
   ![Burp Suite Config](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/agentsudoctf/Agent_Sudo_Burp_Suite_Config.png)
   
   After refreshing the page in Firefox, it is intercepted in Burpsuite. Now we can substitue `r` as our user-agent to test if this works. The forward the requests untill the page loads.
   
   ![Burp Suite Agent R](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/agentsudoctf/Agent_Sudo_Burp_Suite_Agent_R.png)
   
   ![Web Page R](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/agentsudoctf/Agent_Sudo_Web_Page_R.png)
   
   Looks like we are indeed looking for a letter from the alphabet as our code name, but R is not one of them. Lets use Burpsuite's Intruder tool.
   
   Refresh the page again in Firefox and send the request to Intruder in Burpsuite. 
   
   ![Burp Suite Intruder](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/agentsudoctf/Agent_Sudo_Burp_Suite_To_Intruder.png)
   
   Remove the use-agent value and replace it with two payload symbols.
   
   ![Burp Suite Intruder Config](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/agentsudoctf/Agent_Sudo_Burp_Suite_Intruder_Config.png)
   
   In the payloads tab, add all letters one by one or with a file containing them all. Then start the attack.
   
   ![Burp Suite Intruder Payload](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/agentsudoctf/Agent_Sudo_Burp_Suite_Intruder_Payload.png)
   
   From the results we can see one name stand out from the rest with a different length.
   
   ![Burp Suite Results](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/agentsudoctf/Agent_Sudo_Burp_Suite_Results.png)
   
   Lets return to the Proxy tool and substitute 'C' for our code name. And forward in to the browser.
   
   ![Burp Suite Agent C](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/agentsudoctf/Agent_Sudo_Burp_Suite_Agent_C.png)
   
   ![Burp Suite Webpage](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/agentsudoctf/Agent_Sudo_Burp_Suite_Web_Page_C.png)

   Bingo!
   
   Another way is to use `curl -A "<User-agent>" <address>`

   ><details><summary>Click for answer</summary>user-agent</details>

3. What is the agent name?

   From the note on this secret page we can find their full name.

   ><details><summary>Click for answer</summary>chris</details>

### Hash cracking and brute-force

Now that we have more information on the system, we will try to force our way into the machine in this task. 

1. FTP password

   To get the ftp password we will need Hydra as anonymous login is not enabled. We know the username we can try, so using the following command we can guess the password:
   
   ```cmd
   hydra -l chris -P /usr/share/wordlists/rockyou.txt ftp://10.10.203.242 -t 4
   ```
   
   ![FTP Password](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/agentsudoctf/Agent_Sudo_FTP_Password.png)

   ><details><summary>Click for answer</summary>crystal</details>

2. Zip file password

   Now that we have the ftp password we can login.
   
   ![Cracking FTP Login](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/agentsudoctf/Agent_Sudo_Cracking_FTP_Login.png)
   
   Lets see which files are available and download them to our machine using `mget *.*`.
   
   ![Cracking FTP Download](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/agentsudoctf/Agent_Sudo_Cracking_FTP_Download.png)
   
   The two images don't tell us much at this point. The text file, however, gives us some clues as to what we might need to do next.
   
   ![Cracking Text File](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/agentsudoctf/Agent_Sudo_Cracking_Text_File.png)
   
   Lets start with the jpg file. Using steghide we stry to find anything hidden, but unfortunately we need a passphrase and the png file doesn't seem to give us contain anything. Using strings does give us some clues that something is hidden inside.
   
   ```cmd
   strings cutie.png
   ```
   
   ![Cracking PNG Strings](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/agentsudoctf/Agent_Sudo_Cracking_PNG_strings.png)
   
   We can try using `binwalk` to get anything from it.
   
   ```cmd
   binwalk cutie.png -e
   ```
   
   ![Cracking Extract Image](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/agentsudoctf/Agent_Sudo_Cracking_Extract_Image.png)
   
   Looks like there are some files and a zip archive hidden inside. Looking at the text file and the other two files gives us nothing. Neither when using `file` or `strings`. The zip file on the other hand does seem to contain a note. However, it is password protected. We can use `fcrackzip` to try a crack the password
   
   ```cmd
   fcrackzip -v -u -D -p /usr/share/wordlists/rockyou.txt _cutie.png.extracted/8702.zip
   ```
   
   ![Cracking Fcracking](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/agentsudoctf/Agent_Sudo_Cracking_Fcrackzip.png)
   
   Unfortunately, it couldn't find the password. Next thing to try is `john`. But we first need to create a hash from the zipfile using `zip2john`. Then we can use it in John.
   
   ```cmd
   zip2john _cutie.png.extracted/8702.zip > ziphash.txt
   
   john ziphash.txt --wordlist=/usr/share/wordlists/rockyou.txt
   ```
   
   ![Cracking Zip John](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/agentsudoctf/Agent_Sudo_Cracking_Zip_John.png)
   
   With the password found, we can open the textfile and read its contents.
   
   ![Cracking Zip Message](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/agentsudoctf/Agent_Sudo_Cracking_Zip_Message.png)
   
   The name seems to be base64 encoded. Using Cyberchef this gives us Area51.
   
   ![Cracking Cyberchef](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/agentsudoctf/Agent_Sudo_Cracking_CyberChef.png)

   ><details><summary>Click for answer</summary>alien</details>

3. steg password

   To get to the hidden information in the png file above, we need the passphrase. Another method we can try is stegseek.
   
   ```cmd
   stegseek --crack -sf cute-alien.jpg -wl /usr/share/wordlists/rockyou.txt 
   ```
   
   ![Cracking Steg Text](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/agentsudoctf/Agent_Sudo_Cracking_Steg_Text.png)
   
   Looks like it indeed found the passphrase. We could confirm this with steghide if we wanted.
   
   ><details><summary>Click for answer</summary>Area51</details>

4. Who is the other agent (in full name)?

   The name can be found in hidden text file in the image file.
   
   ![Cracking Steg Message](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/agentsudoctf/Agent_Sudo_Cracking_Steg_Message.png)

   ><details><summary>Click for answer</summary>James</details>

5. SSH password

   The SSH password can also be found in the hidden note in the jpg image.

   ><details><summary>Click for answer</summary>hackerrules!</details>

### Capture the user flag

In this task we will found out what we can find by logging in through SSH and find the flag.

1. What is the user flag?

   Using username chris and the password we found doesn't allow us to log in with SSH. James, however, does work.
   
   ```cmd
   ssh james@10.10.186.39
   ```
   
   ![Capture SSH Login](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/agentsudoctf/Agent_Sudo_Capture_SSH_Login.png)
   
   Looking through the directory we can see the user flag and read its contents.
   
   ![Capture User Flag](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/agentsudoctf/Agent_Sudo_Capture_User_Flag.png)

   ><details><summary>Click for answer</summary>b03d975e8c92a7c04146cfa7a5a313c7</details>

2. What is the incident of the photo called?

   We can download the image through `scp`.
   
   ```cmd
   scp james@10.10.186.39:/home/james/Alien_autospy.jpg Alien_autospy.jpg 
   ```
   
   ![Capture  Download Image SSH](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/agentsudoctf/Agent_Sudo_Capture_Download_Image_SSH.png)
   
   ![Capture SSH Image](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/agentsudoctf/Agent_Sudo_Capture_SSH_Image.png)
   
   Looks like there is some kind of alien laying on a table. Lets do a reverse image search to find out more about the picture.

   ![Capture Reverse Search](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/agentsudoctf/Agent_Sudo_Capture_Image_Reverse_Search.png)
   
   ![Capture Image Event](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/agentsudoctf/Agent_Sudo_Capture_Image_Event.png)

   Looks like we found the event this image is from.
   
   ><details><summary>Click for answer</summary>Roswell alien autopsy</details>

### Privilege escalation 

In this final task we will attempt to gain root access to the machine. 

1. CVE number for the escalation 

   First we need to find out what we can abuse. To start we can look at which binaries we are allowed to run with sudo.
   
   ```cmd
   sudo -l
   ```

   ![Privesc Permissions](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/agentsudoctf/Agent_Sudo_Privesc_Permissions.png)
   
   Unfortunately, it seems we can't run bash as root.
   
   ```cmd
   sudo /bin/bash
   ```
   
   ![Privesc Sudo Bash](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/agentsudoctf/Agent_Sudo_Privesc_Sudo_Bash.png)
   
   Lets check what the version of sudo is before continueing.
   
   ```cmd
   sudo -V
   ```
   
   ![Privesc Sudo Version](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/agentsudoctf/Agent_Sudo_Privesc_Sudo_Version.png)
   
   After an online search we come across an exploit we can use.   
   
   ![Privesc Sudo Exploit](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/agentsudoctf/Agent_Sudo_Privesc_Sudo_Exploit.png)

   ><details><summary>Click for answer</summary>CVE-2019-14287</details>

2. What is the root flag?

   The exploit page from the previous question gives us the command we need to run to get root access.
   
   ```cmd
   sudo -u#-1 /bin/bash
   ```
   
   ![Privesc Sudo Root](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/agentsudoctf/Agent_Sudo_Privesc_Sudo_Root.png)
   
   Once we are in, we can look for and read the root flag.
   
   ![Privesc Root Flag](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/agentsudoctf/Agent_Sudo_Privesc_Root_Flag.png)

   ><details><summary>Click for answer</summary>b53a02f55b57d4439e3341834d70c062</details>

3. (Bonus) Who is Agent R?

   In the not left by the author we can see who Agent R really is.

   ><details><summary>Click for answer</summary>DesKel</details>
