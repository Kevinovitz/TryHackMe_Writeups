<p align="center">
   <img src="https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/malmalintroductory/Malware_Introductory_Cover.png" alt="Malware Introductory Logo">
</p>

# [Vulnversity](https://github.com/Kevinovitz/TryHackMe_Writeups/tree/main/malmalintroductory)

This guide contains the answer and steps necessary to get to them for the [MAL: Malware Introductory](https://tryhackme.com/room/malmalintroductory) room.

In this room, a number of questions need to be answered by doing a little research online. Since this is fairly straightforward, I will not be addressed these questions.

## Table of contents

- [Obtaining MD5 Checksums of Provided Files](#Obtaining MD5 Checksums of Provided Files)
- [Now lets see if the MD5 Checksums have been analysed before](#Now lets see if the MD5 Checksums have been analysed before)
- [Identifying if the Executables are obfuscated / packed](#Identifying if the Executables are obfuscated / packed)
- [What is Obfuscation / Packing?](#What is Obfuscation / Packing?)
- [Introduction to Strings](#Introduction to Strings)
- [Introduction to Imports](#Introduction to Imports)
- [Practical Summary](#Practical Summary)

## Obtaining MD5 Checksums of Provided Files



1. The MD5 Checksum of aws.exe 

   

   ><details><summary>Click for answer</summary></details>

2. The MD5 Checksum of Netlogo.exe

   

   ><details><summary>Click for answer</summary></details>

3. The MD5 Checksum of vlc.exe

   

   ><details><summary>Click for answer</summary></details>

## Now lets see if the MD5 Checksums have been analysed before



1. Does Virustotal report this MD5 Checksum / file aws.exe as malicious? (Yay/Nay)

   

   ><details><summary>Click for answer</summary></details>

2. Does Virustotal report this MD5 Checksum / file Netlogo.exe as malicious? (Yay/Nay)

   

   ><details><summary>Click for answer</summary></details>

3. Does Virustotal report this MD5 Checksum / file vlc.exe as malicious? (Yay/Nay)

   

   ><details><summary>Click for answer</summary></details>

## Identifying if the Executables are obfuscated / packed



1. What does PeID propose 1DE9176AD682FF.dll being packed with?

   

   ><details><summary>Click for answer</summary></details>

2. What does PeID propose AD29AA1B.bin being packed with?

   

   ><details><summary>Click for answer</summary></details>

## What is Obfuscation / Packing?


1. What packer does PeID report file "6F431F46547DB2628" to be packed with?

   

   ><details><summary>Click for answer</summary></details>

## Introduction to Strings



1. What is the URL that is outputted after using "strings"

   

   ><details><summary>Click for answer</summary></details>

2. How many unique "Imports" are there?

   

   ><details><summary>Click for answer</summary></details>

## Introduction to Imports



1. How many references are there to the library "msi" in the "Imports" tab of IDA Freeware for "install.exe"

   

   ><details><summary>Click for answer</summary></details>

## Practical Summary



1. What is the MD5 Checksum of the file?

   

   ><details><summary>Click for answer</summary></details>

2. Does Virustotal report this file as malicious? (Yay/Nay)

   

   ><details><summary>Click for answer</summary></details>

Output the strings using Sysinternals "strings" tool.

3. What is the last string outputted?

   

   ><details><summary>Click for answer</summary></details>

4. What is the output of PeID when trying to detect what packer is used by the file?

   

   ><details><summary>Click for answer</summary></details>
