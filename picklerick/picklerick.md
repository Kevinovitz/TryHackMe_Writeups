![Pickle Rick Banner](https://i.imgur.com/BkKtAkO.png)
<p align="center">
   <img src="https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/picklerick/Pickle_Rick_Cover.png" alt="Pickle Rick Logo">
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

   ![Nmap](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/picklerick/Pickle_Rick_Nmap.png)

   Unfortunately, the ssh service require an authentication key and won't work with just a password.

   Dirbuster gives us a couple interesting and usefull results.

   ```cmd
   gobuster dir -u http://10.10.3.164/ -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -x php,html,txt
   ```

   ![Directories](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/picklerick/Pickle_Rick_Directories.png)

   As we can see we have a login page, assets directory with access, server-status page (no access, 403), and robots.txt.

   On the webpage itself, when looking at the source code, we can find Rick's username.

   ![Homepage Username](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/picklerick/Pickle_Rick_Homepage_Username.png)

   On the log in page, we try some basic SQL injection, but that doesn't work.

   For now, the assets directort doesn't contain anything of interest.

   Looking at the robots.txt file, we do come accross something interesting.

   ![Robots](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/picklerick/Pickle_Rick_Robots.png)

   Could this be our password? Login in with these credentials actually works and brings us to the portal screen.

   ![Portal Login](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/picklerick/Pickle_Rick_Portal_Login.png)

   Here we see a command page with which we can execute commands. On the system itself?

   Unfortunately, all the other pages lead to a denied page.

   ![Denied](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/picklerick/Pickle_Rick_Denied.png)

   Lets try some commands. Using `whoami` we can indeed see, we can execute commands on the system.

   ![Commands Whoami](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/picklerick/Pickle_Rick_Commands_Whoami.png)

   Lets try finding any interesting files with `ls`.

   ![Commands Files](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/picklerick/Pickle_Rick_Commands_Files.png)

   Reading the first file gives us an error telling that the command `cat` has been disabled.. 

   ![Commands Cat](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/picklerick/Pickle_Rick_Commands_Cat.png)

   Luckily for us, there are more ways to read a file. `nl` for example. Looks like we just found our first ingredient!

   ![First Ingredient](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/picklerick/Pickle_Rick_First_Ingredient.png)

   ><details><summary>Click for answer</summary>mr. meeseek hair</details>

3. What is the second ingredient in Rick’s potion?

   The clue.txt file tells us to look at other system files for the ingredients.

   ![Commands Clue](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/picklerick/Pickle_Rick_Commands_Clue.png)

   Lets look at the `home` folder for any other users. Looks like there is a rick folder.

   ![Commands Users](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/picklerick/Pickle_Rick_Commands_Users.png)

   Going through these folders we eventually come across a file with the second ingredient.

   ![Second Ingredient](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/picklerick/Pickle_Rick_Second_Ingredient.png)

   ><details><summary>Click for answer</summary>1 jerry tear</details>

5. What is the last and final ingredient?

   Another interesting folder to look at when we were enumerationg the system is the `root` folder. We don't have permissions to view the folder, so we must elevate our privileges somehow.

   Using `sudo -l` we can check what commands we are allowed to execute with sudo privileges.

   ![Commands Sudo](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/picklerick/Pickle_Rick_Commands_Sudo.png)

   Looks like we can execute everything with sudo. So lets look in the root folder using: `sudo ls /root`.

   This works! And we can find a `3rd ingredient` file in this folder.

   ![Third Ingredient](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/picklerick/Pickle_Rick_Third_Ingredient.png)

   ><details><summary>Click for answer</summary>fleeb juice</details>
