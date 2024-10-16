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

   NTLM SCRIPT

   Using `Changeme123` as the password, we use the following command to start the spray attack:

   ```sh
   python3 ntlm_passwordspray.py -u usernames.txt -f za.tryhackme.com -p Changeme123 -a http://ntlmauth.za.tryhackme.com/
   ```

   NTLM CREDENTIALS

   We found four sets of credentials using this attack!

   ><details><summary>Click for answer</summary>gordon.stevens</details>

3. How many valid credentials pairs were found by the password spraying script?

   This is found from the results of the scan in the previous question.

   ><details><summary>Click for answer</summary>4</details>

4. What is the message displayed by the web application when authenticating with a valid credential pair?

   On `http://ntlmauth.za.tryhackme.com/` we get a login screen where we can use our previously found credentials.

   NTLM LOGIN

   Logging in on Firefox didn't work, so I had to switch to Chrome.

   NTLM WELCOME

   ><details><summary>Click for answer</summary>Hello World</details>

### LDAP Bind Credentials

1. What type of attack can be performed against LDAP Authentication systems not commonly found against Windows Authentication systems?



   ><details><summary>Click for answer</summary></details>

2. What two authentication mechanisms do we allow on our rogue LDAP server to downgrade the authentication and make it clear text?



   ><details><summary>Click for answer</summary></details>

3. What is the password associated with the svcLDAP account?



   ><details><summary>Click for answer</summary></details>

### Authentication Relays

1. What is the name of the tool we can use to poison and capture authentication requests on the network?



   ><details><summary>Click for answer</summary></details>

2. What is the username associated with the challenge that was captured?



   ><details><summary>Click for answer</summary></details>

3. What is the value of the cracked password associated with the challenge that was captured?



   ><details><summary>Click for answer</summary></details>

### Microsoft Deployment Toolkit

1. What Microsoft tool is used to create and host PXE Boot images in organisations?



   ><details><summary>Click for answer</summary></details>

2. What network protocol is used for recovery of files from the MDT server?



   ><details><summary>Click for answer</summary></details>

3. What is the username associated with the account that was stored in the PXE Boot image?



   ><details><summary>Click for answer</summary></details>

4. What is the password associated with the account that was stored in the PXE Boot image?



   ><details><summary>Click for answer</summary></details>

5. While you should make sure to cleanup you user directory that you created at the start of the task, if you try you will notice that you get an access denied error. Don't worry, a script will help with the cleanup process but remember when you are doing assessments to always perform cleanup.



   ><details><summary>Click for answer</summary></details>

### Configuration Files

1. What type of files often contain stored credentials on hosts?



   ><details><summary>Click for answer</summary></details>

2. What is the name of the McAfee database that stores configuration including credentials used to connect to the orchestrator?



   ><details><summary>Click for answer</summary></details>

3. What table in this database stores the credentials of the orchestrator?



   ><details><summary>Click for answer</summary></details>

4. What is the username of the AD account associated with the McAfee service?



   ><details><summary>Click for answer</summary></details>

5. What is the password of the AD account associated with the McAfee service?



   ><details><summary>Click for answer</summary></details>

