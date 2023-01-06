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

