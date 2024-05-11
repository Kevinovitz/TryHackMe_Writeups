![DAST Banner](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/dastzap/DAST_Banner.png)

<p align="center">
   <img src="https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/dastzap/Dast_Cover.png" alt="DAST Logo">
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

   ![Spiders Sites](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/dastzap/Dast_Spiders_Sites.png)

   ><details><summary>Click for answer</summary>pass,user</details>

3. What other .php resource, besides nospiders-gallery.php was found by the AJAX spider but not by the regular spider?

   Looking through the results of both scans, we can find another missing url.

   ![Spiders Missing](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/dastzap/Dast_Spiders_Missing.png)

   ><details><summary>Click for answer</summary>/view.php</details>

### Scanning for Vulnerabilities

1. Will disabling some test categories help speed up the scanning phase? (Yea/Nay)

   The answer can be found in the text.

   ><details><summary>Click for answer</summary>Yea</details>

2. There should be two high-risk alerts in your scan results. One is Path Traversal. What's the name of the other one?

   After creating the new scan policiy, we can start the scan. If you can't select the correct starting point, you need to make sure you have done a spider crawl of the site beforehand.

   ![Vulnerabilities Scan](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/dastzap/Dast_Vulnerabilities_Scan.png)

   After the scan has completed we can see two high-severity alerts

   ![Vulnerabilities Results](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/dastzap/Dast_Vulnerabilities_Results.png)

   ><details><summary>Click for answer</summary>Cross Site Scripting Reflected</details>

### Authenticated Scans

1. Which type of script was used to record the authentication process to our site in ZAP?

   The answer can be found in the text.

   ><details><summary>Click for answer</summary>Zest Script</details>

2. What additional high-risk vulnerability was found on the site after running the authenticated scan?

   First we must create a Zest script.

   ![Authentication Script](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/dastzap/Dast_Authentication_Script.png)

   Then we must create a new context.

   ![Authentication Context](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/dastzap/Dast_Authentication_Context.png)

   Then we add the user 'nospiders' in the same window.

   Now we can crawl the site again.

   ![Authentication Crawl](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/dastzap/Dast_Authentication_Crawl.png)

   We should probably exclude the logout page from this context to prevent accidentally loggin out.

   ![Authentication Exclude](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/dastzap/Dast_Authentication_Exclude.png)

   After the crawl we can add the logged in and logged out flags to our context. For the second one it might be necessary to send another request via the built-in browser.

   ![Authentication Requests](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/dastzap/Dast_Authentication_Requests.png)

   ![Authentication Logged In](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/dastzap/Dast_Authentication_Logged_In.png)

   ![Authentication Logged Out](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/dastzap/Dast_Authentication_Logged_Out.png)

   Finally, we add the page 'http://10.10.61.242:8082/aboutme.php' the authenthication verification site.

   Now we can re-run the active scan with our new context and user.

   ![Authentication Scan](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/dastzap/Dast_Authentication_Scan.png)

   Now we can find the added vulnerability.

   ><details><summary>Click for answer</summary></details>

### Checking APIs with ZAP

1. What high-risk vulnerability was found on the/asciiart/generateendpoint?

   After importing the API endpoint, we initiate another active scan. This time on the API site.

   ![Api Results](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/dastzap/Dast_Api_Results.png)

   ><details><summary>Click for answer</summary>Remote OS Command Injection</details>

2. Read the details on the Path Traversal vulnerability detected. Based solely on the information presented by the scanner, would you categorise this finding as a false positive? (yea/nay)

   ><details><summary>Click for answer</summary>Yea</details>

### Integrating DAST into the development pipeline

1. Download the ZAP report for thesimple-webapprepository. How many medium-risk vulnerabilities were found?

   First thing we need to do, is add the ZAP stage to the build process in Jenkings. To do this we must edit the jenkingsfile in Gitea and add (uncomment) this stage.

   ![Integrate Uncomment](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/dastzap/Dast_Integrate_Uncomment.png)

   Unfortunately, I had some issues commiting the change through my kali machine. So I fired up the Tryhackme Attackbox and try again from there. This did work.

   ![Integrate Build](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/dastzap/Dast_Integrate_Build.png)

   Now we can download the report. Here we can see how many vulnerabilities were found.

   ![Integrate Results](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/dastzap/Dast_Integrate_Results.png)

   ><details><summary>Click for answer</summary>3</details>

2. Check the main branch of the simple-api repository on Jenkins. One of the builds failed during theBuild the Docker imagestep. What is the number of the pre-existing failed build?

   Lets first add the ZAP stage to the simple-api, because the scan takes some time. We do this by repeating the steps we did for the simple-webapp.

   In the repo uncomment the third stage and commit.

   In the Jenkings job view for the simple-api, we can see which build previously failed.

   ![Integrate Error](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/dastzap/Dast_Integrate_Error.png)

   ><details><summary>Click for answer</summary>4</details>

3. Download the ZAP report for the simple-apirepository. What high-risk vulnerability was found?

   After the ZAP scan has completed (and failed the build), we can donwload the report and find how many vulnerabilities were found.

   ![Integrate Results 2](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/dastzap/Dast_Integrate_Results_2.png)

   ><details><summary>Click for answer</summary>Remote OS COmmand Injection</details>