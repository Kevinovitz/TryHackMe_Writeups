![After Hours Banner](https://cdn-images.tryhackme.com/room-icons/5dbea226085ab6182a2ee0f7-1785251902930)

<p align="center">
   <img src="https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/hh-afterhours-b090d1f0/After_Hours_Cover.png" alt="After Hours Logo">
</p>

# <img src="https://cdn-images.tryhackme.com/room-icons/5dbea226085ab6182a2ee0f7-1785251914578" alt="image" style="vertical-align: middle;height: 50px;" /> After Hours

This guide contains the answer and steps necessary to get to them for the [After Hours](https://tryhackme.com/room/hh-afterhours-b090d1f0) room.

<h2>Table of contents</h2>

- [Task 1 - Hacker Holidays: Day 12](#task-1---hacker-holidays-day-12)

### Task 1 - Hacker Holidays: Day 12

1.  What is the flag?

    The files we downloaded from the challenge are related to the WMI Repository of a Windows Host. We can use various tools to go through these files. But since the hint mentions standard autoruns/persistence tools don't find anything, we will start with something easier. `strings`. See if we cannot find anything usefull in the files. Some of the strings we will look for are: 'powershell, flag, THM {, CommandLineEventConsumer, bypass\downloadstring'.

    ```console
    strings -a OBJECTS.DATA > obj_ascii.txt

    grep -iE 'flag|thm\{|powershell|CommandLineEventConsumer|bypass\downloadstring' obj_ascii.txt
    ```
    
    ![Strings](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/hh-afterhours-b090d1f0/After_Hours_Strings.png)
    
    We can see many hits, but a few stand out. Related to powershell. Lets narrow down our search to only list those entries.

    ```console
    grep -iE '/C powershell.exe' obj_ascii.txt
    ```

    ![Powershell](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/hh-afterhours-b090d1f0/After_Hours_Powershell.png)

    Looks like we have some base64 encoded payloads. Lets decode these parts.

    ```console
    grep -iE '/C powershell.exe' obj_ascii.txt | grep -ioP '(?<=-enc )\S+' > encoded.txt
    base64 --decode encoded.txt > decoded.txt
    ```

    ![Decoded](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/hh-afterhours-b090d1f0/After_Hours_Decoded.png)

    Here we can see the decoded commands. These seem to be related to a class called "HardwareTelemetry". Lets see if we can find these in the file as well.

    ```console
    grep -iE 'HardwareTelemetry' obj_ascii.txt
    ```

    ![Telemetry](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/hh-afterhours-b090d1f0/After_Hours_Telemetry.png)

    Not much to work with here, but we can add some context and look at some of the previous and trailing lines of code.

    ```console
    grep -C 10 -iE 'HardwareTelemetry' obj_ascii.txt
    ```

    ![Telemetry Context](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/hh-afterhours-b090d1f0/After_Hours_Telemetry_Context.png)

    Here we see some more. Namely, the encoded block below the actual class search hit.

    Simply decoding this using base64 didn't work.

    ![Class](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/hh-afterhours-b090d1f0/After_Hours_Class.png)

    We need to do something else. Looking at the first powershell command we found earlier, we see some compression is used by deflating the stream. We can inflate it to get readable text.

    ![Class Inflated](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/hh-afterhours-b090d1f0/After_Hours_Class_Inflated.png)

    We can see this is a Windows executable by the magic number (MZ). Further down, we find a command used to add a user to the domain containing an encoded string. Lets decode that.

    ![Flag](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/hh-afterhours-b090d1f0/After_Hours_Flag.png)

    ><details><summary>Click for answer</summary>THM{P4tch_op3ned_th3_BacKd00r}</details>
