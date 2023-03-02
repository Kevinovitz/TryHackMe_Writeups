<p align="center">
   <img src="https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/windows10privesc/Windows_PrivEsc_Cover.png" alt="Windows PrivEsc Logo">
</p>

# Windows PrivEsc

This guide contains the answer and steps necessary to get to them for the [Windows PrivEsc](https://tryhackme.com/room/windows10privesc) room.

## Table of contents

- [Generate a Reverse Shell Executable](#generate-a-reverse-shell-executable)
- [Service Exploits - Insecure Service Permissions](#service-exploits--insecure-service-permissions)
- [Service Exploits - Unquoted Service Path](#service-exploits--unquoted-service-path)
- [Service Exploits - Weak Registry Permissions](#service-exploits--weak-registry-permissions)
- [Service Exploits - Insecure Service Executables](#service-exploits--insecure-service-executables)
- [Registry - AutoRuns](#registry--autoruns)
- [Registry - AlwaysInstallElevated](#registry--alwaysinstallelevated)
- [Passwords - Registry](#passwords--registry)
- [Passwords - Saved Creds](#passwords--saved-creds)
- [Passwords - Security Account Manager (SAM)](#passwords--security-account-manager-sam)
- [Passwords - Passing the Hash](#passwords--passing-the-hash)
- [Scheduled Tasks](#scheduled-tasks)
- [Insecure GUI Apps](#insecure-gui-apps)
- [Startup Apps](#startup-apps)
- [Token Impersonation - Rogue Potato](#token-impersonation--rogue-potato)
- [Token Impersonation - PrintSpoofer](#token-impersonation--printspoofer)
- [Privilege Escalation Scripts](#privilege-escalation-scripts)

### Generate a Reverse Shell Executable



 Generate a reverse shell executable and transfer it to the Windows VM. Check that it works!


### Service Exploits - Insecure Service Permissions



1. What is the original BINARY_PATH_NAME of the daclsvc service?

   

   ><details><summary>Click for answer</summary></details>

### Service Exploits - Unquoted Service Path



1. What is the BINARY_PATH_NAME of the unquotedsvc service?

   

   ><details><summary>Click for answer</summary></details>

### Service Exploits - Weak Registry Permissions



Read and follow along with the above.


### Service Exploits - Insecure Service Executables




Read and follow along with the above.


### Registry - AutoRuns




Read and follow along with the above.

### Registry - AlwaysInstallElevated




Read and follow along with the above.

### Passwords - Registry



1. What was the admin password you found in the registry?

   

   ><details><summary>Click for answer</summary></details>

### Passwords - Saved Creds



Read and follow along with the above.

### Passwords - Security Account Manager (SAM)



1. What is the NTLM hash of the admin user?
   
   

   ><details><summary>Click for answer</summary></details>

### Passwords - Passing the Hash



Read and follow along with the above. 

### Scheduled Tasks



Read and follow along with the above. 

### Insecure GUI Apps



Read and follow along with the above. 

### Startup Apps



Read and follow along with the above. 

### Token Impersonation - Rogue Potato



1. Name one user privilege that allows this exploit to work.



   ><details><summary>Click for answer</summary></details>

2. Name the other user privilege that allows this exploit to work.

   

   ><details><summary>Click for answer</summary></details>

### Token Impersonation - PrintSpoofer



Read and follow along with the above.

### Privilege Escalation Scripts



xperiment with all four tools, running them with different options. Do all of them identify the techniques used in this room? 
