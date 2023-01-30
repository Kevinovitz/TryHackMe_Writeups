<p align="center">
   <img src="https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/printerhacking101/printerhacking101_Cover.png" alt="Printer Hacking 101">
</p>

# [Printer Hacking 101](https://github.com/Kevinovitz/TryHackMe_Writeups/tree/main/printerhacking101)

In this challenge we will be looking at some basic printer vulnerabilities using [PRET](https://github.com/RUB-NDS/PRET) and getting access to unsecured printers. The room can be found [here](https://tryhackme.com/room/printerhacking101). A cheat sheet for use with PRET can be found [here](http://hacking-printers.net/wiki/index.php/Printer_Security_Testing_Cheat_Sheet).

A video walkthrough of this room can be found [here](https://www.youtube.com/watch?v=7kcLbblwU9Y).

## Table of Contents
=
- [Unit 2: IPP Port](#unit-2-ipp-port)
- [Unit 3: Targeting & Exploitation](#unit-3-targeting-exploitation)

## Unit 2: IPP Port

1. What port does IPP run on?

   

   ><details><summary>Click for answer</summary>631</details>

## Unit 3: Targeting & Exploitation


1. How would a simple printer TCP DoS attack look as a one-line command?



   ><details><summary>Click for answer</summary>while true; do nc printer 9100; done</details>

2. Review the cheat sheet provided in the task reading above. What attack are printers often vulnerable to which involves sending more and more information until a pre-allocated buffer size is surpassed?



   ><details><summary>Click for answer</summary>Buffer Overflow</details>

3. Connect to the printer per the instructions above. Where's the Fox_Printer located?



   ><details><summary>Click for answer</summary>Skidy's basement</details>

4. What is the size of a test sheet?



   ><details><summary>Click for answer</summary>1k</details>
