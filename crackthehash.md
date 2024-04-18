![Crack the Hash Banner](https://tryhackme.com/img/banners/default_tryhackme.png)

<p align="center">
   <img src="https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/crackthehash/Crack_The_Hash_Cover.png" alt="Crack the Hash Logo">
</p>

# Crack the Hash

This guide contains the answer and steps necessary to get to them for the [Crack the Hash](https://tryhackme.com/room/crackthehash) room.

### Level 1



1. 48bb6e862e54f2a795ffc4e541caed4d
   
   ```cmd
   hashcat 48bb6e862e54f2a795ffc4e541caed4d /usr/share/wordlists/rockyou.txt
   ```
   
   ```cmd
   hashcat -m 0 48bb6e862e54f2a795ffc4e541caed4d /usr/share/wordlists/rockyou.txt
   ```

   ![1](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/crackthehash/Level_One_1.png)
   
   ![1 Password](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/crackthehash/Level_One_1_Password.png)

   
   ><details><summary>Click for answer</summary>easy</details>

2. CBFDAC6008F9CAB4083784CBD1874F76618D2A97 
   
   ```cmd
   hashcat CBFDAC6008F9CAB4083784CBD1874F76618D2A97 /usr/share/wordlists/rockyou.txt 
   ```
   ```cmd
   hashcat -m 100 CBFDAC6008F9CAB4083784CBD1874F76618D2A97 /usr/share/wordlists/rockyou.txt
   ```
   
   ![2](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/crackthehash/Level_One_2.png)
   
   ![2 Password](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/crackthehash/Level_One_2_Password.png)

   
   ><details><summary>Click for answer</summary>password123</details>

3. 1C8BFE8F801D79745C4631D09FFF36C82AA37FC4CCE4FC946683D7B336B63032
   
   ```cmd
   hashcat 1C8BFE8F801D79745C4631D09FFF36C82AA37FC4CCE4FC946683D7B336B63032 /usr/share/wordlists/rockyou.txt
   ```
   ```cmd
   hashcat -m 1400 1C8BFE8F801D79745C4631D09FFF36C82AA37FC4CCE4FC946683D7B336B63032 /usr/share/wordlists/rockyou.txt
   ```

   ![3](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/crackthehash/Level_One_3.png)
   
   ![3 Password](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/crackthehash/Level_One_3_Password.png)

   ><details><summary>Click for answer</summary>letmein</details>

4. $2y$12$Dwt1BZj6pcyc3Dy1FWZ5ieeUznr71EeNkJkUlypTsgbX1H68wsRom
   
   ```cmd
   touch rockyou2.txt
   awk 'length < 5' /usr/share/wordlists/rockyou.txt > rockyou2.txt
   ```
   ```cmd
   hashcat -m 3200 passwd.hash rockyou2.txt     
   ```

   ![4](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/crackthehash/Level_One_4.png)
   
   ![4 Filter](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/crackthehash/Level_One_4_Filter.png)
   
   ![4 Password](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/crackthehash/Level_One_4_password.png)

   ><details><summary>Click for answer</summary>bleh</details>

5. 279412f945939ba78ce0758d3fd83daa
   
   used crackstation
   
   ><details><summary>Click for answer</summary>Eternity22</details>

### Level 2



1. Hash: F09EDCB1FCEFC6DFB23DC3505A882655FF77375ED8AA2D1C13F640FCCC2D0C85
   
   ```cmd
   hashcat -m 1400 F09EDCB1FCEFC6DFB23DC3505A882655FF77375ED8AA2D1C13F640FCCC2D0C85 /usr/share/wordlists/rockyou.txt
   ```

   ![1](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/crackthehash/Level_Two_1.png)
   
   ![1 Password](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/crackthehash/Level_Two_1_Password.png)

   ><details><summary>Click for answer</summary>paule</details>

2. Hash: 1DFECA0C002AE40B8619ECF94819CC1B
   
   ```cmd
   hashcat -m 1000 1DFECA0C002AE40B8619ECF94819CC1B /usr/share/wordlists/rockyou.txt
   ```

   ![2](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/crackthehash/Level_Two_2.png)
   
   ![2 Password](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/crackthehash/Level_Two_2_Password.png)

   ><details><summary>Click for answer</summary>n63umy8lkf4i</details>

3. Hash: $6$aReallyHardSalt$6WKUTqzq.UQQmrm0p/T7MPpMbGNnzXPMAXi4bJMl9be.cfi3/qxIf.hsGpS41BqMhSrHVXgMpdjS6xeKZAs02.
   
   Salt: aReallyHardSalt
   
   ```cmd
   touch rockyou3.txt
   awk 'length < 7' /usr/share/wordlists/rockyou.txt > rockyou3.txt
   ```
   ```cmd
   hashcat -m 1800 passwd.hash rockyou3.txt --force
   ```

   ![3](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/crackthehash/Level_Two_3.png)
   
   ![3 Password](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/crackthehash/Level_Two_3_Password.png)
   
   ![3 Wordlist](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/crackthehash/Level_Two_3_Wordlist.png)

   

   ><details><summary>Click for answer</summary>waka99</details>

4. Hash: e5d8870e5bdd26602cab8dbe07a942c8669e56d6
   
   Salt: tryhackme
   
   ```cmd
   hashcat -m 160 e5d8870e5bdd26602cab8dbe07a942c8669e56d6:tryhackme /usr/share/wordlists/rockyou.txt --force
   ```
   
   ![4](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/crackthehash/Level_Two_4.png)
   
   ![4 Examples](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/crackthehash/Level_Two_4_Examples.png)
   
   ![4 Password](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/crackthehash/Level_Two_4_Password.png)

   

   ><details><summary>Click for answer</summary>481616481616</details>
