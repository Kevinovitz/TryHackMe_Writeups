![Burp Suite: The Basics Banner](https://assets.tryhackme.com/room-banners/burpsuite.svg)

<p align="center">
   <img src="https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/burpsuitebasics/Burp_Suite_The_Basics_Cover.png" alt="Burp Suite: The Basics Logo">
</p>

# Burp Suite: The Basics (Old)

This guide contains the answer and steps necessary to get to them for the [Burp Suite: The Basics](https://tryhackme.com/room/burpsuitebasics) room.

> [!Note]
> Please note the BurpSuite rooms have been updated to reflect a newer version. As such some of these answers might not be correct anymore. Most of them still are but can be out of order of the new room.

## Table of contents

- [Getting Started What is Burp Suite?](#getting-started-what-is-burp-suite)
- [Getting Started Features of Burp Community](#getting-started-features-of-burp-community)
- [Getting Started Options](#getting-started-options)
- [Proxy Introduction to the Burp Proxy](#proxy-introduction-to-the-burp-proxy)
- [Proxy Connecting through the Proxy (FoxyProxy)](#proxy-connecting-through-the-proxy-foxyproxy)
- [Proxy Proxying HTTPS](#proxy-proxying-https)
- [Proxy Scoping and Targeting](#proxy-scoping-and-targeting)
- [Proxy Site Map and Issue Definitions](#proxy-site-map-and-issue-definitions)
- [Practical Example Attack ](#practical-example-attack)

### Getting Started What is Burp Suite?

1. Which edition of Burp Suite will we be using in this module?

   The answer can be found in the text provided or through an internet search.   

   ><details><summary>Click for answer</summary>Burp Suite Community</details>

2. Which edition of Burp Suite runs on a server and provides constant scanning for target web apps?

   The answer can be found in the text provided or through an internet search.   

   ><details><summary>Click for answer</summary>Burp Suite Enterprise</details>

3. Burp Suite is frequently used when attacking web applications and ______ applications.

   The answer can be found in the text provided or through an internet search.   

   ><details><summary>Click for answer</summary>mobile</details>

### Getting Started Features of Burp Community

Some of the functionalities of Burp Suite Community edition.

1. Which Burp Suite feature allows us to intercept requests between ourselves and the target?

   The answer can be found in the text provided or through an internet search.   

   ><details><summary>Click for answer</summary>Proxy</details>

2. Which Burp tool would we use if we wanted to bruteforce a login form?

   The answer can be found in the text provided or through an internet search.   

   ><details><summary>Click for answer</summary>Intruder</details>

### Getting Started Options

The answers to the following questions can be found by looking through the settings menus in Burp Suite.

2. In which Project options sub-tab can you find reference to a "Cookie jar"?

   ![Cookie](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/burpsuitebasics/Burp_Suite_The_Basics_Options_Cookie.png)

   ><details><summary>Click for answer</summary>Sessions</details>

3. In which User options sub-tab can you change the Burp Suite update behaviour?

   ![Update](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/burpsuitebasics/Burp_Suite_The_Basics_Options_Update.png)

   ><details><summary>Click for answer</summary>Misc</details>

4. What is the name of the section within the User options "Misc" sub-tab which allows you to change the Burp Suite keybindings?

   ![Bindings](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/burpsuitebasics/Burp_Suite_The_Basics_Options_Bindings.png)

   ><details><summary>Click for answer</summary>Hotkeys</details>

5. If we have uploaded Client-Side TLS certificates in the User options tab, can we override these on a per-project basis (Aye/Nay)?

   The answer can be found in the text provided or through an internet search.

   ><details><summary>Click for answer</summary>Aye</details>

### Proxy Introduction to the Burp Proxy

1. Which button would we choose to send an intercepted request to the target in Burp Proxy?

   On the proxy tab we can enable intercept, open the browser, and navigating to tryhackme.com. 
   
   ![Intercepted](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/burpsuitebasics/Burp_Suite_The_Basics_Intro_To_Proxy_Intercepted.png)
   
   If we want to send the request to the browser, we must click forward.
   
   ![Forwarded](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/burpsuitebasics/Burp_Suite_The_Basics_Intro_To_Proxy_Forwarded.png)

   ><details><summary>Click for answer</summary>Forward</details>

2. [Research] What is the default keybind for this? **Note**: Assume you are using Windows or Linux (i.e. swap Cmd for Ctrl). 

   With a quick search we can find the required hotkey.

   ><details><summary>Click for answer</summary>Ctrl+F</details>

### Proxy Connecting through the Proxy (FoxyProxy)

Read through the options in the right-click menu.

1. There is one particularly useful option that allows you to intercept and modify the response to your request.

   What is this option? 

   First we make sure to enable the intercept in BurpSuite and FoxyProxy in Firefox.
   
   ![Intercepted](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/burpsuitebasics/Burp_Suite_The_Basics_Connecting_Through_Proxy_Intercepted.png)
   
   After intercepting the request we can inspect the menu options.
   
   ![Option](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/burpsuitebasics/Burp_Suite_The_Basics_Connecting_Through_Proxy_Option.png)

   ><details><summary>Click for answer</summary>Response to this request</details>

### Proxy Proxying HTTPS

I had already configure Firefox before with the certificate for Burp Suite. However, when trying in this room, it seemed to not work anymore. Even downloading the certificate didn't work.

So I made a backup of the current certificate that was loaded, deleted it, and then I could download the certificate again. 

After importing it, I could visit TLS enabled websites in Firefox through FoxyProxy.

### Proxy Scoping and Targeting

No real difference was spotted when targeting the specific URL (http://http://10.10.195.240/). This might be due to the website having no redirects.

![Not Scoped](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/burpsuitebasics/Burp_Suite_The_Basics_Scoping_Targeting_Not_Scoped.png)

### Proxy Site Map and Issue Definitions

Take a look around the site. Visit every page linked to from the homepage, then check your sitemap -- one endpoint should stand out as being very unusual!

Visit this in your browser (or use the "Response" section of the site map entry for that endpoint)

1. What is the flag you receive?

   After visting all sites, we can see our sitemap in BurpSuite
   
   ![URL](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/burpsuitebasics/Burp_Suite_The_Basics_Sitemap_URL.png)
   
   One of these entries does indeed stand out. Lets visit it to see if we get our flag.
   
   ![Flag](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/burpsuitebasics/Burp_Suite_The_Basics_Sitemap_Flag.png)

   ><details><summary>Click for answer</summary>THM{NmNlZTliNGE1MWU1ZTQzMzgzNmFiNWVk}</details>

Look through the Issue Definitions list.

2. What is the typical severity of a Vulnerable JavaScript dependency?

   If we navigate to the Issue Definitions list related to our sitemap, we can find the severity for a Vulnerable JavaScript dependency.
   
   ![Vulnerability](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/burpsuitebasics/Burp_Suite_The_Basics_Sitemap_Vulnerability.png)
   ><details><summary>Click for answer</summary>Low</details>

### Practical Example Attack 

Try to bypass the filter to achieve Cross Site Scripting.

First thing to try obviously, is our payload, to see if it is indeed filtered. This does seem to be the case unfortunately.

After making sure FoxyProxy in Firefox and Intercept in BurpSuite are both turned on, we can enter some fake but allowed data.

![Query](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/burpsuitebasics/Burp_Suite_The_Basics_Example_Query.png)

After submitting, we should have intercepted the request in BurpSuite.

![Request](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/burpsuitebasics/Burp_Suite_The_Basics_Example_Request.png)

Now we can change the email part of the request with our own payload:

```cmd
<script>alert("Succ3ssful XSS")</script>
```

![Script](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/burpsuitebasics/Burp_Suite_The_Basics_Example_Script.png)

Now select the payload and use the `Ctrl + u` shortcut to encode the string.

![Script Encoded](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/burpsuitebasics/Burp_Suite_The_Basics_Example_Script_Encoded.png)

Now we forward the modified request with BurpSuite and we should receieve a pop-up message.

![Success](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/burpsuitebasics/Burp_Suite_The_Basics_Example_Success.png)
