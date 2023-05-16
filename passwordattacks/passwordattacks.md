![Password Attacks Banner](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/passwordattacks/Password_Attacks_Banner.png)

<p align="center">
   <img src="https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/passwordattacks/Password_Attacks_Cover.png" alt="Password Attacks Logo">
</p>

# Password Attacks

This guide contains the answer and steps necessary to get to them for the [Password Attacks](https://tryhackme.com/room/passwordattacks) room.

## Table of contents

- [Password Attacking Techniques](#password-attacking-techniques)
- [Password Profiling #1 - Default, Weak, Leaked, Combined , and Username Wordlists](#password-profiling-#1---default,-weak,-leaked,-combined-,-and-username-wordlists)
- [Password Profiling #2 - Keyspace Technique and CUPP](#password-profiling-#2---keyspace-technique-and-cupp)
- [Offline Attacks - Dictionary and Brute-Force](#offline-attacks---dictionary-and-brute-force)
- [Offline Attacks - Rule-Based](#offline-attacks---rule-based)
- [Online password attacks](#online-password-attacks)
- [Password spray attack ](#password-spray-attack)

### Password Attacking Techniques


1. Which type of password attack is performed locally?

   Password cracking is done after the password hash has been extracted to get the password itself. Password guessing is usually done online towards a service.

   ><details><summary>Click for answer</summary>Password Cracking</details>

### Password Profiling #1 - Default, Weak, Leaked, Combined , and Username Wordlists


1. What is the Juniper Networks ISG 2000 default password? 

   For this we can use one of the default passwords website provided. In this case I used `https://default-password.info`.
   
   PROFILING 1 JUNIPER

   ><details><summary>Click for answer</summary>netscreen:netscreen</details>

### Password Profiling #2 - Keyspace Technique and CUPP


1.  Run the following crunch command:crunch 2 2 01234abcd -o crunch.txt. How many words did crunch generate?

    After runnning the command we can see in the output how many lines are written to the file.
    
    ```cmd
    crunch 2 2 01234abcd -o crunch.txt
    ```
    
    PROFILING 2 CRUNCH LINES

   ><details><summary>Click for answer</summary>81</details>

2. What is the crunch command to generate a list containing THM@! and output to a file named tryhackme.txt?

   Lets break this down:
   
   - We need 5 characters
   - Special options using -t
   - Output to a file

   The argument for special characters is `^`.

   ><details><summary>Click for answer</summary>crunch 5 5 -t THM^^ -o tryhackme.txt</details>

### Offline Attacks - Dictionary and Brute-Force

1.  Considering the following hash: 8d6e34f987851aa599257d3831a1af040886842f. What is the hash type?

   We can use `hash-identifier` to find out what hash type this is.
   
   OFFLINE HASH

   ><details><summary>Click for answer</summary>SHA-1</details>

2. Perform a dictionary attack against the following hash: 8d6e34f987851aa599257d3831a1af040886842f. What is the cracked value? Use rockyou.txt wordlist.

   Lets first find out what the type of this hash is with `hash-identifier`.
   
   OFFLINE HASH 2
   
   Now we can look at the hashcat examples page what the correct argument for SHA-1 is.
   
   OFFLINE HASHTYPE
   
   Putting this together gives us the following command:
   
   ```cmd
   hashcat -a 0 -m 100 8d6e34f987851aa599257d3831a1af040886842f /usr/share/wordlists/rockyou.txt 
   ```
   
   OFFLINE DICTIONARY ATTACK

   ><details><summary>Click for answer</summary>sunshine</details>

3. Perform a brute-force attack against the following MD5 hash: e48e13207341b6bffb7fb1622282247b. What is the cracked value? Note the password is a 4 digit number: [0-9][0-9][0-9][0-9]

   For this we need to use the `-a` argument and the correct chartset from the help page.
   
   ```cmd
   hashcat -a 3 m 0 e48e13207341b6bffb7fb1622282247b ?d?d?d?d
   ```
   
   OFFLINE BRUTE FORCE

   ><details><summary>Click for answer</summary>1337</details>

### Offline Attacks - Rule-Based


1. What syntax would you use to create a rule to produce the following: "S[Word]NN  where N is Number and S is a symbol of !@? 

   For this we must use the knowledge we just learned.
   
   - It begins with the special character
   - Then the word
   - Lastly two digits

   ><details><summary>Click for answer</summary>Az"[0-9][0-9]" ^[!@]</details>

### Online password attacks


1. 

   

   ><details><summary>Click for answer</summary></details>

### Password spray attack 


1. 

   

   ><details><summary>Click for answer</summary></details>
