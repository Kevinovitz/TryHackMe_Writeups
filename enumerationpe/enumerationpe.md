![Enumeration Banner](https://tryhackme-images.s3.amazonaws.com/user-uploads/5f04259cf9bf5b57aed2c476/room-content/ace5bb9cb9c1120a09d88620adb2976b.png)

<p align="center">
   <img src="https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/enumerationpe/Enumeration_Cover.png" alt="Enumeration Logo">
</p>

# Enumeration

This guide contains the answer and steps necessary to get to them for the [Enumeration](https://tryhackme.com/room/enumerationpe) room.

## Table of contents

- [Introduction](#introduction)
- [Purpose](#purpose)
- [Linux Enumeration](#linux-enumeration)
- [Windows Enumeration](#windows-enumeration)
- [DNS, SMB, and SNMP](#dns,-smb,-and-snmp)
- [More Tools for Windows](#more-tools-for-windows)

### Introduction

1. What command would you use to start the PowerShell interactive command line?

   The answer can be found in the text.

   ><details><summary>Click for answer</summary>powershell.exe</details>

### Purpose

1. In SSH key-based authentication, which key does the client need?

   The answer can be found in the text.

   ><details><summary>Click for answer</summary></details>

### Linux Enumeration

1. What is the name of the Linux distribution used in the VM?

   Checking for release files gives us a file we should read.

   ```console
   ls -lh /etc/*-release

   cat /etc/os-release
   ```

   LINUX RELEASE

   ><details><summary>Click for answer</summary>Ubuntu</details>

2. What is its version number?

   This can be found with the previous command.

   ><details><summary>Click for answer</summary>20.04.4</details>

3. What is the name of the user who last logged in to the system?

   To get the last user logged into the system we run `last`.

   LINUX LAST

   ><details><summary>Click for answer</summary>randa</details>

4. What is the highest listening TCP port number?

   To get this we should use `netstat` together with 'ltn'. Otherwise it will resolve the ip and ports. Now we should get the numerical value.

   ```console
   netstat -lnt
   ```

   LINUX PORT

   ><details><summary>Click for answer</summary>6667</details>

5. What is the program name of the service listening on it?

   To get the program associated with the port, we nust add '-p' and run netstat with sudo.

   ```console
   sudo netstat -lntp
   ```

   LINUX PROGRAM

   ><details><summary>Click for answer</summary>inspircd</details>

6. There is a script running in the background. Its name starts with THM. What is the name of the script?

   To list running programs and filter on the script we can use:

   ```console
   ps -aux | grep THM
   ```

   LINUX SCRIPT

   ><details><summary>Click for answer</summary>THM-24765.sh</details>

### Windows Enumeration

1. What is the full OS Name?

   Use `systeminfo` to find this information.

   WINDOWS INFO

   ><details><summary>Click for answer</summary>Microsoft Windows Server 2019 Datacenter</details>

2. What is the OS Version?

   This can be found with the previous command.

   ><details><summary>Click for answer</summary>10.0.17763</details>

3. How many hotfixes are installed on this MS Windows Server?

   We can use `wmic` for this.

   ```console
   wmic qfe get Caption,Description

   wmic qfe get Caption,Description | Measure-Object -Line
   ```

   The second command should give us the amount of updates applied. We must however subtract one from this number as it will include the column header.

   WINDOWS UPDATES

   ><details><summary>Click for answer</summary></details>

4. What is the lowest TCP port number listening on the system?

   For this we should use `netstat`. Use -n to list the numerical values.

   WINDOWS PORTS

   ><details><summary>Click for answer</summary>22</details>

5. What is the name of the program listening on that port?

   In the previous image we can see the binary that is associated with that port.

   ><details><summary>Click for answer</summary>sshd.exe</details>

### DNS, SMB, and SNMP

1. Knowing that the domain name on the MS Windows Server of IP 10.10.150.82 is redteam.thm, use dig to carry out a domain transfer. What is the flag that you get in the records?

   The dig command must be executed on the attackbox itself.

   ```console
   dig -t AXFR redteam.thm @10.10.223.16
   ```

   DNS FLAG

   ><details><summary>Click for answer</summary>THM{DNS_ZONE}</details>

2. What is the name of the share available over SMB protocol and starts with THM?

   To see the available shares, we can use `net share`.

   SMB SHARES

   ><details><summary>Click for answer</summary>THM{829738}</details>

3. Knowing that the community string used by the SNMP service is public, use snmpcheck to collect information about the MS Windows Server of IP 10.10.150.82. What is the location specified?

   Again, this command will be run on our attackbox.

   ```console
   snmpcheck 10.10.223.16 -c public
   ```

   SNMP CHECK

   ><details><summary>Click for answer</summary>THM{SNMP_SERVICE}</details>
   
### More Tools for Windows

1. What utility from Sysinternals Suite shows the logged-in users?

   The answers can be found in the text.
   
   ><details><summary>Click for answer</summary>PsLoggedOn</details>
