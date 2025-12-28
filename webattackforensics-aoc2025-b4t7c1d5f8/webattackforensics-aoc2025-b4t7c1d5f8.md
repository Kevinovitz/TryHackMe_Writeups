![Web Attack Forensics - Drone Alone Banner](https://tryhackme-images.s3.eu-west-1.amazonaws.com/room-icons/5f04259cf9bf5b57aed2c476-1763552144561)

<p align="center">
   <img src="https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/webattackforensics-aoc2025-b4t7c1d5f8/Web_Attack_Forensics_-_Drone_Alone_Cover.png" alt="Web Attack Forensics - Drone Alone Logo">
</p>

# <img src="https://tryhackme-images.s3.amazonaws.com/room-icons/6186e45a4c3e9a0043efd100-1764342232871" alt="image" style="vertical-align: middle;height: 50px;" /> Web Attack Forensics - Drone Alone | Advent of Cyber 2025 - Day 15

This guide contains the answer and steps necessary to get to them for the [Web Attack Forensics - Drone Alone](https://tryhackme.com/room/webattackforensics-aoc2025-b4t7c1d5f8) room.

## Table of contents

- [Web Attack Forensics](#web-attack-forensics)

### Web Attack Forensics

1.  What is the reconnaissance executable file name?

    For this we will ook into any sings of reconnaissance using the following query:

    ```cmd
    index=windows_sysmon *cmd.exe* *whoami*
    ```

    ![Executable](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/webattackforensics-aoc2025-b4t7c1d5f8/Web_Attack_Forensics_-_Drone_Alone_Executable.PNG)

    ><details><summary>Click for answer</summary>whoami.exe</details>

2.  What executable did the attacker attempt to run through the command injection?

    To look through any command injection attempts, we will use the following query:

    ```cmd
    index=windows_apache_access (cmd.exe OR powershell OR "powershell.exe" OR "Invoke-Expression") | table _time host clientip uri_path uri_query status
    ```

    ![Injection](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/webattackforensics-aoc2025-b4t7c1d5f8/Web_Attack_Forensics_-_Drone_Alone_Injection.PNG)

    Here we can see two programs being executed.

    ><details><summary>Click for answer</summary>PowerShell.exe</details>
