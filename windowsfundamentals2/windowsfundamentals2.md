![Windows Fundamentals 2](https://assets.tryhackme.com/room-banners/windows.png)

<p align="center">
   <img src="https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/windowsfundamentals2/Windows_Fundamentals_2_Cover.png" alt="Windows Fundamentals 2 Logo">
</p>

# Windows Fundamentals 2

This guide contains the answer and steps necessary to get to them for the [Windows Fundamentals 2](https://tryhackme.com/room/windowsfundamentals2x0x) room.

### Table of Contents

- [System Configuration](#system-configuration)
- [Change UAC Settings](#change-uac-settings)
- [Computer Management](#computer-management)
- [System Information](#system-information)
- [Resource Monitor](#resource-monitor)
- [Command Prompt](#command-prompt)
- [Registry Editor ](#registry-editor)

### System Configuration

In this task we will be looking at the System Configuration utility which is used to help diagnose startup issues.

1. What is the name of the service that lists Systems Internals as the manufacturer?

   Opening the System Configuration utility we can get the answer in the Services tab.
   
   ![SysInternal Service](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/windowsfundamentals2/Windows_Fundamentals_2_SysInternal_Service.png)

   ><details><summary>Click for answer</summary>PsShutdown</details>

2. Whom is the Windows license registered to?

   For this answer we can open the about windows utility from the tools tab.
   
   ![License](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/windowsfundamentals2/Windows_Fundamentals_2_License.png)

   ><details><summary>Click for answer</summary>Windows User</details>

3. What is the command for Windows Troubleshooting?

   The answer can be found on the tools tab under windows troubleshooting.
   
   ![Troubleshotting](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/windowsfundamentals2/Windows_Fundamentals_2_Troubleshooting.png)

   ><details><summary>Click for answer</summary>C:\Windows\System32\control.exe /name Microsoft.Troubleshooting</details>

4. What command will open the Control Panel? (The answer is  the name of .exe, not the full path)

   The answer can be found on the tools tab under system properties.
   
   ![Control Panel](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/windowsfundamentals2/Windows_Fundamentals_2_Control_Panel.png)

   ><details><summary>Click for answer</summary>control.exe</details>

### Change UAC Settings

In this task we will look more at the user account control settings.

1.  What is the command to open User Account Control Settings? (The answer is the name of the .exe file, not the full path)

   This answer can be found on the tools tab of the system configuration utility under change uac settings.
   
   ![User Account Control](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/windowsfundamentals2/Windows_Fundamentals_2_User_Account_Control.png)

   ><details><summary>Click for answer</summary>UserAccountControlSettings.exe</details>

### Computer Management

In this task we will learn more information about the computer management utility.

1. What is the command to open Computer Management? (The answer is the name of the .msc file, not the full path)

   This answer can again be found on the tools tab of the system configuration utility under computer management.
   
   ![Computer Management](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/windowsfundamentals2/Windows_Fundamentals_2_Computer_Management.png)

   ><details><summary>Click for answer</summary>compmgmt.msc</details>

2. At what time every day is the GoogleUpdateTaskMachineUA task configured to run?

   In the Computer Management utility we can open the Task Scheduler and look for the Google Update task.
   
   ![Task Schedule](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/windowsfundamentals2/Windows_Fundamentals_2_Task_Schedule.png)

   ><details><summary>Click for answer</summary>6:15 AM</details>

3. What is the name of the hidden folder that is shared?
 
   This folder can be found under the Shared Folders tab.
   
   ![Shared Folder](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/windowsfundamentals2/Windows_Fundamentals_2_Shared_Folder.png)

   ><details><summary>Click for answer</summary>sh4r3dF0Ld3r</details>

### System Information

In this task we will look into the System Information utility.

1. What is the command to open System Information? (The answer is the name of the .exe file, not the full path)

   This answer can be found on the tools tab of the system configuration utility under System Information.
   
   ![System Information](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/windowsfundamentals2/Windows_Fundamentals_2_System_Information.png)

   ><details><summary>Click for answer</summary>msinfo32.exe</details>

2. What is listed under System Name?

   This we can find on the first tab.
   
   ![System Name](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/windowsfundamentals2/Windows_Fundamentals_2_System_Name.png)

   ><details><summary>Click for answer</summary>THM-WINFUN2</details>

3. Under Environment Variables, what is the value for ComSpec?

   This answer can be found under Software Environment and Environment Variables.
   
   ![Environment Variable](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/windowsfundamentals2/Windows_Fundamentals_2_Environment_Variable.png)

   ><details><summary>Click for answer</summary>%SystemRoot%\system32\cmd.exe</details>

### Resource Monitor

This task we focus on the Resource Monitor utility.

1. What is the command to open Resource Monitor? (The answer is the name of the .exe file, not the full path) 

   This answer can be found on the tools tab on the System Configuration utility under Resource Monitor.
   
   ![Resource Monitor](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/windowsfundamentals2/Windows_Fundamentals_2_Resource_Monitor.png)

   ><details><summary>Click for answer</summary>resmon.exe</details>

### Command Prompt

In this task we get more info about the command prompt utility.

1. In System Configuration, what is the full command for Internet Protocol Configuration?

   This answer can be found on the tools tab on the System Configuration utility under Internet Protocol Configuration.
   
   ![IP Command](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/windowsfundamentals2/Windows_Fundamentals_2_IP_Command.png)

   ><details><summary>Click for answer</summary>C:\Windows\System32\cmd.exe /k %windir%\system32\ipconfig.exe</details>

2. For the ipconfig command, how do you show detailed information?

   Looking at the help manual for this command we can see how to get all information.
   
   ![IP Config](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/windowsfundamentals2/Windows_Fundamentals_2_Ip_Config.png)

   ><details><summary>Click for answer</summary>ipconfig /all</details>

### Registry Editor 

In this last task we look at the registry editor utility.

1. What is the command to open the Registry Editor? (The answer is the name of  the .exe file, not the full path) 

   This answer can be found on the tools tab on the System Configuration utility under Registry Editor.
   
   ![Registry](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/windowsfundamentals2/Windows_Fundamentals_2_Registry.png)

   ><details><summary>Click for answer</summary>regedt32.exe</details>
