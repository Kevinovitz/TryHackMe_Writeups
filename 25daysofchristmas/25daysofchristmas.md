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

In this task we need to find an exploit for the webserver and gain access using Metasploit.

Machine IP:

**10.10.154.103**

First we run an nmap scan to find out more about our target machine.

![nmap host discovery](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/25daysofchristmas/Day%2010/nmap_host_discovery.png)

We can see there is an Apache Coyote 1.1 service running on port 80 which is of interest to us. From the documentation we find we will be exploiting the struts2  vulnerability.

So open up Metasploit with the `msfconsole` command and type `search struts2` to find any modules we can use.

![Metasploit module search](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/25daysofchristmas/Day%2010/msfconsole_search.png)

For this task we will be using the `exploit/multi/http/struts2_content_type_ognl` module. Type `use` and the moduke name to select it.

![Select module and show options](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/25daysofchristmas/Day%2010/msfconsole_options.png)

Next we will fill out the required information for our payload. Type `show options` to list all the options.
In our example we will set the RHOST, RPORT, and TARGETURI. The LHOST was set correctly. If not, use `ifconfig` to find your ip address under eth0 or tun0 (deppending other wether or not you are using a VPN. After that is done type `run` to run the exploit.

![Add information and run](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/25daysofchristmas/Day%2010/msfconsole_setandrun.png)

In our case the TARGETURI will be `/showcase.action` as this is the base address for the webserver.

![Browser view of our webserver](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/25daysofchristmas/Day%2010/browser_webapplication.png)

Now we have our session running on the target machine.

1. Compromise the web server using Metasploit. What is flag1?

To find the flag we will use the `find` command. However, we first need to change our meterpreter session to a regular shell by using typing `shell` into our session.

![]()


>THM{3ad96bb13ec963a5ca4cb99302b37e12}

2. Now you've compromised the web server, get onto the main system. What is Santa's SSH password?



>rudolphrednosedreindeer

3. Who is on line 148 of the naughty list?



>Melisa Vanhoose

4. Who is on line 52 of the nice list?



>Lindsey Gaffney

### [Day 11] Elf Applications



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

