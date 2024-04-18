![OhSint Banner](https://i.imgur.com/P1nJjnp.png)

<p align="center">
   <img src="https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/ohsint/OhSINT_Cover.png" alt="OhSINT Logo">
</p>

# OhSINT

This guide contains the answer and steps necessary to get to them for the [OhSINT](https://tryhackme.com/room/ohsint) room.

### OhSINT

Lets examine the image we downloaded with Exiftools to see if there is anything interesting embedded in the file.

```cmd
exiftool WindowsXP.jpg
```

![Exiftool](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/ohsint/Exiftool_Results.png)

We find a name here, which we can lookup on Google. Here we find a hit for someones Twitter, Blog site, and Github page.

There are also other tools we can use. Such as reverse image search. But since this is a classic windows background, there will probably be a lot of noise. Also `steghide` could be interesting.

1. What is this users avatar of?

   Looking at his Twitter page, we can find his avatar.
   
   ![Twitter Picture](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/ohsint/Twitter_Page.png)

   ><details><summary>Click for answer</summary>cat</details>

2. What city is this person in?

   This can be found on his Github page or trough Wigle by finding the 'free' network at his house.
   
   ![Github](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/ohsint/Github_Rep.png)

   ><details><summary>Click for answer</summary>London</details>

3. Whats the SSID of the WAP he connected to?

   To find out his SSID, we can use the BSSID we found on his Twitter page. Using https://wigle.net we can lookup where this network is located and get an SSID from there.
   
   ![Wigle Search](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/ohsint/Wiggle_Search_BSSID.png)
   
   This also confirms that he lives in London.

   ><details><summary>Click for answer</summary>UnileverWiFi</details>

4. What is his personal email address?

   This is also present on his Github page.

   ><details><summary>Click for answer</summary>OWoodflint@gmail.com</details>

5. What site did you find his email address on?

   We found it on his Github page.

   ><details><summary>Click for answer</summary>Github</details>

6. Where has he gone on holiday?

   Looking at his blog page, it looks like he was indeed on a trip.
   
   ![Blog Page](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/ohsint/Blog_Web_Page.png)

   ><details><summary>Click for answer</summary>New York</details>

7. What is this persons password?

   This one took me a little longer to figure out (but in hindsight it was dead simple). I looked around on his webpage and Github page for any comments or changes he made to his repository that could contain a password. Also looking for hidden directories yielded nothing directly (more on that later).
   
   Then I also looked at the source code of the web page and found something that looked like a password. Seems like it was hidden in plain site. As mentioned before, the `atom` folder found by Dirbuster contained a file which also had the password in it.
   
   ![Blog Source](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/ohsint/Blog_Source.png)
   
   ![Blog Password](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/ohsint/Blog_Password.png)

   ><details><summary>Click for answer</summary>pennYDr0pper.!</details>
