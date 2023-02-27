<p align="center">
   <img src="https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/blaster/Blaster_Cover.png" alt="Blaster Logo">
</p>

# Blaster

This guide contains the answer and steps necessary to get to them for the [Blaster](https://tryhackme.com/room/blaster) room.

## Table of contents

- [Activate Forward Scanners and Launch Proton Torpedoes](#activate-forward-scanners-and-launch-proton-torpedoes)
- [Breaching the Control Room](#breaching-the-control-room)
- [Adoption into the Collective](#adoption-into-the-collective)

### Activate Forward Scanners and Launch Proton Torpedoes



1. How many ports are open on our target system?

   

   ><details><summary>Click for answer</summary></details>

2. Looks like there's a web server running, what is the title of the page we discover when browsing to it?

   

   ><details><summary>Click for answer</summary></details>

3. Interesting, let's see if there's anything else on this web server by fuzzing it. What hidden directory do we discover?

   

   ><details><summary>Click for answer</summary></details>

4. Navigate to our discovered hidden directory, what potential username do we discover?

   

   ><details><summary>Click for answer</summary></details>

5. Crawling through the posts, it seems like our user has had some difficulties logging in recently. What possible password do we discover?

   

   ><details><summary>Click for answer</summary></details>

6. Log into the machine via Microsoft Remote Desktop (MSRDP) and read user.txt. What are it's contents?

   

   ><details><summary>Click for answer</summary></details>

### Breaching the Control Room



1. When enumerating a machine, it's often useful to look at what the user was last doing. Look around the machine and see if you can find the CVE which was researched on this server. What CVE was it?

   

   ><details><summary>Click for answer</summary></details>

2. Looks like an executable file is necessary for exploitation of this vulnerability and the user didn't really clean up very well after testing it. What is the name of this executable?

   

   ><details><summary>Click for answer</summary></details>

*Research vulnerability and how to exploit it. Exploit it now to gain an elevated terminal!*

4. Now that we've spawned a terminal, let's go ahead and run the command 'whoami'. What is the output of running this?

   

   ><details><summary>Click for answer</summary></details>

5. Now that we've confirmed that we have an elevated prompt, read the contents of root.txt on the Administrator's desktop. What are the contents? Keep your terminal up after exploitation so we can use it in task four!

   

   ><details><summary>Click for answer</summary></details>

### Adoption into the Collective



*Return to your attacker machine for this next bit. Since we know our victim machine is running Windows Defender, let's go ahead and try a different method of payload delivery! For this, we'll be using the script web delivery exploit within Metasploit. Launch Metasploit now and select 'exploit/multi/script/web_delivery' for use.*

2. First, let's set the target to PSH (PowerShell). Which target number is PSH?

   

   ><details><summary>Click for answer</summary></details>

*After setting your payload, set your lhost and lport accordingly such that you know which port the MSF web server is going to run on and that it'll be running on the TryHackMe network.*

*Finally, let's set our payload. In this case, we'll be using a simple reverse HTTP payload. Do this now with the command: 'set payload windows/meterpreter/reverse_http'. Following this, launch the attack as a job with the command 'run -j'.*

*Return to the terminal we spawned with our exploit. In this terminal, paste the command output by Metasploit after the job was launched. In this case, I've found it particularly helpful to host a simple python web server (python3 -m http.server) and host the command in a text file as copy and paste between the machines won't always work. Once you've run this command, return to our attacker machine and note that our reverse shell has spawned. *

6. Last but certainly not least, let's look at persistence mechanisms via Metasploit. What command can we run in our meterpreter console to setup persistence which automatically starts when the system boots? Don't include anything beyond the base command and the option for boot startup. 

   

   ><details><summary>Click for answer</summary></details>

*Run this command now with options that allow it to connect back to your host machine should the system reboot. Note, you'll need to create a listener via the handler exploit to allow for this remote connection in actual practice. Congrats, you've now gain full control over the remote host and have established persistence for further operations!*
