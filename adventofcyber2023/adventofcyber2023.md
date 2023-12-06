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
<!--- [Day 6 ](#day-6-)
- [Day 7 ](#day-7-)
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

More days are yet to come!

<!---

### Day 6 



1. 

   ><details><summary>Click for answer</summary></details>

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
