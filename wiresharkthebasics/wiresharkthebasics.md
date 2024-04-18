![Title Banner](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/wiresharkthebasics/Wireshark_Basics_Banner.png)

<p align="center">
   <img src="https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/wiresharkthebasics/Wireshark_Basics_Cover.png" alt="Wireshark: The Basics Logo">
</p>

# Wireshark: The Basics

This guide contains the answer and steps necessary to get to them for the [Wireshark: The Basics](https://tryhackme.com/room/wiresharkthebasics) room.

## Table of contents

- [Introduction](#introduction)
- [Tool Overview](#tool-overview)
- [Packet Dissection](#packet-dissection)
- [Packet Navigation](#packet-navigation)
- [Packet Filtering](#packet-filtering)

### Introduction

1. Which file is used to simulate the screenshots?

   ><details><summary>Click for answer</summary>http1.pcapng</details>

2. Which file is used to answer the questions?

   ><details><summary>Click for answer</summary>Exercise.pcapng</details>

### Tool Overview

Use the "Exercise.pcapng" file to answer the questions.

For these questions we must look at the Capture File Properties.

![Overview Answers](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/wiresharkthebasics/Wireshark_Basics_Overview_Answers.png)

1. Read the "capture file comments". What is the flag?

   ><details><summary>Click for answer</summary>TryHackMe_Wireshark_Demo</details>

2. What is the total number of packets?

   ><details><summary>Click for answer</summary>58620</details>

3. What is the SHA256 hash value of the capture file?

   ><details><summary>Click for answer</summary>f446de335565fb0b0ee5e5a3266703c778b2f3dfad7efeaeccb2da5641a6d6eb</details>

### Packet Dissection

Use the "Exercise.pcapng" file to answer the questions.

1. View packet number 38. Which markup language is used under the HTTP protocol?

   After selecting the corresponding packet, the used markup language is displayed at the bottom of the details pane.

   ![Dissection Markup](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/wiresharkthebasics/Wireshark_Basics_Dissection_Markup.png)

   ><details><summary>Click for answer</summary>eXtensible Markup Language</details>

3. What is the arrival date of the packet? (Answer format: Month/Day/Year)

   This can be found under the Frame layer.

   ![Dissection Time](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/wiresharkthebasics/Wireshark_Basics_Dissection_Time.png)

   ><details><summary>Click for answer</summary>05/13/2004</details>

5. What is the TTL value?

   This can be found under the IP Source layer.

   ![Dissection TTL](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/wiresharkthebasics/Wireshark_Basics_DissectionTTL.png)

   ><details><summary>Click for answer</summary>47</details>

7. What is the TCP payload size?

   This can be found under the TCP layer.

   ![Dissection Payload](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/wiresharkthebasics/Wireshark_Basics_Dissection_Payload.png)

   ><details><summary>Click for answer</summary>424</details>

9. What is the e-tag value?

   This can be found under the HTTP layer.

   ![Dissection Etag](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/wiresharkthebasics/Wireshark_Basics_Dissection_Etag.png)

   ><details><summary>Click for answer</summary>9a01a-4696-7e354b00</details>

### Packet Navigation

Use the "Exercise.pcapng" file to answer the questions.

1. Search the "r4w" string in packet details. What is the name of artist 1?

   Searching for "r4w" in the packets details pane, we get a hit for packet 43362.

   ![Navigation Artist](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/wiresharkthebasics/Wireshark_Basics_Navigation_Artist.png)
   
   ><details><summary>Click for answer</summary>r4w8173</details>

3. Go to packet 12 and read the comments. What is the answer?

   Package 12 contains the following comment.

   ```
   Go to packet number 39765
   Look at the "packet details pane". Right-click on the JPEG section and "Export packet bytes". This is an alternative way of extracting data from a capture file. What is the MD5 hash value of extracted image?
   ```

   ![Navigation Answer 1](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/wiresharkthebasics/Wireshark_Basics_Navigation_Answer_1.png)

   After navigating to packet 39765 and exporting the object, we can extract its hash using `md5sum`.

   ![Navigation Download](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/wiresharkthebasics/Wireshark_Basics_Navigation_Download.png)

   ![Navigation Hash](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/wiresharkthebasics/Wireshark_Basics_Navigation_Hash.png)

   ><details><summary>Click for answer</summary>911cd574a42865a956ccde2d04495ebf</details>

3. There is a ".txt" file inside the capture file. Find the file and read it; what is the alien's name?

   To get this file, we navigate to the 'export http objects' menu. Here we filter on text/plain files. This gives us one hit. From here we can preview it to find the name.

   ![Navigation Alien](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/wiresharkthebasics/Wireshark_Basics_Navigation_Alien.png)

   ><details><summary>Click for answer</summary>Packetmaster</details>

5. Look at the expert info section. What is the number of warnings?

   The warning row has a column with the number of errors.

   ![Navigation Warnings](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/wiresharkthebasics/Wireshark_Basics_Navigation_Warnings.png)

   ><details><summary>Click for answer</summary>1636</details>

### Packet Filtering 

Use the "Exercise.pcapng" file to answer the questions.

1. Go to packet number 4. Right-click on the "Hypertext Transfer Protocol" and apply it as a filter. Now, look at the filter pane. What is the filter query?

   After applying the filter, we see the query in the display filter box.

   ![Filtering Http](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/wiresharkthebasics/Wireshark_Basics_Filtering_Http.png)

   ><details><summary>Click for answer</summary>http</details>

3. What is the number of displayed packets?

   At the bottom of the window we get the number of displayed packets.

   ><details><summary>Click for answer</summary>1089</details>

4. Go to packet number 33790 and follow the stream. What is the total number of artists?

   After navigating to packet 33790 and following the http stream, we can see the entire communication stream. We can get the number of artist by looking at the stream or by exporting the relevant html file.

   ![Filtering Follow](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/wiresharkthebasics/Wireshark_Basics_Filtering_Follow.png)

   ![Filtering Artists](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/wiresharkthebasics/Wireshark_Basics_Filtering_Artists.png)

   ><details><summary>Click for answer</summary>3</details>

6. What is the name of the second artist?

   ><details><summary>Click for answer</summary>Blad3</details>
