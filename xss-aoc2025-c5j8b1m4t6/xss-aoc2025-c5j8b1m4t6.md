![XSS - Merry XSSMas Banner](https://tryhackme-images.s3.eu-west-1.amazonaws.com/room-icons/5f9c7574e201fe31dad228fc-1763405801743)

<p align="center">
   <img src="https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/xss-aoc2025-c5j8b1m4t6/XSS_-_Merry_XSSMas_Cover.png" alt="XSS - Merry XSSMas Logo">
</p>

# <img src="https://tryhackme-images.s3.amazonaws.com/room-icons/5f9c7574e201fe31dad228fc-1763405859947" alt="image" style="vertical-align: middle;height: 50px;" /> XSS - Merry XSSMas | Advent of Cyber 2025 - Day 11

This guide contains the answer and steps necessary to get to them for the [XSS - Merry XSSMas](https://tryhackme.com/room/xss-aoc2025-c5j8b1m4t6) room.

## Table of contents

- [Leave the Cookies, Take the Payload](#leave-the-cookies-take-the-payload)

### Leave the Cookies, Take the Payload

1.  Which type of XSS attack requires payloads to be persisted on the backend?

    This answer can be found in the text.

    ><details><summary>Click for answer</summary>Stored</details>

2.  What's the reflected XSS flag?

    We can test to see if the website is indeed vulnerable to XSS.

    ```cmd
    <script>alert('Reflected Meow Meow')</script>
    ```

    ![Reflected Proof](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/xss-aoc2025-c5j8b1m4t6/XSS_-_Merry_XSSMas_Reflected_Proof.png)

    If we search for this term, we get our flag in the pup-up.

    ```cmd
    https://trygiftme.thm/search?term=<script>alert( atob("VEhNe0V2aWxfQnVubnl9") )</script>
    ```

    ![Reflected Flag](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/xss-aoc2025-c5j8b1m4t6/XSS_-_Merry_XSSMas_Reflected_Flag.png)

    ><details><summary>Click for answer</summary>THM{Evil_Bunny}</details>

3.  What's the stored XSS flag?

    After adding this comment to the form and submit it. We get notified about the flag.

    ![Stored Flag](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/xss-aoc2025-c5j8b1m4t6/XSS_-_Merry_XSSMas_Stored_Flag.png)

    If you are savvy, the flag can already be deduced from the search term and the comment. As it is Base64 encoded in the text.
    
    ><details><summary>Click for answer</summary>THM{Evil_Stored_Egg}</details>

4.  If you enjoyed todays's room, you might want to have a look at the [Intro to Cross-site Scripting](https://tryhackme.com/room/xss) room!
