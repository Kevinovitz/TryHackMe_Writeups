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




### Abusing Service Misconfigurations




### Abusing dangerous privileges




### Abusing vulnerable software




### Tools of the Trade 



1. 

   

   ><details><summary>Click for answer</summary></details>
