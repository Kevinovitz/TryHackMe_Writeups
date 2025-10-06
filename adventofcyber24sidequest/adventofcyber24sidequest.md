![Advent of Cyber '24 Side Quest Banner](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber24sidequest/Advent_of_Cyber_'24_Side_Quest_Banner.png)

<p align="center">
   <img src="https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber24sidequest/Advent_of_Cyber_'24_Side_Quest_Cover.png" alt="Advent of Cyber '24 Side Quest Logo">
</p>

# Advent of Cyber '24 Side Quest

This guide contains the answer and steps necessary to get to them for the [Advent of Cyber '24 Side Quest](https://tryhackme.com/r/room/adventofcyber24sidequest) room.

## Table of contents

- [T1: Operation Tiny Frostbite](#t1-operation-tiny-frostbite)
- [T2: Yin and Yang](#t2-yin-and-yang)
- [T3: Escaping the Blizzard](#t3-escaping-the-blizzard)
- [T4: Krampus Festival](#t4-krampus-festival)
- [T5: An Avalanche of Web Apps](#t5-an-avalanche-of-web-apps)
- [The End?](#the-end)

### T1: Operation Tiny Frostbite

The keycard for the first challenge can be found in the following room (this was hinted in the questions section of this task.)

<summary>Day 1</summary>

In the hint we are led to the github repos we have been looking at for the AoC task. Before digging deeper there, I will run an `nmap` scan to see if we can find something.

```cmd
sudo nmap -sS -Pn 10.10.156.173
```

![Key Nmap](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/9b9fbc9a60808308a2443e5db9e1239ad379c49e/adventofcyber24sidequest/Advent_of_Cyber_'24_Side_Quest_Q1_Key_Nmap.png)

Besides ssh and the regular webpage, there seems to be another http server on port 8000.

Navigating there, we can see there is a hidden C2 server login page.

![Key Login](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/9b9fbc9a60808308a2443e5db9e1239ad379c49e/adventofcyber24sidequest/Advent_of_Cyber_'24_Side_Quest_Q1_Key_Login.png)

We don't have any credentials, but this might be where the github repos come in. We can see another user that commented on the issue.

![Key Github Issue](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/9b9fbc9a60808308a2443e5db9e1239ad379c49e/adventofcyber24sidequest/Advent_of_Cyber_'24_Side_Quest_Q1_Key_Github_Issue.png)

Looking on his profile page, we can see some repos. This C2 repo might be of interest.

![Key Github Repo](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/9b9fbc9a60808308a2443e5db9e1239ad379c49e/adventofcyber24sidequest/Advent_of_Cyber_'24_Side_Quest_Q1_Key_Github_Repo.png)

In this repo there is a script used for the server in flask.

![Key Github C2](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/9b9fbc9a60808308a2443e5db9e1239ad379c49e/adventofcyber24sidequest/Advent_of_Cyber_'24_Side_Quest_Q1_Key_Github_C2.png)

In this script we can see various functions including a login function and several endpoints. It also includes default credentials and a secret. 

![Key Github Script](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/9b9fbc9a60808308a2443e5db9e1239ad379c49e/adventofcyber24sidequest/Advent_of_Cyber_'24_Side_Quest_Q1_Key_Github_Script.png)

I already tried the default credentials, but this didn't work. However, since we have a secret key, we can try to force a session cookie using `flask-unsign`.

In the script we can see that the login function looks for two values:

- "logged_in" = True
- username

We can try with the admin user to forge a session cookie using the following command:

```cmd
flask-unsign -s --cookie "{'logged_in': True, 'username':'admin'}" --secret "@09JKD0934jd712?djD"
```

![Key Flask Command](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/9b9fbc9a60808308a2443e5db9e1239ad379c49e/adventofcyber24sidequest/Advent_of_Cyber_'24_Side_Quest_Q1_Key_Flask_Command.png)

In our browser we open the developer console and add a cookie whilst on the login page. Make sure to use the following values:

- Name = session
- value = <our forged cookie>
- path = / (this enables the cookie for all endpoints)

![Key Login Cookie](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/9b9fbc9a60808308a2443e5db9e1239ad379c49e/adventofcyber24sidequest/Advent_of_Cyber_'24_Side_Quest_Q1_Key_Login_Cookie.png)

Now we simply reload the page and we should be able to look at the dashboard.

![Key Dashboard](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/9b9fbc9a60808308a2443e5db9e1239ad379c49e/adventofcyber24sidequest/Advent_of_Cyber_'24_Side_Quest_Q1_Key_Dashboard.png)

Success! Now we can look at the data page and get out keycard for the first challenge.

![Key Card](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/9b9fbc9a60808308a2443e5db9e1239ad379c49e/adventofcyber24sidequest/Advent_of_Cyber_'24_Side_Quest_Q1_Key_Card.png)

References:
https://blog.paradoxis.nl/defeating-flasks-session-management-65706ba9d3ce
https://flask.palletsprojects.com/en/stable/config/

1. What is the password the attacker used to register on the site?

   After opening the pcap file we can filter on the http traffic.

   For the first question, we are looking for registration credentials. This is probably located on a register page. In our case, there is a `register.php` page. We will filter this on POST requests as well so we get data which has been `POSTED` to the server. 

   ```cmd
   http contains "POST" and http contains "register.php"
   ```

   ![Registered Credentials](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/9b9fbc9a60808308a2443e5db9e1239ad379c49e/adventofcyber24sidequest/Advent_of_Cyber_'24_Side_Quest_Q1_Registered_Credentials.png)

   ><details><summary>Click for answer</summary>QU9DMjAyNHtUaW55X1R</details>

2. What is the password that the attacker captured?

   For this we can use a similar approach, but instead we will be looking at login requests rather than register requests. 

   ```cmd
   http contains "POST" and http contains "login.php"
   ```

   ![Captured Credentials](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/9b9fbc9a60808308a2443e5db9e1239ad379c49e/adventofcyber24sidequest/Advent_of_Cyber_'24_Side_Quest_Q1_Captured_Credentials.png)

   ><details><summary>Click for answer</summary>pbnlfVGlueV9TaDNsbF</details>

3. What is the password of the zip file transferred by the attacker?

   We are looking for a zip archive. This wasn't found in the http objects unfortunately. I did find two interesting looking executables which my be of interest later on.

   ![Http Objects](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/adventofcyber24sidequest/Advent_of_Cyber_'24_Side_Quest_Q1_Http_Objects.png)

   We could look for the magic bytes of a zip file. Which in this case would be 'PK' or '50 4B' in Hex form.

   ![Signature](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/adventofcyber24sidequest/Advent_of_Cyber_'24_Side_Quest_Q1_Signature.png)

   We can filter out the traffic from port 22 and 80 to make things more clear. In this filter we can look for the hex value of '50 4B'.

   ![Archive Packet](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/adventofcyber24sidequest/Advent_of_Cyber_'24_Side_Quest_Q1_Archive_Packet.png)

   We see something in packet 158339 coming from the host to the assumed attack machine via port 9002. It also contains something similar to an sql database called 'elves.sql'.

   ![Database Name](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/adventofcyber24sidequest/Advent_of_Cyber_'24_Side_Quest_Q1_Database_Name.png)

   To extract this archive we must follow the TCP stream. Then make sure to format the data in 'raw' format instead of 'ASCII'. Save it as a '.zip' file.

   ![Extract Archive](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/adventofcyber24sidequest/Advent_of_Cyber_'24_Side_Quest_Q1_Extract_Archive.png)

   Unfortunately, the zip archive is password protected which we don't have. Yet.

   We do however, have two executable that we found were downloaded from the attack machine to the host machine: 'ff' and 'exp_file_credentials'. Running their has through virustotal gives us an idea of what we are working with. It seems to be some kind of Linux backdoor. More specifically (from the community notes), a Tinyshell backdoor. https://github.com/creaktive/tsh/

   Now the next few steps were a bit lost on me (maybe if I put a little more time into it, I might understand), so I followed some steps in the following [write-up](https://0xb0b.gitbook.io/writeups/tryhackme/2024/advent-of-cyber-24-side-quest/t1-operation-tiny-frostbite#decrypt-the-traffic).

   The basic idea is that we have a copy of a malware executable as well as its source code. This source code tells us how it encrypts the data (i.e., the network traffic we logged on port 9001) and what we need to decrypt the data. 

   It starts with a secret and two initialization vectors. This secret is stored in the executable. Using a reverse-engineering program such as Binary Ninja we can look through the file and find the secret in the data header.

   ![Secret](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/adventofcyber24sidequest/Advent_of_Cyber_'24_Side_Quest_Q1_Secret.png)

   Now that we have the secret, we should use a script that performs the same steps as the malware to decrypt the data. This was also used from the above mentioned link. Take not that it is required to export the relevant entries to a text file using:

   ```cmd
   tshark -r traffic.pcap -Y "tcp.dstport == 9001" -T fields -e data > port_9001_data.txt
   ```

   We can now run the script and we should see some of the commands that have been executed via the shell.

   ```cmd
   python3 extract-commands.py
   ```

   ![Decrypted Commands](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/adventofcyber24sidequest/Advent_of_Cyber_'24_Side_Quest_Q1_Decrypted_Commands.png)

   We can see the command that has been used to create the archive at then end (including the password). It also shows us some of the sql commands used which reveal the password we need for the next question. If this was not the case, however, we could use the archive password to open the database and look for the password inside.

   ><details><summary>Click for answer</summary>9jYW5fRW5jcnlwVF9iVXR</details>

4. What is McSkidy's password that was inside the database file stolen by the attacker?

   With the password we can extract the database file and open it to find the password. Be sure to note, this isn't an actual database file. It is a dump file containing various commands. Simply opening it up in a text editor should be enough to find the password.

   ![Password](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/adventofcyber24sidequest/Advent_of_Cyber_'24_Side_Quest_Q1_Password.png)

   ><details><summary>Click for answer</summary>faXRfSXNfTjB0X0YwMGxwcm8wZn0</details>

### T2: Yin and Yang

1. What is the flag for YIN?



   ><details><summary>Click for answer</summary></details>

2. What is the flag for YANG?



   ><details><summary>Click for answer</summary></details>

### T3: Escaping the Blizzard

1. What is the content of the file foothold.txt?



   ><details><summary>Click for answer</summary></details>

2. What is the content of the file user.txt?



   ><details><summary>Click for answer</summary></details>

3. What is the content of the file root.txt?



   ><details><summary>Click for answer</summary></details>

### T4: Krampus Festival

1. What is the content of flag.txt?



   ><details><summary>Click for answer</summary></details>

2. What is the content of user.txt?



   ><details><summary>Click for answer</summary></details>

3. What is the content of root.txt?



   ><details><summary>Click for answer</summary></details>

### T5: An Avalanche of Web Apps

1. What is the value of flag 1?



   ><details><summary>Click for answer</summary></details>

2. What is the value of flag 2?



   ><details><summary>Click for answer</summary></details>

3. What is the value of flag 3?



   ><details><summary>Click for answer</summary></details>

4. What is the value of flag 4?



   ><details><summary>Click for answer</summary></details>

### The End?

1. What is the flag you get at the end of thesurvey? Please make sure to copy the flag before closing the tab!



   ><details><summary>Click for answer</summary></details>

