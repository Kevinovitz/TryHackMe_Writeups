![Obfuscation - The Egg Shell File Banner](https://tryhackme-images.s3.eu-west-1.amazonaws.com/room-icons/5f9c7574e201fe31dad228fc-1763962125617)

<p align="center">
   <img src="https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/obfuscation-aoc2025-e5r8t2y6u9/Obfuscation_-_The_Egg_Shell_File_Cover.png" alt="Obfuscation - The Egg Shell File Logo">
</p>

# <img src="https://tryhackme-images.s3.amazonaws.com/room-icons/5f9c7574e201fe31dad228fc-1763962163689" alt="image" style="vertical-align: middle;height: 50px;" /> Obfuscation - The Egg Shell File | Advent of Cyber 2025 - Day 18

This guide contains the answer and steps necessary to get to them for the [Obfuscation - The Egg Shell File](https://tryhackme.com/room/obfuscation-aoc2025-e5r8t2y6u9) room.

## Table of contents

- [Obfuscation & Deobfuscation](#obfuscation--deobfuscation)

### Obfuscation & Deobfuscation

1.  What is the first flag you get after deobfuscating the C2 URL and running the script?

    In the first part of the script we see a variable we need to decode. 

    ![Part1](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/obfuscation-aoc2025-e5r8t2y6u9/Obfuscation_-_The_Egg_Shell_File_Part1.png)

    Lets add this to Cyberchef and use the recipe "From Base64". This should give us a valid URL. We will paste this back into the script and run the script.

    ![Flag1](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/obfuscation-aoc2025-e5r8t2y6u9/Obfuscation_-_The_Egg_Shell_File_Flag1.png)

    ><details><summary>Click for answer</summary>THM{C2_De0bfuscation_29838}</details>

2.  What is the second flag you get after obfuscating the API key and running the script again?

    In the second part of the script is an API key we need to obfuscate using XOR. Then add it back into the script.

    ![Part2](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/obfuscation-aoc2025-e5r8t2y6u9/Obfuscation_-_The_Egg_Shell_File_Part2.png)

    We copy the API key into Cyberchef and add the 'XOR' recipe. Set the key to '0x37' HEX. Next, add the 'To HEX' recipe. 
    
    ![Obfuscate](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/obfuscation-aoc2025-e5r8t2y6u9/Obfuscation_-_The_Egg_Shell_File_Obfuscate.png)
    
    Paste back the result and re-run the script.

    ![Flag2](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/obfuscation-aoc2025-e5r8t2y6u9/Obfuscation_-_The_Egg_Shell_File_Flag2.png)

    ><details><summary>Click for answer</summary>THM{API_Obfusc4tion_ftw_0283}</details>

3.  If you want to learn more about Obfuscation, check out our [Obfuscation Principles](https://tryhackme.com/room/obfuscationprinciples) room!
