![Hacking with PowerShell Banner](https://assets.tryhackme.com/additional/banners/powershell.png)

<p align="center">
   <img src="https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/powershell/Hacking_Powershell_Cover.png" alt="Hacking with PowerShell Logo">
</p>

# Hacking with PowerShell

This guide contains the answer and steps necessary to get to them for the [Hacking with PowerShell](https://tryhackme.com/room/powershell) room.

## Table of contents

- [What is Powershell?](#what-is-powershell?)
- [Basic Powershell Commands](#basic-powershell-commands)
- [Enumeration](#enumeration)
- [Basic Scripting Challenge](#basic-scripting-challenge)
- [Intermediate Scripting ](#intermediate-scripting)

### What is Powershell?

1. What is the command to get a new object?

   We will use a verb to describe what we want to do and then a noun describing what we want to do it to.

   ><details><summary>Click for answer</summary>get-new</details>

### Basic Powershell Commands

1. What is the location of the file "interesting-file.txt"

   For this we can use 'Get-ChildItem' and specify the path and filename we want to look for.
   
   ```cmd
   Get-ChildItem -Path C:\ -Recurse -File -Include *interesting-file* -ErrorAction SilentlyContinue
   ```
   
   BASIC COMMANDS LOCATION

   ><details><summary>Click for answer</summary>C:\Program FIles</details>

3. Specify the contents of this file

   Viewing the contents can be done with the 'Get-Content' command.
   
   ```cmd
   Get-Content -Path "C:\Program Files\interesting-file.txt.txt"
   ```
   
   BASIC COMMANDS CONTENT

   ><details><summary>Click for answer</summary>notsointerestingcontent</details>

5. How many cmdlets are installed on the system(only cmdlets, not functions and aliases)?

   'Get-Command' can be used to view the installed cmdlets. However, we must also filter to only show cmdlets. This can be done by piping the output to 'Where-Object'.
   
   ```cmd
   Get-Command | Where-Object -Property CommandType -eq Cmdlet | Measure
   ```
   
   BASIC COMMANDS CMDLETS

   ><details><summary>Click for answer</summary>6638</details>

7. Get the MD5 hash of interesting-file.txt

   The file hash can be obtained using 'Get-FileHash'.
   
   ```cmd
   Get-FileHash -Algorithm MD5 -Path "C:\Program Files\interesting-file.txt.txt"
   ```
   
   BASIC COMMANDS HASH

   ><details><summary>Click for answer</summary>49A586A2A9456226F8A1B4CEC6FAB329</details>

9. What is the command to get the current working directory?
   
   BASIC COMMANDS DIRECTORY

   ><details><summary>Click for answer</summary>Get-Location</details>

11. Does the path "C:\Users\Administrator\Documents\Passwords" Exist (Y/N)?

   We can simply try to view the contents of this directory to see if it exists.
   
   ```cmd
   Get-ChildItem -Path "C:\Users\Administrator\Documents\Passwords"
   ```
   
   BASIC COMMANDS EXIST

   ><details><summary>Click for answer</summary>N</details>

11. What command would you use to make a request to a web server?

   Using 'Get-Command' we can look for the correct command.
   
   BASIC COMMANDS REQUEST

   ><details><summary>Click for answer</summary>Invoke-WebRequest</details>

11. Base64 decode the file b64.txt on Windows. 

   After getting the contents of the file, we can decode the base64 encoded string using CyberChef.
   
   ```cmd
   Get-ChildItem -Path C:\ -File -Recurse -Include *b64.txt -ErrorAction SilentlyContinue
    Get-Content C:\Users\Administrator\Desktop\b64.txt
   ```
   
   BASIC COMMANDS B64

   BASIC COMMANDS FLAG

   ><details><summary>Click for answer</summary>ihopeyoudidthisonwindows</details>

### Enumeration

1. How many users are there on the machine?



   ><details><summary>Click for answer</summary></details>

2. Which local user does this SID(S-1-5-21-1394777289-3961777894-1791813945-501) belong to?



   ><details><summary>Click for answer</summary></details>

3. How many users have their password required values set to False?



   ><details><summary>Click for answer</summary></details>

4. How many local groups exist?



   ><details><summary>Click for answer</summary></details>

5. What command did you use to get the IP address info?



   ><details><summary>Click for answer</summary></details>

6. How many ports are listed as listening?



   ><details><summary>Click for answer</summary></details>

7. What is the remote address of the local port listening on port 445?



   ><details><summary>Click for answer</summary></details>

8. How many patches have been applied?



   ><details><summary>Click for answer</summary></details>

9. When was the patch with ID KB4023834 installed?



   ><details><summary>Click for answer</summary></details>

10. Find the contents of a backup file.



   ><details><summary>Click for answer</summary></details>

11. Search for all files containing API_KEY



   ><details><summary>Click for answer</summary></details>

12. What command do you do to list all the running processes?



   ><details><summary>Click for answer</summary></details>

13. What is the path of the scheduled task called new-sched-task?



   ><details><summary>Click for answer</summary></details>

14. Who is the owner of the C:\



   ><details><summary>Click for answer</summary></details>

### Basic Scripting Challenge

1. What file contains the password?



   ><details><summary>Click for answer</summary></details>

2. What is the password?



   ><details><summary>Click for answer</summary></details>

3. What files contains an HTTPS link?



   ><details><summary>Click for answer</summary></details>

### Intermediate Scripting 

1. How many open ports did you find between 130 and 140(inclusive of those two)?



   ><details><summary>Click for answer</summary></details>
