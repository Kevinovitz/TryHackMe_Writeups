![File Inclusion Banner](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/fileinc/File_Inclusion_Banner.png)

<p align="center">
   <img src="https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/fileinc/File_Inclusion_Cover.png" alt="File Inclusion Logo">
</p>

# File Inclusion

This guide contains the answer and steps necessary to get to them for the [File Inclusion](https://tryhackme.com/room/fileinc) room.

## Table of contents

- [Path Traversal](#path-traversal)
- [Local File Inclusion - LFI](#local-file-inclusion---lfi)
- [Local File Inclusion - LFI #2](#local-file-inclusion---lfi-2)
- [Challenge ](#challenge)

### Path Traversal

1. What function causes path traversal vulnerabilities in PHP?

   The answer can be found in the text.

   ><details><summary>Click for answer</summary>get_file_contents</details>

### Local File Inclusion - LFI

1. Give Lab #1 a try to read /etc/passwd. What would the request URI be?

   LFI1 PASSWORD 2

   ><details><summary>Click for answer</summary>/lab1.php?file=/etc/passwd</details>

2. In Lab #2, what is the directory specified in the include function?

   LFI1 DIRECTORY

   ><details><summary>Click for answer</summary>includes</details>

### Local File Inclusion - LFI #2

1. Give Lab #3 a try to read /etc/passwd. What is the request look like?

   LFI2 PASSWORD 1

   ><details><summary>Click for answer</summary>lab3.php?file=../../../../etc/passwd%00</details>

2. Which function is causing the directory traversal in Lab #4?

   The answer is the same as for the previous task.

   ><details><summary>Click for answer</summary>get_file_contents</details>

3. Try out Lab #6 and check what is the directory that has to be in the input field?

   LFI2 FOLDER PASSWD

   ><details><summary>Click for answer</summary>THM-profile</details>

4. Try out Lab #6 and read /etc/os-release. What is the VERSION_ID value?

   LFI2 OS

   ><details><summary>Click for answer</summary>12.04</details>

### Challenge 

1. Capture Flag1 at /etc/flag1

   

   ><details><summary>Click for answer</summary>F1x3d-iNpu7-f0rrn</details>

2. Capture Flag2 at /etc/flag2

   

   ><details><summary>Click for answer</summary>c00k13_i5_yuMmy1</details>

3. Capture Flag3 at /etc/flag3

   

   ><details><summary>Click for answer</summary>P0st_1s_w0rk1in9</details>

4. Gain RCE in Lab #Playground /playground.php with RFI to execute the hostname command. What is the output?

      

   ><details><summary>Click for answer</summary>lfi-vm-thm-f8c5b1a78692</details>




