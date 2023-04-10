![Content Discovery](https://tryhackme-images.s3.amazonaws.com/user-uploads/5efe36fb68daf465530ca761/room-content/03376575e888fd097280c51469c29fbc.png)

<p align="center">
   <img src="https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/contentdiscovery/Content_Discovery_Cover.png" alt="Content Discovery Logo">
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

   ><details><summary>Click for answer</summary>/staff-portal</details>

### Manual Discovery - Favicon

In this task we will be looking at the favicon to find out more about the underlying framework of the website.

We will use the following website as an example:

https://static-labs.tryhackme.cloud/

We look at the source of the page and note the link to the favicon. Then we can use curl to download the image and get its hash.

```cmd
curl https://static-labs.tryhackme.cloud/sites/favicon/images/favicon.ico | md5sum
```

><details><summary>MD5 hash</summary>f276b19aabcb4ae8cda4d22625c6735f</details>

Now we can navigate to the following website to compare the hash and find the framework:

https://wiki.owasp.org/index.php/OWASP_favicon_database


   ><details><summary>Click for answer</summary>cgiirc</details>

### Manual Discovery - Sitemap.xml

In this task we will look at the sitemap of the demo website. 

1. What is the path of the secret area that can be found in the sitemap.xml file?

   Looking at the sitemap, we can see a secret page.

   ><details><summary>Click for answer</summary>/s3cr3t-area</details>

### Manual Discovery - HTTP Headers

In this task we will look into more detail to HTTP headers.

1. What is the flag value from the X-FLAG header?

   To get the header information we use the following command with verbose mode enabled:
   
   ```cmd
   curl http://10.10.43.213/ -v
   ```

   ><details><summary>Click for answer</summary>THM{HEADER_FLAG}</details>

### Manual Discovery - Framework Stack

In this task we will look at the framework stack of the website.

1. What is the flag from the framework's administration portal? 

   On the page source of the website we find a link to the framework used. 
   
   
   
   Here we find a link to the framework documentation which reveals a hidden admin panel.
   
   
   
   We can login to this panel with the default credentials if they haven't been changed.

   ><details><summary>Click for answer</summary>THM{CHANGE_DEFAULT_CREDENTIALS}</details>

### OSINT - Google Hacking / Dorking



   ><details><summary>Click for answer</summary></details>

### OSINT - Wappalyzer



   ><details><summary>Click for answer</summary></details>

### OSINT - Wayback Machine



   ><details><summary>Click for answer</summary></details>

### OSINT - GitHub



   ><details><summary>Click for answer</summary></details>

### OSINT - S3 Buckets



   ><details><summary>Click for answer</summary></details>

### Automated Discovery



   ><details><summary>Click for answer</summary></details>
