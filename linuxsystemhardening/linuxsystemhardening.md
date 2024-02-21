![Linux System Hardening Banner](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/linuxsystemhardening/Linux_System_Hardening_Banner.png)

<p align="center">
   <img src="https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/linuxsystemhardening/Linux_System_Hardening_Cover.png" alt="Linux System Hardening Logo">
</p>

# Linux System Hardening

This guide contains the answer and steps necessary to get to them for the [Linux System Hardening](https://tryhackme.com/room/linuxsystemhardening) room.

## Table of contents

- [Physical Security](#physical-security)
- [Filesystem Partitioning and Encryption](#filesystem-partitioning-and-encryption)
- [Firewall](#firewall)
- [Remote Access](#remote-access)
- [Securing User Accounts](#securing-user-accounts)
- [Software and Services](#software-and-services)
- [Update and Upgrade Policies](#update-and-upgrade-policies)
- [Audit and Log Configuration](#audit-and-log-configuration)

### Physical Security

1. What command can you use to create a password for the GRUB bootloader?

   The answer can be found in the text.

   ><details><summary>Click for answer</summary>grub2-mkpasswd-pbkdf2</details>

2. What does PBKDF2 stand for?

   A quick search can give us the answer.

   ><details><summary>Click for answer</summary>Password-based Key Derivation Function 2</details>

### Filesystem Partitioning and Encryption

1. What does LUKS stand for?

   The answer can be found in the text.

   ><details><summary>Click for answer</summary>Linux Unified Key Set</details>

2. We cannot attach external storage to theVM, so we have created a `/home/tryhackme/secretvault.img` file instead. It is encrypted with the password `2N9EdZYNkszEE3Ad`. To access it, you need to open it using `cryptsetup` and then mount it to an empty directory, such as `myvault`. What is the flag in the secret vault?

   First we must open the encrypted image using `cryptsetup`.

   ```console
   sudo cryptsetup luksOpen secretvault.img secretvault
   or
   sudo cryptsetup open --type luks /path/to/dump desired-name
   ```

   Now we can mount this device to the `myvault` folder and look inside.

   ```console
   sudo umount /dev/mapper/secretvault
   ```

   ![FileSystem Open](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/linuxsystemhardening/Linux_System_Hardening_FileSystem_Open.png)

   Now we can check to see if the device is mounted and look for our flag.

   ![Filesystem Flag](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/linuxsystemhardening/Linux_System_Hardening_Filesystem_Flag.png)

   ><details><summary>Click for answer</summary>THM{LUKS_not_LUX}</details>

### Firewall

1. There is a firewall running on the Linux VM. It is allowing port 22 TCP as we can ssh into the machine. It is allowing another TCP port; what is it?

   For this we can use the handy `ufw` command.

   ```console
   ufw status
   ```

   ![Firewall](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/linuxsystemhardening/Linux_System_Hardening_Firewall.png)

   ><details><summary>Click for answer</summary>12526</details>

2. What is the allowed UDP port?

   The can be found with the previous command.

   ><details><summary>Click for answer</summary>14298</details>

### Remote Access

1. What flag is hidden in the sshd_configfile?

   To find the flag, we must open the files located at:

   ```console
   /etc/ssh/sshd_config
   ```

   ![Remote Sshd](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/linuxsystemhardening/Linux_System_Hardening_Remote_Sshd.png)

   ><details><summary>Click for answer</summary>THM{secure_SEA_shell}</details>

### Securing User Accounts

1. One way to disable an account is to edit the passwd file and change the account’s shell. What is the suggested value to use for the shell?

   The answer to this question can be found in the text.

   ><details><summary>Click for answer</summary>/sbin/nologin</details>

2. What is the name of the RedHat and Fedora systems sudoers group?

   The answer to this question can be found in the text.

   ><details><summary>Click for answer</summary>wheel</details>

3. What is the name of the sudoers group on Debian and Ubuntu systems?

   The answer to this question can be found in the text.

   ><details><summary>Click for answer</summary>sudo</details>

4. Other than tryhackme and ubuntu, what is the username that belongs to the sudoers group?

   This can be found by looking through the /etc/passwd file and filtering on 'root'.

   ><details><summary>Click for answer</summary>blacksmith</details>

### Software and Services

1. Besides FTPS, what is another secure replacement for TFTP and FTP?

   The answer to this question can be found in the text.

   ><details><summary>Click for answer</summary>SFTP</details>

### Update and Upgrade Policies

1. What command would you use to update an older Red Hat system?

   The answer to this question can be found in the text.

   ><details><summary>Click for answer</summary>yum update</details>

2. What command would you use to update a modern Fedora system?

   The answer to this question can be found in the text.

   ><details><summary>Click for answer</summary>dnf update</details>

3. What two commands are required to update a Debian system? (Connect the two commands with&&.)

   The answer to this question can be found in the text.

   ><details><summary>Click for answer</summary>apt update && apt upgrade</details>

4. What does yum stand for?

   A quick search should give us the answer.

   ><details><summary>Click for answer</summary>Yellowdog Updater Modified</details>

5. What does dnf stand for?

   A quick search should give us the answer.

   ><details><summary>Click for answer</summary>Dandified YUM</details>

6. What flag is hidden in the sources.list file?

   We can find the file by using:

   ```console
   find / -name sources.list 2>/dev/null
   ```

   ![Update File](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/linuxsystemhardening/Linux_System_Hardening_Update_File.png)

   ><details><summary>Click for answer</summary>THM{not_Advanced_Persistent_Threat}</details>

### Audit and Log Configuration

1. What command can you use to display the last 15 lines of kern.log?

   The answer to this question can be found in the text.

   ><details><summary>Click for answer</summary>tail -n 15 kern.log</details>

2. What command can you use to display the lines containing the word denied in the filesecure?

   The answer to this question can be found in the text.

   ><details><summary>Click for answer</summary>grep denied secure</details>