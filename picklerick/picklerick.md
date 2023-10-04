![Pickle Rick Banner](https://i.imgur.com/BkKtAkO.png)
<p align="center">
   <img src="https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/picklerick/Pickle_Rick_Cover.png" alt="Pickle Rick Logo">
</p>

# Pickle Rick

This guide contains the answer and steps necessary to get to them for the [Pickle Rick](https://tryhackme.com/room/picklerick) room.

### Pickle Rick 

In this room we are tasked with finding the three ingredients necessary to turn Rick back into a human by finding vulnerabilities in a web application.

1. What is the first ingredient that Rick needs?

   Lets do some enumeration first with `nmap` and `dirbuster`.

   `nmap` gives us two open ports 22 (ssh) and 80 (http).

   ```cmd
   sudo nmap -sS -sV 10.10.3.164
   ```

   NMAP

   Unfortunately, the ssh service require an authentication key and won't work with just a password.

   Dirbuster gives us a couple interesting and usefull results.

   ```cmd
   gobuster dir -u http://10.10.3.164/ -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -x php,html,txt
   ```

   DIRECTORIES

   As we can see we have a login page, assets directory with access, server-status page (no access, 403), and robots.txt.

   On the webpage itself, when looking at the source code, we can find Rick's username.

   HOMEPAGE USERNAME

   On the log in page, we try some basic SQL injection, but that doesn't work.

   For now, the assets directort doesn't contain anything of interest.

   Looking at the robots.txt file, we do come accross something interesting.

   ROBOTS

   Could this be our password? Login in with these credentials actually works and brings us to the portal screen.

   PORTAL LOGIN

   Here we see a command page with which we can execute commands. On the system itself?

   Unfortunately, all the other pages lead to a denied page.

   DENIED

   Lets try some commands. Using `whoami` we can indeed see, we can execute commands on the system.

   COMMANDS WHOAMI

   Lets try finding any interesting files with `ls`.

   COMMANDS FILES

   Reading the first file gives us an error telling that the command `cat` has been disabled.. 

   COMMANDS CAT

   Luckily for us, there are more ways to read a file. `nl` for example. Looks like we just found our first ingredient!

   FIRST INGREDIENT   

   ><details><summary>Click for answer</summary>mr. meeseek hair</details>

3. What is the second ingredient in Rick’s potion?

   The clue.txt file tells us to look at other system files for the ingredients.

   COMMANDS CLUE

   Lets look at the `home` folder for any other users. Looks like there is a rick folder.

   COMMANDS USERS

   Going through these folders we eventually come across a file with the second ingredient.

   SECOND INGREDIENT

   ><details><summary>Click for answer</summary>1 jerry tear</details>

5. What is the last and final ingredient?

   Another interesting folder to look at when we were enumerationg the system is the `root` folder. We don't have permissions to view the folder, so we must elevate our privileges somehow.

   Using `sudo -l` we can check what commands we are allowed to execute with sudo privileges.

   COMMANDS SUDO

   Looks like we can execute everything with sudo. So lets look in the root folder using: `sudo ls /root`.

   This works! And we can find a `3rd ingredient` file in this folder.

   THIRD INGREDIENT

   ><details><summary>Click for answer</summary>fleeb juice</details>
