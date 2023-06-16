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
   
### Repeater Inspector
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
### Extra Mile SQLi with Repeater
### Conclusion Room Conclusion



1. 

   

   ><details><summary>Click for answer</summary></details>

