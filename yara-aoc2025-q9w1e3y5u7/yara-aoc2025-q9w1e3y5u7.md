![YARA Rules - YARA mean one! Banner](https://tryhackme-images.s3.eu-west-1.amazonaws.com/room-icons/674d9727a22822c1eb46cb31-1763551875716)

<p align="center">
   <img src="https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/yara-aoc2025-q9w1e3y5u7/YARA_Rules_-_YARA_mean_one!_Cover.png" alt="YARA Rules - YARA mean one! Logo">
</p>

# <img src="https://tryhackme-images.s3.amazonaws.com/room-icons/674d9727a22822c1eb46cb31-1763551899077" alt="image" style="vertical-align: middle;height: 50px;" /> YARA Rules - YARA mean one! | Advent of Cyber 2025 - Day 13

This guide contains the answer and steps necessary to get to them for the [YARA Rules - YARA mean one!](https://tryhackme.com/room/yara-aoc2025-q9w1e3y5u7) room.

## Table of contents

- [Yara Rules](#yara-rules)

### Yara Rules

1.  How many images contain the string TBFC?

    We will create our own YARA rule that will look for the specific string "TBFC". Since there is only one string, it can trigger for any of them.

    ```cmd
    rule TBFC_yara_rule
    {
        meta:
            author = "Kevinovitz"
            description = "TBFC Rule"
            date = "2025-10-10"
            confidence = "low"

        strings:
            $s1 = “TBFC:”
            
        condition:
            any of them
    }
    ```

    ![Script1](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/yara-aoc2025-q9w1e3y5u7/YARA_Rules_-_YARA_mean_one!_Script1.PNG)

    Upon executing the YARA rule, we can see a number of files returned that contain the string.

    ```cmd
    yara -r rule.yar /home/ubuntu/Downloads/easter/
    ```

    ![String1](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/yara-aoc2025-q9w1e3y5u7/YARA_Rules_-_YARA_mean_one!_String1.PNG)

    ><details><summary>Click for answer</summary>5</details>

2.  What regex would you use to match a string that begins with TBFC: followed by one or more alphanumeric ASCII characters?

    Next, we want to add a part to our search string. Using regex notation we can include one or more alphanumeric characters as follows:

    ```cmd
    rule TBFC_yara_rule
    {
        meta:
            author = "Kevinovitz"
            description = "TBFC Rule"
            date = "2025-10-10"
            confidence = "low"

        strings:
            $s1 = /TBFC:[A-Za-z0-9]+/
            
        condition:
            any of them
    }
    ```

    ![Script2](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/yara-aoc2025-q9w1e3y5u7/YARA_Rules_-_YARA_mean_one!_Script2.PNG)

    ><details><summary>Click for answer</summary>/TBFC:[A-Za-z0-9]+/</details>

3.  What is the message sent by McSkidy?

    Running this script (whilst outputting the found strings) will reveall the secret message we are looking for.

    ```cmd
    yara -r rule.yar /home/ubuntu/Downloads/easter/
    ```

    ![String2](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/yara-aoc2025-q9w1e3y5u7/YARA_Rules_-_YARA_mean_one!_String2.PNG)

    ><details><summary>Click for answer</summary>Find me in HopSec Island</details>
