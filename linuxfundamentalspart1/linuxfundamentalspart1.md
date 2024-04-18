![Linux Fundamentals Part 1 Banner](https://assets.tryhackme.com/room-banners/linuxfund.png)

<p align="center">
   <img src="https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/linuxfundamentalspart1/Linux_Fundamentals_1_Cover.png" alt="Linux Fundamentals Part 1 Logo">
</p>

# Linux Fundamentals Part 1

This guide contains the answer and steps necessary to get to them for the [Linux Fundamentals Part 1](https://tryhackme.com/room/linuxfundamentalspart1) room.

## Table of contents

- [A Bit of Background on Linux](#a-bit-of-background-on-linux)
- [Running Your First few Commands](#running-your-first-few-commands)
- [Interacting With the Filesystem!](#interacting-with-the-filesystem)
- [Searching for Files](#searching-for-files)
- [An Introduction to Shell Operators](#an-introduction-to-shell-operators)

### A Bit of Background on Linux

1. Research: What year was the first release of a Linux operating system? 

   A quick Google search gives us the answer.
   
   ><details><summary>Click for answer</summary>1991</details>

### Running Your First few Commands

1. If we wanted to output the text "TryHackMe", what would our command be?
   
   ><details><summary>Click for answer</summary>echo TryHackMe</details>

2. What is the username of who you're logged in as on your deployed Linux machine?
   
   Type `whoami` to find out who you are logged in as.
   
   ><details><summary>Click for answer</summary>tryhackme</details>

### Interacting With the Filesystem!


1. On the Linux machine that you deploy, how many folders are there?
   
   Use `ls -la` to find out how many folders are present.

   ><details><summary>Click for answer</summary>4</details>
   
2. Which directory contains a file?
   
   Use `cd` to navigate to each folder and then use `ls` to find any files.
   
   ><details><summary>Click for answer</summary>folder4</details>

3. What is the contents of this file?
   
   Read the content of the file using `cat ...txt`.
   
   ><details><summary>Click for answer</summary>Hello World</details>

4. Use the cd command to navigate to this file and find out the new current working directory. What is the path?
   
   Use `cd` to navigate to the file if not already done. Then use `pwd` to print the current working directory.
   
   ><details><summary>Click for answer</summary>/home/tryhackme/folder4</details>

### Searching for Files

1. Use grep on "access.log" to find the flag that has a prefix of "THM". What is the flag?
   
   Use the `grep` command to find any string in a file.
      
   ```cmd
   grep "THM" access.log
   ```
   
   ><details><summary>Click for answer</summary>THM{ACCESS}</details>

### An Introduction to Shell Operators

1. If we wanted to run a command in the background, what operator would we want to use?
   
   The `&` operator allows you to run a command in the backgroun.
   
   ><details><summary>Click for answer</summary>&</details>

2. If I wanted to replace the contents of a file named "passwords" with the word "password123", what would my command be?

   To replace the contents of a file, use the `>` operator.
   
   ><details><summary>Click for answer</summary>echo password123 > passwords</details>
   
3. Now if I wanted to add "tryhackme" to this file named "passwords" but also keep "passwords123", what would my command be
   
   To add text to a file without deleting anything, us the `>>` operator.
   
   ><details><summary>Click for answer</summary>echo tryhackme >> passwords</details>
