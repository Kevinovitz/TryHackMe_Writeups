![Burp Suite: Other Modules Banner](https://assets.tryhackme.com/room-banners/burpsuite.svg)

<p align="center">
   <img src="https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/burpsuiteom/Burp_Suite_Other_Modules_Cover.png" alt="Burp Suite: Other Modules Logo">
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

   This is the button on the bottom of the page.

   ![Overview](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/burpsuiteom/Burp_Suite_Other_Modules_Overview.png)

   ><details><summary>Click for answer</summary>Smart Decode</details>

### Decoder: Encoding/Decoding

Base64 encode the phrase: Let's Start Simple.

1. What is the base64 encoded version of this text?

   Use encode as base64.

   ![Encoding_Base64](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/burpsuiteom/Burp_Suite_Other_Modules_Encoding_Base64.png)

   ><details><summary>Click for answer</summary>TGV0J3MgU3RhcnQgU2ltcGxl</details>

URL Decode this data: %4e%65%78%74%3a%20%44%65%63%6f%64%69%6e%67.

2. What is the plaintext returned?

   Use decode as URL.

   ![Encoding_URL](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/burpsuiteom/Burp_Suite_Other_Modules_Encoding_URL.png)

   ><details><summary>Click for answer</summary>Next: Decoding</details>

Use Smart decode to decode this data: &#x25;&#x33;&#x34;&#x25;&#x33;&#x37;.

3. What is the decoded text?

   Click the smart decode button.

   ![Encoding_Smart](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/burpsuiteom/Burp_Suite_Other_Modules_Encoding_Smart.png)

   ><details><summary>Click for answer</summary>47</details>

Encode this phrase: Encoding Challenge.

Start with base64 encoding. Take the output of this and convert it into ASCII Hex. Finally, encode the hex string into octal.

4. What is the final string?

   First use encode as base64, then encode as ASCII hex, and finally use encode as octal.

   ![Encoding_Octal](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/burpsuiteom/Burp_Suite_Other_Modules_Encoding_Octal.png)

   ><details><summary>Click for answer</summary>24034214a720270024142d541357471232250253552c1162d1206c</details>

### Decoder: Hashing

Using Decoder, what is the SHA-256 hashsum of the phrase: Let's get Hashing!?

1. Convert this into an ASCII Hex string for the answer to this question.

   First we select the SHA-256 hash. Then we encode the output as ASCII hex.

   ![Hashing_SHA256](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/burpsuiteom/Burp_Suite_Other_Modules_Hashing_SHA256.png)

   ><details><summary>Click for answer</summary>6b72350e719a8ef5af560830164b13596cb582757437e21d1879502072238abe</details>

Generate an MD4 hashsum of the phrase: Insecure Algorithms.

2. Encode this as base64 (not ASCII Hex) before submitting.

   ![Hashing_Base64](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/burpsuiteom/Burp_Suite_Other_Modules_Hashing_Base64.png)

   ><details><summary>Click for answer</summary>TcV4QGZZN7y7lwYFRMMoeA==</details>

Let's look at an in-context example:

First, download the file attached to this task.

Note: This file can also be downloaded from the deployed VM with wget http://MACHINE_IP:9999/AlteredKeys.zip — you may find this helpful if you are using the AttackBox.

Now read the problem specification below:

"Some joker has messed with my SSH key! There are four keys in the directory, and I have no idea which is the real one. The MD5 hashsum for my key is 3166226048d6ad776370dc105d40d9f8 — could you find it for me?"

3. What is the correct key name?

   After hashing the key files, we get on hash that is the same as the provided hash.

   ![Hashing_Key](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/burpsuiteom/Burp_Suite_Other_Modules_Hashing_Key.png)

   ><details><summary>Click for answer</summary>key3</details>

### Sequencer: Overview

1. What does Sequencer allow us to evaluate?

   This answers can be found in the text.

   ><details><summary>Click for answer</summary>Entropy</details>

### Sequencer: Live Capture

1. What is the overall quality of randomness estimated to be?

   Make sure you capture the request of the webpage itself, not the login attempt. Send the request to sequencer and select the token form field.

   Start the live capture and wait until you have around 10000 tokens before performing the analysis.

   ![Capture_Quality](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/burpsuiteom/Burp_Suite_Other_Modules_Capture_Quality.png)

   ><details><summary>Click for answer</summary>Excellent</details>
   
### Organizer: Overview 

1. Are saved requests read-only? (yea/nay) 

   The answer can be found in the text.

   ><details><summary>Click for answer</summary>yea</details>
