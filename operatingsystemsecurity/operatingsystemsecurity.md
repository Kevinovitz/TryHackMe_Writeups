![Operating System Security Banner](https://assets.tryhackme.com/room-banners/intro-to-offensive-security.png)

<p align="center">
   <img src="https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/operatingsystemsecurity/Operating_System_Security_Cover.png" alt="Operating System Security Logo">
</p>

# Operating System Security

This guide contains the answer and steps necessary to get to them for the [Operating System Security](https://tryhackme.com/room/operatingsystemsecurity) room.

## Table of contents

- [Introduction to Operating System Security](#introduction-to-operating-system-security)
- [Common Examples of OS Security](#common-examples-of-os-security)
- [Practical Example of OS Security](#practical-examples-of-os-security)

### Introduction to Operating System Security

1. Which of the following is not an operating system?

   - AIX
   - Android
   - Chrome OS
   - Solaris
   - Thunderbird

   Thunderbird is a type of email client.

   ><details><summary>Click for answer</summary>Thunderbird</details>

### Common Examples of OS Security

1. Which of the following is a strong password, in your opinion?

   - iloveyou
   - 1q2w3e4r5t
   - LearnM00r
   - qwertyuiop

   The first one is a simple phrase which can be easily guessed. The second and fourth ones are all simple passwords when looking at the layout of a standard qwerty keyboard.

   ><details><summary>Click for answer</summary>LearnM00r</details>

### Practical Example of OS Security

In this task we will attempt to get into the system and see if we can find password information for other users. After a quick scan we see that SSH is running on its default port.

```cmd
nmap -sV 10.10.55.195
```

![Nmap](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/operatingsystemsecurity/Operating_System_Security_Nmap.png)

With the information we found on the notes we can try logging into sammie's account through SSH.

```cmd
ssh sammie@10.10.55.195
```

![SSH Sammie Login](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/operatingsystemsecurity/Operating_System_Security_SSH_Sammie_Login.png)

Next we use the mentioned commands to get some more info on the system

![Sammie Commands](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/operatingsystemsecurity/Operating_System_Security_Sammie_Commands.png)

We also look at the terminal history with `history`.

![Sammie History](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/operatingsystemsecurity/Operating_System_Security_Sammie_History.png)

They mentioned others users. We can check this by looking at the home folder.

```cmd
ls -lh /home/
```

![Users](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/operatingsystemsecurity/Operating_System_Security_Users.png)

1. Based on the top 7 passwords, let’s try to find Johnny’s password. What is the password for the user johnny?

   I looked a different websites and the top 7 of the rockyou.txt file, but couldn't find the correct password.
   
   ```cmd
   sed -n 1,7p /usr/share/wordlists/rockyou.txt
   ```
   
   ![Top 7 Rockyou](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/operatingsystemsecurity/Operating_System_Security_Top_7_Rockyou.png)
   
   I then decided to cheat a little and use hydra to crack it using the rockyou list.
   
   ```cmd
   hydra -l sammie -P /usr/share/wordlists/rockyou.txt ssh://10.10.55.195 -t 4
   ```
   
   ![Hydra Johnny](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/operatingsystemsecurity/Operating_System_Security_Hydra_Johnny.png)
   
   ![Johnny Login](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/operatingsystemsecurity/Operating_System_Security_Johnny_Login.png)

   ><details><summary>Click for answer</summary>abc123</details>

2. Once you are logged in as Johnny, use the command history to check the commands that Johnny has typed. We expect Johnny to have mistakenly typed the root password instead of a command. What is the root password?

   Looking through the `history` file we can see a password.
   
   ![Johnny Files](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/operatingsystemsecurity/Operating_System_Security_Johnny_Files.png)

   ><details><summary>Click for answer</summary>happyHack!NG</details>

3. While logged in as Johnny, use the command su - root to switch to the root account. Display the contents of the file flag.txt in the root directory. What is the content of the file?

   We use `su - root` to switch to the root user with our found password and look for the flag on the system.
   
   ![Root](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/operatingsystemsecurity/Operating_System_Security_Root.png)

   ><details><summary>Click for answer</summary>THM{YouGotRoot}</details>
