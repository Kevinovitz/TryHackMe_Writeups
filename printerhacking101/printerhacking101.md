![Printer Hacking 101 Banner](https://assets.tryhackme.com/room-banners/printerhacking101.png)

<p align="center">
   <img src="https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/printerhacking101/printerhacking101_Cover.png" alt="Printer Hacking 101">
</p>

# [Printer Hacking 101](https://github.com/Kevinovitz/TryHackMe_Writeups/tree/main/printerhacking101)

In this challenge we will be looking at some basic printer vulnerabilities using [PRET](https://github.com/RUB-NDS/PRET) and getting access to unsecured printers. The room can be found [here](https://tryhackme.com/room/printerhacking101). A cheat sheet for use with PRET can be found [here](http://hacking-printers.net/wiki/index.php/Printer_Security_Testing_Cheat_Sheet).

A video walkthrough of this room can be found [here](https://www.youtube.com/watch?v=7kcLbblwU9Y).

## Table of Contents

- [Unit 2: IPP Port](#unit-2-ipp-port)
- [Unit 3: Targeting & Exploitation](#unit-3-targeting-exploitation)

## Unit 2: IPP Port

1. What port does IPP run on?

   This answer can be found with a quick Google search.

   ><details><summary>Click for answer</summary>631</details>

## Unit 3: Targeting & Exploitation


1. How would a simple printer TCP DoS attack look as a one-line command?

   For this question we can look at the cheat sheet [provided](http://hacking-printers.net/wiki/index.php/Printer_Security_Testing_Cheat_Sheet). Here we look for any commands related to TCP.

   ><details><summary>Click for answer</summary>while true; do nc printer 9100; done</details>

2. Review the cheat sheet provided in the task reading above. What attack are printers often vulnerable to which involves sending more and more information until a pre-allocated buffer size is surpassed?

   This answer can also be found in the attached cheat sheet whilst looking for anything related to `buffer`.

   ><details><summary>Click for answer</summary>Buffer Overflow</details>

3. Connect to the printer per the instructions above. Where's the Fox_Printer located?

   Lets navigate to the appropriate page `10.10.7.6:631`. Here we get a home page for the CUPS server. Navigating to the printers tab, we get a list of available printers.
   
   ![Website Printers](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/printerhacking101/Website_Printers.png)

   ><details><summary>Click for answer</summary>Skidy's basement</details>

4. What is the size of a test sheet?

   For this we can click on the printer in question and under the `maintenance` dropdown select `print test page`.
   
   ![Website Printer](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/printerhacking101/Website_Printer.png)
   
   ![Test Page](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/printerhacking101/Website_Test_Page.png)
   
   Now we can find more information for this job on the jobs page.
   
   ![Test Job](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/printerhacking101/Website_Test_Job.png)

   ><details><summary>Click for answer</summary>1k</details>

**Extra** I tried logging into the printer by brute-forcing the password. Unfortunately, Hydra kept crashing (the try rate was very slow). 

![Hydra Attempt](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/printerhacking101/Printer_Hydra.png)

So I was unable to get the password. But several other walkthroughs listed the password with which I could log in. Have yet to try out things to do after that.

><details><summary>Click for answer</summary>password123</details>
