![John The Ripper Banner](https://assets.tryhackme.com/room-banners/johntheripper.png)

<p align="center">
   <img src="https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/johntheripper0/John_The_Ripper_Cover.png" alt="John The Ripper Logo">
</p>

# John The Ripper

This guide contains the answer and steps necessary to get to them for the [John The Ripper](https://tryhackme.com/room/johntheripper0) room.

## Table of contents

- [Setting up John the Ripper](#setting-up-john-the-ripper)
- [Wordlists](#wordlists)
- [Cracking Basic Hashes](#cracking-basic-hashes)
- [Cracking Windows Authentication Hashes](#cracking-windows-authentication-hashes)
- [Cracking /etc/shadow Hashes](#cracking-/etc/shadow-hashes)
- [Single Crack Mode](#single-crack-mode)
- [Custom Rules](#custom-rules)
- [Cracking Password Protected Zip Files](#cracking-password-protected-zip-files)
- [Cracking Password Protected RAR Archives](#cracking-password-protected-rar-archives)
- [Cracking SSH Keys with John ](#cracking-ssh-keys-with-john)

### Setting up John the Ripper

1. What is the most popular extended version of John the Ripper?

   ><details><summary>Click for answer</summary>Jumbo John</details>
   
### Wordlists

1.  What website was the rockyou.txt wordlist created from a breach on?

   ><details><summary>Click for answer</summary>rockyou.com</details>

### Cracking Basic Hashes

1. What type of hash is hash1.txt?

   The types can all be found using `hash-identifier`.

   BASIC 1 HASH

   ><details><summary>Click for answer</summary>MD5</details>

3. What is the cracked value of hash1.txt?

   The correct format here is `raw-md5`.

   ```cmd
   john hash1.txt --wordlist=/usr/share/wordlists/rockyou.txt --format=raw-md5
   ```

   BASIC 1 VALUE

   ><details><summary>Click for answer</summary>biscuit</details>

5. What type of hash is hash2.txt?

   BASIC 2 HASH

   ><details><summary>Click for answer</summary><SHA1/details>

6. What is the cracked value of hash2.txt

   The correct format here is `raw-sha1`.

   ```cmd
   john hash2.txt --wordlist=/usr/share/wordlists/rockyou.txt --format=raw-sha1
   ```

   BASIC 2 VALUE

   ><details><summary>Click for answer</summary>kangeroo</details>

8. What type of hash is hash3.txt?

   BASIC 3 HASH

   ><details><summary>Click for answer</summary>SHA256</details>

9. What is the cracked value of hash3.txt

   The correct format here is `raw-sha256`.

   ```cmd
   john hash3.txt --wordlist=/usr/share/wordlists/rockyou.txt --format=raw-sha256
   ```

   BASIC 3 VALUE

   ><details><summary>Click for answer</summary>microphone</details>

11. What type of hash is hash4.txt?

   BASIC 4 HASH

   After testing, SHA-512 didn't seem to work.

   ><details><summary>Click for answer</summary>Whirlpool</details>

11. What is the cracked value of hash4.txt

   The correct format here is `whirlpool`.

   ```cmd
   john hash4.txt --wordlist=/usr/share/wordlists/rockyou.txt --format=whirlpool
   ```

   BASIC 4 VALUE

   ><details><summary>Click for answer</summary>colossal</details>

### Cracking Windows Authentication Hashes

1. What do we need to set the "format" flag to, in order to crack this?

   As the name comes from NTHash, 'NT' might be a first guess. Looking at the available formats we can see this is indeed the case.

   ```cmd
   john --list=formats | grep -iF "nt" 
   ```

   WINDOWS FORMAT

   ><details><summary>Click for answer</summary>NT</details>

3. What is the cracked value of this password?

   We can use the following command with John to crack the NTLM hash.

   ```cmd
   john ntlm.txt --wordlist=/usr/share/wordlists/rockyou.txt --format=nt
   ```

   WINDOWS VALUE
   
   ><details><summary>Click for answer</summary>mushroom</details>

### Cracking /etc/shadow Hashes

1. What is the root password?

   For this question we can do multiple things. One is to simple copy the hash into a separate file and crack it with John. Or we can split the entries into their respective files and with `unshadow` create a single file we can use in John. For now I will use the latter method.

   ```cmd
   unshadow passwd.txt shadow.txt > Passwords.txt
   ```

   SHADOW FILE

   This gives us one file with the hash and username.

   ```cmd
   john Passwords.txt --wordlist=/usr/share/wordlists/rockyou.txt --format=sha512crypt
   ```

   SHADOW VALUE

   ><details><summary>Click for answer</summary>1234</details>

### Single Crack Mode




### Custom Rules




### Cracking Password Protected Zip Files




### Cracking Password Protected RAR Archives




### Cracking SSH Keys with John 



1. 

   

   ><details><summary>Click for answer</summary></details>
