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



   ><details><summary>Click for answer</summary></details>

   Now try to do the same trick and see if you can log in as arthur.

2. What is the flag that you found in arthur's account?



   ><details><summary>Click for answer</summary></details>

### Software Integrity Failures

1. What is the SHA-256 hash of https://code.jquery.com/jquery-1.12.4.min.js?



   ><details><summary>Click for answer</summary></details>

### Data Integrity Failures

1. Try logging into the application as guest. What is guest's account password?



   ><details><summary>Click for answer</summary></details>

2. What is the name of the website's cookie containing a JWT token?



   ><details><summary>Click for answer</summary></details>

   Use the knowledge gained in this task to modify the JWT token so that the application thinks you are the user "admin".

3. What is the flag presented to the admin user?



   ><details><summary>Click for answer</summary></details>

### Security Logging and Monitoring Failures

1. What IP address is the attacker using?



   ><details><summary>Click for answer</summary></details>

2. What kind of attack is being carried out?



   ><details><summary>Click for answer</summary></details>
   
### Server-Side Request Forgery (SSRF) 

1. Explore the website. What is the only host allowed to access the admin area?



   ><details><summary>Click for answer</summary></details>

2. Check the "Download Resume" button. Where does the server parameter point to?



   ><details><summary>Click for answer</summary></details>

3. Using SSRF, make the application send the request to your AttackBox instead of the secure file storage. Are there any API keys in the intercepted request?



   ><details><summary>Click for answer</summary></details>

   Going the Extra Mile: There's a way to use SSRF to gain access to the site's admin area. Can you find it? 

   Note: You won't need this flag to progress in the room. You are expected to do some research in order to achieve your goal.
