![OWASP Juice Shop Banner](https://i.imgur.com/JaX5W2u.png)

<p align="center">
   <img src="https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/owaspjuiceshop/OWASP_Juice_Shop_Cover.png" alt="OWASP Juice Shop Logo">
</p>

# OWASP Juice Shop

This guide contains the answer and steps necessary to get to them for the [OWASP Juice Shop](https://tryhackme.com/room/owaspjuiceshop) room.

## Table of contents

- [Let's go on an adventure!](#lets-go-on-an-adventure)
- [Inject the juice](#inject-the-juice)
- [Who broke my lock?!](#who-broke-my-lock)
- [AH! Don't look!](#ah-dont-look)
- [Who's flying this thing?](#whos-flying-this-thing)
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

   Looking at the url for the legal document, we can access the ftp server directly.

   LOOK FTP
   
   From here we get a flag for accessing secret documents.

   LOOK FLAG
   
   ><details><summary>Click for answer</summary>edf9281222395a1c5fee9b89e32175f1ccf50c5b</details>

3. Question #2: Log into MC SafeSearch's account!

   After watching the clip (or using the text) we can log into Mc Safe Search's account.

   LOOK MCSAFE LOGIN

   ><details><summary>Click for answer</summary>66bdcffad9e698fd534003fbb3cc7e2b7b55d7f0</details>

5. Question #3: Download the Backup file!

   Using the Poison Null Byte as suggested, we can bypass the file extension restriction and download the backup file.

   ```cmd
   10.10.204.165/ftp/package.json.bak%2500.md
   ```

   LOOK BACKUP

   ><details><summary>Click for answer</summary>bfc1e6b4a16579e85e06fee4c36ff8c02fb13795</details>

### Who's flying this thing?

1. Question #1: Access the administration page!

   Looking at the javascript in the debugger we see this mention of an administration panel.
   
   FLYING ADMIN

   Logging into the admin account with our previously found credentials and navigating to `#/administration` gives us access to the admin panel.
   
   FLYING ADMIN PANEL
   
   ><details><summary>Click for answer</summary>946a799363226a24822008503f5d1324536629a0</details>

3. Question #2: View another user's shopping basket!

   First we capture the request and change the basket number to something else.

   FLYING REQUEST

   This lets us view another user's basket.
   
   FLYING BASKET

   ><details><summary>Click for answer</summary>41b997a36cc33fbe4f0ba018474e19ae5ce52121</details>

5. Question #3: Remove all 5-star reviews!

   Under the feedback column, we can delete a five-start review.

   FLYING REMOVE

   FLYING FLAG
   
   ><details><summary>Click for answer</summary>50c97bcce0b895e446d61c83a21df371ac2266ef</details>

### Where did that come from?

1. Question #1: Perform a DOM XSS!

   For our first XSS attack we use the following code in the search bar.

   ```cmd
   <iframe src="javascript:alert(`xss`)"> 
   ```

   WHERE DOM

   ><details><summary>Click for answer</summary>9aaf4bbea5c30d00a1f5bbcfce4db6d4b0efe0bf</details>

3. Question #2: Perform a persistent XSS!

   For this XSS attack we enable intercept in Burpsuite and log out of our account. In this request we head the following header.

   ```cmd
   True-Client-IP: <iframe src="javascript:alert(`xss`)">
   ```

   WHERE HEADER

   Now we can log back in again and go to the last login ip page.

   WHERE IP

   ><details><summary>Click for answer</summary>149aa8ce13d7a4a8a931472308e269c94dc5f156</details>

5. Question #3: Perform a reflected XSS!

   For this final XSS attack we navigate to the order history page and click on the track button.

   WHERE ORDER

   Now we can cange the `id` parameter in the URL with:

   ```cmd
    ```cmd
   <iframe src="javascript:alert(`xss`)"> 
   ```

   WHERE FLAG

   ><details><summary>Click for answer</summary>23cefee1527bde039295b2616eeb29e1edc660a0</details>

### Exploration! 

1.  Access the /#/score-board/ page 

   This can si,ply be found by navigating to the `/#/score-board/` page.

   ><details><summary>Click for answer</summary>7efd3174f9dd5baa03a7882027f2824d2f72d86e</details>
