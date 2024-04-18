![Crack the Hash Banner](https://tryhackme.com/img/banners/default_tryhackme.png)

<p align="center">
   <img src="https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/crackthehash/Crack_The_Hash_Cover.png" alt="Crack the Hash Logo">
</p>

# Crack the Hash

This guide contains the answer and steps necessary to get to them for the [Crack the Hash](https://tryhackme.com/room/crackthehash) room.

### Level 1

In this task we will start with some easier hashes which can be cracked with online tools such as crackstation. However, I used a combination of online and local tools. 

1. 48bb6e862e54f2a795ffc4e541caed4d
   
   This looks like the classic MD5 hash. We can use multiple ways to identify the right hash. In this case I used 'hash-identifier' and the 'hashcat' auto detect function:

   ```cmd
   hashcat 48bb6e862e54f2a795ffc4e541caed4d /usr/share/wordlists/rockyou.txt
   ```

   ![1](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/crackthehash/Level_One_1.png)
   
   It is indeed MD5. This is mode 0 in hashcat.
   
   ```cmd
   hashcat -m 0 48bb6e862e54f2a795ffc4e541caed4d /usr/share/wordlists/rockyou.txt
   ```

   ![1 Password](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/crackthehash/Level_One_1_Password.png)

   ><details><summary>Click for answer</summary>easy</details>

2. CBFDAC6008F9CAB4083784CBD1874F76618D2A97 
   
   This time using 'hashcat' it seems this is a SHA-1 hash. This is mode 100 in hashcat.
   
   ```cmd
   hashcat CBFDAC6008F9CAB4083784CBD1874F76618D2A97 /usr/share/wordlists/rockyou.txt 
   ```

   ![2](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/crackthehash/Level_One_2.png)
   
   ```cmd
   hashcat -m 100 CBFDAC6008F9CAB4083784CBD1874F76618D2A97 /usr/share/wordlists/rockyou.txt
   ```

   ![2 Password](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/crackthehash/Level_One_2_Password.png)

   ><details><summary>Click for answer</summary>password123</details>

3. 1C8BFE8F801D79745C4631D09FFF36C82AA37FC4CCE4FC946683D7B336B63032
   
   Using hashcat auto detect we can find the hash type.

   ```cmd
   hashcat 1C8BFE8F801D79745C4631D09FFF36C82AA37FC4CCE4FC946683D7B336B63032 /usr/share/wordlists/rockyou.txt
   ```

   ![3](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/crackthehash/Level_One_3.png)
   
   Looks like a SHA-256 hash which is mode 1400 in hashcat.

   ```cmd
   hashcat -m 1400 1C8BFE8F801D79745C4631D09FFF36C82AA37FC4CCE4FC946683D7B336B63032 /usr/share/wordlists/rockyou.txt
   ```

   ![3 Password](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/crackthehash/Level_One_3_Password.png)

   ><details><summary>Click for answer</summary>letmein</details>

4. $2y$12$Dwt1BZj6pcyc3Dy1FWZ5ieeUznr71EeNkJkUlypTsgbX1H68wsRom
   
   This time neither hashcat nor hash-identifier could give me any hints. So I looked at the hashcat example page.

   ![4](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/crackthehash/Level_One_4.png)
   
   It looks very similar to a bcrypt hash. Running this takes a long time, so I filtered the wordlist per the hint given. 

   ```cmd
   touch rockyou2.txt
   awk 'length < 5' /usr/share/wordlists/rockyou.txt > rockyou2.txt
   ```

   ![4 Filter](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/crackthehash/Level_One_4_Filter.png)
   
   ```cmd
   hashcat -m 3200 passwd.hash rockyou2.txt     
   ```

   ![4 Password](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/crackthehash/Level_One_4_password.png)

   ><details><summary>Click for answer</summary>bleh</details>

5. 279412f945939ba78ce0758d3fd83daa
   
   This password appeared to be MD4. Unfortunately, however, neither hashcat nor john could crack it. 

   I therefore used crackstation. 
   
   ![5 Password](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/crackthehash/Level_One_5_Password.png)
   
   ><details><summary>Click for answer</summary>Eternity22</details>

### Level 2

In this task we will face some more challenging hashes which could be solved with hashcat and the hashcat example page. 

1. Hash: F09EDCB1FCEFC6DFB23DC3505A882655FF77375ED8AA2D1C13F640FCCC2D0C85
   
   Using hashcats auto detect mode, it looks to be a SHA-256 hash.

   ![1](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/crackthehash/Level_Two_1.png)
   
   This would be mode 1400 in hashcat.
   ```cmd
   hashcat -m 1400 F09EDCB1FCEFC6DFB23DC3505A882655FF77375ED8AA2D1C13F640FCCC2D0C85 /usr/share/wordlists/rockyou.txt
   ```

   ![1 Password](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/crackthehash/Level_Two_1_Password.png)

   ><details><summary>Click for answer</summary>paule</details>

2. Hash: 1DFECA0C002AE40B8619ECF94819CC1B
   
   This hash was a little trickier. I got the following suggestions. 

   ![2](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/crackthehash/Level_Two_2.png)
   
   I had to try multiple types. Eventually, NTLM seemed to do the trick. NTLM is mode 1000 in hashcat.

   ```cmd
   hashcat -m 1000 1DFECA0C002AE40B8619ECF94819CC1B /usr/share/wordlists/rockyou.txt
   ```

   ![2 Password](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/crackthehash/Level_Two_2_Password.png)

   ><details><summary>Click for answer</summary>n63umy8lkf4i</details>

3. Hash: $6$aReallyHardSalt$6WKUTqzq.UQQmrm0p/T7MPpMbGNnzXPMAXi4bJMl9be.cfi3/qxIf.hsGpS41BqMhSrHVXgMpdjS6xeKZAs02.

   Salt: aReallyHardSalt
   
   This time I used the hashcat example page to find out which hash type this was. It was similar to SHA-512crypt which is mode 1400 in hashcat.

   ![3](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/crackthehash/Level_Two_3.png)
   
   However, it would take a long time to crack, so I filtered the list again as per the hint. 

   ```cmd
   touch rockyou3.txt
   awk 'length < 7' /usr/share/wordlists/rockyou.txt > rockyou3.txt
   ```

   ![3 Wordlist](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/crackthehash/Level_Two_3_Wordlist.png)

   ```cmd
   hashcat -m 1800 passwd.hash rockyou3.txt --force
   ```

   ![3 Password](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/crackthehash/Level_Two_3_Password.png)
   
   ><details><summary>Click for answer</summary>waka99</details>

4. Hash: e5d8870e5bdd26602cab8dbe07a942c8669e56d6
   
   Salt: tryhackme
   
   The last hash was the most difficult and took some trail and error. 

   Hash-identifier didn't produce any correct suggestions.

   ![4 Examples](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/crackthehash/Level_Two_4_Examples.png)
   
   Looking at the example page, multiple candidates were found and tried. 

   ![4](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/crackthehash/Level_Two_4.png)
   
   Eventually, it appeared to be a HMAC-SHA1 hash.

   ```cmd
   hashcat -m 160 e5d8870e5bdd26602cab8dbe07a942c8669e56d6:tryhackme /usr/share/wordlists/rockyou.txt --force
   ```

   ![4 Password](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/crackthehash/Level_Two_4_Password.png)

   ><details><summary>Click for answer</summary>481616481616</details>
