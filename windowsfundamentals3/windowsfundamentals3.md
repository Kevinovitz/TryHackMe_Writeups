![Windows Fundamentals 3](https://assets.tryhackme.com/room-banners/windows.png)

<p align="center">
   <img src="https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/windowsfundamentals3/Windows_Fundamentals_3_Cover.png" alt="Windows Fundamentals 3 Logo">
</p>

# Windows Fundamentals 3

This guide contains the answer and steps necessary to get to them for the [Windows Fundamentals 3](https://tryhackme.com/room/windowsfundamentals3xzx) room.

### Table of Contents

- [Windows Updates](#windows-updates)
- [Windows Security](#windows-security)
- [Virus & threat protection](#virus-&-threat-protection)
- [Firewall & network protection](#firewall-&-network-protection)
- [Device security](#device-security)
- [BitLocker](#bitlocker)
- [Volume Shadow Copy Service](#volume-shadow-copy-service)

### Windows Updates

This task focusses on the Windows update mechanism.

1. There were two definition updates installed in the attached VM. On what date were these updates installed?
   
   To find this answer, we go to the Update section of the settings window and click the 'view update history'.
   
   ![Updates](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/windowsfundamentals3/Windows_Fundamentals_3_Updates.png)

   ><details><summary>Click for answer</summary>5/3/2021</details>

### Windows Security

This task focusses on the Windows Security utility.

1. In the above image, which area needs immediate attention?

   When opening the Windows Security utility from the settings window, we can see which action requires our attention.
   
   ![Security](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/windowsfundamentals3/Windows_Fundamentals_3_Security.png)

   ><details><summary>Click for answer</summary>Virus & Threat Protection</details>

### Virus & threat protection

This task goes more into the virus and threat protection in the Windows Security utility.

1. Specifically, what is turned off that Windows is notifying you to turn on?

   In the same window as the previous question, we can see what we need to do specifically.

   ![Security Action](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/windowsfundamentals3/Windows_Fundamentals_3_Security_Action.png)

   ><details><summary>Click for answer</summary>Real-time protection</details>

### Firewall & network protection

This task gives more information about the Windows firewall and network protection.

1. If you were connected to airport Wi-Fi, what most likely will be the active firewall profile?   

   Although net immediatly visible from the network and protection window, we can take an educated guess as to what the answer might be. Considering airport Wi-Fi networks are available to anyone and may not always be secure.

   ![Firewall Profile](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/windowsfundamentals3/Windows_Fundamentals_3_Firewal_Profile.png)

   ><details><summary>Click for answer</summary>Public network</details>

### Device security

This task focusses on how Windows attempts to secure the device.

1. What is the TPM?

   The answer to this file can be found in the provided image as this information is not available for our virtual machine.
   
   ![TPM](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/windowsfundamentals3/Windows_Fundamentals_3_TPM.png)

   ><details><summary>Click for answer</summary>Trusted Platform Module</details>

### BitLocker

This task gives more info about the BitLocker encryption.

1. What must a user insert on computers that DO NOT have a TPM version 1.2 or later?

   For this answer we must visit the BitLocker [documentation](https://docs.microsoft.com/en-us/windows/security/information-protection/bitlocker/bitlocker-overview) which was provided to us.
   
   ![Bitlocker](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/windowsfundamentals3/Windows_Fundamentals_3_Bitlocker.png)

   ><details><summary>Click for answer</summary>USB startup key</details>

### Volume Shadow Copy Service

In this task we will learn more about the Windows Volume Shadow Copy Service.

1. What is VSS? 

   The answer is available in the text. Otherwise a simple Google search should give the answer.

   ><details><summary>Click for answer</summary>Volume Shadow Copy Service</details>
