![The Lay of the Land Banner](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/thelayoftheland/Lay_Of_The_Land_Banner.png)

<p align="center">
   <img src="https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/thelayoftheland/Lay_Of_The_Land_Cover.png" alt="The Lay of the Land Logo">
</p>

# The Lay of the Land

This guide contains the answer and steps necessary to get to them for the [The Lay of the Land](https://tryhackme.com/room/thelayoftheland) room.

## Table of contents

- [Active Directory (AD) environment](#active-directory-ad-environment)
- [Users and Groups Management](#users-and-groups-management)
- [Host Security Solution #1](#host-security-solution-1)
- [Applications and Services ](#applications-and-services)

### Active Directory (AD) environment

In order to check whether the Windows machine is part of the AD environment or not, one way, we can use the command prompt systeminfo command. The output of the systeminfo provides information about the machine, including the operating system name and version, hostname, and other hardware information as well as the AD domain.
Powershell

From the above output, we can see that the computer name is an AD with thmdomain.com as a domain name which confirms that it is a part of the AD environment. 

Note that if we get WORKGROUP in the domain section, then it means that this machine is part of a local workgroup.

1. Before going any further, ensure the attached machine is deployed and try what we discussed. Is the attached machine part of the AD environment? (Y|N)

   To get this info, we run `systeminfo` on the machine.

   ![AD Info](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/thelayoftheland/Lay_Of_The_Land_AD_Info.png)

   Here we can cleary see it is part of an AD. It is even the Domain Controller.

   ><details><summary>Click for answer</summary>Y</details>

3. If it is part of an AD environment, what is the domain name of the AD?

   With the previous command we can also see the specific domain it is a part of.

   ><details><summary>Click for answer</summary>thmredteam.com</details>

### Users and Groups Management

1. Use the Get-ADUser -Filter * -SearchBase command to list the available user accounts within THM OU in the thmredteam.com domain. How many users are available?

   Using powershell we can find all users in the THM OU.

   ```ps
   Get-ADUser -Filter * -SearchBase "OU=THM,DC=THMREDTEAM,DC=COM"
   ```

   ![Users Thm](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/thelayoftheland/Lay_Of_The_Land_Users_Thm.png)

   ><details><summary>Click for answer</summary>6</details>

2. Once you run the previous command, what is the UserPrincipalName (email) of the admin account?

   From the previous command we can get the email for the admin.

   ![Users Admin](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/thelayoftheland/Lay_Of_The_Land_Users_Admin.png)

   ><details><summary>Click for answer</summary>thmadmin@thmredteam.com</details>

### Host Security Solution #1

1. Enumerate the attached Windows machine and check whether the host-based firewall is enabled or not! (Y|N)

   Running the following command, we can check whether or not the firewall is running.

   ```ps
   Get-NetFirewallProfile | Format-Table Name, Enabled
   ```

   ![Host Firewall](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/thelayoftheland/Lay_Of_The_Land_Host_Firewall.png)

   ><details><summary>Click for answer</summary>N</details>

2. Using PowerShell cmdlets such Get-MpThreat can provide us with threats details that have been detected using MS Defender. Run it and answer the following: What is the file name that causes this alert to record?

   Using `Get-MpThreat` we can see a list of alerts. Some of them are related to the same file.

   ![Host Threat](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/thelayoftheland/Lay_Of_The_Land_Host_Threat.png)

   ><details><summary>Click for answer</summary>PowerView.ps1</details>

3. Enumerate the firewall rules of the attached Windows machine. What is the port that is allowed under the THM-Connection rule?

   There are many rules in the firewall, so it is best if we filter based on the given name.

   ```ps
   Get-NetFirewallRule | Where-Object -Property DisplayName -eq THM-Connection
   ```

   ![Host Port](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/thelayoftheland/Lay_Of_The_Land_Host_Port.png)

   ><details><summary>Click for answer</summary>17337</details>

In the next task, we will keep discussing the host security solution. I'm ready!

### Applications and Services 

1. Finally, we can see it is listening on port 8080. Now try to apply what we discussed and find the port number for THM Service. What is the port number?

   First we must check what the name of the specific service file is.

   ```ps
   wmic service where "name like 'THM Service' "get Name,PathName
   ```

   ![Applications Service Name](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/thelayoftheland/Lay_Of_The_Land_Applications_Service_Name.png)

   Now we can check if it is running and if so, what its id is.

   ```ps
   Get-Process -Name thm-service
   ```

   ![Applications Service Id](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/thelayoftheland/Lay_Of_The_Land_Applications_Service_Id.png)

   Finally we can check if it is listening on any ports.

   ```ps
   netstat -noa | findstr "LISTENING" | findstr "2848"
   ```

   ![Applications Service Port](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/thelayoftheland/Lay_Of_The_Land_Applications_Service_Port.png)

   ><details><summary>Click for answer</summary>13337</details>

2. Visit the localhost on the port you found in Question #1. What is the flag?

   We can visit this port in a browser at `localhost:13337`.

   ![Applications Flag](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/thelayoftheland/Lay_Of_The_Land_Applications_Flag.png)

   ><details><summary>Click for answer</summary>THM{S3rv1cs_1s_3numerat37ed</details>

3. Now enumerate the domain name of the domain controller, thmredteam.com, using the nslookup.exe, and perform a DNS zone transfer. What is the flag for one of the records?

   Performing the following commands should give us the flag.

   ```ps
   nslookup.exe
   server 10.10.91.103
   ls -d thmredteam.com
   ```

   ![Applications Dns](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/thelayoftheland/Lay_Of_The_Land_Applications_Dns.png)

   ><details><summary>Click for answer</summary>THM{DNS-15-Enumerated!}</details>
