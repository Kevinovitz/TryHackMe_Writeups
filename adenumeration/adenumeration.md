![Enumerating Active Directory Banner](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adenumeration/Enumerating_Active_Directory_Banner.png)

<p align="center">
   <img src="https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adenumeration/Enumerating_Active_Directory_Cover.png" alt="Enumerating Active Directory Logo">
</p>

# Enumerating Active Directory

This guide contains the answer and steps necessary to get to them for the [Enumerating Active Directory](https://tryhackme.com/r/room/adenumeration) room.

## Table of contents

- [Credential Injection](#credential-injection)
- [Enumeration through Microsoft Management Console](#enumeration-through-microsoft-management-console)
- [Enumeration through Command Prompt](#enumeration-through-command-prompt)
- [Enumeration through PowerShell](#enumeration-through-powershell)
- [Enumeration through Bloodhound](#enumeration-through-bloodhound)

### Credential Injection

1. What native Windows binary allows us to inject credentials legitimately into memory?

   The answer can be found in the text.

   ><details><summary>Click for answer</summary>runas.exe</details>

2. What parameter option of the runas binary will ensure that the injected credentials are used for all network connections?

   The answer can be found in the text.

   ><details><summary>Click for answer</summary>/netonly</details>

3. What network folder on a domain controller is accessible by any authenticated AD account and stores GPO information?

   The answer can be found in the text.

   ><details><summary>Click for answer</summary>SYSVOL</details>

4. When performing dir \\za.tryhackme.com\SYSVOL, what type of authentication is performed by default?

   The answer can be found in the text.

   ><details><summary>Click for answer</summary>Kerberos Authentication</details>

### Enumeration through Microsoft Management Console

1. How many Computer objects are part of the Servers OU?

   After setting up MMC we can select the "Servers" object to see the number of servers.

   MMC SERVERS

   ><details><summary>Click for answer</summary>2</details>

2. How many Computer objects are part of the Workstations OU?

   Select the "Workstations object to get the answers.

   MMC WORKSTATIONS

   ><details><summary>Click for answer</summary>1</details>

3. How many departments (Organisational Units) does this organisation consist of?

   Expand the "People" section so we can see the number of Organizational Units.

   MMC OUS

   ><details><summary>Click for answer</summary>7</details>

4. How many Admin tiers does this organisation have?

   Expand the "Admins" section to see the number of admin tiers.

   MMC ADMINS

   ><details><summary>Click for answer</summary>3</details>

5. What is the value of the flag stored in the description attribute of the t0_tinus.green account?

   In the Admins tier 0 object, we can select the object for tinus.green. In the description we will found our flag.

   MMC FLAG

   ><details><summary>Click for answer</summary>THM{Enumerating.Via.MMC}</details>

### Enumeration through Command Prompt

1. Apart from the Domain Users group, what other group is the aaron.harris account a member of?



   ><details><summary>Click for answer</summary></details>

2. Is the Guest account active? (Yay,Nay)



   ><details><summary>Click for answer</summary></details>

3. How many accounts are a member of the Tier 1 Admins group?



   ><details><summary>Click for answer</summary></details>

4. What is the account lockout duration of the current password policy in minutes?



   ><details><summary>Click for answer</summary></details>

### Enumeration through PowerShell

1. What is the value of the Title attribute of Beth Nolan (beth.nolan)?



   ><details><summary>Click for answer</summary></details>

2. What is the value of the DistinguishedName attribute of Annette Manning (annette.manning)?



   ><details><summary>Click for answer</summary></details>

3. When was the Tier 2 Admins group created?



   ><details><summary>Click for answer</summary></details>

4. What is the value of the SID attribute of the Enterprise Admins group?



   ><details><summary>Click for answer</summary></details>

5. Which container is used to store deleted AD objects?



   ><details><summary>Click for answer</summary></details>

### Enumeration through Bloodhound

1. What command can be used to execute Sharphound.exe and request that it recovers Session information only from the za.tryhackme.com domain without touching domain controllers?



   ><details><summary>Click for answer</summary></details>

2. Apart from the krbtgt account, how many other accounts are potentially kerberoastable?



   ><details><summary>Click for answer</summary></details>

3. How many machines do members of the Tier 1 Admins group have administrative access to?



   ><details><summary>Click for answer</summary></details>

4. How many users are members of the Tier 2 Admins group?



   ><details><summary>Click for answer</summary></details>

