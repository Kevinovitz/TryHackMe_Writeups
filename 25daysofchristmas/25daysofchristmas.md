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



### [Day 9] Requests

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

### [Day 10] Metasploit-a-ho-ho-ho

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

### [Day 11] Elf Applications

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

Does is contain any intersting tables? It looks like it! Lets enumerate the content of the table.

```sql
SELECT * FROM USERS
```

![MySQL User Creds](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/25daysofchristmas/Day%2011/Elf_Applications_SQL_User_Creds.png)

>bestpassword

### [Day 12] Elfcryption



### [Day 13] Accumulate



### [Day 14] Unknown Storage



### [Day 15] LFI



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

