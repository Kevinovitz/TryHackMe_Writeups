![Burp Suite: Other Modules Banner](https://assets.tryhackme.com/room-banners/burpsuite.svg)

<p align="center">
   <img src="https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/burpsuiteom/Burpsuite_Modules_Cover.png" alt="Burp Suite: Other Modules Logo">
</p>

# Burp Suite: Other Modules

This guide contains the answer and steps necessary to get to them for the [Burp Suite: Other Modules](https://tryhackme.com/room/burpsuiteom) room.

## Table of contents

- [Decoder: Overview](#decoder-overview)
- [Decoder: Encoding/Decoding](#decoder-encodingdecoding)
- [Decoder: Hashing](#decoder-hashing)
- [Sequencer: Overview](#sequencer-overview)
- [Sequencer: Live Capture](#sequencer-live-capture)
- [Organizer: Overview](#organizer-overview)

### Decoder: Overview

1. Which feature attempts auto-decode of the input?



   ><details><summary>Click for answer</summary></details>

### Decoder: Encoding/Decoding

Base64 encode the phrase: Let's Start Simple.

1. What is the base64 encoded version of this text?



   ><details><summary>Click for answer</summary></details>

URL Decode this data: %4e%65%78%74%3a%20%44%65%63%6f%64%69%6e%67.

2. What is the plaintext returned?



   ><details><summary>Click for answer</summary></details>

Use Smart decode to decode this data: &#x25;&#x33;&#x34;&#x25;&#x33;&#x37;.

3. What is the decoded text?



   ><details><summary>Click for answer</summary></details>

Encode this phrase: Encoding Challenge.

Start with base64 encoding. Take the output of this and convert it into ASCII Hex. Finally, encode the hex string into octal.

4. What is the final string?



   ><details><summary>Click for answer</summary></details>

### Decoder: Hashing

Using Decoder, what is the SHA-256 hashsum of the phrase: Let's get Hashing!?

1. Convert this into an ASCII Hex string for the answer to this question.



   ><details><summary>Click for answer</summary></details>

Generate an MD4 hashsum of the phrase: Insecure Algorithms.

2. Encode this as base64 (not ASCII Hex) before submitting.



   ><details><summary>Click for answer</summary></details>

Let's look at an in-context example:

First, download the file attached to this task.

Note: This file can also be downloaded from the deployed VM with wget http://MACHINE_IP:9999/AlteredKeys.zip — you may find this helpful if you are using the AttackBox.

Now read the problem specification below:

"Some joker has messed with my SSH key! There are four keys in the directory, and I have no idea which is the real one. The MD5 hashsum for my key is 3166226048d6ad776370dc105d40d9f8 — could you find it for me?"

3. What is the correct key name?



   ><details><summary>Click for answer</summary></details>

### Sequencer: Overview

1. What does Sequencer allow us to evaluate?



   ><details><summary>Click for answer</summary></details>

### Sequencer: Live Capture

1. What is the overall quality of randomness estimated to be?



   ><details><summary>Click for answer</summary></details>
   
### Organizer: Overview 

1. Are saved requests read-only? (yea/nay) 

   

   ><details><summary>Click for answer</summary></details>
