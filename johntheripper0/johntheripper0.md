![John The Ripper Banner](https://assets.tryhackme.com/room-banners/johntheripper.png)

<p align="center">
   <img src="https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/johntheripper0/John_The_Ripper_Cover.png" alt="John The Ripper Logo">
</p>

# John The Ripper

This guide contains the answer and steps necessary to get to them for the [John The Ripper](https://tryhackme.com/room/johntheripper0) room.

## Table of contents

- [Setting up John the Ripper](#setting-up-john-the-ripper)
- [Wordlists](#wordlists)
- [Cracking Basic Hashes](#cracking-basic-hashes)
- [Cracking Windows Authentication Hashes](#cracking-windows-authentication-hashes)
- [Cracking /etc/shadow Hashes](#cracking-etcshadow-hashes)
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

   ![Basic 1 Hash](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/johntheripper0/John_The_Ripper_Basic_1_Hash.png)

   ><details><summary>Click for answer</summary>MD5</details>

3. What is the cracked value of hash1.txt?

   The correct format here is `raw-md5`.

   ```cmd
   john hash1.txt --wordlist=/usr/share/wordlists/rockyou.txt --format=raw-md5
   ```

   ![Basic 1 Value](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/johntheripper0/John_The_Ripper_Basic_1_Value.png)

   ><details><summary>Click for answer</summary>biscuit</details>

5. What type of hash is hash2.txt?

   ![Basic 2 Hash](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/johntheripper0/John_The_Ripper_Basic_2_Hash.png)

   ><details><summary>Click for answer</summary><SHA1/details>

6. What is the cracked value of hash2.txt

   The correct format here is `raw-sha1`.

   ```cmd
   john hash2.txt --wordlist=/usr/share/wordlists/rockyou.txt --format=raw-sha1
   ```

   BASIC 2 VALUE

   ><details><summary>Click for answer</summary>kangeroo</details>

8. What type of hash is hash3.txt?

   ![Basic 3 Hash](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/johntheripper0/John_The_Ripper_Basic_3_Hash.png)

   ><details><summary>Click for answer</summary>SHA256</details>

9. What is the cracked value of hash3.txt

   The correct format here is `raw-sha256`.

   ```cmd
   john hash3.txt --wordlist=/usr/share/wordlists/rockyou.txt --format=raw-sha256
   ```

   ![Basic 3 Value](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/johntheripper0/John_The_Ripper_Basic_3_Value.png)

   ><details><summary>Click for answer</summary>microphone</details>

11. What type of hash is hash4.txt?

   ![Basic 4 Hash](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/johntheripper0/John_The_Ripper_Basic_4_Hash.png)

   After testing, SHA-512 didn't seem to work.

   ><details><summary>Click for answer</summary>Whirlpool</details>

11. What is the cracked value of hash4.txt

   The correct format here is `whirlpool`.

   ```cmd
   john hash4.txt --wordlist=/usr/share/wordlists/rockyou.txt --format=whirlpool
   ```

   ![Basic 4 Value](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/johntheripper0/John_The_Ripper_Basic_4_Value.png)

   ><details><summary>Click for answer</summary>colossal</details>

### Cracking Windows Authentication Hashes

1. What do we need to set the "format" flag to, in order to crack this?

   As the name comes from NTHash, 'NT' might be a first guess. Looking at the available formats we can see this is indeed the case.

   ```cmd
   john --list=formats | grep -iF "nt" 
   ```

   ![Windows Format](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/johntheripper0/John_The_Ripper_Windows_Format.png)

   ><details><summary>Click for answer</summary>NT</details>

3. What is the cracked value of this password?

   We can use the following command with John to crack the NTLM hash.

   ```cmd
   john ntlm.txt --wordlist=/usr/share/wordlists/rockyou.txt --format=nt
   ```

   ![Windows Value](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/johntheripper0/John_The_Ripper_Windows_Value.png)

   ><details><summary>Click for answer</summary>mushroom</details>

### Cracking /etc/shadow Hashes

1. What is the root password?

   For this question we can do multiple things. One is to simple copy the hash into a separate file and crack it with John. Or we can split the entries into their respective files and with `unshadow` create a single file we can use in John. For now I will use the latter method.

   ```cmd
   unshadow passwd.txt shadow.txt > Passwords.txt
   ```

   ![Shadow File](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/johntheripper0/John_The_Ripper_Shadow_File.png)

   This gives us one file with the hash and username.

   ```cmd
   john Passwords.txt --wordlist=/usr/share/wordlists/rockyou.txt --format=sha512crypt
   ```

   ![Shadow Value](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/johntheripper0/John_The_Ripper_Shadow_Value.png)

   ><details><summary>Click for answer</summary>1234</details>

### Single Crack Mode

1. What is Joker's password?

   First we need to add the username in front of the hash, then we can use Johns single mode cracking.

   ```cmd
   joker:<hash>
   
   john --single --format=raw-md5 hash7.txt
   ```

   ![Single Value](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/johntheripper0/John_The_Ripper_Single_Value.png)

   ><details><summary>Click for answer</summary>Jok3r</details>

### Custom Rules

1.  What do custom rules allow us to exploit?

   This answer can be found in the text.

   ><details><summary>Click for answer</summary>password complexity predictability</details>

2. What rule would we use to add all capital letters to the end of the word?

   Using the information from the text we can get the answer.

   ><details><summary>Click for answer</summary>Az"[A-Z]"</details>

3. What flag would we use to call a custom rule called "THMRules"

    This can be found in the text.

   ><details><summary>Click for answer</summary>--rule=THMRules</details>
   
### Cracking Password Protected Zip Files

1.  What is the password for the secure.zip file?

   We first use `zip2john` to get a hash and then pass that through to john.

   ```cmd
   zip2john secure.zip > ziphash.txt

   john --wordlist=/usr/share/wordlists/rockyou.txt ziphash.txt
   ```

   ![Zip Password](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/johntheripper0/John_The_Ripper_Zip_Password.png)

   ><details><summary>Click for answer</summary>pass123</details>

2. What is the contents of the flag inside the zip file?

   ![Zip Flag](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/johntheripper0/John_The_Ripper_Zip_Flag.png)

   ><details><summary>Click for answer</summary>THM{w3ll_d0n3_h4sh_r0y4l}</details>
  
### Cracking Password Protected RAR Archives

1. What is the password for the secure.rar file?

   We first use `rar2john` to get a hash and then pass that through to john.

   ```cmd
   rar2john secure.rar > rarhash.txt

   john --wordlist=/usr/share/wordlists/rockyou.txt rarhash.txt
   ```

   ![Rar Password](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/johntheripper0/John_The_Ripper_Rar_Password.png)

   ><details><summary>Click for answer</summary>password</details>

1. What is the contents of the flag inside the zip file?

   ![Rar Flag](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/johntheripper0/John_The_Ripper_Rar_Flag.png)

   ><details><summary>Click for answer</summary>THM{r4r_4rch1ve5_th15_t1m3}</details>

### Cracking SSH Keys with John 

1. What is the SSH private key password?

   We first use `ssh2john` to get a hash and then pass that through to john.

   ```cmd
   ssh2john idrsa.id_rsa > sshhash.txt
   
   john --wordlist=/usr/share/wordlists/rockyou.txt sshhash.txt
   ```

   ![Ssh Password](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/johntheripper0/John_The_Ripper_Ssh_Password.png)

   ><details><summary>Click for answer</summary>mango</details>
