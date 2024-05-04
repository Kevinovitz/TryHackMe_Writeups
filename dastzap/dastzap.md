![DAST Banner](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/dastzap/DAST_Banner.png)

<p align="center">
   <img src="https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/dastzap/DAST_Cover.png" alt="DAST Logo">
</p>

# DAST

This guide contains the answer and steps necessary to get to them for the [DAST](https://tryhackme.com/r/room/dastzap) room.

## Table of contents

- [Dynamic Application Security Testing (DAST)](#dynamic-application-security-testing-(dast))
- [Spiders and Crawlers](#spiders-and-crawlers)
- [Scanning for Vulnerabilities](#scanning-for-vulnerabilities)
- [Authenticated Scans](#authenticated-scans)
- [Checking APIs with ZAP](#checking-apis-with-zap)
- [Integrating DAST into the development pipeline](#integrating-dast-into-the-development-pipeline)

### Dynamic Application Security Testing (DAST)

The answers to the questions below can be found in the text.

1. Is DAST a replacement for SAST or SCA? (Yea/Nay)Correct Answer

   ><details><summary>Click for answer</summary>Nay</details>

2. What is the process of mapping an application's surface and parameters usually called?Correct Answer

   ><details><summary>Click for answer</summary>Spidering/Crawling</details>

3. Does DAST check the code of an application for vulnerabilities?(Yea/Nay)Correct Answer

   ><details><summary>Click for answer</summary>Nay</details>

### Spiders and Crawlers

1. ZAP can run an AJAX spider by using browsers without a Graphical User Interface(GUI). What are these browsers called?

   The answer can be found in te text.

   ><details><summary>Click for answer</summary>Headless</details>

2. Analysing the Sites tab, what HTTP parameters can be passed to login.php using the POST method? (In alphabetical order and separated by commas)

   After performing the scan, we can expand the sites tab to the left and look for the parameters.

   SPIDERS SITES

   ><details><summary>Click for answer</summary>pass,user</details>

3. What other .php resource, besides nospiders-gallery.php was found by the AJAX spider but not by the regular spider?

   Looking through the results of both scans, we can find another missing url.

   SPIDERS MISSING

   ><details><summary>Click for answer</summary>/view.php</details>

### Scanning for Vulnerabilities

1. Will disabling some test categories help speed up the scanning phase? (Yea/Nay)



   ><details><summary>Click for answer</summary></details>

2. There should be two high-risk alerts in your scan results. One is Path Traversal. What's the name of the other one?



   ><details><summary>Click for answer</summary></details>

### Authenticated Scans

1. Which type of script was used to record the authentication process to our site in ZAP?



   ><details><summary>Click for answer</summary></details>

2. What additional high-risk vulnerability was found on the site after running the authenticated scan?



   ><details><summary>Click for answer</summary></details>

### Checking APIs with ZAP

1. What high-risk vulnerability was found on the/asciiart/generateendpoint?



   ><details><summary>Click for answer</summary></details>

2. Read the details on the Path Traversal vulnerability detected. Based solely on the information presented by the scanner, would you categorise this finding as a false positive? (yea/nay)



   ><details><summary>Click for answer</summary></details>

### Integrating DAST into the development pipeline

1. Download the ZAP report for thesimple-webapprepository. How many medium-risk vulnerabilities were found?



   ><details><summary>Click for answer</summary></details>

2. Check themainbranch of thesimple-apirepository onJenkins. One of the builds failed during theBuild the Docker imagestep. What is the number of the pre-existing failed build?



   ><details><summary>Click for answer</summary></details>

3. Download the ZAP report for thesimple-apirepository. What high-risk vulnerability was found?



   ><details><summary>Click for answer</summary></details>

