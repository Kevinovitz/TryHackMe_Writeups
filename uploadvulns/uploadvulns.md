![Upload Vulnerabilities Banner](https://i.imgur.com/wVEQ3Fe.png)

<p align="center">
   <img src="https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/uploadvulns/Upload_Vulnerabilities_Cover.png" alt="Upload Vulnerabilities Logo">
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
- [Example Methodology](#example-methodology)
- [Challenge ](#challenge)

### Overwriting Existing Files

1. What is the name of the image file which can be overwritten?

   When looking at the source code of the website, we can see which file is used as background.

   OVERWRITE BACKGROUND

   ><details><summary>Click for answer</summary>mountains.jpg</details>

2. Overwrite the image. What is the flag you receive?

   I first rename a image I have on my PC to `mountains.jpg`. I then upload it through the form on the webpage.

   OVERWRITE NEW

   After refreshing, we see that the background has changed and we get our flag.

   OVERWRITE FLAG

   ><details><summary>Click for answer</summary>THM{OTBiODQ3YmNjYWZhM2UyMmYzZDNiZjI5}</details>

### Remote Code Execution

1. Run a Gobuster scan on the website using the syntax from the screenshot above. What directory looks like it might be used for uploads?

   ```cmd
   gobuster dir -u shell.uploadvulns.thm -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt 
   ```

   After running Gobuster, we see two directories. One of which is probably used for file upload.

   RCE DIRECTORIES

   ><details><summary>Click for answer</summary>/resources</details>

2. Get either a web shell or a reverse shell on the machine.
   What's the flag in the /var/www/ directory of the server?

   First thing I did, was edit the reverse php shell script to include my IP and port. I then upload it through the webpage.

   RCE UPLOAD

   Now I must set up a listener with netcat, navigate to the file upload directory and execute the script.

   ```cmd
   nc -nlvp 1337
   ```

   RCE EXECUTE

   RCE CONNECTION

   We managed to get a connection. All we need to do now is look for the flag.

   RCE FLAG

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




### Bypassing Server-Side Filtering: File Extensions




### Bypassing Server-Side Filtering: Magic Numbers




### Example Methodology




### Challenge



1. 

   

   ><details><summary>Click for answer</summary></details>
