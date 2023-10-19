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

1. What is the name of the button which is used to launch a scan?



   ><details><summary>Click for answer</summary></details>
   
2. What side menu option allows us to create custom templates?



   ><details><summary>Click for answer</summary></details>
   
3. What menu allows us to change plugin properties such as hiding them or changing their severity?



   ><details><summary>Click for answer</summary></details>
   
4. In the 'Scan Templates' section after clicking on 'New Scan', what scan allows us to see simply what hosts are alive?



   ><details><summary>Click for answer</summary></details>
   
5. One of the most useful scan types, which is considered to be 'suitable for any host'?



   ><details><summary>Click for answer</summary></details>
   
6. What scan allows you to 'Authenticate to hosts and enumerate missing updates'?



   ><details><summary>Click for answer</summary></details>
   
7. What scan is specifically used for scanning Web Applications? 



   ><details><summary>Click for answer</summary></details>

### Scanning!

1. Create a new 'Basic Network Scan' targeting the deployed VM. What option can we set under 'BASIC' (on the left) to set a time for this scan to run? This can be very useful when network congestion is an issue.



   ><details><summary>Click for answer</summary></details>
   
2. Under 'DISCOVERY' (on the left) set the 'Scan Type' to cover ports 1-65535. What is this type called?



   ><details><summary>Click for answer</summary></details>

3. What 'Scan Type' can we change to under 'ADVANCED' for lower bandwidth connection?



   ><details><summary>Click for answer</summary></details>

With these options set,  launch the scan. 

4. After the scan completes, which 'Vulnerability' in the 'Port scanners' family can we view the details of to see the open ports on this host?



   ><details><summary>Click for answer</summary></details>

5. What Apache HTTP Server Version is reported by Nessus?



   ><details><summary>Click for answer</summary></details>

### Scanning a Web Application! 

1. What is the plugin id of the plugin that determines the HTTP server type and version?



   ><details><summary>Click for answer</summary></details>

2. What authentication page is discovered by the scanner that transmits credentials in cleartext?



   ><details><summary>Click for answer</summary></details>

3. What is the file extension of the config backup?



   ><details><summary>Click for answer</summary></details>

4. Which directory contains example documents? (This will be in a php directory)



   ><details><summary>Click for answer</summary></details>

5. What vulnerability is this application susceptible to that is associated with X-Frame-Options?



   ><details><summary>Click for answer</summary></details>
