![Mother's Secret Banner](https://assets.tryhackme.com/room-banners/pipelines.png)

<p align="center">
   <img src="https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/codeanalysis/Mother's_Secret_Cover.png" alt="Mother's Secret Logo">
</p>

# Mother's Secret

This guide contains the answer and steps necessary to get to them for the [Mother's Secret](https://tryhackme.com/r/room/codeanalysis) room.

## Table of contents

- [Mother's Secrets!](#mother's-secrets!)

### Mother's Secrets!

1. What is the number of the emergency command override?

   The answer to this question can be found in the text.

   ><details><summary>Click for answer</summary>100375</details>

2. What is the special order number?

   In the api routes file we downloaded, we can find two endpoints. Yaml and Nostromo. Visiting either one gives us a message telling us we are hitting the wrong route.

   ![Wrong Route](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/codeanalysis/Mothers_Secret_Wrong_Route.png)

   I looked through the routes using semgrep for static analysis and ZAP spiders and scans for Dynamic analysis. Both without any results.

   Looking closer at the routes we can see that the Yaml endpoint has declared a variable 'file_path' which is related to a Yaml file the system can read. This might be something we can use.

   Since hitting the endpoint doesn't seem to do anything, we can capture the api request in Burpsuite and modify it to contain the 'file_path' variable. We can either modify it and forward the request or send it to repeater. The latter would be better as it would enable us to test various payloads.

   ![To Repeater](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/codeanalysis/Mothers_Secret_To_Repeater.png)

   We must change it to a POST request and add two lines. Our payload should contain the variable name and its value. If this value is not a yaml file, we get an error back.

   If it is a yaml file extension, we get a message telling us the system is unable to read the file. This means we are on the right track.

   ![Yaml Endpoint File](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/codeanalysis/Mothers_Secret_Yaml_Endpoint_File.png)

   We just need to create the right payload/filename. It might be the code for the 'alian loaders' we got in the beginning (100375). The webpage on ALien Loader mentions a 'YAML' loaders that parses and loads YAML data. This is exactly what the yaml endpoint does judging from the api routes file.

   ![Yaml Order Number](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/codeanalysis/Mothers_Secret_Yaml_Order_Number.png)

   Looks like this was correct. The message gives us the order number!

   ><details><summary>Click for answer</summary>937</details>

3. What is the hidden flag in the Nostromo route?

   Our next step would be to follow the Nostromo endpoint as suggested in the message. We capture it again in Burpsuite to modify the request in Repeater.

   ![Nostromo Endpoint](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/codeanalysis/Mothers_Secret_Nostromo_Endpoint.png)

   Again we change the request to a POST request and add our payload in the form of the order number filename.

   ![Nostromo Message](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/codeanalysis/Mothers_Secret_Nostromo_Message.png)

   Here we find our first hidden flag.

   ><details><summary>Click for answer</summary>Flag{X3n0M0Rph}</details>

4. What is the name of the Science Officer with permissions?

   If we had used a different filename, we would have gotten an error message that we are not the Science Officer. This is also apparent from the route file.

   ![Nostromo Permission](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/codeanalysis/Mothers_Secret_Nostromo_Permission.png)

   So apparently we have now been identified as a Science Officer. If we look at the web application and navigate to role, we can see the name of this Science Officer.

   ![Name](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/codeanalysis/Mothers_Secret_Name.png)

   ><details><summary>Click for answer</summary>ash</details>

5. What are the contents of the classified "Flag" box?

   This can be found in the same webpage under Flag.

   ><details><summary>Click for answer</summary>THM_FLAG{0RD3R_937}</details>

6. Where is Mother's secret?

   So we should now be identified as a Science Officer. Now we should be able to use the last endpoint. nostromo/mother.

   In the text we are give a clue for a file located at this endpoint, 'secret.txt'. Lets try it and use it as the filename in our api request.

   ![Secret](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/codeanalysis/Mothers_Secret_Secret.png)

   ><details><summary>Click for answer</summary>/opt/m0th3r</details>

7. What is Mother's secret?

   Now that we know the secrets location, we must read it. From the Pathways message we learn we should utilized path traversal. From the api routes file, we can see this would indeed be possible as the filname value is added to the filepath without sanitation.

   Since we need to go all the way back to /opt/, we should add a few extra folder up commands just to be sure we hit the root folder.

   ```console
   ../../../../../../opt/m0th3r
   ```

   Success! If we try with fewer folder up movements, we can see that it won't work.

   ![Secret Message](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/codeanalysis/Mothers_Secret_Secret_Message.png)

   ><details><summary>Click for answer</summary>Flag{Ensure_return_of_organism_meow_meow!}</details>