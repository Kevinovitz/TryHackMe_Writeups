![Auditing and Monitoring Banner](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/auditingandmonitoringse/Auditing_Monitoring_Banner.png)

<p align="center">
   <img src="https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/auditingandmonitoringse/Auditing_Monitoring_Cover.png" alt="Auditing and Monitoring Logo">
</p>

# Auditing and Monitoring

This guide contains the answer and steps necessary to get to them for the [Auditing and Monitoring](https://tryhackme.com/room/auditingandmonitoringse) room.

## Table of contents

- [Introduction](#introduction)
- [Audit Objectives and Types](#audit-objectives-and-types)
- [Audit Frameworks](#audit-frameworks)
- [Auditing IT Infrastructure and Operations](#auditing-it-infrastructure-and-operations)
- [Log Management on Linux](#log-management-on-linux)
- [Log Management on MS Windows](#log-management-on-ms-windows)

### Introduction

1. What do you call the systematic review of an organisation’s technological infrastructure, policies and operations?

   The answer to this question can be found in the text.

   ><details><summary>Click for answer</summary>Auditing</details>

2. What do you call the continuous observation of an organisation’s computer technologies and related resources?

   The answer to this question can be found in the text.

   ><details><summary>Click for answer</summary>Monitoring</details>

### Audit Objectives and Types

1. Which type of audit is conducted by independent auditors?

   The answer to this question can be found in the text.

   ><details><summary>Click for answer</summary>External audit</details>

2. Which type of audit is conducted by an organisation’s own personnel?

   The answer to this question can be found in the text.

   ><details><summary>Click for answer</summary>Internal audit</details>

### Audit Frameworks

1. What is the standard used by organisations that process card payments?

   The answer to this question can be found in the text.

   ><details><summary>Click for answer</summary>PCI DSS</details>

2. Who developed ITIL?

   To answer this question, a search is necessary.

   ><details><summary>Click for answer</summary>CCTA</details>

3. Who developed COBIT?

   To answer this question, a search is necessary.

   ><details><summary>Click for answer</summary>ISACA</details>

### Auditing IT Infrastructure and Operations

1. Which step do we present our findings about non-conformities, weaknesses and issues noted?

   The answer to this question can be found in the text.

   ><details><summary>Click for answer</summary>4</details>

2. At which stage does an organisation review the steps based on recommendations for proper and satisfactory implementation?

   The answer to this question can be found in the text.

   ><details><summary>Click for answer</summary>5</details>

3. At which stage do the auditors establish the audit scope and define its objectives?

   The answer to this question can be found in the text.

   ><details><summary>Click for answer</summary>1</details>

### Log Management on Linux

1. Usingaureport, how many failed logins have occurred so far?

   This can be done with `aureport` and its summary option.
   
   ```console
   aureport --summary
   ```

   ![Linux Summary](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/auditingandmonitoringse/Auditing_Monitoring_Linux_Summary.png)

   ><details><summary>Click for answer</summary>263</details>

2. Usingausearch, how many failed logins are related to the usernamemike?

   We can use the following command to get the failed login attempts for mike. 

   The first part gets all failed attempts, `grep` filters on mike, and `wc` counts the lines.
   
   ```console
   ausearch -m USER_LOGIN -sv no -i | grep ct=mike | wc -l
   ```

   ![Linux Mike](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/auditingandmonitoringse/Auditing_Monitoring_Linux_Mike.png)

   ><details><summary>Click for answer</summary>4</details>

3. Usingausearch, how many failed logins are related to the usernameroot?

   We can use the following command to get the failed login attempts for root. 

   The first part gets all failed attempts, `grep` filters on root, and `wc` counts the lines.
   
   ```console
   ausearch -m USER_LOGIN -sv no -i | grep ct=root | wc -l
   ```

   ![Linux Root](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/auditingandmonitoringse/Auditing_Monitoring_Linux_Root.png)

   ><details><summary>Click for answer</summary>227</details>

### Log Management on MS Windows

1. What is the event ID for a failed login attempt?

   The answer to this question can be found in the text.

   ><details><summary>Click for answer</summary>4625</details>

2. How many failed login attempts do you have under the security events?

   After opening Event Viewer it is a good idea to filter the log on the failed login attemps.

   Go to the SECURITY log and `filter log` based on EVENT ID 4625.

   ![Windows Logs](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/auditingandmonitoringse/Auditing_Monitoring_Windows_Logs.png)

   ><details><summary>Click for answer</summary>2</details>

3. How many failed login attempts took place in 2021?

   From the image above we can also the date of the events.

   ><details><summary>Click for answer</summary>1</details>

