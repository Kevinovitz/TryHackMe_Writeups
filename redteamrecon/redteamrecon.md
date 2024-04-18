![Red Team Recon Banner](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/redteamrecon/Red_Team_Recon_Banner.png)

<p align="center">
   <img src="https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/redteamrecon/Red_Team_Recon_Cover.png" alt="Red Team Recon Logo">
</p>

# Red Team Recon

This guide contains the answer and steps necessary to get to them for the [Red Team Recon](https://tryhackme.com/room/redteamrecon) room.

## Table of contents

- [Taxonomy of Reconnaissance](#taxonomy-of-reconnaissance)
- [Built-in Tools](#built-in-tools)
- [Advanced Searching](#advanced-searching)
- [Specialized Search Engines](#specialized-search-engines)
- [Recon-ng](#recon-ng)
- [Maltego](#maltego)

### Built-in Tools

1. When was thmredteam.com created (registered)? (YYYY-MM-DD)

   We can use whois to look for this information
   
   ```cmd
   whois thmredteam.com
   ```
   
   ![Creation Date](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/redteamrecon/Red_Team_Recon_Built_In_Creation_Date.png)

   ><details><summary>Click for answer</summary>2021-09-24</details>

2. To how many IPv4 addresses does clinic.thmredteam.com resolve?

   For this we can use multiple tools (nslookup, dig, host)
   
   ```cmd
   host clinic.thmredteam.com
   ```
   
   ![IP Addresses](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/redteamrecon/Red_Team_Recon_Built_In_IP_Addresses.png)

   ><details><summary>Click for answer</summary>2</details>

3. To how many IPv6 addresses does clinic.thmredteam.com resolve?

   This was found using the same command as for the previous question.

   ><details><summary>Click for answer</summary>2</details>

### Advanced Searching

1. How would you search using Google for xls indexed for http://clinic.thmredteam.com?

   For this we need to specify the filetype we want to search for, as well as the site. The syntaxt can be found in the text.

   ><details><summary>Click for answer</summary>filetype:xls site:clinic.thmredteam.com</details>

2. How would you search using Google for files with the word passwords for http://clinic.thmredteam.com?

   For this we need to specify the site we want to search for. The syntaxt can be found in the text.

   ><details><summary>Click for answer</summary>passwords site:clinic.thmredteam.com</details>

### Specialized Search Engines

1. What is the shodan command to get your Internet-facing IP address?

   For this answer, we need to head over to the shodan website. Searching for the shodan cli gives us the correct page with many commands.
   
   ![Shodan](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/redteamrecon/Red_Team_Recon_Specialized_Search_Engines_Shodan.png)

   ><details><summary>Click for answer</summary>shodan myip</details>

### Recon-ng

1. How do you start recon-ng with the workspace clinicredteam?

   This is mentioned in the text.

   ><details><summary>Click for answer</summary>recon-ng -w clinicredteam</details>

2. How many modules with the name virustotal exist?

   Using the following command gives us all modules related to this term.
   
   ```cmd
   marketplace search virustotal
   ```
   
   ![Virustotal](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/redteamrecon/Red_Team_Recon_Recon_NG_Virustotal.png)

   ><details><summary>Click for answer</summary>2</details>

3. There is a single module under hosts-domains. What is its name?

   We can search for modules related to this term with:
   
   ```cmd
   marketplace search host-domains
   ```
   
   ![Domain](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/redteamrecon/Red_Team_Recon_Recon_NG_Domain.png)

   ><details><summary>Click for answer</summary>migrate_hosts</details>

4. censys_email_address is a module that “retrieves email addresses from the TLS certificates for a company.” Who is the author?

   We can look up information about this modules by using:
   
   ```cmd
   marketplace info censys_email_address
   ```
   
   ![Censys](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/redteamrecon/Red_Team_Recon_Recon_NG_Censys.png)

   ><details><summary>Click for answer</summary>Censys Team</details>

### Maltego

1. What is the name of the transform that queries NIST’s National Vulnerability Database?

   When visiting the webpage (https://www.maltego.com/transform-hub/) and searching for 'NIST' we find the entry we are looking for.
   
   ![NIST](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/redteamrecon/Red_Team_Recon_Maltego_NIST.png)

   ><details><summary>Click for answer</summary>NIST NVD</details>

2. What is the name of the project that offers a transform based on ATT&CK?

   When visiting the webpage (https://www.maltego.com/transform-hub/) and searching for 'ATT' we find the entry we are looking for.
   
   ![ATTACK](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/redteamrecon/Red_Team_Recon_Maltego_ATTACK.png)

   ><details><summary>Click for answer</summary>MISP Project</details>
