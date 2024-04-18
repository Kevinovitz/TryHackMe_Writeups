![Linux Fundamentals Part 3 Banner](https://assets.tryhackme.com/room-banners/linuxfund.png)

<p align="center">
   <img src="https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/linuxfundamentalspart3/Linux_Fundamentals_3_Cover.png" alt="Linux Fundamentals Part 3 Logo">
</p>

# Linux Fundamentals Part 3

This guide contains the answer and steps necessary to get to them for the [Linux Fundamentals Part 3](https://tryhackme.com/room/linuxfundamentalspart3) room.

## Table of contents

- [Terminal Text Editors](#terminal-text-editors)
- [General/Useful Utilities](#generaluseful-utilities)
- [Processes 101](#processes-101)
- [Maintaining Your System: Automation](#maintaining-your-system-automation)
- [Maintaining Your System: Logs](#maintaining-your-system-logs)

### Terminal Text Editors

*Create a file using Nano.*

To create a file with `nano` we use the following command:

```cmd
nano textfile.txt
```

![Create Nano File](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/linuxfundamentalspart3/Linux_Fundamentals_3_Create_File.png)

Another method of creating and editing files is `vim`. More info can be found [here](https://vim.rtorr.com/).

1. Edit "task3" located in "tryhackme"'s home directory using Nano. What is the flag?

   We can log into the system using ssh and the provided credentials using:
   
   ```cmd
   ssh tryhackme@10.10.181.62
   ```
   
   Next we can edit the required file using:
   
   ```cmd
   nano task3
   ```
   
   ![Edit File](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/linuxfundamentalspart3/Linux_Fundamentals_3_Edit_File.png)
   
   Here we find our flag.

   ><details><summary>Click for answer</summary>THM{TEXT_EDITORS}</details>

### General/Useful Utilities

*Ensure you are connected to the deployed instance (MACHINE_IP)*

*Now, use Python 3's "HTTPServer" module to start a web server in the home directory of the "tryhackme" user on the deployed instance.*

To start the http server on the target machine we use the following command:

```cmd
python3 -m http.server
```

*Download the file http://MACHINE_IP:8000/.flag.txt onto the TryHackMe AttackBox*

3. What are the contents?

   To download the file we use the following command after setting up the http server:
   
   ```cmd
   wget http://10.10.181.62:8000/.flag.txt
   cat .flag.txt
   ```
   
   ![Transfer File](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/linuxfundamentalspart3/Linux_Fundamentals_3_Transfer_File.png)

   ><details><summary>Click for answer</summary>THM{WGET_WEBSERVER}</details>

*Create and download files to further apply your learning -- see how you can read the documentation on Python3's "HTTPServer" module.*

*Use Ctrl + C to stop the Python3 HTTPServer module once you are finished.*

### Processes 101

2. If we were to launch a process where the previous ID was "300", what would the ID of this new process be?

   The next process would have their pid incremented by 1.

   ><details><summary>Click for answer</summary>301</details>

3. If we wanted to cleanly kill a process, what signal would we send it?

   This is one of the signals we can send with the `kill` command.

   ><details><summary>Click for answer</summary>SIGTERM</details>

4. Locate the process that is running on the deployed instance (MACHINE_IP). What flag is given?

   To locate this process we use the `ps aux` command to list all running processes.
   
   ![Flag Process](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/linuxfundamentalspart3/Linux_Fundamentals_3_Flag_Proccess.png)

   ><details><summary>Click for answer</summary>THM{PROCESSES}</details>

5. What command would we use to stop the service "myservice"?

   This is done with the `systemctl` command.

   ><details><summary>Click for answer</summary>systemctl stop myservice</details>

6. What command would we use to start the same service on the boot-up of the system?

   This is also done with the `systemctl` command.

   ><details><summary>Click for answer</summary>systemctl enable myservice</details>

7. What command would we use to bring a previously backgrounded process back to the foreground?

   This can be done with the `fg` command.

   ><details><summary>Click for answer</summary>fg</details>

### Maintaining Your System: Automation

*Ensure you are connected to the deployed instance and look at the running crontabs.*

2. When will the crontab on the deployed instance (MACHINE_IP) run?

   To view the existing cronjobs on the machine we can use:
   
   ```cmd
   crontab -e
   ```
   
   ![Crontabs](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/linuxfundamentalspart3/Linux_Fundamentals_3_Crontabs.png)

   ><details><summary>Click for answer</summary>@reboot</details>

### Maintaining Your System: Logs

*Look for the apache2 logs on the deployable Linux machine*

2. What is the IP address of the user who visited the site?

   We can find the logs in `/var/log/apache2` folder.
   
   Looks like we don't have access to the log file. However, it looks like there is a backup of this file present in the same folder which we can view.
   
   ![Logs](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/linuxfundamentalspart3/Linux_Fundamentals_3_Logs.png)

   ><details><summary>Click for answer</summary>10.9.232.111</details>

3. What file did they access?

   In this same log file, we can see which file they accessed.

   ><details><summary>Click for answer</summary>catsanddogs.jpg</details>
