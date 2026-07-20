![IronShade Banner](https://cdn-images.tryhackme.com/user-uploads/5e8dd9a4a45e18443162feab/room-content/5e8dd9a4a45e18443162feab-1722907697776.png)

<p align="center">
   <img src="https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/ironshade/IronShade_Cover.png" alt="IronShade Logo">
</p>

# <img src="https://cdn-images.tryhackme.com/room-icons/5e8dd9a4a45e18443162feab-1722907649226" alt="image" style="vertical-align: middle;height: 50px;" /> IronShade

This guide contains the answer and steps necessary to get to them for the [IronShade](https://tryhackme.com/room/ironshade) room.

## Table of contents

- [Task 1 - Linux Challenge](#task-1---linux-challenge)

### Task 1 - Linux Challenge

1.  What is the Machine ID of the machine we are investigating?

    To get detailed system information, we can use the command `hostnamectl`.

    ![Machine Id](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/ironshade/Ironshade_Machine_Id.png)

    ><details><summary>Click for answer</summary>dc7c8ac5c09a4bbfaf3d09d399f10d96</details>

2.  What backdoor user account was created on the server?

    We can use osqueryi to see all users on the system.

    ```console
    osqueryi
    SELECT * from users;
    ```

    We can see at least three 'normal' user accounts.

    ![Users](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/ironshade/Ironshade_Users.png)

    We can confirm this by looking at the home folder.

    ```console
    ls -lh /home
    ```

    This tells us which account was created as a backdoor.

    ><details><summary>Click for answer</summary>mircoservice</details>

3.  What is the cronjob that was set up by the attacker for persistence?

    Looking at the system wide cronjobs, we don't see anything suspicious. `ls -la /etc/cron.*`.

    We can then look at user specific created cronjobs.

    ```console
    sudo ls -al /var/spool/cron/crontabs/
    sudo cat /var/spool/cron/crontabs/<username>
    ```

    First we check which users have cronjobs configured. We then inspect them for each user. The root users seems to have a suspicious entry that runs after each reboot. It runs something from the backdoor user account directory as well.

    ![Cronjob](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/ironshade/Ironshade_Cronjob.png)

    ><details><summary>Click for answer</summary>@reboot /home/mircoservice/printer_app</details>

4.  Examine the running processes on the machine. Can you identify the suspicious-looking hidden process from the backdoor account?

    Again, using `osquery`, we can look for any processes from the backdoor account (note the typo in the name).

    ```console
    SELECT pid, name, path, cmdline, start_time FROM processes WHERE cmdline LIKE '%mircoservice%';
    ```

    ![Services](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/ironshade/Ironshade_Services.png)

    Here we see another suspicious process running.

    ><details><summary>Click for answer</summary>strokes</details>

5.  How many processes are found to be running from the backdoor account’s directory?

    From the previous question, we can see the number of processes.

    ><details><summary>Click for answer</summary>2</details>

6.  What is the name of the hidden file in memory from the root directory?

    I was trown of by the wording and was looking for hidden files in the root user diretory instead of the root of the disk.

    This we can find using `ls`:

    ```console
    ls -la /
    ```

    ![Hidden File](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/ironshade/Ironshade_Hidden_File.png)

    ><details><summary>Click for answer</summary>.systmd</details>

7.  What suspicious services were installed on the server? Format is service a, service b in alphabetical order.

    We can use `ls -la /etc/systemd/system` to list all installed services.

    ![Installed Services](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/ironshade/Ironshade_Installed_Services.png)

    From this we can identify two suspicious services. One is the strokes service, we also found earlier. The other is the backup service. We can check the service to confirm this is correct.

    ```console
    systemctl cat backup.service
    ```

    ![Backup Service](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/ironshade/Ironshade_Backup_Service.png)

    This service executes a file from the backdoor account.

    ><details><summary>Click for answer</summary>backup.service, strokes.service</details>

8.  Examine the logs; when was the backdoor account created on this infected system?

    We can look through the auth logs for this.

    ```console
    grep -a "useradd" /var/log/auth.log*
    ```

    ![Account Creation](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/ironshade/Ironshade_Account_Creation.png)

    ><details><summary>Click for answer</summary>Aug  5 22:05:33</details>

9.  From which IP address were multiple SSH connections observed against the suspicious backdoor account?

    We can look through the auth logs to see which ssh connections have been made. We filter for the backdoor account and entries listing an address.

    ```console
    grep -a "ssh" /var/log/auth.log* | grep -i "mircoservice" | grep -i "port"
    ```

    ![Ssh](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/ironshade/Ironshade_Ssh.png)

    ><details><summary>Click for answer</summary>10.11.75.247</details>

10.  How many failed SSH login attempts were observed on the backdoor account?

     From the previous command sustituting "port" for "Failed password". We can see how many attempts have failed.

     ```console
     grep -a "ssh" /var/log/auth.log* | grep -i "mircoservice" | grep -i "Failed password"
     ```

     ![Failed Ssh](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/ironshade/Ironshade_Failed_Ssh.png)

     We can see a few single fails, and two double fail messages. These need to be added together (4x1)+(2x2).

     ><details><summary>Click for answer</summary>8</details>

11.  Which malicious package was installed on the host?

     We can again use `osquery` for this. We look at all installed packages and filter out those maintained by ubuntu.

     ```console
     select name, version, source, maintainer, admindir from deb_packages where maintainer not like '%ubuntu%';
     ```

     ![Packages](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/ironshade/Ironshade_Packages.png)

     This list one package with a weird maintainer name and the filename also raises suspicion.

     ><details><summary>Click for answer</summary>pscanner</details>

12.  What is the secret code found in the metadata of the suspicious package?

     We can find more information about this package by looking at the package meta-information using `apt show`.

     ```console
     apt show pscanner
     ```

     ![Meta](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/ironshade/Ironshade_Meta.png)

     ><details><summary>Click for answer</summary>{_tRy_Hack_ME_}</details>

