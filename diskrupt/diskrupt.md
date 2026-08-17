![Diskrupt Banner](https://cdn-images.tryhackme.com/user-uploads/5e8dd9a4a45e18443162feab/room-content/5e8dd9a4a45e18443162feab-1741040888908.png)

<p align="center">
   <img src="https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/diskrupt/Diskrupt_Cover.png" alt="Diskrupt Logo">
</p>

# <img src="https://cdn-images.tryhackme.com/room-icons/5e8dd9a4a45e18443162feab-1743007209488" alt="image" style="vertical-align: middle;height: 50px;" /> Diskrupt

This guide contains the answer and steps necessary to get to them for the [Diskrupt](https://tryhackme.com/room/diskrupt) room.

## Table of contents

- [Table of contents](#table-of-contents)
  - [Task 1 - Challenge Scenario](#task-1---challenge-scenario)

### Task 1 - Challenge Scenario

1.  What are the corrupted bytes in the boot sector that caused the disk to be damaged?

    We can see the image can indeed not be loaded using Autpsy.

    ![MDR Issue](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/diskrupt/Diskrupt_Mdr_Issue.png)

    If we open the image in a hex editor, we can see if the MDR signature at the end is intact. This is represented by two bytes (55 AA) at the end of the MDR section (which is 512 bytes long).

    ![MDR Fix](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/diskrupt/Diskrupt_Mdr_Fix.png)

    Looks like that has been corrupted. Change it to '55 AA ', save it and reload in autopsy.

    ><details><summary>Click for answer</summary>ACBD</details>

2.  What are the bytes representing the total sector of the second partition? (Little Endian)

    We can find this in the partitions block of the MBR.

    ![Sectors](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/diskrupt/Diskrupt_Sectors.png)

    The highlighted part is the total number of sectors in Little Endian format. So we need to reverse that.

    ><details><summary>Click for answer</summary>0x01387800</details>

3.  What is the size of the first partition in GB? (up to 2 decimals e.g: 15.25)

    We can find this using FTK Images after fixing the image. We need to convert this to GB first (i.e., MB -> /1024 -> GB).

    ![Partitions](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/diskrupt/Diskrupt_Partitions.png)

    ><details><summary>Click for answer</summary>30.23</details>

4.  What is the size of the second partition in GB? (up to 2 decimals e.g: 15.25)

    Can be found in the same place.

    ><details><summary>Click for answer</summary>9.76</details>

5.  In the NTFS partition, when was the text file related to the password created on the system?

    Lets download the Master File Table and parse it using Cemd to see what we can find.

    ![Mft](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/diskrupt/Diskrupt_Mft.png)

    Then we run `MfteCmd` to parse the MFT.

    ```powershell
    .\MFTECmd.exe -f '..\Evidence\$MFT' --csv ..\Evidence\ --csvf MFT_record.csv
    ```

    ![Mftecmd](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/diskrupt/Diskrupt_Mftecmd.png)

    Now we can look through the file using Timeline Explorer and filter on extention and file name.

    ![Passwords](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/diskrupt/Diskrupt_Passwords.png)

    ><details><summary>Click for answer</summary>2025-03-19 22:01:57</details>

6.  What is the full name of the sensitive pdf document accessed on this disk?

    We can also investigate the journal file to any accesses documents.

    ```powershell
    .\MFTECmd.exe -f '..\Evidence\$J' --csv ..\Evidence\ --csvf USNjournal.csv
    ```

    ![Journal](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/diskrupt/Diskrupt_Journal.png)

    We can see a certain sensitive pdf file being accessed multiple times.

    ><details><summary>Click for answer</summary>Quantum-Resistant Cryptographic Algorithms.pdf</details>

7.  When this file was first found on this disk?

    This can be found in the timestamp column. We need to find the first occurence.

    ><details><summary>Click for answer</summary>2025-03-20 00:44:37</details>

8.  What is the entry number of the directory in the Journal that was created and then deleted for exfiltration purposes on the disk?

    We can either filter the csv on type: Directory and update reason: RenameNewName or we can filter the name on somthing used for data exfiltration such as 'exfil'.

    ![Folder](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/diskrupt/Diskrupt_Folder.png)

    ><details><summary>Click for answer</summary>163896</details>

9.  What is the starting offset of the first zip file found after the offset 4E7B00000?

    Using HxD, we can navigate to the given offset then perform a forward search for a zipfile. Easiest is to use the magic number used for a zip file. In this case: `50 4B 03 04 14 00 06 00`.

    ![Zip](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/diskrupt/Diskrupt_Zip.png)

    ><details><summary>Click for answer</summary>4E7B0E000</details>

10.  What is the ending offset of the zip file?

     The trailer for a zip file is `50 4B 05 06` followed by 18 bytes. This gives us the end offset.

     ![End](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/diskrupt/Diskrupt_End.png

     ><details><summary>Click for answer</summary>4E7B0E43D</details>

11.  What is the flag hidden within the file inside the zip file?

     I found a secret.zip fil in FTK Images, but that couldn't be loaded. So I decided to export the raw bytes that we just found. We can select the entire section and save it as a zip file.
     
     ![Export](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/diskrupt/Diskrupt_Export.png)

     ![Flag](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/diskrupt/Diskrupt_Flag.png)

     ><details><summary>Click for answer</summary>FLAG:{RECOVERED_SECRET_THM}</details>

12.  In the FAT32 partition, a tool related to the disk wiping was installed and then deleted. Can you find the name of that executable?

     In FTK Imager, we can see a few deleted files on the second (FAT32) partition.

     ![Diskwipe](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/diskrupt/Diskrupt_Diskwipe.png)

     ><details><summary>Click for answer</summary>DiskWipe.exe</details>
