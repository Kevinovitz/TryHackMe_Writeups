![Kenobi Banner](https://i.imgur.com/zWNY3JF.png)

<p align="center">
   <img src="https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/kenobi/ROOM_TITLE_Cover.png" alt="Kenobi Logo">
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



   ><details><summary>Click for answer</summary></details>

2. Scan the machine with nmap, how many ports are open?



   ><details><summary>Click for answer</summary></details>

### Enumerating Samba for shares

1. Using nmap we can enumerate a machine forSMBshares.Nmaphas the ability to run to automate a wide variety of networking tasks. There is a script to enumerate shares!nmap -p 445 --script=smb-enum-shares.nse,smb-enum-users.nse MACHINE_IPSMBhas two ports, 445 and 139.Using the nmap command above, how many shares have been found?



   ><details><summary>Click for answer</summary></details>

2. On most distributions ofLinuxsmbclient is already installed. Lets inspect one of the shares.smbclient //MACHINE_IP/anonymousUsing your machine, connect to the machines network share.Once you're connected, list the files on the share. What is the file can you see?



   ><details><summary>Click for answer</summary></details>

3. You can recursively download theSMBshare too. Submit the username and password as nothing.smbget -R smb://MACHINE_IP/anonymousOpen the file on the share. There is a few interesting things found.Information generated for Kenobi when generating anSSHkey for the userInformation about the ProFTPD server.What port isFTPrunning on?



   ><details><summary>Click for answer</summary></details>

4. Your earlier nmap port scan will have shown port 111 running the service rpcbind. This is just a server that converts remote procedure call (RPC) program number into universal addresses. When an RPC service is started, it tells rpcbind the address at which it is listening and the RPC program number its prepared to serve.In our case, port 111 is access to a network file system. Lets use nmap to enumerate this.nmap -p 111 --script=nfs-ls,nfs-statfs,nfs-showmount MACHINE_IPWhat mount can we see?



   ><details><summary>Click for answer</summary></details>

### Gain initial access with ProFtpd

1. Lets get the version of ProFtpd. Use netcat to connect to the machine on theFTPport.What is the version?



   ><details><summary>Click for answer</summary></details>

2. We can use searchsploit to find exploits for a particular software version.Searchsploit is basically just a command line search tool for exploit-db.com.How many exploits are there for the ProFTPd running?



   ><details><summary>Click for answer</summary></details>

3. You should have found an exploit from ProFtpd'smod_copy module.The mod_copy module implementsSITE CPFRandSITE CPTOcommands, which can be used to copy files/directories from one place to another on the server. Any unauthenticated client can leverage these commands to copy files from anypart of the filesystem to a chosen destination.We know that theFTPservice is running as the Kenobi user (from the file on the share) and an ssh key is generated for that user.



   ><details><summary>Click for answer</summary></details>

4. We're now going to copyKenobi's private key using SITE CPFR and SITE CPTO commands.We knew that the /var directory was a mount we could see (task 2, question 4). So we've now moved Kenobi's private key to the /var/tmp directory.



   ><details><summary>Click for answer</summary></details>

5. Lets mount the /var/tmp directory to our machinemkdir /mnt/kenobiNFSmount MACHINE_IP:/var /mnt/kenobiNFSls -la /mnt/kenobiNFSWe now have a network mount on our deployed machine! We can go to /var/tmp and get the private key then login to Kenobi's account.What is Kenobi's user flag (/home/kenobi/user.txt)?



   ><details><summary>Click for answer</summary></details>

### Privilege Escalation with Path Variable Manipulation

1. SUID bits can be dangerous, some binaries such as passwd need to be run with elevated privileges (as its resetting your password on the system), however other custom files could that have the SUID bit can lead to all sorts of issues.To search the a system for these type of files run the following:find / -perm -u=s -type f 2>/dev/nullWhat file looks particularly out of the ordinary?



   ><details><summary>Click for answer</summary></details>

2. Run the binary, how many options appear?



   ><details><summary>Click for answer</summary></details>

3. Strings is a command onLinuxthat looks for human readable strings on a binary.This shows us the binary is running without a full path (e.g. not using /usr/bin/curl or /usr/bin/uname).As this file runs as the root users privileges, we can manipulate our path gain a root shell.We copied the /bin/sh shell, called it curl, gave it the correct permissions and then put its location in our path. This meant that when the /usr/bin/menu binary was run, its using our path variable to find the "curl" binary.. Which is actually a version of /usr/sh, as well as this file being run as root it runs our shell as root!



   ><details><summary>Click for answer</summary></details>

4. What is the root flag (/root/root.txt)?



   ><details><summary>Click for answer</summary></details>

