![Nessus Banner](https://i.imgur.com/qopFZj9.jpg)

<p align="center">
   <img src="https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/rpnessusredux/Nessus_Cover.png" alt="Nessus Logo">
</p>

# Nessus

This guide contains the answer and steps necessary to get to them for the [Nessus](https://tryhackme.com/room/rpnessusredux) room.

## Table of contents

- [Navigation and Scans](#navigation-and-scans)
- [Scanning!](#scanning)
- [Scanning a Web Application! ](#scanning-a-web-application)

### Navigation and Scans

The next 3 questions can be answered from the home screen (depicted in the image below).

NAVIGATION HOME

1. What is the name of the button which is used to launch a scan?

   ><details><summary>Click for answer</summary>New scan</details>
   
2. What side menu option allows us to create custom templates?

   ><details><summary>Click for answer</summary>Policies</details>
   
3. What menu allows us to change plugin properties such as hiding them or changing their severity?

   ><details><summary>Click for answer</summary>Plugin Rules</details>

The next 4 questions can be answered from the scan templates screen (depicted in the image below).

NAVIGATION TEMPLATES

4. In the 'Scan Templates' section after clicking on 'New Scan', what scan allows us to see simply what hosts are alive?

   ><details><summary>Click for answer</summary>Host Discovery</details>
   
5. One of the most useful scan types, which is considered to be 'suitable for any host'?

   ><details><summary>Click for answer</summary>Basic Network Scan</details>
   
6. What scan allows you to 'Authenticate to hosts and enumerate missing updates'?

   ><details><summary>Click for answer</summary>Credentialed Patch Audit</details>
   
7. What scan is specifically used for scanning Web Applications? 

   ><details><summary>Click for answer</summary>Web Application Tests</details>

### Scanning!

1. Create a new 'Basic Network Scan' targeting the deployed VM. What option can we set under 'BASIC' (on the left) to set a time for this scan to run? This can be very useful when network congestion is an issue.

   SCANNING SCHEDULE

   ><details><summary>Click for answer</summary>Schedule</details>
   
2. Under 'DISCOVERY' (on the left) set the 'Scan Type' to cover ports 1-65535. What is this type called?

   SCANNING PORTS

   ><details><summary>Click for answer</summaryPort scan (all ports)details>

3. What 'Scan Type' can we change to under 'ADVANCED' for lower bandwidth connection?

   SCANNING BANDWITDH

   ><details><summary>Click for answer</summary>Scan low bandwidth links</details>

With these options set,  launch the scan. 

4. After the scan completes, which 'Vulnerability' in the 'Port scanners' family can we view the details of to see the open ports on this host?

   SCANNING PORTSCANNER

   ><details><summary>Click for answer</summary>Nessus SYN Scanner</details>

5. What Apache HTTP Server Version is reported by Nessus?

   SCANNING APACHE

   ><details><summary>Click for answer</summary>2.4.99</details>

### Scanning a Web Application! 

1. What is the plugin id of the plugin that determines the HTTP server type and version?

   This plugin can be found under Vulnerabilities in: HTTP (Web Servers) -> HTTP Server Type and Version.

   APPLICATION HTTP PLUGIN

   ><details><summary>Click for answer</summary>10107</details>

3. What authentication page is discovered by the scanner that transmits credentials in cleartext?

   This vulnerability can be found under Vulnerabilities: Web Server -> Web Server Transmits Cleartext Credentials.

   APPLICATION AUTHENTICATION

   ><details><summary>Click for answer</summary></details>

5. What is the file extension of the config backup?

   In the vulnerabilities list in: Backup Files Disclosures, we can find the backup file extension.

   APPLICATION BACKUP

   ><details><summary>Click for answer</summary>.bak</details>

7. Which directory contains example documents? (This will be in a php directory)

   Under Browsable Web Directories we can see a directory containing example documents.

   APPLICATION DIRECTORY

   ><details><summary>Click for answer</summary/external/phpids/0.6/docs/examples/details>

9. What vulnerability is this application susceptible to that is associated with X-Frame-Options?

   Looking through the vulnerabilties, we see one that is related to X-frame options under Web Application Potentially Vulnerable to Clickjacking.

   APPLICATION XFRAME

   ><details><summary>Click for answer</summary>Clickjacking</details>
