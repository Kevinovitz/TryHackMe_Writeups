![Active Directory Basics Banner](https://i.imgur.com/bEG08k9.png)

<p align="center">
   <img src="https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/winadbasics/Active_Directory_Basics_Cover.png" alt="Active Directory Basics Logo">
</p>

# Active Directory Basics

This guide contains the answer and steps necessary to get to them for the [Active Directory Basics](https://tryhackme.com/room/winadbasics) room.

## Table of contents

- [Windows Domains](#windows-domains)
- [Active Directory](#active-directory)
- [Managing Users in AD](#managing-users-in-ad)
- [Managing Computers in AD](#managing-computers-in-ad)
- [Group Policies](#group-policies)
- [Authentication Methods](#authentication-methods)
- [Trees, Forests and Trusts](#trees forests and trusts)

### Windows Domains

1. In a Windows domain, credentials are stored in a centralised repository called...

   The answer to this question can be found in the text.

   ><details><summary>Click for answer</summary>Active Directory</details>

2. The server in charge of running the Active Directory services is called...

   The answer to this question can be found in the text.

   ><details><summary>Click for answer</summary>Domain Controller</details>

### Active Directory

1. Which group normally administrates all computers and resources in a domain?



   ><details><summary>Click for answer</summary></details>

2. What would be the name of the machine account associated with a machine named TOM-PC?



   ><details><summary>Click for answer</summary></details>

3. Suppose our company creates a new department for Quality Assurance. What type of containers should we use to group all Quality Assurance users so that policies can be applied consistently to them?



   ><details><summary>Click for answer</summary></details>

### Managing Users in AD

1. What was the flag found on Sophie's desktop?



   ><details><summary>Click for answer</summary></details>

2. The process of granting privileges to a user over some OU or other AD Object is called...



   ><details><summary>Click for answer</summary></details>

### Managing Computers in AD

1. After organising the available computers, how many ended up in the Workstations OU?



   ><details><summary>Click for answer</summary></details>

2. Is it recommendable to create separate OUs for Servers and Workstations? (yay/nay)



   ><details><summary>Click for answer</summary></details>

### Group Policies

1. What is the name of the network share used to distribute GPOs to domain machines?



   ><details><summary>Click for answer</summary></details>

2. Can aGPObe used to apply settings to users and computers? (yay/nay)



   ><details><summary>Click for answer</summary></details>

### Authentication Methods

1. Will a current version of Windows use NetNTLM as the preferred authentication protocol by default? (yay/nay)



   ><details><summary>Click for answer</summary></details>

2. When referring toKerberos, what type of ticket allows us to request further tickets known as TGS?



   ><details><summary>Click for answer</summary></details>

3. When using NetNTLM, is a user's password transmitted over the network at any point? (yay/nay)



   ><details><summary>Click for answer</summary></details>

### Trees, Forests and Trusts

1. What is a group of Windows domains that share the same namespace called?



   ><details><summary>Click for answer</summary></details>

2. What should be configured between two domains for a user in Domain A to access a resource in Domain B?



   ><details><summary>Click for answer</summary></details>

