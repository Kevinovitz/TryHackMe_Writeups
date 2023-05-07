![Operating System Security Banner](https://assets.tryhackme.com/room-banners/intro-to-offensive-security.png)

<p align="center">
   <img src="https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/operatingsystemsecurity/Operating_System_Security_Cover.png" alt="Operating System Security Logo">
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

NMAP

SSH SAMMIE LOGIN

SAMMIE COMMANDS

SAMMIE HISTORY

USERS

1. Based on the top 7 passwords, let’s try to find Johnny’s password. What is the password for the user johnny?

   TOP 7 ROCKYOU
   
   HYDRA JOHNNY
   
   JOHNNY LOGIN

   ><details><summary>Click for answer</summary>abc123</details>

2. Once you are logged in as Johnny, use the command history to check the commands that Johnny has typed. We expect Johnny to have mistakenly typed the root password instead of a command. What is the root password?

   JOHNNY FILES

   ><details><summary>Click for answer</summary>happyHack!NG</details>

3. While logged in as Johnny, use the command su - root to switch to the root account. Display the contents of the file flag.txt in the root directory. What is the content of the file?

   ROOT

   ><details><summary>Click for answer</summary>THM{YouGotRoot}</details>
