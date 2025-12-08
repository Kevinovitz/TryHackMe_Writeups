![IDOR - Santa’s Little IDOR Banner](https://tryhackme-images.s3.eu-west-1.amazonaws.com/room-icons/66c44fd9733427ea1181ad58-1762448313373)

<p align="center">
   <img src="https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/idor-aoc2025-zl6MywQid9/IDOR_-_Santa’s_Little_IDOR_Cover.png" alt="IDOR - Santa’s Little IDOR Logo">
</p>

# <img src="https://tryhackme-images.s3.amazonaws.com/room-icons/66c44fd9733427ea1181ad58-1761823903831" alt="image" style="vertical-align: middle;height: 50px;" /> IDOR - Santa’s Little IDOR | Advent of Cyber 2025 - Day 5

This guide contains the answer and steps necessary to get to them for the [IDOR - Santa’s Little IDOR](https://tryhackme.com/room/idor-aoc2025-zl6MywQid9) room.

## Table of contents

- [IDOR on the Shelf](#idor-on-the-shelf)

### IDOR on the Shelf

1.  What does IDOR stand for?

    The answer to this question can be found in the text.

    ><details><summary>Click for answer</summary>Insecure Direct Object Reference</details>

2.  What type of privilege escalation are most IDOR cases?

    The answer to this question can be found in the text.

    ><details><summary>Click for answer</summary>horizontal</details>

3.  Exploiting the IDOR found in theview_accountsparameter, what is theuser_idof the parent that has 10 children?

    After loggin in, we can see that our user id is 10 from the developer tools.

    ![Id](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/idor-aoc2025-zl6MywQid9/IDOR_-_Santas_Little_IDOR_Id.png)

    This ID is stored in the sessions ... variable. We can change this to allow us to see information from other accounts. Lets change it a few times and reload the page untill we find the account with ten children.

    Instead of manually altering the ID and reloading the page, we can also use Burpsuite to automate this process. If we extract the account GET request and add it to repeater. We can specify which variable to alter for each request. We can then inspect the received responses for the amount of children in the account.

    First, make sure to enable the Burpsuite proxy in the Firefox "Foxy Proxy" extension. This enables Burpsuite to intercept the requests from the browser.

    ![Proxy](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/idor-aoc2025-zl6MywQid9/IDOR_-_Santas_Little_IDOR_Proxy.png)

    In Burpsuite, enable the intercept switch on the Proxy tab. Now reload the page in your browser. The page should not load and Burpsuite should indicate in received and intercepted a request.

    Make sure to select the correct request (the one with the user id). So you can forward any request that are not related. Now send this request to Intruder.

    ![Send](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/idor-aoc2025-zl6MywQid9/IDOR_-_Santas_Little_IDOR_Send.png)

    In the Intruder tab we must prepare the request and payload for our attack. Add the variable to the user id part of the request (remove the number).

    Now select a number list from the payload types and setup a sequential list from 0 to 20 in steps of 1. 

    Select "sniper attack" and run the attack.

    ![Attack](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/idor-aoc2025-zl6MywQid9/IDOR_-_Santas_Little_IDOR_Attack.png)

    After the attack is done, we can see all the responses. Some of the ids have no valid account behind them as indicated by the "404" response. We can now go through each of the responses and determine how many children are linked to the account. However, if we look closely at the list, we can see that one of the responses is longer than the others. This could indicate a longer children list. 

    Looking at the response we can indeed see there are 10 children listen under this account (the first child has id "11").

    ![Account](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/idor-aoc2025-zl6MywQid9/IDOR_-_Santas_Little_IDOR_Account.png)

    ><details><summary>Click for answer</summary>15</details>

4.  Bonus Task:If you want to dive even deeper, use either the base64 or md5 child endpoint and try to find theid_numberof the child born on 2019-04-17? To make the iteration faster, consider using something like Burp's Intruder. If you want to check your answer, click the hint on the question.



    ><details><summary>Click for answer</summary></details>

5.  Bonus Task:Want to go even further? Using the/parents/vouchers/claimendpoint, find the voucher that is valid on 20 November 2025. Insider information tells you that the voucher was generated exactly on the minute somewhere between 20:00 - 24:00 UTC that day. What is the voucher code? If you want to check your answer, click the hint on the question.



    ><details><summary>Click for answer</summary></details>

6.  If you enjoyed today's room, check out our completeIDORroom!



    ><details><summary>Click for answer</summary></details>
