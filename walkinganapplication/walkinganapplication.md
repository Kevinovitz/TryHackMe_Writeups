![Walking An Application Banner](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/walkinganapplication/Walking_Application_Banner.png)

<p align="center">
   <img src="https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/walkinganapplication/Walking_Application_Cover.png" alt="Walking An Application Logo">
</p>

# Walking An Application

This guide contains the answer and steps necessary to get to them for the [Walking An Application](https://tryhackme.com/room/walkinganapplication) room.

## Table of contents

- [Viewing The Page Source](#viewing-the-page-source)
- [Developer Tools - Inspector](#developer-tools---inspector)
- [Developer Tools - Debugger](#developer-tools---debugger)
- [Developer Tools - Network](#developer-tools---network)

### Viewing The Page Source

1.  What is the flag from the HTML comment?

   If we access the page at: https://10.10.196.128.p.thmlabs.com we can view the page source. Here we find a comment that brings us to an unfinished page.
   
   ![Comment](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/walkinganapplication/Walking_Application_Page_Source_Comment.png)
   
   On this page we can find our flag.
   
   ![Comment Flag](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/walkinganapplication/Walking_Application_Page_Source_Comment_Flag.png)
   
   ><details><summary>Click for answer</summary>THM{HTML_COMMENTS_ARE_DANGEROUS}</details>

2. What is the flag from the secret link?

   On the same page source we can see there is a mention of a secret page. If we navigate to it we can find out flag.
   
   ![Secret Page](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/walkinganapplication/Walking_Application_Page_Source_Secret_Page.png)
   
   ><details><summary>Click for answer</summary>THM{NOT_A_SECRET_ANYMORE}</details>
   
3. What is the directory listing flag?

   After opening one of the external files of the website, we can try traversing to the parent folder to see if we can access any files.
   
   ![Directory Flag](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/walkinganapplication/Walking_Application_Page_Source_Directory_Flag.png)
   
   Looks like we can!

   ><details><summary>Click for answer</summary>THM{INVALID_DIRECTORY_PERMISSIONS}</details>

4. What is the framework flag?

   Again on the page source, we see a comment about a framework used on the website.
   
   ![Page Source](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/walkinganapplication/Walking_Application_Page_Source_Page_Source.png)
   
   Navigating to this page we can get more info about this framework. We find an admin panel which we can login to with the default credentials. However, this was not the correct flag. 
   
   ![Framework Login](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/walkinganapplication/Walking_Application_Page_Source_Framework_Login.png)
   
   After looking further, we see there is a file available to download from the changelog.
   
   ![Changelog File](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/walkinganapplication/Walking_Application_Page_Source_Changelog_File.png)
   
   In this zip file, we can find our flag.
   
   ![Zip](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/walkinganapplication/Walking_Application_Page_Source_Zip.png)

   ><details><summary>Click for answer</summary>THM{KEEP_YOUR_SOFTWARE_UPDATED}</details>

### Developer Tools - Inspector

1. What is the flag behind the paywall?

   When looking at the source of the page in Inspector, we can search for the element that is blocking the text.
   
   ![Div](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/walkinganapplication/Walking_Application_Inspector_Div.png)
   
   We could change the value of this element to not block the text. However, in this case, it also works by simply removing the element from the page.
   
   ![Flag](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/walkinganapplication/Walking_Application_Inspector_Flag.png)

   ><details><summary>Click for answer</summary>THM{NOT_SO_HIDDEN}</details>

### Developer Tools - Debugger

1. What is the flag in the red box?

   Looking at the debugger tab, we can see the related javascript file.
   
   ![Java File](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/walkinganapplication/Walking_Application_Debugger_Java_File.png)
   
   Upon further inspection we see which part removes the message.
   
   ![File End](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/walkinganapplication/Walking_Application_Debugger_File_End.png)
   
   Adding a breakpoint here, allows us to see the message before it is removed.
   
   ![Flag](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/walkinganapplication/Walking_Application_Debugger_Flag.png)

   ><details><summary>Click for answer</summary>THM{CATCH_ME_IF_YOU_CAN}</details>

### Developer Tools - Network

1. What is the flag shown on the contact-msg network request?

   On the contact page, we can submit some data this see what is retrieved.
   
   ![Form](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/walkinganapplication/Walking_Application_Network_Form.png)

   Looks like we can find our flag in the response of the request.
   
   ![Flag](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/walkinganapplication/Walking_Application_Network_Flag.png)

   ><details><summary>Click for answer</summary>THM{GOT_AJAX_FLAG}</details>
