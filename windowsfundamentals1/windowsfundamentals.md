![Windows Fundamentals 1](https://assets.tryhackme.com/room-banners/windows.png)

<p align="center">
   <img src="https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/windowsfundamentals1/Windows_Fundamentals_1_Cover.png" alt="Windows Fundamentals 1 Logo">
</p>

# Windows Fundamentals 1

This guide contains the answer and steps necessary to get to them for the [Windows Fundamentals 1](https://tryhackme.com/room/windowsfundamentals1xbx) room.

### Table of Contents

- [Windows Editions](#windows-editions)
- [The Desktop (GUI)](#the-desktop-gui)
- [The File System](#the-file-system)
- [The Windows\System32 Folders](#the-windows\system32-folders)
- [User Accounts, Profiles, and Permissions](#user-accounts,-profiles,-and-permissions)
- [User Account Control](#user-account-control)
- [Settings and the Control Panel](#settings-and-the-control-panel)
- [Task Manager](#task-manager)

### Windows Editions

In this task we will learn more about the different versions of Windows.

1. What encryption can you enable on Pro that you can't enable in Home?

   For this answer we can go to the [website](https://www.microsoft.com/en-us/windows/compare-windows-10-home-vs-pro) with the differences between Home and Pro.

   ><details><summary>Click for answer</summary>BitLocker</details>

### The Desktop (GUI)

In this task we will look more into the GUI of Windows.

1.  Which selection will hide/disable the Search box?

   To answer this question, we can right-click the taskbar and navigate to 'Search'.
   
   ![Searchbox](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/windowsfundamentals1/Windows_Fundamentals_1_Searchbox.png)

   ><details><summary>Click for answer</summary>Hidden</details>

2. Which selection will hide/disable the Task View button?

   This answer can be found in the same context window as the previous question.

   ><details><summary>Click for answer</summary>Show Task View button</details>

3. Besides Clock and Network, what other icon is visible in the Notification Area?

   If we right-click this icon, we can see its name.
   
   ![Action Center](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/windowsfundamentals1/Windows_Fundamentals_1_Action_Center.png)

   ><details><summary>Click for answer</summary>Action Center</details>

### The File System

In this task, we will learn more about Windows file system.

1.  What is the meaning of NTFS? 

   The answer for to this question can be found in the text.

   ><details><summary>Click for answer</summary>New Technology File System</details>

### The Windows\System32 Folders

In this task we will go into more detail about the system32 folder and what it does.

1.  What is the system variable for the Windows folder? 

   Again, the answer to this question can be found in the text.

   ><details><summary>Click for answer</summary>%windir%</details>

### User Accounts, Profiles, and Permissions

In this task we will look into Windows user accounts and permissions.

1. What is the name of the other user account?

   We can find the other usename in two ways. Firstly, we can go to the users folder in C:\Users.

   ![Other Users](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/windowsfundamentals1/Windows_Fundamentals_1_Other_Users.png)
   
   Or in the Local Users and Groups utility.
   
   ![Lusrmgr Users](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/windowsfundamentals1/Windows_Fundamentals_1_Lusrmgr_Users.png)

   ><details><summary>Click for answer</summary>tryhackmebilly</details>

2. What groups is this user a member of?

   In the Local Users and Groups utility we can right-click the user name and view its properties. 
   
   ![Lusrmgr Groups](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/windowsfundamentals1/Windows_Fundamentals_1_Lusrmgr_Groups.png)

   ><details><summary>Click for answer</summary>Remote Desktop Users,Users</details>

3. What built-in account is for guest access to the computer?

   This user can also be found in the user window of the Local User and Groups utility.

   ><details><summary>Click for answer</summary>Guest</details>

4. What is the account status?

   Viewing the properties of the guest accounts gives us the status.
   
   ![Lusrmgr Guest](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/windowsfundamentals1/Windows_Fundamentals_1_Lusrmgr_Guest.png)

   ><details><summary>Click for answer</summary>Account is disabled</details>

### User Account Control

In this task we look more into the user account control mechanism.

1. What does UAC mean? 

   The answer can be found in the text.
   
   ><details><summary>Click for answer</summary>User Account Control</details>

### Settings and the Control Panel

In this task we get more information about the Windows settings and control panel.

1. In the Control Panel, change the view to Small icons. What is the last setting in the Control Panel view? 

   Using the 'view by' buttons in the top right, we can get the answer.
   
   ![Control Panel](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/windowsfundamentals1/Windows_Fundamentals_1_Control_Panel.png)

   ><details><summary>Click for answer</summary>Windows Defender Firewall</details>

### Task Manager 

In this last task we look into the task manager utility.

1.  What is the keyboard shortcut to open Task Manager? 

   The shortcut was already known to me, but more information on this can be found in the references [blog post](https://www.howtogeek.com/405806/windows-task-manager-the-complete-guide/).

   ><details><summary>Click for answer</summary>Ctrl+Shift+Esc</details>
