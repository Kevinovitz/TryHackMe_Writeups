![Wireshark: Packet Operations Banner](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/wiresharkthebasics/Wireshark_Basics_Banner.png)

<p align="center">
   <img src="https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/wiresharkpacketoperations/Wireshark_Packet_Operations_Cover.png" alt="Wireshark: Packet Operations Logo">
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

   Navigating to: "Statistics -> IPv4 Statistics -> Source and Destination Addresses" we can see the number of destination addresses.

   ![Details IPv4](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/wiresharkpacketoperations/Wireshark_Packet_Operations_Details_IPv4.png)

   ><details><summary>Click for answer</summary>10.100.1.33</details>

3. What is the max service request-response time of the DNS packets?

   This we can find under: "Statistics -> DNS -> Service Stats". Make sure that you use the same unit as the question (i.e., seconds vs miliseconds).

   ![Details Response](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/wiresharkpacketoperations/Wireshark_Packet_Operations_Details_Response.png)

   ><details><summary>Click for answer</summary>0.467897</details>

5. What is the number of HTTP Requests accomplished by "rad[.]msn[.]com?

   This can be found in the "HTTP -> Request" statistics menu. We can filter the data on our specified host name using:

   ```cmd
   http.host matches ".*rad.msn.com.*"

   ![Details Requests](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/wiresharkpacketoperations/Wireshark_Packet_Operations_Details_Requests.png)

   ><details><summary>Click for answer</summary>39</details>

### Packet Filtering | Protocol Filters

1. What is the number of IP packets?

   Use the following display filter:

   ```cmd
   ip
   ```

   ><details><summary>Click for answer</summary>81420</details>

3. What is the number of packets with a "TTL value less than 10"?

   Use the following display filter:

   ```cmd
   ip.ttl < 10
   ```

   ><details><summary>Click for answer</summary>66</details>

4. What is the number of packets which uses "TCP port 4444"?
   
   Use the following display filter:

   ```cmd
   tcp.port == 4444
   ```

   ><details><summary>Click for answer</summary>632</details>

5. What is the number of "HTTP GET" requests sent to port "80"?

   Use the following display filter:

   ```cmd
   (http.request.method == "GET") && (tcp.dstport == 80)
   ```

   For some strange reason the amount I found here wasn't correct. Luckily, it was just 1 shy of the correct answer.

   ![Filters HTTP Get](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/wiresharkpacketoperations/Wireshark_Packet_Operations_Filters_HTTP_Get.png)

   ><details><summary>Click for answer</summary>527</details>

7. What is the number of "type A DNS Queries"?

   Use the following display filter:

   ```cmd
   dns.a
   ```

   ><details><summary>Click for answer</summary>51</details>

### Advanced Filtering 

1. Find all Microsoft IIS servers. What is the number of packets that did not originate from "port 80"?

   Use the following display filter:

   ```cmd
   http.server contains "IIS" && !(tcp.srcport == 80)
   ```

   ><details><summary>Click for answer</summary>21</details>

3. Find all Microsoft IIS servers. What is the number of packets that have "version 7.5"?

   Use the following display filter:

   ```cmd
   http.server matches "IIS.*7.5.*"
   ```

   ><details><summary>Click for answer</summary>71</details>

5. What is the total number of packets that use ports 3333, 4444 or 9999?

   Use the following display filter:

   ```cmd
   tcp.port in {3333,4444,9999}
   ```

   ><details><summary>Click for answer</summary>2235</details>

7. What is the number of packets with "even TTL numbers"?

   Use the following display filter:

   ```cmd
   string(ip.ttl) matches ".*[02468]$"
   ```

   This first converts the TTL value to a string and matches it the a regex expression looking for strings ending with an even number (hence the `.*`).

   ><details><summary>Click for answer</summary>77289</details>

9. Change the profile to "Checksum Control". What is the number of "Bad TCP Checksum" packets?

   In the bottom right, we must right-click to switch to the "Checksum Profile".

   Looking through the display filter expression menu for `checksum`, we get a hit that we can use.

   ```cmd
   tcp.checksum_bad.expert
   ```

   ><details><summary>Click for answer</summary></details>

11. Use the existing filtering button to filter the traffic. What is the number of displayed packets?

   After switching to the correct profile a display filter button is visible for us to use. It uses the following filter:
   
   ```cmd
   (http.response.code == 200 ) && (http.content_type matches "image(gif||jpeg)")
   ```

   ![Advanced Button](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/wiresharkpacketoperations/Wireshark_Packet_Operations_Advanced_Button.png)

   ><details><summary>Click for answer</summary>261</details>
