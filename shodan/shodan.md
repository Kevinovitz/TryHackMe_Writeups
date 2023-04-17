![Shodanio Banner](https://i.imgur.com/J1ik7ZU.png)

<p align="center">
   <img src="https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/shodan/Shodan_Cover.png" alt="Shodan Logo">
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

![IP](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/shodan/Google_Filtering_IP.png)

![ASN](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/shodan/Google_Filtering_ASN.png)

1. What is the top operating system for MYSQL servers in Google's ASN?    

   asn:AS15169 product:MYSQL
   
   ![OS](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/shodan/Google_Filtering_OS.png)

   ><details><summary>Click for answer</summary>5.6.40-84.0-log</details>

2. What is the 2nd most popular country for MYSQL servers in Google's ASN?

   ![Country](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/shodan/Google_Filtering_Country.png)

   ><details><summary>Click for answer</summary>Netherlands</details>

3. Under Google's ASN, which is more popular for nginx, Hypertext Transfer Protocol or Hypertext Transfer Protocol with SSL?

   asn:AS15169 product:nginx
   
   ![Nginx](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/shodan/Google_Filtering_Nginx.png)

   ><details><summary>Click for answer</summary>Hypertext Transfer Protocol </details>

4. Under Google's ASN, what is the most popular city?

   asn:AS15169 country:"US"
   
   ![City](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/shodan/Google_Filtering_City.png)

   ><details><summary>Click for answer</summary>Mountain View</details>

5. Under Google's ASN in Los Angeles, what is the top operating system according to Shodan?

   asn:AS15169 city:"Los Angeles"
   
   ![LA OS](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/shodan/Google_Filtering_LA_OS.png)

   ><details><summary>Click for answer</summary>PAN-OS</details>

6. Using the top Webcam search from the explore page, does Google's ASN have any webcams? Yay / nay.

   webcam asn:AS15169
   
   ![Webcam](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/shodan/Google_Filtering_Webcam.png)

   ><details><summary>Click for answer</summary>Nay</details>

### Shodan Monitor



1. What URL takes you to Shodan Monitor?

   

   ><details><summary>Click for answer</summary></details>

### Shodan Dorking



1. What dork lets us find PCs infected by Ransomware? 

   

   ><details><summary>Click for answer</summary></details>
