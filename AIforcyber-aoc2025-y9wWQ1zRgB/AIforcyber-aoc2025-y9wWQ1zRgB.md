![AI in Security - old sAInt nick Banner](https://tryhackme-images.s3.eu-west-1.amazonaws.com/room-icons/5f9c7574e201fe31dad228fc-1762631132838)

<p align="center">
   <img src="https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/AIforcyber-aoc2025-y9wWQ1zRgB/AI_in_Security_-_old_sAInt_nick_Cover.png" alt="AI in Security - old sAInt nick Logo">
</p>

# <img src="https://tryhackme-images.s3.amazonaws.com/room-icons/5de96d9ca744773ea7ef8c00-1762182384720" alt="image" style="vertical-align: middle;height: 50px;" /> AI in Security - old sAInt nick | Advent of Cyber 2025 - Day 4

This guide contains the answer and steps necessary to get to them for the [AI in Security - old sAInt nick](https://tryhackme.com/room/AIforcyber-aoc2025-y9wWQ1zRgB) room.

## Table of contents

- [AI for Cyber Security Showcase](#ai-for-cyber-security-showcase)

### AI for Cyber Security Showcase

1. Complete the AI showcase by progressing through all of the stages. What is the flag presented to you?

   For this flag we need to progress through all stages of the showcase. 

   ![Flag](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/AIforcyber-aoc2025-y9wWQ1zRgB/AI_in_Security_-_old_sAInt_nick_Flag.png)

   ><details><summary>Click for answer</summary>THM{AI_MANIA}</details>

2. Execute the exploit provided by the red team agent against the vulnerable web application hosted at 10.82.155.191:5000. What flag is provided in the script's output after it?Remember, you will need to update the IP address placeholder in the script with the IP of your vulnerable machine (10.82.155.191:5000)

   In the second part of the task there is a red team exercise to generate a script to exploit a vulnerable application. After tasking the AI to generate the script, we can take its output and place it into a python file.

   ![Script](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/AIforcyber-aoc2025-y9wWQ1zRgB/AI_in_Security_-_old_sAInt_nick_Script.png)

   Make sure to update the IP with your current target machine IP. Then run the exploit. It will exploit the SQL injection vulnerability which will enable us to log into the admin account without having its password. This gives us our flag.

   ![Login](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/AIforcyber-aoc2025-y9wWQ1zRgB/AI_in_Security_-_old_sAInt_nick_Login.png)

   ><details><summary>Click for answer</summary>THM{SQLI_EXPLOIT}</details>

3. If you enjoyed today's room, feel free to check out theDefending Adverserial Attacksroom, where you will learn how to harden and secure AI models.
