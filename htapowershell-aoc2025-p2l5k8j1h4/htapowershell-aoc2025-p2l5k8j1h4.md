![Malware Analysis - Malhare.exe Banner](https://tryhackme-images.s3.eu-west-1.amazonaws.com/room-icons/66c44fd9733427ea1181ad58-1762448313373)

<p align="center">
   <img src="https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/htapowershell-aoc2025-p2l5k8j1h4/Malware_Analysis_-_Malhare.exe_Cover.png" alt="Malware Analysis - Malhare.exe Logo">
</p>

# <img src="https://tryhackme-images.s3.amazonaws.com/room-icons/6093e17fa004d20049b6933e-1763893187327" alt="image" style="vertical-align: middle;height: 50px;" /> Malware Analysis - Malhare.exe | Advent of Cyber 2025 - Day 21

This guide contains the answer and steps necessary to get to them for the [Malware Analysis - Malhare.exe](https://tryhackme.com/room/htapowershell-aoc2025-p2l5k8j1h4) room.

## Table of contents

- [Malware Analysis](#malware-analysis)

### Malware Analysis

1.  What is the title of the HTA application?

    After starting the attackbox, open the `hta` file at `/root/Rooms/AoC2025/Day21/survey.hta`

    ![Title](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/htapowershell-aoc2025-p2l5k8j1h4/Malware_Analysis_-_Malhare.exe_Title.png)

    ><details><summary>Click for answer</summary>Best Festival Company Developer Survey</details>

2.  What VBScript function is acting as if it is downloading the survey questions?

    Scrolling down a little, we can see a VBScript that is being called to get the questions.

    ![Questions](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/htapowershell-aoc2025-p2l5k8j1h4/Malware_Analysis_-_Malhare.exe_Questions.png)

    ><details><summary>Click for answer</summary>getQuestions</details>

3.  What URL domain (including sub-domain) is the "questions" being downloaded from?

    Looking at this function definition, we can see where it download the questions from.

    ![Url](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/htapowershell-aoc2025-p2l5k8j1h4/Malware_Analysis_-_Malhare.exe_Url.png)

    ><details><summary>Click for answer</summary>survey.bestfestiivalcompany.com</details>

4.  Malhare seems to be using typosquatting, domains that look the same as the real one, in an attempt to hide the fact that the domain is not the inteded one, what character in the domain gives this away?

    If we look closely, we can see it actually isn't the 'bestfestivalcompany' domain. They added an extra letter.

    ><details><summary>Click for answer</summary>i</details>

5.  Malicious HTAs often include real-looking data, like survey questions, to make the file seem authentic. How many questions does the survey have?

    Scrolling down to the 'survey content' section, we can see the questions of this survey.

    ![Survey](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/htapowershell-aoc2025-p2l5k8j1h4/Malware_Analysis_-_Malhare.exe_Survey.png)

    ><details><summary>Click for answer</summary>4</details>

6.  Notice how even in code, social engineering persists, fake incentives like contests or trips hide in plain sight to build trust. The survey entices participation by promising a chance to win a trip to where?

    Beneath the questions, is a sentence describing what can be won.

    ![Prize](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/htapowershell-aoc2025-p2l5k8j1h4/Malware_Analysis_-_Malhare.exe_Prize.png)

    ><details><summary>Click for answer</summary>South Pole</details>

7.  The HTA is enumerating information from the local host executing the application. What two pieces of information about the computer it is running on are being exfiltrated? You should provide the two object names separated by commas.

    At the top of the script, in one of the functions, we can see two pieces of information that are being exfiltrated.

    ![Enumeration](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/htapowershell-aoc2025-p2l5k8j1h4/Malware_Analysis_-_Malhare.exe_Enumeration.png)

    ><details><summary>Click for answer</summary>ComputerName,UserName</details>

8.  What endpoint is the enumerated data being exfiltrated to?

    In the previous image, we can also see to which endpoint this data is sent.

    ><details><summary>Click for answer</summary>/details</details>

9.  What HTTP method is being used to exfiltrate the data?

    Since the data is added in the URL of the request, we are dealing with a 'GET' request.

    ><details><summary>Click for answer</summary>GET</details>

10. After reviewing the function intended to get the survey questions, it seems that the data from the download of the questions is actually being executed. What is the line of code that executes the contents of the download?

    Below the exfiltration function, we can see the line of code responsible to execute the contents of the download using powershell.

    ![Command](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/htapowershell-aoc2025-p2l5k8j1h4/Malware_Analysis_-_Malhare.exe_Command.png)

    ><details><summary>Click for answer</summary>runObject.Run "powershell.exe -nop -w hidden -c " & feedbackString, 0, False</details>

11. It seems as if the malware site has been taken down, so we cannot download the contents that the malware was executing. Fortunately, one of the elves created a copy when the site was still active. Download the contents from [here](https://assets.tryhackme.com/additional/aoc2025/files/blob.txt). What popular encoding scheme was used in an attempt to obfuscate the download?

    After downloading and opening the asset, we can see there is some encoding used. Find out which one it is using the magic recipe in CyberChef for example.

    ![Content](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/htapowershell-aoc2025-p2l5k8j1h4/Malware_Analysis_-_Malhare.exe_Content.png)

    ><details><summary>Click for answer</summary>Base64</details>

12. Decode the payload. It seems as if additional steps where taken to hide the malware! What common encryption scheme was used in the script?

    If we look at the decoded script, we can see an encrpyted flag. The function show us how it is encrypted. It look to be substituting each character with another. This could indicate a ROT cipher. As for the amount of steps, this can be derived from the amount added to each character.

    ![Script](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/htapowershell-aoc2025-p2l5k8j1h4/Malware_Analysis_-_Malhare.exe_Script.png) 

    ><details><summary>Click for answer</summary>ROT13</details>

13. Either run the script or decrypt the flag value using online tools such as CyberChef. What is the flag value?

    We can get our flag by either decrypting it using CyberChef and the 'ROT13' recipe. Or we can execute the code with Powershell.

    ![Flag](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/htapowershell-aoc2025-p2l5k8j1h4/Malware_Analysis_-_Malhare.exe_Flag.png)

    ><details><summary>Click for answer</summary>THM{Malware.Analysed}</details>

14. For those who want another challenge, download the HTA file from [here](https://assets.tryhackme.com/additional/aoc2025/SQ4/NorthPole.zip) to get the key for Side Quest 4, accessible through our [Side Quest Hub](https://tryhackme.com/adventofcyber25/sidequest). The password for the file is CanYouREM3?.

    In this file there is a base64 encoded string. Used `sed -n 's/.*"\([^"]*\)".*/\1/p' input.txt | tr -d '\n' > output.txt` to extract the string. Decoding this gives us a script with another base64 encoded string. This then needs to be decoded using a XOR recipe with decimal key 23 (or hex 17).

    This now seems to be a PNG file, but the file is not fully correct yet.

    ><details><summary>Click for answer</summary></details>

15. If you enjoyed today's room, you may also like the [MalDoc: Static Analysis](https://tryhackme.com/room/maldoc) room.
