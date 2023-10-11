![Wireshark: Packet Operations Banner](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/wiresharkthebasics/Wireshark_Basics_Banner.png)

<p align="center">
   <img src="https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/wiresharkpacketoperations/Wireshark_Packet_Operations_Cover.png" alt="Wireshark: Packet Operations Logo">
</p>

# Wireshark: Packet Operations

This guide contains the answer and steps necessary to get to them for the [TITLE](https://tryhackme.com/room/wiresharkpacketoperations) room.

## Table of contents

- [Statistics | Summary](#statistics--summary)
- [Statistics | Protocol Details](#statistics--protocol-details)
- [Packet Filtering | Protocol Filters](#packet-filtering--protocol-filters)
- [Advanced Filtering ](#advanced-filtering)

### Statistics | Summary

1. Investigate the resolved addresses. What is the IP address of the hostname starts with "bbc"?

   
   
   
   
   SUMMARIES IP

   ><details><summary>Click for answer</summary>199.232.24.81</details>

3. What is the number of IPv4 conversations?

   SUMMARIES IPV4

   ><details><summary>Click for answer</summary>a435</details>

4. How many bytes (k) were transferred from the "Micro-St" MAC address?

   SUMMARIES MICRO 1

   SUMMARIES MICRO 2

   ><details><summary>Click for answer</summary>7474</details>

6. What is the number of IP addresses linked with "Kansas City"?

   ```cmd
   ip.geoip.city == "Kansas CIty"
   ```

   SUMMARIES KANSAS

   ><details><summary>Click for answer</summary>4</details>

8. Which IP address is linked with "Blicnet" AS Organisation?

   ```cmd
   ip.geoip.org matches "Blicnet.*"
   ```

   SUMMARIES BLICNET

   ><details><summary>Click for answer</summary>188.246.82.7</details>

### Statistics | Protocol Details

1. What is the most used IPv4 destination address?



   ><details><summary>Click for answer</summary></details>

2. What is the max service request-response time of the DNS packets?



   ><details><summary>Click for answer</summary></details>

3. What is the number of HTTP Requests accomplished by "rad[.]msn[.]com?



   ><details><summary>Click for answer</summary></details>

### Packet Filtering | Protocol Filters

1. What is the number of IP packets?



   ><details><summary>Click for answer</summary></details>

2. What is the number of packets with a "TTL value less than 10"?



   ><details><summary>Click for answer</summary></details>

3. What is the number of packets which uses "TCP port 4444"?



   ><details><summary>Click for answer</summary></details>

4. What is the number of "HTTP GET" requests sent to port "80"?



   ><details><summary>Click for answer</summary></details>

5. What is the number of "type A DNS Queries"?



   ><details><summary>Click for answer</summary></details>

### Advanced Filtering 

1. Find all Microsoft IIS servers. What is the number of packets that did not originate from "port 80"?



   ><details><summary>Click for answer</summary></details>

2. Find all Microsoft IIS servers. What is the number of packets that have "version 7.5"?



   ><details><summary>Click for answer</summary></details>

3. What is the total number of packets that use ports 3333, 4444 or 9999?



   ><details><summary>Click for answer</summary></details>

4. What is the number of packets with "even TTL numbers"?



   ><details><summary>Click for answer</summary></details>

5. Change the profile to "Checksum Control". What is the number of "Bad TCP Checksum" packets?



   ><details><summary>Click for answer</summary></details>

6. Use the existing filtering button to filter the traffic. What is the number of displayed packets?



   ><details><summary>Click for answer</summary></details>
