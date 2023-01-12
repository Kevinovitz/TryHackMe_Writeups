<p align="center">
   <img src="https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/25daysofchristmas/Advent_of_Cyber_1_2019_Logo.png" alt="Advent of Cyber 1 2019 Logo">
</p>

# Advent of Cyber 1 [2019]

This guide contains the answer and steps necessary to get to them for the [Advent of Cyber](https://tryhackme.com/room/25daysofchristmas) room.

### [Day 1] Inventory Management



### [Day 1] Inventory Management



### [Day 2] Arctic Forum



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

   >sCrIPtKiDd

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

   >THM{3ad96bb13ec963a5ca4cb99302b37e12}

2. Now you've compromised the web server, get onto the main system. What is Santa's SSH password?

   Going through some of the directories, we find a file called `ssh-creds.txt`. This look interesting. Inside we find some credentials we can use to ssh into the machine.

   ![SSH credentials](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/25daysofchristmas/Day%2010/msfconsole_searchcreds.png)

   ![SSH credentials](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/25daysofchristmas/Day%2010/msfconsole_sshcreds.png)

   >rudolphrednosedreindeer

3. Who is on line 148 of the naughty list?

   In terminal window (not meterpreter) we can ssh into the machine and look around for the files. We spot two lists here.

   ![Directory files](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/25daysofchristmas/Day%2010/ssh_directory.png)

   To see who is on line 148 of the naughty list we could just count the lines, but using cat with some extra options will be easier.

   ```bash
   cat -n naughty_list.txt | grep -i 148
   ```

   The `-n` argument shows line numbers in the output which we can use to search with `grep`.

   Produces

   ![Naughty list result](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/25daysofchristmas/Day%2010/ssh_naughty.png)

   >Melisa Vanhoose

4. Who is on line 52 of the nice list?

   Same command can be used here.

   ```bash
   cat -n nice_list.txt | grep -i 52
   ```
   Produces

   ![Naughty list result](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/25daysofchristmas/Day%2010/ssh_nice.png)

   >Lindsey Gaffney

### [Day 11] [Elf Applications](https://github.com/Kevinovitz/TryHackMe_Writeups/tree/main/25daysofchristmas/Day%2011)

In this task we need to access some services on the target machine. See the accompanying [documentation](https://docs.google.com/document/d/1qCMuPwBR0gWIDfk_PXt0Jr220JIJAQ-N4foDZDVX59U/edit#) for mor help.
Machine IP:
10.10.223.45

We first run an nmap scan to find all available services on the target machine by running:

```bash
nmap -sV 10.10.223.45
```

![Nmap host scan](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/25daysofchristmas/Day%2011/Elf_Applications_Nmap_Scan.png)

Here we can see we have three services running on their default ports. FTP on port 21, NFS on port 111, and MySQL on port 3306.

1. What is the password inside the creds.txt file?

   To get the password we need to access the NFS service. First we need to find out which shares are available for us to mount

   ```bash
   showmount -e 10.10.223.45
   ```

   Now we can mount this share to our system.

   ```bash
   sudo mount 10.10.223.45:/opt/files /mnt
   ```

   ![Mounting NFS share](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/25daysofchristmas/Day%2011/Elf_Applications_NFS_Mount.png)

   Now we can go to the newly mounted directory and read the contents of the file.

   ![Read file from NFS share](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/25daysofchristmas/Day%2011/Elf_Applications_NFS_Open_File.png)

   The file can also be opened from the folder itself.

   ![Access NFS through folder](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/25daysofchristmas/Day%2011/Elf_Applications_NFS_File_Directory.png)

   >securepassword123

2. What is the name of the file running on port 21?

   The FTP service is active on port 21, so we will see if we can login anonymously.

   ![Login anynomously to FTP](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/25daysofchristmas/Day%2011/Elf_Applications_FTP_Login.png)

   Success! No lets search for the file and copy it to our machine with the `get` command.

   ![Download FTP file](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/25daysofchristmas/Day%2011/Elf_Applications_FTP_FIle_Download.png)

   >file.txt

3. What is the password after enumerating the database?

   Reading the `file.txt` file we found on the FTP server, we see it contains some credentials for a SQL service. Lets see if they still work.

   ![FTP file contents](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/25daysofchristmas/Day%2011/Elf_Applications_FTP_File_Open.png)

   ```bash
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

   >bestpassword

### [Day 12] [Elfcryption](https://github.com/Kevinovitz/TryHackMe_Writeups/tree/main/25daysofchristmas/Day%2012)

In this task we will look at various encryption techniques to decrypt some files we received. The supporting documentation can be found [here](https://docs.google.com/document/d/1xUOtEZOTS_L8u_S5Fbs1Wof7mdpWQrj2NkgWLV9tqns/edit?usp=sharing).

We first unzip the contents of the file using either the `unzip tosend.zip` command or through the GUI.

1. What is the md5 hashsum of the encrypted note1 file?

   To read the md5 hash of the `note1.txt.gpg` file we use the following command:
   
   ```bash
   md5sum note1.txt.gpg
   ```
   
   ![GPG File Hash](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/25daysofchristmas/Day%2012/Encryption_GPG_Hash.png)

   >24cf615e2a4f42718f2ff36b35614f8f

2. Where was elf Bob told to meet Alice?

   To decrypt the file we need a passphrase. I didn't know what it was so I used to one provided by the hint: `25daysofchristmas`. Now we can decrypt it by using typing `gpg -d note1.txt.gpg1` and entering the passphrase when prompted.
   
   ![GPG File Decrypt](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/25daysofchristmas/Day%2012/Encryption_GPG_Decrypt.png)

   >santa's grotto

3. Decrypt note2 and obtain the flag!

   To decrypt the message we use the command as specified in the supporting material. Again, we use the passphrase supplied by the hint `hello`.
   
   ```bash
   openssl rauthl -decrypt -inkey private.key -in note2_encrypted.txt -out note2_decrypted.txt
   ```
   
   ![AES File Decrypt](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/25daysofchristmas/Day%2012/Encryption_AES_Decrypt.png)

   >THM{ed9ccb6802c5d0f905ea747a310bba23}

### [Day 13] [Accumulate](https://github.com/Kevinovitz/TryHackMe_Writeups/tree/main/25daysofchristmas/Day%2013)

In this task we are asked to use our previously gathered knowledge to gain access to a system with only its IP address.

The first thing we do, is run a network scan to find all open ports and their services.

```bash
nmap -sV 10.10.85.141
```

![Nmap Network Scan](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/25daysofchristmas/Day%2013/Accumulate_Nmap_scan.png)

Here we see a server running on port 80. Remember the other service for later. 

1. A web server is running on the target. What is the hidden directory which the website lives on?

   Lets open the browser and navigate to the machine's IP and port 80. Here we indeed find a page for windows server. None of the links on this page will lead us anywhere, as there is no internet connections. Instead we will use a tool we used in day 2 of this challenge `dirsearch`. With the following command we can enumerate different directories present on the server.
   
   ```bash
   dirsearch -u 10.10.85.141:80 -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
   ```
   
   ![DirSearch Results](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/25daysofchristmas/Day%2013/Accumulate_Dirsearch_Enumeration.png)
   
   This quickly gives us a directory to use. When navigating to the website, we see this is indeed available!
   
   ![Retro Website](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/25daysofchristmas/Day%2013/Accumulate_Website.png)

   >/retro

2. Gain initial access and read the contents of user.txt

   We need to find a way into the system and read its contents. First we start looking around for any interesting information on the blog. None of the posts have anything of interest. However, we can also see a comment posted by Wade the author. This seems to hold some private stuff you would not want out in the open. Could it possibly be a password?
   
   ![Website Comment](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/25daysofchristmas/Day%2013/Accumulate_Website_Comment.png)
   
   After some searching we find a login page for the Wordpress website. We can indeed login using the password we found earlier and username Wade. However, this will again lead us nowhere, as we cannot access the files from here. Remember the other service we found running on port 3389? A quick Google search tells us this is used for RPD connections, how fortunate!
   
   Using Remmina with `remmina -c rdp:wade@10.10.85.141:80` to login to the machine we need to supply a password at the prompt.
   
   ![RDP Login](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/25daysofchristmas/Day%2013/Accumulate_RDP_Login.png)
   
   Here we find a conveniently placed file on our desktop. Sweet!

   >THM{HACK_PLAYER_ONE}

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

   >THM{COIN_OPERATED_EXPLOITATION}

### [Day 14] [Unknown Storage](https://github.com/Kevinovitz/TryHackMe_Writeups/tree/main/25daysofchristmas/Day%2014)

In this task we will need to look for leaked information from an improperly configured AWS bucket. The supporting material can be found [here](https://docs.google.com/document/d/13uHBw3L9wdDAFboErSq_QV8omb3yCol0doo6uMGzJWo/edit#).

1. What is the name of the file you found?

   All we need here is the name of the bucket `advent-bucket-one`.
   
   We can navigate to `advent-bucket-one.s3.amazonaws.com` to see if the bucket is publicly accessible. And if so, which file is available.
   
   ![AWS Bucket Information](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/25daysofchristmas/Day%2014/Storage_AWS_Bucket.png)
   
   >employee_names.txt

2. What is in the file?

   To view a certain file, we can either use the AWS CLI (account necessary) or through the browser. In this case it is easier to use the browser.
   
   `advent-bucket-one.s3.amazonaws.com/employee_names.txt`
   
   >mcchef

### [Day 15] LFI

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

### [Day 16] File Confusion



### [Day 17] Hydra-ha-ha-haa



### [Day 18] ELF JS



### [Day 19] Commands



### [Day 20] Cronjob Privilege Escalation



### [Day 21] Reverse Elf-ineering



### [Day 22] If Santa, Then Christmas



### [Day 23] LapLANd (SQL Injection)



### [Day 24] Elf Stalk



### [Day 25] Challenge-less 

