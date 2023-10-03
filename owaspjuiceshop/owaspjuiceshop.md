![OWASP Juice Shop Banner](https://i.imgur.com/JaX5W2u.png)

<p align="center">
   <img src="https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/owaspjuiceshop/OWASP_Juice_Shop_Cover.png" alt="OWASP Juice Shop Logo">
</p>

# OWASP Juice Shop

This guide contains the answer and steps necessary to get to them for the [OWASP Juice Shop](https://tryhackme.com/room/owaspjuiceshop) room.

## Table of contents

- [Let's go on an adventure!](#let's-go-on-an-adventure)
- [Inject the juice](#inject-the-juice)
- [Who broke my lock?!](#who-broke-my-lock)
- [AH! Don't look!](#ah-don't-look)
- [Who's flying this thing?](#who's-flying-this-thing)
- [Where did that come from?](#where-did-that-come-from)
- [Exploration! ](#exploration)

### Let's go on an adventure!

1. Question #1: What's the Administrator's email address?

   Clicking one of the products gives us the admin's email address in the review.

   ADVENTURE EMAIL

   ><details><summary>Click for answer</summary>admin@juice-sh.op</details>

3. Question #2: What parameter is used for searching?

   After searching, we can see the parameter in the address bar.

   ADVENTURE SEARCH

   ><details><summary>Click for answer</summary>q</details>

5. Question #3: What show does Jim reference in his review? 

   This answer can even be found in the text.

   ><details><summary>Click for answer</summary>Star Trek</details>

### Inject the juice

1. Question #1: Log into the administrator account!

   We can use Burpsuite to intercept and modify the request or we can input in directly into the username field.

   INJECTION LOGIN

   INJECTION ADMIN

   ><details><summary>Click for answer</summary>32a5e0f21372bcc1000a6088b93b458e41f0e02a</details>

3. Question #2: Log into the Bender account!

   Now we do the same, but we add the user's email and add `'--` to the end.

   INJECTION LOGIN BENDER

   INJECTION BENDER

   ><details><summary>Click for answer</summary>fb364762a3c102b2db932069c0e6b78e738d4066</details>

### Who broke my lock?!

1. Question #1: Bruteforce the Administrator account's password!

   First lets intercept a login request using the admin's password. And send it to Intruder in Burpsuite.

   LOCK REQUEST

   Now we add a position for the password field. We don't have to do this for the username as we will be using the same for each try.

   LOCK POSITIONS

   Next we add items to try from a wordlist from Seclists (best1050).

   LOCK PAYLOADS

   Now we start the attack and wait for a response status of 200, this should be our password.

   LOCK PASSWORD

   Finally, we can log in with the password we found.

   LOCK ADMIN   

   ><details><summary>Click for answer</summary>c2110d06dc6f81c67cd8099ff0ba601241f1ac0e</details>

3. Question #2: Reset Jim's password!

   For this we can simply answer the security question with the answer from the text.

   LOCK RESET

   LOCK FLAG

   ><details><summary>Click for answer</summary>094fbc9b48e525150ba97d05b942bbf114987257</details>

### AH! Don't look!

1. Question #1: Access the Confidential Document!



   ><details><summary>Click for answer</summary></details>

2. Question #2: Log into MC SafeSearch's account!



   ><details><summary>Click for answer</summary></details>

3. Question #3: Download the Backup file!



   ><details><summary>Click for answer</summary></details>

### Who's flying this thing?

1. Question #1: Access the administration page!



   ><details><summary>Click for answer</summary></details>

2. Question #2: View another user's shopping basket!



   ><details><summary>Click for answer</summary></details>

3. Question #3: Remove all 5-star reviews!



   ><details><summary>Click for answer</summary></details>

### Where did that come from?

1. Question #1: Perform a DOM XSS!



   ><details><summary>Click for answer</summary></details>

2. Question #2: Perform a persistent XSS!



   ><details><summary>Click for answer</summary></details>

4. Question #3: Perform a reflected XSS!



   ><details><summary>Click for answer</summary></details>

### Exploration! 

1.  Access the /#/score-board/ page 

   This can si,ply be found by navigating to the `/#/score-board/` page.

   ><details><summary>Click for answer</summary>7efd3174f9dd5baa03a7882027f2824d2f72d86e</details>
