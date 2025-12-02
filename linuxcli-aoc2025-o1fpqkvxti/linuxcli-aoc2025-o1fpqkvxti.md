![Linux CLI - Shells Bells Banner](https://tryhackme-images.s3.eu-west-1.amazonaws.com/room-icons/678ecc92c80aa206339f0f23-1762176216100)

<p align="center">
   <img src="https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/linuxcli-aoc2025-o1fpqkvxti/Linux_Cli_Shells_Bells_Cover.png" alt="Linux CLI - Shells Bells Logo">
</p>

# Linux CLI - Shells Bells

This guide contains the answer and steps necessary to get to them for the [Linux CLI - Shells Bells](https://tryhackme.com/room/linuxcli-aoc2025-o1fpqkvxti) room.

## Table of contents

- [Linux CLI](#linux-cli)

### Linux CLI

1. Which CLI command would you use to list a directory?

   The answer to this question can be found in the text.

   ><details><summary>Click for answer</summary>ls</details>

2. Complete on machine: Identify the flag inside of the McSkidy's guide.

   After listing the directory, we can see a readme file. Lets read it using: `cat README.txt`.

   This tells us there is a hidden guide in the guides folder. We navigate into it and look for any files using:

   ```cmd
   cd Guides
   ls -la
   ```

   Here we find the file '.guide.txt' which will hold the first flag. Opening it (`cat .guide.txt`) will automatically answer the question in Tryhackme.

   ![Guide](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/raw/linuxcli-aoc2025-o1fpqkvxti/Linux_Cli_Shells_Bells_Cli_Guide.png)

   ><details><summary>Click for answer</summary>THM{learning-linux-cli}</details>

3. Which command helped you filter the logs for failed logins?

   The answer to this question can be found in the text.

   ><details><summary>Click for answer</summary>grep</details>

4. Complete on machine: Identify the flag inside the Eggstrike script.

   As stated in the text we look for failed login attempts in the 'auth' log.

   ```cmd
   grep "Failed password" auth.log
   ```

   This gives us a few failed attempts for user 'socmas'. Next we will look into its home directory for any suspicious files.

   ```cmd
   find /home/socmas/ -name *eggs*
   cat /home/socmas/2025/eggstrike.sh
   ```

   Here we see a possibly malicious script file. Opening it reveals the next flag.

   ![Script](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/raw/linuxcli-aoc2025-o1fpqkvxti/Linux_Cli_Shells_Bells_Script.png)

   ><details><summary>Click for answer</summary>THM{sir-carrotbane-attacks}</details>

5. Which command would you run to switch to the root user?

   The answer to this question can be found in the text.

   ><details><summary>Click for answer</summary>sudo su</details>

6. Finally, what flag did Sir Carrotbane leave in the root bash history?

   To view the bash history of the roort user, we must first switch to the root user using `sudo su`. Now we can use `history` to view the used bash commands.

   ![History](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/raw/linuxcli-aoc2025-o1fpqkvxti/Linux_Cli_Shells_Bells_History.png)

   Indeed we find the flag left behind for us.

   ><details><summary>Click for answer</summary>THM{until-we-meet-again}</details>

7. For those who consider themself intermediate and want another challenge, check McSkidy's hidden note in/home/mcskidy/Documents/to get access to the key forSide Quest 1!

   Navigating to '/home/mcskidy/Documents/' we find a file called 'read-me-please.txt'. This files contains some information and several clues needed for us to find the key for the first sidequest of 2025. This will be further investigated in [Advent of Cyber '25 Side Quest](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/adventofcyber25sidequest/adventofcyber25sidequest.md)

   ><details><summary>Click for answer</summary></details>