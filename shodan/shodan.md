![Shodanio Banner](https://i.imgur.com/J1ik7ZU.png)

<p align="center">
   <img src="https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/shodan/Shodan_Cover.png" alt="Shodan Logo">
</p>

# Shodan.io

This guide contains the answer and steps necessary to get to them for the [Shodan.io](https://tryhackme.com/room/shodan) room.

## Table of contents

- [Filters](#filters)
- [Google & Filtering](#google--Filtering)
- [Shodan Monitor](#shodan-monitor)
- [Shodan Dorking](#shodan-dorking)

### Filters



1. How do we find Eternal Blue exploits on Shodan?

   

   ><details><summary>Click for answer</summary>vuln:ms17-010</details>

### Google & Filtering

![IP](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/shodan/Google_Filtering_IP.png)

![ASN](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/shodan/Google_Filtering_ASN.png)

1. What is the top operating system for MYSQL servers in Google's ASN?    

   asn:AS15169 product:MYSQL
   
   ![OS](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/shodan/Google_Filtering_OS.png)

   ><details><summary>Click for answer</summary>5.6.40-84.0-log</details>

2. What is the 2nd most popular country for MYSQL servers in Google's ASN?

   ![Country](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/shodan/Google_Filtering_Country.png)

   ><details><summary>Click for answer</summary>Netherlands</details>

3. Under Google's ASN, which is more popular for nginx, Hypertext Transfer Protocol or Hypertext Transfer Protocol with SSL?

   asn:AS15169 product:nginx
   
   ![Nginx](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/shodan/Google_Filtering_Nginx.png)

   ><details><summary>Click for answer</summary>Hypertext Transfer Protocol </details>

4. Under Google's ASN, what is the most popular city?

   asn:AS15169 country:"US"
   
   ![City](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/shodan/Google_Filtering_City.png)

   ><details><summary>Click for answer</summary>Mountain View</details>

5. Under Google's ASN in Los Angeles, what is the top operating system according to Shodan?

   asn:AS15169 city:"Los Angeles"
   
   ![LA OS](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/shodan/Google_Filtering_LA_OS.png)

   ><details><summary>Click for answer</summary>PAN-OS</details>

6. Using the top Webcam search from the explore page, does Google's ASN have any webcams? Yay / nay.

   webcam asn:AS15169
   
   ![Webcam](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/shodan/Google_Filtering_Webcam.png)

   ><details><summary>Click for answer</summary>Nay</details>

### Shodan Monitor

In this task we will look at a premium Shodan feature called Shodan Monitor.

1. What URL takes you to Shodan Monitor?

   Unfortunately, this feature is paid, so I am not able to check it out for myself. In addition the images in the room of this feature have been deleted as well.
   
   The answer can, fortunately, be found in the text itself.

   ><details><summary>Click for answer</summary>https://monitor.shodan.io/dashboard</details>

### Shodan Dorking



1. What dork lets us find PCs infected by Ransomware? 

   For this we can either look at the text or look at the search examples on Shodan and use the following search query:
   
   ```cmd
   has_screenshot:true encrypted attention
   ```
   
   1[]() ADD IMAGE HERE

   ><details><summary>Click for answer</summary>has_screenshot:true encrypted attention </details>
