![Passwords - A Cracking Christmas Banner](https://tryhackme-images.s3.eu-west-1.amazonaws.com/room-icons/5fc2847e1bbebc03aa89fbf2-1763007372515)

<p align="center">
   <img src="https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/attacks-on-ecrypted-files-aoc2025-asdfghj123/Passwords_-_A_Cracking_Christmas_Cover.png" alt="Passwords - A Cracking Christmas Logo">
</p>

# <img src="https://tryhackme-images.s3.amazonaws.com/room-icons/5fc2847e1bbebc03aa89fbf2-1763007383191" alt="image" style="vertical-align: middle;height: 50px;" /> Passwords - A Cracking Christmas | Advent of Cyber 2025 - Day 9

This guide contains the answer and steps necessary to get to them for the [Passwords - A Cracking Christmas](https://tryhackme.com/room/attacks-on-ecrypted-files-aoc2025-asdfghj123) room.

## Table of contents

- [Attacks Against Encrypted Files](#attacks-against-encrypted-files)

### Attacks Against Encrypted Files

1.  What is the flag inside the encrypted PDF?

    We can try obtaining the password for the PDF using `pdfcrack`.

    ```cmd
    pdfcrack -f flag.pdf -w /usr/share/wordlists/rockyou.txt
    ```

    ![Pdfcrack](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/attacks-on-ecrypted-files-aoc2025-asdfghj123/Passwords_-_A_Cracking_Christmas_Pdfcrack.png)

    We can see that `pdfcrack` managed to get a password. Now we can get our flag by unlocking the pdf file with this key.

    ![Pdf Flag](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/attacks-on-ecrypted-files-aoc2025-asdfghj123/Passwords_-_A_Cracking_Christmas_Pdf_Flag.png)

    ><details><summary>Click for answer</summary>THM{Cr4ck1ng_PDFs_1s_34$y}</details>

2.  What is the flag inside the encrypted zip file?

    Since `fcrackzip` is not installed on our machine, we will use `john`.

    ```cmd
    zip2john flag.zip > ziphash.txt
    john --wordlist=/usr/share/wordlists/rockyou.txt ziphash.txt
    ```

    ![Zipcrack](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/attacks-on-ecrypted-files-aoc2025-asdfghj123/Passwords_-_A_Cracking_Christmas_Zipcrack.png)

    We can see it managed to obtain the used password. Now we can extract the file using this password and get our second flag.

    ![Zip Flag](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/attacks-on-ecrypted-files-aoc2025-asdfghj123/Passwords_-_A_Cracking_Christmas_Zip_Flag.png)

    ><details><summary>Click for answer</summary>THM{Cr4ck1n6_z1p$_1s_34$yyyy}</details>

3.  For those who want another challenge, have a look around the VM to get access to the key for Side Quest 2! Accessible through our [Side Quest Hub](https://tryhackme.com/adventofcyber25/sidequest)!



    ><details><summary>Click for answer</summary></details>

4.  If you enjoyed this task, feel free to check out the [Password Attacks](https://tryhackme.com/room/passwordattacks) room.
