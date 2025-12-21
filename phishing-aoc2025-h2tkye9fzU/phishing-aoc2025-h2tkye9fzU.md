![Phishing - Merry Clickmas Banner](https://tryhackme-images.s3.eu-west-1.amazonaws.com/room-icons/5f9c7574e201fe31dad228fc-1762630275389)

<p align="center">
   <img src="https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/phishing-aoc2025-h2tkye9fzU/Phishing_-_Merry_Clickmas_Cover.png" alt="Phishing - Merry Clickmas Logo">
</p>

# <img src="https://tryhackme-images.s3.amazonaws.com/room-icons/6645aa8c024f7893371eb7ac-1761822143495" alt="image" style="vertical-align: middle;height: 50px;" /> Phishing - Merry Clickmas | Advent of Cyber 2025 - Day 2


This guide contains the answer and steps necessary to get to them for the [Phishing - Merry Clickmas](https://tryhackme.com/room/phishing-aoc2025-h2tkye9fzU) room.

## Table of contents

- [Phishing Exercise for TBFC](#phishing-exercise-for-tbfc)

### Phishing Exercise for TBFC

1.  What is the password used to access the TBFC portal?

    After downloading the script, we run it and navigate to the binded address to confirm it works.

    ```cmd
    ./server.py
    ```

    ![Server](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/phishing-aoc2025-h2tkye9fzU/Phishing_-_Merry_Clickmas_Server.png)

    Now we create our phishing email using `setoolkit`.

    ![Tool](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/phishing-aoc2025-h2tkye9fzU/Phishing_-_Merry_Clickmas_Tool.png)
    
    Choose the following options:

    - 1 - Social-Engineering Attacks
    - 5 - Mass Mailer Attack
    - 1 - E-Mail Attack Single Email Address
    - 2 - One-Time Use Email Template

    And for the contents:

    - Subject: Shipping Schedule Changes
    - Plaintext
    - Body: Dear Elves,
      Kindly note that there have been significant changes to the shipping schedule.
      Please confirm the new schedule by visiting http://192.168.170.75:8000
      Kind regards,
      Flying Deer
      END
    - Recipient: factory@wareville.thm
    - Use own server
    - Sender: updates@flyingdeer.thm
    - Sender Name: Flying Deer
    - SMTP server: 10.82.186.195
    - Port nr: 25
    - High priority: no
    - No attachments

    After setting things up, the mail should be sent. And after a few minutes we receive a notification.

    ![Credentials](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/phishing-aoc2025-h2tkye9fzU/Phishing_-_Merry_Clickmas_Credentials.png)

    ><details><summary>Click for answer</summary>unranked-wisdom-anthem</details>

2.  Browse to http://MACHINE_IP from within the AttackBox and try to access the mailbox of the factory user to see if the previously harvested admin password has been reused on the email portal. What is the total number of toys expected for delivery?

    We can use these credentials to log into the email server.

    ![Login](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/phishing-aoc2025-h2tkye9fzU/Phishing_-_Merry_Clickmas_Login.png)

    This works and we can se the amount in one of the received emails.

    ![Toys](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/phishing-aoc2025-h2tkye9fzU/Phishing_-_Merry_Clickmas_Toys.png)

    ><details><summary>Click for answer</summary>1984000</details>

3.  If you enjoyed today's room, feel free to check out the Phishing Prevention room.