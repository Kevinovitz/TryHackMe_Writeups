<p align="center">
   <img src="https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/linuxfundamentalspart3/Linux_Fundamentals_3_Cover.png" alt="Linux Fundamentals Part 3 Logo">
</p>

# Linux Fundamentals Part 3

This guide contains the answer and steps necessary to get to them for the [Linux Fundamentals Part 3](https://tryhackme.com/room/linuxfundamentalspart3) room.

## Table of contents

- [Terminal Text Editors](#terminal-text-editors)
- [General/Useful Utilities](#generaluseful-utilities)
- [Processes 101](#processes-101)
- [Maintaining Your System: Automation](#maintaining-your-system-automation)
- [Maintaining Your System: Package Management](#maintaining-your-system-package-management)
- [Maintaining Your System: Logs](#maintaining-your-system-logs)
- [Conclusions & Summaries](#conclusions--summaries)

### Terminal Text Editors

Create a file using Nano

1. Edit "task3" located in "tryhackme"'s home directory using Nano. What is the flag?

   

   ><details><summary>Click for answer</summary></details>

### General/Useful Utilities



Ensure you are connected to the deployed instance (MACHINE_IP)

Now, use Python 3's "HTTPServer" module to start a web server in the home directory of the "tryhackme" user on the deployed instance.

Download the file http://MACHINE_IP:8000/.flag.txt onto the TryHackMe AttackBox

3. What are the contents?

   

   ><details><summary>Click for answer</summary></details>

Create and download files to further apply your learning -- see how you can read the documentation on Python3's "HTTPServer" module. 

Use Ctrl + C to stop the Python3 HTTPServer module once you are finished.

### Processes 101


2. If we were to launch a process where the previous ID was "300", what would the ID of this new process be?

   

   ><details><summary>Click for answer</summary></details>

3. If we wanted to cleanly kill a process, what signal would we send it?

   

   ><details><summary>Click for answer</summary></details>

4. Locate the process that is running on the deployed instance (MACHINE_IP). What flag is given?

   

   ><details><summary>Click for answer</summary></details>

5. What command would we use to stop the service "myservice"?

   

   ><details><summary>Click for answer</summary></details>

6. What command would we use to start the same service on the boot-up of the system?

   

   ><details><summary>Click for answer</summary></details>

7. What command would we use to bring a previously backgrounded process back to the foreground?

   

   ><details><summary>Click for answer</summary></details>

### Maintaining Your System: Automation



Ensure you are connected to the deployed instance and look at the running crontabs.

2. When will the crontab on the deployed instance (MACHINE_IP) run?

   

   ><details><summary>Click for answer</summary></details>

### Maintaining Your System: Logs


Look for the apache2 logs on the deployable Linux machine

2. What is the IP address of the user who visited the site?

   

   ><details><summary>Click for answer</summary></details>

3. What file did they access?

   

   ><details><summary>Click for answer</summary></details>
