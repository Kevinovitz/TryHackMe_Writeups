![Burp Suite: Repeater Banner](https://assets.tryhackme.com/room-banners/burpsuite.svg)

<p align="center">
   <img src="https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/burpsuiterepeater/Burp_Suite_Repeater_Cover.png" alt="Burp Suite: Repeater Logo">
</p>

# Burp Suite: Repeater

This guide contains the answer and steps necessary to get to them for the [Burp Suite: Repeater](https://tryhackme.com/room/burpsuiterepeater) room.

## Table of contents

- [Repeater Basic Usage](#repeater-basic-usage)
- [Repeater Views](#repeater-views)
- [Repeater Inspector](#repeater-inspector)
- [Practical Example](#practical-example)
- [Practical Challenge](#practical-challenge)
- [Extra Mile SQLi with Repeater](#extra-mile-sqli-with-repeater)
- [Conclusion Room Conclusion](#conclusion-room-conclusion)

### Repeater Basic Usage

*Capture a request to http://10.10.34.19 in the Proxy and send it to Repeater.*

*Practice modifying and re-sending the request numerous times.*

First we enable FoxyProxy in Firefox and capture the request from the website.

BASIC PROXY

Then we can send this request to repeater and send it to get a response. Note the connection argument.

BASIC SEND

Now we can change the connection argument and see the difference in response when we send it again.

BASIC REPEAT

### Repeater Views

1. Which view option displays the response in the same format as your browser would?

   THe answers can be found in the text.
   
   ><details><summary>Click for answer</summary>Render</details>
   
### Practical Example

1. Send the request. What is the flag you receive?

   First we enable FoxyProxy in Firefox and capture the request from the website.

   BASIC PROXY

   Then we can send this request to repeater and send it to get a response. Note the connection argument.

   BASIC SEND

   Now add the following argument at the bottom of the request and add two blank lines.

   ```cmd
   FlagAuthorised: True
   ```

   EXAMPLE FLAG

   ><details><summary>Click for answer</summary>THM{Yzg2MWI2ZDhlYzdlNGFiZTUzZTIzMzVi}</details>
   
### Practical Challenge

See if you can get the server to error out with a "500 Internal Server Error" code by changing the number at the end of the request to extreme inputs.

1. What is the flag you receive when you cause a 500 error in the endpoint?

   CHALLENGE PRODUCT PAGE

   CHALLENGE REPEAT

   CHALLENGE FLAG

   ><details><summary>Click for answer</summary>THM{N2MzMzFhMTA1MmZiYjA2YWQ4M2ZmMzhl}</details>

### Extra Mile SQLi with Repeater

Exploit the union SQL injection vulnerability in the site.

1. What is the flag?

   SQLI REQUEST

   SQLI RESPONSE

   SQLI ENUMERATION

   SQLI TABLE

   SQLI CEO

   SQLI FLAG

   ><details><summary>Click for answer</summary>THM{ZGE3OTUyZGMyMzkwNjJmZjg3Mzk1NjJh}</details>
