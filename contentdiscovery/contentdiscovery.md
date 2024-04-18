![Content Discovery](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/contentdiscovery/Content_Discovery_Banner.png)

<p align="center">
   <img src="https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/contentdiscovery/Content_Discovery_Cover.png" alt="Content Discovery Logo">
</p>

# Content Discovery

This guide contains the answer and steps necessary to get to them for the [Content Discovery](https://tryhackme.com/room/contentdiscovery) room.

### Table of Contents

- [What Is Content Discovery?](#what-is-content-discovery)
- [Manual Discovery - Robots.txt](#manual-discovery---robots.txt)
- [Manual Discovery - Favicon](#manual-discovery---favicon)
- [Manual Discovery - Sitemap.xml](#manual-discovery---sitemap.xml)
- [Manual Discovery - HTTP Headers](#manual-discovery---http-headers)
- [Manual Discovery - Framework Stack](#manual-discovery---framework-stack)
- [OSINT - Google Hacking / Dorking](#osint---google-hacking-/-dorking)
- [OSINT - Wappalyzer](#osint---wappalyzer)
- [OSINT - Wayback Machine](#osint---wayback-machine)
- [OSINT - GitHub](#osint---github)
- [OSINT - S3 Buckets](#osint---s3-buckets)
- [Automated Discovery](#automated-discovery)

### What is Content Discovery?

1. What is the Content Discovery method that begins with M?

   This answer can be found in the text.

   ><details><summary>Click for answer</summary>Manually</details>

2. What is the Content Discovery method that begins with A?

   This answer can be found in the text.

   ><details><summary>Click for answer</summary>Automated</details>

3. What is the Content Discovery method that begins with O?

   This answer can be found in the text.

   ><details><summary>Click for answer</summary>OSINT</details>

### Manual Discovery - Robots.txt

This task gives more information about the robots text file.

1. What is the directory in the robots.txt that isn't allowed to be viewed by web crawlers?

   Open the browser and navigate to the webpage's robots file. http://10.10.43.213/robots.txt

   ![Robots](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/contentdiscovery/Content_Discovery_Robots.png)

   ><details><summary>Click for answer</summary>/staff-portal</details>

### Manual Discovery - Favicon

In this task we will be looking at the favicon to find out more about the underlying framework of the website.

We will use the following website as an example:

https://static-labs.tryhackme.cloud/

We look at the source of the page and note the link to the favicon. Then we can use curl to download the image and get its hash.

![Source](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/contentdiscovery/Content_Discovery_Favicon_Source.png)

```cmd
curl https://static-labs.tryhackme.cloud/sites/favicon/images/favicon.ico | md5sum
```

![Hash](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/contentdiscovery/Content_Discovery_Favicon_Hash.png)

><details><summary>Click for answer</summary>f276b19aabcb4ae8cda4d22625c6735f</details>

Now we can navigate to the following website to compare the hash and find the framework:

https://wiki.owasp.org/index.php/OWASP_favicon_database

![Compare](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/contentdiscovery/Content_Discovery_Favicon_Compare.png)

   ><details><summary>Click for answer</summary>cgiirc</details>

### Manual Discovery - Sitemap.xml

In this task we will look at the sitemap of the demo website. 

1. What is the path of the secret area that can be found in the sitemap.xml file?

   Looking at the sitemap, we can see a secret page.

   ![Sitemap](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/contentdiscovery/Content_Discovery_Sitemap.png)

   ><details><summary>Click for answer</summary>/s3cr3t-area</details>

### Manual Discovery - HTTP Headers

In this task we will look into more detail to HTTP headers.

1. What is the flag value from the X-FLAG header?

   To get the header information we use the following command with verbose mode enabled:
   
   ```cmd
   curl http://10.10.43.213/ -v
   ```

   ![Headers](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/contentdiscovery/Content_Discovery_HTTP_Headers.png)
   
   ><details><summary>Click for answer</summary>THM{HEADER_FLAG}</details>

### Manual Discovery - Framework Stack

In this task we will look at the framework stack of the website.

1. What is the flag from the framework's administration portal? 

   On the page source of the website we find a link to the framework used. 
   
   ![Link](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/contentdiscovery/Content_Discovery_Framework_Link.png)
   
   Here we find a link to the framework documentation which reveals a hidden admin panel.
   
   ![Page](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/contentdiscovery/Content_Discovery_Framework_Page.png)
   
   We can login to this panel with the default credentials if they haven't been changed.

   ![Panel](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/contentdiscovery/Content_Discovery_Admin_Panel.png)

   ![Password](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/contentdiscovery/Content_Discovery_Admin_Password.png)

   ><details><summary>Click for answer</summary>THM{CHANGE_DEFAULT_CREDENTIALS}</details>

### OSINT - Google Hacking / Dorking

This room tels us more about google dorking and how it can be used to get better results.

1. What Google dork operator can be used to only show results from a particular site?

   This answer can be found in the supplied text.

   ><details><summary>Click for answer</summary>site:</details>

### OSINT - Wappalyzer

This task introduces the Wappalyzer tool.

1. What online tool can be used to identify what technologies a website is running?

   ><details><summary>Click for answer</summary>Whappalyzer</details>

### OSINT - Wayback Machine

This task gives us more info about the Wayback Machine website and its activities.

1. What is the website address for the Wayback Machine?

   The link to the service can be found in the text.
   
   ><details><summary>Click for answer</summary>https://archive.org/web/</details>

### OSINT - GitHub

This task show us how we can use GitHub to get information about a certain company, website, etc.

1. What is Git? 

   The answer to this question can be found in the text.
   
   ><details><summary>Click for answer</summary>Version Control System</details>

### OSINT - S3 Buckets

This task focusses on Amazon AWS buckets and their use.

1.  What URL format do Amazon S3 buckets end in?

   The answer to this question can be found in the text.

   ><details><summary>Click for answer</summary>s3.amazonaws.com</details>

### Automated Discovery

This task tell us more about the various automated ways we can discovery hidden content.

We can use multiple tools to perform this automated discovery. Below are the commands used for three common enumeration tools.

```cmd
ffuf -w /usr/share/wordlists/SecLists/Discovery/Web-Content/common.txt -u http://10.10.69.221/FUZZ

dirb http://10.10.69.221 /usr/share/wordlists/SecLists/Discovery/Web-Content/common.txt

gobuster dir -u http://10.10.69.221/ -w /usr/share/wordlists/SecLists/Discovery/Web-Content/common.txt
```

![Automated](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/contentdiscovery/Content_Discovery_Automated.png)

1. What is the name of the directory beginning "/mo...." that was discovered?

   ><details><summary>Click for answer</summary>/monthly</details>

2. What is the name of the log file that was discovered?

   ><details><summary>Click for answer</summary>/development.log</details>
