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



   ><details><summary>Click for answer</summary></details>

4. What is McSkidy's password that was inside the database file stolen by the attacker?



   ><details><summary>Click for answer</summary></details>

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

