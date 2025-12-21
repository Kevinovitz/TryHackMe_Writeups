![Forensics - Registry Furensics Banner](https://tryhackme-images.s3.eu-west-1.amazonaws.com/room-icons/5e9c5d0148cf664325c8a075-1763744545793)

<p align="center">
   <img src="https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/registry-forensics-aoc2025-h6k9j2l5p8/Forensics_-_Registry_Furensics_Cover.png" alt="Forensics - Registry Furensics Logo">
</p>

# <img src="https://tryhackme-images.s3.amazonaws.com/room-icons/6645aa8c024f7893371eb7ac-1763316546050" alt="image" style="vertical-align: middle;height: 50px;" /> Forensics - Registry Furensics | Advent of Cyber 2025 - Day 16

This guide contains the answer and steps necessary to get to them for the [Forensics - Registry Furensics](https://tryhackme.com/room/registry-forensics-aoc2025-h6k9j2l5p8) room.

## Table of contents

- [Investigate the Gifts Delivery Malfunctioning](#investigate-the-gifts-delivery-malfunctioning)

### Investigate the Gifts Delivery Malfunctioning

1.  What application was installed on the dispatch-srv01 before the abnormal activity started?

    Looking at the provided table, this can most likely be found in the SOFTWARE hive. Lets load it in Registry Explorer (don't forget to add the logs).

    The first path to look in is: `HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall` as it stores information on all installed programs. 

    ![Program](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/registry-forensics-aoc2025-h6k9j2l5p8/Forensics_-_Registry_Furensics_Program.png)

    Sorting the list by the install date makes things a bit easier. We are looking for something installed on or before the 21st of October 2025. Looks like there is a program that was installed just before or on the date when strange things started happening.

    ><details><summary>Click for answer</summary>Dronemanager Updater</details>

2.  What is the full path where the user launched the application (found in question 1) from?

    For this we need to load the NTUSER.DAT hive as well. Then we can look into the `HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\UserAssist` key for the previously found program.

    ![Launch](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/registry-forensics-aoc2025-h6k9j2l5p8/Forensics_-_Registry_Furensics_Launch.png)

    ><details><summary>Click for answer</summary>C:\Users\dispatch.admin\Downloads\DroneManager_Setup.exe</details>

3.  Which value was added by the application to maintain persistence on startup?

    To look at values related to automatically run programs we should look into the `HKLM\Software\Microsoft\Windows\CurrentVersion\Run` key.

    ![Run](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/registry-forensics-aoc2025-h6k9j2l5p8/Forensics_-_Registry_Furensics_Run.png)

    Here we see one entry that looks related to the previously found program. Lets look at the value that was added to this entry.

    ><details><summary>Click for answer</summary>C:\Program Files\DroneManager\dronehelper.exe" --background</details>

4.  If you enjoyed today's room, feel free to check out the [Expediting Registry Analysis](https://tryhackme.com/room/expregistryforensics) room.
