![Mal Introductory Banner](https://i.imgur.com/2GCM5pZ.png)

<p align="center">
   <img src="https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/malmalintroductory/Malware_Introductory_Cover.png" alt="Malware Introductory Logo">
</p>

# [Vulnversity](https://github.com/Kevinovitz/TryHackMe_Writeups/tree/main/malmalintroductory)

This guide contains the answer and steps necessary to get to them for the [MAL: Malware Introductory](https://tryhackme.com/room/malmalintroductory) room.

In this room, a number of questions need to be answered by doing a little research online. Since this is fairly straightforward, I will not be addressed these questions.

## Table of contents

- [Obtaining MD5 Checksums of Provided Files](#obtaining-md5-checksums-of-provided-files)
- [Now lets see if the MD5 Checksums have been analysed before](#now-lets-see-if-the-md5-checksums-have-been-analysed-before)
- [Identifying if the Executables are obfuscated / packed](#identifying-if-the-executables-are-obfuscated--packed)
- [What is Obfuscation / Packing?](#what-is-obfuscation--packing)
- [Introduction to Strings](#introduction-to-strings)
- [Introduction to Imports](#introduction-to-imports)
- [Practical Summary](#practical-summary)

## Obtaining MD5 Checksums of Provided Files

After connecting to the Windows machine we can obtain the hashes of the files using Hashtab. This utility is built-in to the properties window when selecting the file.

1. The MD5 Checksum of aws.exe 

   ![MD5 Hash Aws](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/malmalintroductory/MAL_Aws_Checksum.png)

   ><details><summary>Click for answer</summary>D2778164EF643BA8F44CC202EC7EF157</details>

2. The MD5 Checksum of Netlogo.exe

   ![Md5 Hash Netlogo](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/malmalintroductory/MAL_NetLogo_Checksum.png)

   ><details><summary>Click for answer</summary>59CB421172A89E1E16C11A428326952C</details>

3. The MD5 Checksum of vlc.exe

   ![Md5 Hash Vlc](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/malmalintroductory/MAL_Vlc_Checksum.png)

   ><details><summary>Click for answer</summary>5416BE1B8B04B1681CB39CF0E2CAAD9F</details>

## Now lets see if the MD5 Checksums have been analysed before

Now we should use [VirusTotal](https://www.virustotal.com/gui/home/search) to find out if these hashes (and as such, the original executables) have been analysed.

1. Does Virustotal report this MD5 Checksum / file aws.exe as malicious? (Yay/Nay)

   ![Virus Total Aws](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/malmalintroductory/MAL_VT_Aws.png)

   ><details><summary>Click for answer</summary>Nay</details>

2. Does Virustotal report this MD5 Checksum / file Netlogo.exe as malicious? (Yay/Nay)

   ![Virus Total Netlogo](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/malmalintroductory/MAL_VT_NetLogo.png)

   ><details><summary>Click for answer</summary>Nay</details>

3. Does Virustotal report this MD5 Checksum / file vlc.exe as malicious? (Yay/Nay)

   ![Virus Total Vlc](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/malmalintroductory/MAL_VT_Vlc.png)

   ><details><summary>Click for answer</summary>Nay</details>

## Identifying if the Executables are obfuscated / packed

In this task we wil use PEiD to find out more information about the files. Especially which packer has been used to pack the files.

1. What does PeID propose 1DE9176AD682FF.dll being packed with?

   ![Packer 1](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/malmalintroductory/MAL_Packer_1.png)

   ><details><summary>Click for answer</summary>Microsoft Visual C++ 6.0 DLL</details>

2. What does PeID propose AD29AA1B.bin being packed with?

   ![Packer 2](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/malmalintroductory/MAL_Packer_2.png)

   ><details><summary>Click for answer</summary>Microsoft Visual C++ 6.0</details>

## What is Obfuscation / Packing?

In this task we use the same method as in the previous task to get more information about the packing method of the file.

1. What packer does PeID report file "6F431F46547DB2628" to be packed with?

   ![Packer 3](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/malmalintroductory/MAL_Packer_3.png)

   ><details><summary>Click for answer</summary>FSG 1.0 -> dulek/xt</details>

## Introduction to Strings

In this task we will try to find out more about the files by extracting any strings present in the file.

1. What is the URL that is outputted after using "strings"

   We first navigate to the folder containing SysInternalTools.
   
   ```cmd
   cd C:\Users\Analysis\Desktop\Tools\SysInternalsSuite
   ```
   
   The we use the following command to extract any strings from the file:
   
   ```cmd
   strings "C:\Users\Analysis\Desktop\Task 12\67844C01"
   ```

   ![Strings Command](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/malmalintroductory/MAL_Strings_Command.png)
   
   Scrolling through the results we can find the URL we are looking for.
   
   ![Strings Result](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/malmalintroductory/MAL_Strings_Result.png)

   ><details><summary>Click for answer</summary>practicalmalwareanalysis.com</details>

2. How many unique "Imports" are there?

   The same information can also be found using PE Explorer. After importing the file into the program, we can navigate to `view/imports` to get an answer to the question.
   
   ![Pe Explorer](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/malmalintroductory/MAL_Pe_Explorer.png)

   ><details><summary>Click for answer</summary>5</details>

## Introduction to Imports

In this task we will use IDA to find more information about the files.

1. How many references are there to the library "msi" in the "Imports" tab of IDA Freeware for "install.exe"

   After opening the file in IDA we select the portable executable to import.
   
   ![Load Executable](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/malmalintroductory/MAL_Load_Exe.png)
   
   After importing the executable we go to the imports tab and look for any MSI libraries.
   
   ![Ida imports](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/malmalintroductory/MAL_Ida_Msi.png)

   ><details><summary>Click for answer</summary>9</details>

## Practical Summary

In this last task we will use the skills we have learned so far to find the answers to the next questions.

1. What is the MD5 Checksum of the file?

   We can open the properties window after selecting the file.
   
   ![Calculator MD5](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/malmalintroductory/MAL_Calc_MD5.png)

   ><details><summary>Click for answer</summary>f5bd8e6dc6782ed4dfa62b8215bdc429</details>

2. Does Virustotal report this file as malicious? (Yay/Nay)

   For this we use the hash we found and look it up on VirusTotal.
   
   ![Calculator Virus Total](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/malmalintroductory/MAL_Calc_VT.png)

   ><details><summary>Click for answer</summary>Yay</details>

Output the strings using Sysinternals "strings" tool.

3. What is the last string outputted?

   We can use the following command to find the strings in the executable.
   
   ```cmd
   strings "C:\Users\Analysis\Desktop\Task 14\ComplexCalculator.exe"
   ```
   
   ![Calculator Strings](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/malmalintroductory/MAL_Calc_Strings.png)

   ><details><summary>Click for answer</summary>d:h:</details>

4. What is the output of PeID when trying to detect what packer is used by the file?

   For this question we use PEiD and import the file. 
   
   ![Calculator PE ID](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/malmalintroductory/MAL_Calc_Packer.png)

   ><details><summary>Click for answer</summary>Nothing Found</details>
