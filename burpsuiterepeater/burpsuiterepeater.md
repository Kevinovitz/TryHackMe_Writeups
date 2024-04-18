![Burp Suite: Repeater Banner](https://assets.tryhackme.com/room-banners/burpsuite.svg)

<p align="center">
   <img src="https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/burpsuiterepeater/Burp_Suite_Repeater_Cover.png" alt="Burp Suite: Repeater Logo">
</p>

# Burp Suite: Repeater (Old)

This guide contains the answer and steps necessary to get to them for the [Burp Suite: Repeater](https://tryhackme.com/room/burpsuiterepeater) room.

> [!Note]
> Please note the BurpSuite rooms have been updated to reflect a newer version. As such some of these answers might not be correct anymore. Most of them still are but can be out of order of the new room.

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

![Basic Proxy](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/burpsuiterepeater/Burp_Suite_Repeater_Basic_Proxy.png)

Then we can send this request to repeater and send it to get a response. Note the connection argument.

![Basic Send](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/burpsuiterepeater/Burp_Suite_Repeater_Basic_Send.png)

Now we can change the connection argument and see the difference in response when we send it again.

![Repeated](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/burpsuiterepeater/Burp_Suite_Repeater_Basic_Repeated.png)

### Repeater Views

1. Which view option displays the response in the same format as your browser would?

   THe answers can be found in the text.
   
   ><details><summary>Click for answer</summary>Render</details>
   
### Practical Example

1. Send the request. What is the flag you receive?

   First we enable FoxyProxy in Firefox and capture the request from the website.

   ![Basic Proxy](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/burpsuiterepeater/Burp_Suite_Repeater_Basic_Proxy.png)

   Then we can send this request to repeater and send it to get a response. Note the connection argument.

   ![Basic Send](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/burpsuiterepeater/Burp_Suite_Repeater_Basic_Send.png)

   Now add the following argument at the bottom of the request and add two blank lines.

   ```cmd
   FlagAuthorised: True
   ```

   ![Flag](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/burpsuiterepeater/Burp_Suite_Repeater_Example_Flag.png)

   ><details><summary>Click for answer</summary>THM{Yzg2MWI2ZDhlYzdlNGFiZTUzZTIzMzVi}</details>
   
### Practical Challenge

See if you can get the server to error out with a "500 Internal Server Error" code by changing the number at the end of the request to extreme inputs.

1. What is the flag you receive when you cause a 500 error in the endpoint?

   On the product page, we can see an ID nr being used to display the current product.
   
   ![Product Page](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/burpsuiterepeater/Burp_Suite_Repeater_Challenge_Product_Page.png)

   Lets intercept this request in Burpsuite and send it to Repeater.
   
   ![Send To](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/burpsuiterepeater/Burp_Suite_Repeater_Challenge_Send_To.png)

   Now we can try different values for the ID nr to see if we can get an error. The following values were tried and all but one worked.

   ```cmd
   0
   10000
   999999999999999999
   aaaaaaadasdas
   qwe134@#!
   -0
   -1
   ```
   
   ![Flag](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/burpsuiterepeater/Burp_Suite_Repeater_Challenge_Flag.png)

   ><details><summary>Click for answer</summary>THM{N2MzMzFhMTA1MmZiYjA2YWQ4M2ZmMzhl}</details>

### Extra Mile SQLi with Repeater

Exploit the union SQL injection vulnerability in the site.

1. What is the flag?

   Lets capture the request again in Burpsuite and send it to Repeater.

   ![Request](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/burpsuiterepeater/Burp_Suite_Repeater_SQLi_Request.png)

   No quickly check for sql injection vulnerabilities we can add an `'` after the ID. Looks like there is.

   ![Response](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/burpsuiterepeater/Burp_Suite_Repeater_SQLi_Response.png)

   Next thing we need to do is enumerate the people table for column names. We should change the ID to a non-existant number to avoid any output.

   ```cmd
   UNION all SELECT column_name,null,null,null,null FROM information_schema.columns WHERE table_name="people"
   ```

   ![Enumeration](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/burpsuiterepeater/Burp_Suite_Repeater_SQLi_Enumeration.png)

   We see one column name, but we wan't them all. We can use concat to get them all.

   ```cmd
   UNION all SELECT group_concat(column_name),null,null,null,null FROM information_schema.columns WHERE table_name="people"
   ```   

   ![Table](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/burpsuiterepeater/Burp_Suite_Repeater_SQLi_Table.png)

   Now we get all the column names in the people table. We probably want to read the notes column. Looking at the website, we can find the corrensponding ID for the CEO (1).

   ![CEO](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/burpsuiterepeater/Burp_Suite_Repeater_SQLi_CEO.png)

   ```cmd
   UNION all SELECT notes,null,null,null,null FROM people WHERE id=1
   ```

   ![Flag](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/burpsuiterepeater/Burp_Suite_Repeater_SQLi_Flag.png)

   ><details><summary>Click for answer</summary>THM{ZGE3OTUyZGMyMzkwNjJmZjg3Mzk1NjJh}</details>
