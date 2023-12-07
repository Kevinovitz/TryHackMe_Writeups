![Advent of Cyber 2023 Banner](https://tryhackme-images.s3.amazonaws.com/user-uploads/62c435d1f4d84a005f5df811/room-content/1eb7b51908dee3e6a463ed1b4158f55d.svg)

<p align="center">
   <img src="https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/adventofcyber2023/Advent_Of_Cyber_2023_Cover.png" alt="Advent of Cyber 2023 Cover">
</p>

# Advent of Cyber 2023

This guide contains the answer and steps necessary to get to them for the [Advent of Cyber 2023](https://tryhackme.com/room/adventofcyber2023) room.

> [!Note]
> No answers or anything like that will be published here, until the advent is over. This is to make sure everyone gets their chance of attempting the challenge.

## Table of contents

- [Day 1 Chatbot, tell me, if you're really safe?](#day-1-chatbot-tell-me-if-youre-really-safe)
- [Day 2 Day 2 O Data, All Ye Faithful](#day-2-o-data-all-ye-faithful)
- [Day 3 Hydra is Coming to Town](#day-3-hydra-is-coming-to-town)
- [Day 4 Baby, it's CeWLd outside](#day-4-baby-its-cewld-outside)
- [Day 5 Memories of Christmas Past](#day-5-memories-of-christmas-past)
- [Day 6 ](#day-6-)
<!--- [Day 7 ](#day-7-)
- [Day 8 ](#day-8-)
- [Day 9 ](#day-9-)
- [Day 10 ](#day-10-)
- [Day 11 ](#day-11-)
- [Day 12 ](#day-12-)
- [Day 13 ](#day-13-)
- [Day 14 ](#day-14-)
- [Day 15 ](#day-15-)
- [Day 16 ](#day-16-)
- [Day 17 ](#day-17-)
- [Day 18 ](#day-18-)
- [Day 19 ](#day-19-)
- [Day 20 ](#day-20-)
- [Day 21 ](#day-21-)
- [Day 22 ](#day-22-)
- [Day 23 ](#day-23-)
- [Day 24 ](#day-24-)-->

### Day 1 Chatbot, tell me, if you're really safe? 

In this task we will look at how we can use prompt injection to bypass security measures put in place to prevent an AI chatbot from leaking sensitive information.

1. What is McGreedy's personal email address?



   ><details><summary>Click for answer</summary>Walkthrough: https://www.youtube.com/watch?v=dQw4w9WgXcQ</details>

2. What is the password for the IT server room door?



   ><details><summary>Click for answer</summary></details>

3. What is the name of McGreedy's secret project?



   ><details><summary>Click for answer</summary></details>

If you enjoyed this room, we invite you to join our Discord server for ongoing support, exclusive tips, and a community of peers to enhance your Advent of Cyber experience!

### Day 2 O Data, All Ye Faithful

In this task we will be looking at a captured network traffic packet and analyse its contents using Jupyter Notebooks.

1. Open the notebook "Workbook" located in the directory "4_Capstone" on the VM. Use what you have learned today to analyse the packet capture.



   ><details><summary>Click for answer</summary></details>

2. How many packets were captured (looking at the PacketNumber)?



   ><details><summary>Click for answer</summary></details>

3. What IP address sent the most amount of traffic during the packet capture?



   ><details><summary>Click for answer</summary></details>

4. What was the most frequent protocol?



   ><details><summary>Click for answer</summary></details>

If you enjoyed today's task, check out the Intro to Log Analysis room.

### Day 3 Hydra is Coming to Town

In this task we will be using Hydra to bruteforce our way into the security system for the IT server room.

When trying the access the login page, make sure to use `http` (not https) and append the port number to the ip address.

So if your ip is `10.10.10.10` and your provided port number is `8000`, you need to visit `http://10.10.10.10:8000`.

1. Using crunch and hydra, find the PIN code to access the control system and unlock the door. What is the flag?



   ><details><summary>Click for answer</summary></details>

If you have enjoyed this room please check out the Password Attacks room.

### Day 4 Baby, it's CeWLd outside

In this task we will be using cewl to generate wordlists and wfuzz to brute-force our way into a web application.

1. What is the correct username and password combination? Format username:password



   ><details><summary>Click for answer</summary></details>

2. What is the flag?



   ><details><summary>Click for answer</summary></details>

If you enjoyed this task, feel free to check out the Web Enumeration room.

### Day 5 Memories of Christmas Past

In this task we will be looking at how memory corruption through a buffer overflow vulnerability can be exploited in a web game.

1. If the coins variable had the in-memory value in the image below, how many coins would you have in the game?

   ![Money]()

   ><details><summary>Click for answer</summary></details>

2. What is the value of the final flag?



   ><details><summary>Click for answer</summary></details>

We have only explored the surface of buffer overflows in this task. Buffer overflows are the basis of many public exploits and can even be used to gain complete control of a machine. If you want to explore this subject more in-depth, feel free to check the Buffer Overflows room.

Van Jolly still thinks the Ghost of Christmas Past is in the game. She says she has seen it with her own eyes! She thinks the Ghost is hiding in a glitch, whatever that means. What could she have seen?

### Day 6 

In this task we will be looking at how to parse log files to find information using basic linux commands.

1. How many unique IP addresses are connected to the proxy server?

   Lets first look at the structure of the log file using: `head -1 access.log`.

   We need the second column. Lets select that and sort the unique values.
   
   ```cmd
   cut -d ' ' -f2 access.log | sort | uniq
   ```

   We can also use `wc` to simply count that amount for us.

   ```cmd
   cut -d ' ' -f2 access.log | sort | uniq | wc -l
   ```

   UNIQUE IP
   
   ><details><summary>Click for answer</summary>9</details>

2. How many unique domains were accessed by all workstations?

   For this we can use a similar approach but look at the third column. We then split the domain on the '=' character. Then we can sort the unique domains.

   ```cmd
   cut -d ' ' -f3 access.log | cut -d ':' -f1 | sort | uniq | wc -l
   ```
   
   UNIQUE DOMAINS

   ><details><summary>Click for answer</summary>111</details>

3. What status code is generated by the HTTP requests to the least accessed domain?

   We use the same approach as before to get the unique domains. Next we sort this list and use `head -1` to get the least requested domain.

   ```cmd
   head -1 access.log 
   cut -d ' ' -f3 access.log | cut -d ':' -f1 | sort | uniq -c | sort -n | head -1
   ```

   Now we can use `grep` to search the log for this domain and look for the status code column and sort for unique values.
   
   ```cmd
   grep 'partnerservices.getmicrosoftkey.com' access.log | cut -d ' ' -f6 | sort | uniq
   ```

   STATUS CODE

   ><details><summary>Click for answer</summary>503</details>

4. Based on the high count of connection attempts, what is the name of the suspicious domain?

   For this question we now sort and view the most requested domains using `tail`.
   
   ```cmd
   head -1 access.log 
   cut -d ' ' -f3 access.log | cut -d ':' -f1 | sort | uniq -c | sort -n | tail -10
   ```
   
   MALICIOUS DOMAIN
   
   ><details><summary>Click for answer</summary>frostlings.bigbadstash.thm</details>

5. What is the source IP of the workstation that accessed the malicious domain?

   We can search the log file for the malicious domain using `grep`. Then we can filter the second column and sort for unique values.

   ```cmd
   grep 'frostlings.bigbadstash.thm' access.log | cut -d ' ' -f2 | sort | uniq
   ```

   SOURCE IP

   ><details><summary>Click for answer</summary>10.10.185.225</details>

6. How many requests were made on the malicious domain in total?

   We ca either look at the image from question 4 (the domains have a count in front of them) or we can use the following command:

   ```cmd
   grep 'frostlings.bigbadstash.thm' access.log | wc -l   
   ```

   ><details><summary>Click for answer</summary>1581</details>

8. Having retrieved the exfiltrated data, what is the hidden flag?

   After looking at the entries of the malicious domain, we can see their is a payload being extracted.

   We can get a clearer image using `cut` to filter out the request and then filter out just the payload. Since this looks to be base64 encoded we can decode it using `base64`.

   ```cmd
   grep 'frostlings.bigbadstash.thm' access.log | cut -d ' ' -f5 | cut -d '=' -f2 | base64 -d
   ```

   It is possible to look for the flag manually through this list. But since we know it will contain a bracket '{', we can also use grep to search for the entry with the flag.

   ```cmd
   grep 'frostlings.bigbadstash.thm' access.log | cut -d ' ' -f5 | cut -d '=' -f2 | base64 -d | grep '{'
   ```

   FLAG

   ><details><summary>Click for answer</summary>THM{a_gift_for_you_awesome_analyst!}</details>

If you enjoyed doing log analysis, check out the Log Analysis module in the SOC Level 2 Path.

More days are yet to come!

<!---

### Day 7 



1. 

   ><details><summary>Click for answer</summary></details>

### Day 8 



1. 

   ><details><summary>Click for answer</summary></details>

### Day 9 



1. 

   ><details><summary>Click for answer</summary></details>

### Day 10 



1. 

   ><details><summary>Click for answer</summary></details>

### Day 11 



1. 

   ><details><summary>Click for answer</summary></details>

### Day 12 



1. 

   ><details><summary>Click for answer</summary></details>

### Day 13 



1. 

   ><details><summary>Click for answer</summary></details>

### Day 14 



1. 

   ><details><summary>Click for answer</summary></details>

### Day 15 



1. 

   ><details><summary>Click for answer</summary></details>

### Day 16 



1. 

   ><details><summary>Click for answer</summary></details>

### Day 17 



1. 

   ><details><summary>Click for answer</summary></details>

### Day 18 



1. 

   ><details><summary>Click for answer</summary></details>

### Day 19 



1. 

   ><details><summary>Click for answer</summary></details>

### Day 20 



1. 

   ><details><summary>Click for answer</summary></details>

### Day 21 



1. 

   ><details><summary>Click for answer</summary></details>

### Day 22 



1. 

   ><details><summary>Click for answer</summary></details>

### Day 23 



1. 

   ><details><summary>Click for answer</summary></details>

### Day 24 



1. 

   ><details><summary>Click for answer</summary></details>

-->
