![Windows Network Analysis Banner](https://cdn-images.tryhackme.com/user-uploads/62c435d1f4d84a005f5df811/room-content/a62b45e7c5c103c14c04aa8152c91624.png)

<p align="center">
   <img src="https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/windowsnetworkanalysis/Windows_Network_Analysis_Cover.png" alt="Windows Network Analysis Logo">
</p>

# <img src="https://cdn-images.tryhackme.com/room-icons/5de96d9ca744773ea7ef8c00-1718362213946" alt="image" style="vertical-align: middle;height: 50px;" /> Windows Network Analysis

This guide contains the answer and steps necessary to get to them for the [Windows Network Analysis](https://tryhackme.com/room/windowsnetworkanalysis) room.

## Table of contents

- [Task 2 - Windows Network Analysis](#task-2---windows-network-analysis)
- [Task 3 - Network Analysis via PowerShell](#task-3---network-analysis-via-powershell)
- [Task 4 - Internal Tooling](#task-4---internal-tooling)
- [Task 5 - Practical](#task-5---practical)

### Task 2 - Windows Network Analysis

1.  What is the full name of the Windows feature that tracks the last 30 to 60 days of system statistics?

    The answers can be found in the text.

    ><details><summary>Click for answer</summary></details>

2.  What is the full path to the directory that Windows will output Firewall logs to?

    The answers can be found in the text.

    ><details><summary>Click for answer</summary></details>

### Task 3 - Network Analysis via PowerShell

1.  What cmdlet can be used to display active TCP connections?

    The answers can be found in the text.

    ><details><summary>Click for answer</summary></details>

2.  What cmdlet can be used to display the DNS cache on the host?

    The answers can be found in the text.

    ><details><summary>Click for answer</summary></details>

3.  What command can be used to list all active RDP sessions on the host?

    The answers can be found in the text.

    ><details><summary>Click for answer</summary></details>

### Task 4 - Internal Tooling

1.  What netstat flag can we use to display the executable responsible for a connection?

    The answers can be found in the text.

    ><details><summary>Click for answer</summary></details>

2.  If we wanted to display all TCP connections and the associated process ID using netstat, what flag would we use?

    The answers can be found in the text.

    ><details><summary>Click for answer</summary></details>

3.  What special character can we use to save the output of netstat to a text file?

    The answers can be found in the text.

    ><details><summary>Click for answer</summary></details>

### Task 5 - Practical

First, make sure both machines are connected.

![Check](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/windowsnetworkanalysis/Windows_Network_Analysis_Check.png)

1.  Use the Get-NetTCPConnection PowerShell cmdlet to list the connections currently active. A popular port for reverse shells is currently active. What is the port number? If nothing sticks out, wait a few minutes and run the command again.

    We will use the following command to list all TCP connections and look for any reverse shell connections.

    ```powershell
    Get-NetTCPConnection | select LocalAddress,localport,remoteaddress,remoteport,state,@{name="process";Expression={(get-process -id $_.OwningProcess).ProcessName}}, @{Name="cmdline";Expression={(Get-WmiObject Win32_Process -filter "ProcessId = $($_.OwningProcess)").commandline}} | sort Remoteaddress -Descending | ft -wrap -autosize
    ```

    ![Tcp](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/windowsnetworkanalysis/Windows_Network_Analysis_Tcp.png)

    We can see two connections on port 5000 connected to the same IP as the C2 server.

    ><details><summary>Click for answer</summary>5000</details>

2.  What is the name of the process that is connecting to the C2 server?

    Although these don't have any attached processes. We can see another process on the same port listening on every interface.

    ><details><summary>Click for answer</summary>pythonw.exe</details>

3.  What is the domain that has been added to the workstation's host file?

    We can query the hosts file to find out.

    ```powershell
    gc -tail 4 "C:\Windows\System32\drivers\etc\hosts"
    ```

    ![Hosts](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/windowsnetworkanalysis/Windows_Network_Analysis_Hosts.png)

    ><details><summary>Click for answer</summary>attackerc2.thm</details>

4.  Analyse the SRUM database. There is another process that has sent a large amount of bytes, indicating data exfil. What is the full path to the process (as listed in SRUM)?

    After opening the SRUM analysis file, we can look at the data in the "Network Data Usage" sheet. Sort on the "Bytes sent" column.

    ![Exfil](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/windowsnetworkanalysis/Windows_Network_Analysis_Exfil.png)

    ><details><summary>Click for answer</summary>\device\harddiskvolume3\program files\updater\exfil.exe</details>

5.  Finally, analyse the SMB shares present on the analyst machine. What is the name of the share that stands out?

    My first command didn't work so I used another one to enumerate the SMB shares.

    ```powershell
    Get-SmbConnection
    Get-SmbShare
    ```

    ![Shares](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/windowsnetworkanalysis/Windows_Network_Analysis_Shares.png)

    ><details><summary>Click for answer</summary>confidential</details>

![Check](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/windowsnetworkanalysis/Windows_Network_Analysis_Check.png)