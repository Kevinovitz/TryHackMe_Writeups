![Traverse Banner](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/traverse/Traverse_Banner.png)

<p align="center">
   <img src="https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/traverse/Traverse_Cover.png" alt="Traverse Logo">
</p>

# Traverse

This guide contains the answer and steps necessary to get to them for the [Traverse](https://tryhackme.com/r/room/traverse) room.

## Table of contents

- [Traverse](#traverse)

### Traverse

1. What type of encoding is used by the hackers to obfuscate the JavaScript file?

   We can see that the website has been hacked.

   MAIN PAGE

   If we look at the source code, we can see there is a custom Javascript file referenced.

   SOURCE

   When opening this script, we see it is obfuscated. If you do a little searching related to the format, you can find out what kind of encoding has been used.

   CUSTOM JS

   ><details><summary>Click for answer</summary>Hex</details>

2. What is the flag value after deobfuscating the file?

   Using Cyberchef, we can convert the Hex value to text. Here we can also make up some parts of the flag. But it is easier to run the script.

   FUNCTION

   To do this we add the function to a 'custom.js' file and create a simple html file that references the script.

   ```html
   <html>
   <head>
   <title>My Script</title>
   <script src='custom.js'></script>
   </head>
   <body></body>
   </html>
   ```

   When opening the page in a browser and navigate to the console in the developer pane we are given our flag.

   FLAG

   ><details><summary>Click for answer</summary>DIRECTORY LISTING IS THE ONLY WAY</details>

3. Logging is an important aspect. What is the name of the file containing email dumps?

   Judging from the previous flag, we should use server directories to find the files we are looking for. As we are looking for log files, lets try 'logs' first.

   DIRECTORY

   If this wouldn't work. A hint to the directory could also be found on the main webpage source.

   DIRECTORIES

   ><details><summary>Click for answer</summary>email_dump.txt</details>

4. The logs folder contains email logs and has a message for the software team lead. What is the name of the directory that Bob has created?

   The name is the same as the first phase of SSDLC.

   ><details><summary>Click for answer</summary>Planning</details>

5. What is the key file for opening the directory that Bob has created for Mark?

   The key to open the file will probably be the flag found in the message.

   ><details><summary>Click for answer</summary>THM{100100111}</details>

6. What is the email address for ID 5 using the leaked API endpoint?

   Navigating to the webpage '/planning' we are prompted to log in with the key.

   API FOLDER

   On the page we see the API call format. We can use this to request the data for user with ID=1.

   USER 5

   ><details><summary>Click for answer</summary>john@traverse.com</details>

7. What is the ID for the user with admin privileges?

   We could try every customer ID by hand, or we can utilize Burpsuite Intruder.

   In burpsuite we must first capture an API request call and send it to intruder. 

   1. Select the ID and add a selector for the attack.
   2. Add a payload consisting of a list of numbers ranging from 1-10.
   3. Use a sniper attack.
   4. Start the attack. 
   5. In the results window, navigate to response tab.
   6. The users role will be displayed here.

    BURPSUITE

   ><details><summary>Click for answer</summary>3</details>

8. What is the endpoint for logging in as theadmin? Mention the last endpoint instead of the URL. For example, if the answer is URL is tryhackme.com/admin - Just write/admin.

   In the API call for the admin user, we will also find the login url.

   ><details><summary>Click for answer</summary>/realadmin</details>

9. The attacker uploaded a web shell and renamed a file used for managing the server. Can you find the name of the web shell that the attacker has uploaded?

   Now that we have the admin login page and their credentials, we can log into the system.

   ADMIN LOGIN

   Here we have an admin panel to execute commands with on the underlying system. Unfortunately, there are only two commands for us to use.

   ADMIN PANEL

   However, if we take a closer look at the page source, we can see that the commands are listed in the item element. Perhaps we can change them. Lets try `ls`.

   ADMIN HACK

   It works! Input is not checked and we can execute arbitrary commands on the system. To make sending commands easier, lets login to the admin panel through burpsuite. We then capture one of the two available commands and send it to Repeater. Now we can easily issue any command we like!

   BURPSUITE COMMANDS

   From the available files, one of them seems to be the shell.

   ><details><summary>Click for answer</summary>thm_shell.php</details>

10. What is the name of the file renamed by the attacker for managing the web server?

    Using the same command as the previous questions, we can also see a file that has been renamed.

    ><details><summary>Click for answer</summary>renamed_file_manager.php</details>

11. Can you use the file manager to restore the original website by removing the "FINALLY HACKED" message? What is the flag value after restoring the main website?

    Looking at the renamed config file, we can see it generates some output, but it isn't clear. The files itself is also very large. So I doubt we need to do anything inside the file.
    
    CONFIG CAT
    
    I tried accessing the files through the browser, but it couldn't find it. Renaming it didn't work either.

    Perhaps we need to move it to another folder.

    Using the admin panel we can look for the other webpages. Looks like everything is stored in `var/www/html`.

    Lets move and rename the config file to this folder.

    ```console
    cp renamed_file_manager.php ../file_manager.php
    ```

    CONFIG LOGIN

    This worked! And now we can login to the config panel. The key has been provided to us previously and is located in the user folder for the realadmin.

    Here we have a list of available files.

    CONFIG FILES

    Lets edit `index.php` and remove the malicious text.

    RESTORED

   ><details><summary>Click for answer</summary>THM{WEBSITE_RESTORED}</details>

