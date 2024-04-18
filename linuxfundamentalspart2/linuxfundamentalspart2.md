![Linux Fundamentals Part 1 Banner](https://assets.tryhackme.com/room-banners/linuxfund.png)

<p align="center">
   <img src="https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/linuxfundamentalspart2/Linux_Fundamentals_2_Cover.png" alt="Linux Fundamentals Part 2 Logo">
</p>

# Linux Fundamentals Part 2

This guide contains the answer and steps necessary to get to them for the [Linux Fundamentals Part 2](https://tryhackme.com/room/linuxfundamentalspart2) room.

## Table of contents

- [Introduction to Flags and Switches](#introduction-to-flags-and-switches)
- [Filesystem Interaction Continued](#filesystem-interaction-continued)
- [Permissions 101](#permissions-101)
- [Common Directories](#common-directories)

### Introduction to Flags and Switches

We will begin by loggin into the machine via ssh.

```cmd
ssh tryhackme@10.10.161.119
```

2. What directional arrow key would we use to navigate down the manual page?

   ><details><summary>Click for answer</summary>down</details>

3. What flag would we use to display the output in a "human-readable" way?

Typing `ls --help` or `man ls` will give us the answer.

   ><details><summary>Click for answer</summary>-h</details>

### Filesystem Interaction Continued

1. How would you create the file named "newnote"?

For this we can use the `touch` command.

   ><details><summary>Click for answer</summary>touch newnote</details>

2. On the deployable machine, what is the file type of "unknown1" in "tryhackme's" home directory?

For this we can use the `file` command.

![File Type(https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/linuxfundamentalspart2/Linux_Fundamentals_2_File_Type.png)

   ><details><summary>Click for answer</summary>ASCII text</details>

3. How would we move the file "myfile" to the directory "myfolder" 

We can use `mv --help` to find the correct command.

![Move File](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/linuxfundamentalspart2/Linux_Fundamentals_2_Move_File.png)

   ><details><summary>Click for answer</summary>mv myfile myfolder</details>

4. What are the contents of this file?

Use `cat` to read the contents of a file.

![Myfile](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/linuxfundamentalspart2/Linux_Fundamentals_2_Myfile.png)

   ><details><summary>Click for answer</summary>THM{FILESYSTEM}</details>

### Permissions 101

1. On the deployable machine, who is the owner of "important"?

To find the owner of a file, we can use the command `ls -la` or `ls -lh` for less noise.

![Owner](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/linuxfundamentalspart2/Linux_Fundamentals_2_Owner.png)

   ><details><summary>Click for answer</summary>user2</details>

2. What would the command be to switch to the user "user2"?

   ><details><summary>Click for answer</summary>su user2</details>
   
3. Output the contents of "important", what is the flag?

Same as before, use `cat`.

   ><details><summary>Click for answer</summary>THM{SU_USER2}</details>

### Common Directories

These three questions can be answered using the information provided in the text.

2. What is the directory path that would we expect logs to be stored in?

   ><details><summary>Click for answer</summary>/var/log</details>

3. What root directory is similar to how RAM on a computer works?

   ><details><summary>Click for answer</summary>/tmp</details>

4. Name the home directory of the root user 

   ><details><summary>Click for answer</summary>/root</details>
