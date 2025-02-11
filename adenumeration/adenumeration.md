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

   ![Mmc Servers](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/adenumeration/Enumerating_Active_Directory_Mmc_Servers.png)

   ><details><summary>Click for answer</summary>2</details>

2. How many Computer objects are part of the Workstations OU?

   Select the "Workstations object to get the answers.

   ![Mmc Workstations](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/adenumeration/Enumerating_Active_Directory_Mmc_Workstations.png)

   ><details><summary>Click for answer</summary>1</details>

3. How many departments (Organisational Units) does this organisation consist of?

   Expand the "People" section so we can see the number of Organizational Units.

   ![Mmc Ous](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/adenumeration/Enumerating_Active_Directory_Mmc_Ous.png)

   ><details><summary>Click for answer</summary>7</details>

4. How many Admin tiers does this organisation have?

   Expand the "Admins" section to see the number of admin tiers.

   ![Mmc Admins](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/adenumeration/Enumerating_Active_Directory_Mmc_Admins.png)

   ><details><summary>Click for answer</summary>3</details>

5. What is the value of the flag stored in the description attribute of the t0_tinus.green account?

   In the Admins tier 0 object, we can select the object for tinus.green. In the description we will found our flag.

   ![Mmc Flag](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/adenumeration/Enumerating_Active_Directory_Mmc_Flag.png)

   ><details><summary>Click for answer</summary>THM{Enumerating.Via.MMC}</details>

### Enumeration through Command Prompt

Lets connect to the jump server using our retrieved credentials via SSH.

```cmd
ssh za.tryhackme.com\\mitchell.murphy@thmjmp1.za.tryhackme.com
```

1. Apart from the Domain Users group, what other group is the aaron.harris account a member of?

   To find the groups a user is a member of we can use `net user`.

   ```cmd
   net user aaron.harris /domain
   ```

   ![Cmd Groups](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/adenumeration/Enumerating_Active_Directory_Cmd_Groups.png)

   ><details><summary>Click for answer</summary>Internet Access</details>

2. Is the Guest account active? (Yay,Nay)

   We can use the same command, but with a different account name.

   ```cmd
   net user Guest /domain
   ```

   ![Cmd Guest](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/adenumeration/Enumerating_Active_Directory_Cmd_Guest.png)

   ><details><summary>Click for answer</summary>Nay</details>

3. How many accounts are a member of the Tier 1 Admins group?

   For this we can use the `groups` command together with the group name.

   ```cmd
   net groups "Tier 1 Admins" /domain
   ```

   ![Cmd Admins](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/adenumeration/Enumerating_Active_Directory_Cmd_Admins.png)

   ><details><summary>Click for answer</summary>7</details>

4. What is the account lockout duration of the current password policy in minutes?

   This can be found using `accounts`.

   ```cmd
   net accounts /domain
   ```

   ![Cmd Accounts](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/adenumeration/Enumerating_Active_Directory_Cmd_Accounts.png)

   ><details><summary>Click for answer</summary>30</details>

### Enumeration through PowerShell

1. What is the value of the Title attribute of Beth Nolan (beth.nolan)?

   We should enumerate the user properties and filter on 'Title'.

   ```PowerShell
   Get-ADUser -Identity beth.nolan -Server za.tryhackme.com -Property * | ft Name,Title
   ```

   ![Ps Title](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/adenumeration/Enumerating_Active_Directory_Ps_Title.png)

   ><details><summary>Click for answer</summary>Senior</details>

2. What is the value of the DistinguishedName attribute of Annette Manning (annette.manning)?

   We should enumerate the user properties and filter on 'DistinguishedName'.

   ```PowerShell
   Get-ADUser -Identity beth.nolan -Server za.tryhackme.com | ft Name,Surname,DistinguishedName
   ```

   ![Ps Distinguishedname](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/adenumeration/Enumerating_Active_Directory_Ps_Distinguishedname.png)

   ><details><summary>Click for answer</summary>CN=annette.manning,OU=Marketing,OU=People,DC=za,DC=tryhackme,DC=com</details>

3. When was the Tier 2 Admins group created?

   We need to enumerate the 'Tier 2 Admins' group showing all properties and filter on the 'whenCreated' property.

   ```PowerShell
   Get-ADGroup -Identity 'Tier 2 Admins'  -Server za.tryhackme.com -Properties * | ft Name,whenCreated
   ```

   ![Ps Admin](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/adenumeration/Enumerating_Active_Directory_Ps_Admin.png)

   ><details><summary>Click for answer</summary>2/24/2022 10:04:41 PM</details>

4. What is the value of the SID attribute of the Enterprise Admins group?

   We need to enumerate the 'Enterprise Admins' group.

   ```PowerShell
   Get-ADGroup -Identity 'Enterprise Admins'  -Server za.tryhackme.com
   ```

   ![Ps Enterprise Admins](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/adenumeration/Enumerating_Active_Directory_Ps_Enterprise_Admins.png)

   ><details><summary>Click for answer</summary>S-1-5-21-3330634377-1326264276-632209373-519</details>

5. Which container is used to store deleted AD objects?

   We need to get information about the domain using `Get-ADDomain`.

   ```powershell
   Get-ADDomain -Server za.tryhackme.com
   ```

   ![Ps Domain](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/adenumeration/Enumerating_Active_Directory_Ps_Domain.png)

   ><details><summary>Click for answer</summary>CN=Deleted Objects,DC=za,DC=tryhackme,DC=com</details>

### Enumeration through Bloodhound

1. What command can be used to execute Sharphound.exe and request that it recovers Session information only from the za.tryhackme.com domain without touching domain controllers?

   This command can be found in the text.

   ><details><summary>Click for answer</summary>Sharphound.exe --CollectionMethods Session --Domain za.tryhackme.com --ExcludeDCs</details>

2. Apart from the krbtgt account, how many other accounts are potentially kerberoastable?

   First we run the Sharphound command to perform the enumeration and output a zip file.

   ```powershell
    .\SharpHound.exe --CollectionMethods All --Domain za.tryhackme.com --ExcludeDCs
   ```

   ![Bloodhound Sharphound](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/adenumeration/Enumerating_Active_Directory_Bloodhound_Sharphound.png)

   We should transfer this file over to our attackmachine. This can be done using `scp`.

   ```cmd
   scp mitchell.murphy@THMJMP1.za.tryhackme.com:C:/Users/mitchell.murphy/Documents/20250211101554_BloodHound.zip .
   ```

   ![Bloodhound Transfer](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/adenumeration/Enumerating_Active_Directory_Bloodhound_Transfer.png)

   After importing the zip file into BloodHound, we can look at the analysis part to find kerberoastable accounts.

   ![Bloodhound Kerberoastable](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/adenumeration/Enumerating_Active_Directory_Bloodhound_Kerberoastable.png)

   ><details><summary>Click for answer</summary>4</details>

3. How many machines do members of the Tier 1 Admins group have administrative access to?

   I was unable to find this answer in the results.

   ><details><summary>Click for answer</summary>2</details>

4. How many users are members of the Tier 2 Admins group?

   We should search for the T2 admin group and read the node information in Bloodhound.

   ![Bloodhound T2](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/adenumeration/Enumerating_Active_Directory_Bloodhound_T2.png)

   ><details><summary>Click for answer</summary>15</details>

