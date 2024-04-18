![Upload Vulnerabilities Banner](https://i.imgur.com/wVEQ3Fe.png)

<p align="center">
   <img src="https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/uploadvulns/Upload_Vulnerabilities_Cover.png" alt="Upload Vulnerabilities Logo">
</p>

# Upload Vulnerabilities

This guide contains the answer and steps necessary to get to them for the [Upload Vulnerabilities](https://tryhackme.com/room/uploadvulns) room.

## Table of contents

- [Overwriting Existing Files](#overwriting-existing-files)
- [Remote Code Execution](#remote-code-execution)
- [Filtering](#filtering)
- [Bypassing Client-Side Filtering](#bypassing-client-side-filtering)
- [Bypassing Server-Side Filtering: File Extensions](#bypassing-server-side-filtering-file-extensions)
- [Bypassing Server-Side Filtering: Magic Numbers](#bypassing-server-side-filtering-magic-numbers)
- [Challenge ](#challenge)

### Overwriting Existing Files

1. What is the name of the image file which can be overwritten?

   When looking at the source code of the website, we can see which file is used as background.

   ![Overwriting Background](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/uploadvulns/Upload_Vulnerabilities_Overwriting_Background.png)

   ><details><summary>Click for answer</summary>mountains.jpg</details>

2. Overwrite the image. What is the flag you receive?

   I first rename a image I have on my PC to `mountains.jpg`. I then upload it through the form on the webpage.

   ![Overwriting New](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/uploadvulns/Upload_Vulnerabilities_Overwriting_New.png)

   After refreshing, we see that the background has changed and we get our flag.

   ![Overwriting Flag](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/uploadvulns/Upload_Vulnerabilities_Overwriting_Flag.png)

   ><details><summary>Click for answer</summary>THM{OTBiODQ3YmNjYWZhM2UyMmYzZDNiZjI5}</details>

### Remote Code Execution

1. Run a Gobuster scan on the website using the syntax from the screenshot above. What directory looks like it might be used for uploads?

   ```cmd
   gobuster dir -u shell.uploadvulns.thm -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt 
   ```

   After running Gobuster, we see two directories. One of which is probably used for file upload.

   ![RCE Directories](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/uploadvulns/Upload_Vulnerabilities_RCE_Directories.png)

   ><details><summary>Click for answer</summary>/resources</details>

2. Get either a web shell or a reverse shell on the machine.
   What's the flag in the /var/www/ directory of the server?

   First thing I did, was edit the reverse php shell script to include my IP and port. I then upload it through the webpage.

   ![RCE Upload](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/uploadvulns/Upload_Vulnerabilities_RCE_Upload.png)

   Now I must set up a listener with netcat, navigate to the file upload directory and execute the script.

   ```cmd
   nc -nlvp 1337
   ```

   ![RCE Execute](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/uploadvulns/Upload_Vulnerabilities_RCE_Execute.png)

   ![RCE Connection](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/uploadvulns/Upload_Vulnerabilities_RCE_Connection.png)

   We managed to get a connection. All we need to do now is look for the flag.

   ![RCE Flag](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/uploadvulns/Upload_Vulnerabilities_RCE_Flag.png)

   ><details><summary>Click for answer</summary>THM{YWFhY2U3ZGI4N2QxNmQzZjk0YjgzZDZk}</details>

### Filtering

1. What is the traditionally predominant server-side scripting language?

   The answer can be found in the text.

   ><details><summary>Click for answer</summary>PHP</details>

2. When validating by file extension, what would you call a list of accepted extensions (whereby the server rejects any extension not in the list)?

   The answer can be found in the text.

   ><details><summary>Click for answer</summary>Whitelist</details>

3. [Research] What MIME type would you expect to see when uploading a CSV file?

   Performing a search for: 'MIME csv header', give us the answer we are after.

   ><details><summary>Click for answer</summary>text/csv</details>

### Bypassing Client-Side Filtering

1. What is the flag in /var/www/?

   First we edit our reverse shell. We can indeed see that we cannot upload this script.

   ![Client Filtering Script](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/uploadvulns/Upload_Vulnerabilities_Client_Filtering_Script.png)

   ![Client Filtering Failed](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/uploadvulns/Upload_Vulnerabilities_Client_Filtering_Failed.png)

   Lets use Gobuster to find the upload directory of the file.

   ```cmd
   gobuster dir -u http://java.uploadvulns.thm -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
   ```

   ![Client Filtering Directory](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/uploadvulns/Upload_Vulnerabilities_Client_Filtering_Directory.png)

   In Burpsuite we capture the page request and make sure to capture the response as well.

   ![Client Filtering Capture](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/uploadvulns/Upload_Vulnerabilities_Client_Filtering_Capture.png)

   Now we can simply remove the script from the response.

   ![Client Filtering Remove](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/uploadvulns/Upload_Vulnerabilities_Client_Filtering_Remove.png)

   We then setup a listener with `nc -nlvp 1337`. Navigate to URL/images and execute the script.

   ![Client Filtering Connection](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/uploadvulns/Upload_Vulnerabilities_Client_Filtering_Connection.png)

   Now we can look for the flag on the machine.

   ![Client Filtering Flag](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/uploadvulns/Upload_Vulnerabilities_Client_Filtering_Flag.png)

   The second method also works. We rename the file and upload in through the un-modified page. We then capture the upload request and modify the filetype and name.

   ![Client Filtering Change](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/uploadvulns/Upload_Vulnerabilities_Client_Filtering_Change.png)

   We should then receive another connection.

   ![Client Filtering Connection2](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/uploadvulns/Upload_Vulnerabilities_Client_Filtering_Connection2.png)

   ><details><summary>Click for answer</summary>THM{NDllZDQxNjJjOTE0YWNhZGY3YjljNmE2}</details>

### Bypassing Server-Side Filtering: File Extensions

1. What is the flag in /var/www/?

   First, we look for the upload directory using Gobuster.

   ```cmd
   gobuster dir -u http://annex.uploadvulns.thm -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
   ```
   
   ![Server Filtering Extension Directory](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/uploadvulns/Upload_Vulnerabilities_Server_Filtering_Extension_Directory.png)

   I tried several extensions which can be used for a `php` file. It appears `php5` isn't blocked.

   ![Server Filtering Extension Correct](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/uploadvulns/Upload_Vulnerabilities_Server_Filtering_Extension_Correct.png)

   Now that we know this, we can upload our shell to the server with `.php5` extension. And it should work when executed.

   ![Server Filtering Extension Connection](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/uploadvulns/Upload_Vulnerabilities_Server_Filtering_Extension_Connection.png)

   Looking through the directory gives us the flag.

   ![Server Filtering Extension Flag](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/uploadvulns/Upload_Vulnerabilities_Server_Filtering_Extension_Flag.png)

   ><details><summary>Click for answer</summary>THM{MGEyYzJiYmI3ODIyM2FlNTNkNjZjYjFl}</details>

### Bypassing Server-Side Filtering: Magic Numbers

1. Grab the flag from /var/www/

   First, we look for the upload directory using Gobuster.

   ```cmd
   gobuster dir -u http://magic.uploadvulns.thm -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
   ```

   ![Server Filtering Magic Directory](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/uploadvulns/Upload_Vulnerabilities_Server_Filtering_Magic_Directory.png)

   After uploading a `jpg` file, we can an error. It appears it will only accept `gif` files.

   ![Server Filtering Magic Error](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/uploadvulns/Upload_Vulnerabilities_Server_Filtering_Magic_Error.png)

   Using the provided link, we can look for the magic number related to gifs. We must then prepend the same number of characters to the script.

   ![Server Filtering Magic Script](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/uploadvulns/Upload_Vulnerabilities_Server_Filtering_Magic_Script.png)

   Now we can open the file with `hexeditor` and change the characters to the corrects ones.

   ![Server Filtering Magic Hex](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/uploadvulns/Upload_Vulnerabilities_Server_Filtering_Magic_Hex.png)

   Checking the file type of the file, indeed gives us `gif`.

   ![Server Filtering Magic Type](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/uploadvulns/Upload_Vulnerabilities_Server_Filtering_Magic_Type.png)

   Since we cannot access the upload page (graphics), we can simply call the url of the file firectly (i.e., http://magic.uploadvulns.thm/graphics/shell.php).

   ![Server Filtering Magic Connection](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/uploadvulns/Upload_Vulnerabilities_Server_Filtering_Magic_Connection.png)

   Now we can locate and read the flag.

   ![Server Filtering Magic Flag](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/uploadvulns/Upload_Vulnerabilities_Server_Filtering_Magic_Flag.png)

   ><details><summary>Click for answer</summary>THM{MWY5ZGU4NzE0ZDlhNjE1NGM4ZThjZDJh}</details>
   
### Challenge

1. Hack the machine and grab the flag from /var/www/

   When looking at the source code of the page (either in the browser or through BurpSuite), we can see there is a script called `upload.js` which is probably doing the client-side filtering. Upon further investigation we can see it filters based on size, and file type. I couldn't simply remove the script as that would break the upload functionality. We can also see that the framework used here is node.js.

   ![Challenge Response](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/uploadvulns/Upload_Vulnerabilities_Challenge_Response.png)

   So I had to remove the filter lines from the script by intercepting the response with BurpSuite.

   ![Challenge Java](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/uploadvulns/Upload_Vulnerabilities_Challenge_Java.png)

   After trying to upload a normal jpg file, I looked for various directories on the server. One of these could be the correct one.

   ![Challenge Directory](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/uploadvulns/Upload_Vulnerabilities_Challenge_Directory.png)

   After further inspection of the website, we see that background images are stored in the `contents` folder. Perhaps the uploaded images will as well.

   ![Challenge Backgrounds](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/uploadvulns/Upload_Vulnerabilities_Challenge_Backgrounds.png)

   First, we must setup our reverse shell. Since the server uses Node.js instead of PHP we must use a different shell from [here](https://github.com/swisskyrepo/PayloadsAllTheThings/raw/master/Methodology%20and%20Resources/Reverse%20Shell%20Cheatsheet.md#nodejs).

   We then supply it with our IP and chosen port.

   ![Challenge Shell](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/uploadvulns/Upload_Vulnerabilities_Challenge_Shell.png)

   The things I tried to upload the file, was to change the MIME header, but this didn't seem to work. Also adding magic numbers to the beginning of the file didn't seem to work.

   In the end I had to simply rename the file to `.jpg` and this would in fact work. Since Node.js doesn't care what extension the file has.

   ![Challenge MIME](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/uploadvulns/Upload_Vulnerabilities_Challenge_MIME.png)

   However, it also doesn't allow direct execution of the file. For this we can use the admin panel we found earlier.

   But first, we must find the correct URL of our shell. We can do that with Gobuster again and the provided wordlist. This time we search in the contents folder.

   ```cmd
   gobuster dir -u http://jewel.uploadvulns.thm/content -w ~/Downloads/UploadVulnsWordlist.txt -x jpg
   ```

   I had tried several times before to get the shell to work without success. Therefore, there are more files present in this folder. I took several snapshots of this folder before and I knew it would be a smaller file (smaller than the php shell). So our shell would be `TLZ.jpg`.

   ![Challenge Images](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/uploadvulns/Upload_Vulnerabilities_Challenge_Images.png)

   Now we can head over to the admin panel and try to execute the file. Since both the `modules` folder and `contents` folder are root folder on the server, we can access it using a path traversal vulnerability if present using `../`.

   ```cmd
   ../contents/TLZ.jpg
   ```

   After setting up our listener with `nc -nlvp 1337` we can execute the file to receive a connection.

   ![Challenge Connection](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/uploadvulns/Upload_Vulnerabilities_Challenge_Connection.png)

   Now, all we have to do is navigate to our flag on the machine.

   ![Challenge Flag](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/uploadvulns/Upload_Vulnerabilities_Challenge_Flag.png)
   
   ><details><summary>Click for answer</summary>THM{NzRlYTUwNTIzODMwMWZhMzBiY2JlZWU2}</details>
