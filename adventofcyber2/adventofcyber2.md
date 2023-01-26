<p align="center">
   <img src="https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/adventofcyber2/Advent_of_Cyber_2_2020_Logo.png" alt="Advent of Cyber 2 2020 Logo">
</p>

# Advent of Cyber 2 [2020]

This guide contains the answer and steps necessary to get to them for the [Advent of Cyber 2](https://tryhackme.com/room/adventofcyber2) room.

## Table of contents

- [[Day 1] [A Christmas Crisis](#day-1-a-christmas-crisis)
- [[Day 2] [The Elf Strikes Back!](#day-2-the-elf-strikes-back)
- [[Day 3] [Christmas Chaos](#day-3-christmas-chaos)
- [[Day 4] ](#day-4-)
- [[Day 5] ](#day-5-)
- [[Day 6] ](#day-6-)
- [[Day 7] ](#day-7-)
- [[Day 8] ](#day-8-)
- [[Day 9] ](#day-9-)
- [[Day 10] ](#day-10-)
- [[Day 11] ](#day-11-)
- [[Day 12] ](#day-12-)
- [[Day 13] ](#day-13-)
- [[Day 14] ](#day-14-)
- [[Day 15] ](#day-15-)
- [[Day 16] ](#day-16-)
- [[Day 17] ](#day-17-)
- [[Day 18] ](#day-18-)
- [[Day 19] ](#day-19-)
- [[Day 20] ](#day-20-)
- [[Day 21] ](#day-21-)
- [[Day 22] ](#day-22-)
- [[Day 23] ](#day-23-)
- [[Day 24] ](#day-24-)

### [Day 1] [A Christmas Crisis](https://github.com/Kevinovitz/TryHackMe_Writeups/tree/main/adventofcyber2/Day%2001)

In this task we will be using cookies to escalate our account priveleges and restart some Christmas services.

Register for an account, and then login.

1. What is the name of the cookie used for authentication?

After registering for an account, we see we cannot activate any services. So we need to open the developer tools to view our current cookie.

![Cookie](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/adventofcyber2/Day%2001/Crisis_Cookie.png)

   ><details><summary>Click for answer</summary>auth</details>

2. In what format is the value of this cookie encoded?

Judging from the characters, this might be hex encoded. Inputting the string in CyberChef, it indeed suggest hexadecimal encoding.

   ><details><summary>Click for answer</summary>Hexadecimal</details>

3. Having decoded the cookie, what format is the data stored in?

   If we use CyberChef to decode the string from `hex` it appears to be a JSON formatted string.
   
   ![Decoded Cookie](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/adventofcyber2/Day%2001/Crisis_Cookie_Decoded.png)

   ><details><summary>Click for answer</summary>JSON</details>

Figure out how to bypass the authentication.

4. What is the value of Santa's cookie?

   To log in as Santa, we need to change our cookie value. From the JSON formatted string we can see we need to substitute our username for `santa`. Now can encode this string back to hexadecimal with CyberChef.
   
   ![New Cookie](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/adventofcyber2/Day%2001/Crisis_Santa_Cookie.png)

   ><details><summary>Click for answer</summary>7b22636f6d70616e79223a22546865204265737420466573746976616c20436f6d70616e79222c2022757365726e616d65223a2273616e7461227d</details>

Now that you are the santa user, you can re-activate the assembly line!

5. What is the flag you're given when the line is fully active?

   After replacing our cookie with this new value and reloading the page, we see we can now activate the services. After activating them all, we get the flag.
   
   ![Restored](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/adventofcyber2/Day%2001/Crisis_Restored.png)

   ><details><summary>Click for answer</summary>THM{MjY0Yzg5NTJmY2Q1NzM1NjBmZWFhYmQy}</details>

### [Day 2] [The Elf Strikes Back!](https://github.com/Kevinovitz/TryHackMe_Writeups/tree/main/adventofcyber2/Day%2002)

In this task, we will try to upload a reverse shell to a server to gain access and read the flag.

ID number: `ODIzODI5MTNiYmYw`

1. What string of text needs adding to the URL to get access to the upload page?

   We need to login with the ID number given. We will use `GET` parameters to send extra information to the browser and the parameter is `id` with value `ODIzODI5MTNiYmYw`.
   
   ![Log In Page](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/adventofcyber2/Day%2002/Elf_Strikes_Login_Page.png)

   ><details><summary>Click for answer</summary>?id=ODIzODI5MTNiYmYw</details>

2. What type of file is accepted by the site?

   On the next page we can see an upload prompt. Apparently, it will accept images.
   
   ![Logged In](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/adventofcyber2/Day%2002/Elf_Strikes_Logged_In.png)

   ><details><summary>Click for answer</summary>Image</details>

Bypass the filter and upload a reverse shell.

3. In which directory are the uploaded files stored?

   To bypass the filter, we can use what we learned and try the `.jpg.php` extension. If configured improperly, it will think the file is an image. But first we need to modify our reverse shell which can be copied from `/usr/share/webshells/php-reverse-shell.php`. We need to add our ip address (tun0, since we are connected through a VPN) and a port that is available.
   
   ![PHP Shell](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/adventofcyber2/Day%2002/Elf_Strikes_PHP_Shell.png)
   
   ![Upload File](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/adventofcyber2/Day%2002/Elf_Strikes_Upload_File.png)
   
   This seems to have worked. To find where the file is located on the server we can use `DirSearch` to enumerate the directories using:
   
   ```cmd
   dirsearch -u 10.10.55.59 -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -r
   ```
   
   ![Dir Search](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/adventofcyber2/Day%2002/Elf_Strikes_Directory.png)
   
   Navigating to `uploads`, we can indeed see the file we just uploaded.
   
   ![File](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/adventofcyber2/Day%2002/Elf_Strikes_File.png)

   ><details><summary>Click for answer</summary>/uploads/</details>

4. What is the flag in /var/www/flag.txt?

   Before continueing we should open a listener with `netcat` on the port we specified in the reverse shell.
   
   ```cmd
   nc -nlvp 1337
   ```
   
   Now we can click on the file on the server and see if we get any incoming connections to our listener.
   
   ![Netcat ssh](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/adventofcyber2/Day%2002/Elf_Strikes_SSH.png)
   
   Now we can view the flag on the system with `cat /var/www/flag.txt`.
   
   ![Flag](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/adventofcyber2/Day%2002/Elf_Strikes_Flag.png)

   ><details><summary>Click for answer</summary>THM{MGU3Y2UyMGUwNjExYTY4NTAxOWJhMzhh}</details>

### [Day 3] [Christmas Chaos](https://github.com/Kevinovitz/TryHackMe_Writeups/tree/main/adventofcyber2/Day%200)



1. 

   ><details><summary>Click for answer</summary></details>

### [Day 4] []()



1. 

   ><details><summary>Click for answer</summary></details>

### [Day 5] []()



1. 

   ><details><summary>Click for answer</summary></details>

### [Day 6] []()



1. 

   ><details><summary>Click for answer</summary></details>

### [Day 7] []()



1. 

   ><details><summary>Click for answer</summary></details>

### [Day 8] []()



1. 

   ><details><summary>Click for answer</summary></details>

### [Day 9] []()



1. 

   ><details><summary>Click for answer</summary></details>

### [Day 10] []()



1. 

   ><details><summary>Click for answer</summary></details>

### [Day 11] []()



1. 

   ><details><summary>Click for answer</summary></details>

### [Day 12] []()



1. 

   ><details><summary>Click for answer</summary></details>

### [Day 13] []()



1. 

   ><details><summary>Click for answer</summary></details>

### [Day 14] []()



1. 

   ><details><summary>Click for answer</summary></details>

### [Day 15] []()



1. 

   ><details><summary>Click for answer</summary></details>

### [Day 16] []()



1. 

   ><details><summary>Click for answer</summary></details>

### [Day 17] []()



1. 

   ><details><summary>Click for answer</summary></details>

### [Day 18] []()



1. 

   ><details><summary>Click for answer</summary></details>

### [Day 19] []()



1. 

   ><details><summary>Click for answer</summary></details>

### [Day 20] []()



1. 

   ><details><summary>Click for answer</summary></details>

### [Day 21] []()



1. 

   ><details><summary>Click for answer</summary></details>

### [Day 22] []()



1. 

   ><details><summary>Click for answer</summary></details>

### [Day 23] []()



1. 

   ><details><summary>Click for answer</summary></details>

### [Day 24] []()



1. 

   ><details><summary>Click for answer</summary></details>

