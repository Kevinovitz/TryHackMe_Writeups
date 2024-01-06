![Buffer Overflows Banner](https://tryhackme.com/img/banners/default_tryhackme.png)

<p align="center">
   <img src="https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/bof1/Buffer_Overflows_Cover.png" alt="Buffer Overflows Logo">
</p>

# Buffer Overflows

This guide contains the answer and steps necessary to get to them for the [Buffer Overflows](https://tryhackme.com/room/bof1) room.

## Table of contents

- [Process Layout](#process-layout)
- [x86-64 Procedures](#x86-64-procedures)
- [Procedures Continued](#procedures-continued)
- [Overwriting Variables](#overwriting-variables)
- [Overwriting Function Pointers](#overwriting-function-pointers)
- [Buffer Overflows](#buffer-overflows)
- [Buffer Overflow 2 ](#buffer-overflow-2)

### Process Layout

1. Where is dynamically allocated memory stored?

   The answer can be found in the text.

   ><details><summary>Click for answer</summary>Heap</details>

2. Where is information about functions(e.g. local arguments) stored?

The answer can be found in the text.

   ><details><summary>Click for answer</summary>Stack</details>

### x86-64 Procedures

1. What direction does the stack grown(l for lower/h for higher)

   The answer can be found in the text.

   ><details><summary>Click for answer</summary>l</details>

2. What instruction is used to add data onto the stack?

   The answer can be found in the text.

   ><details><summary>Click for answer</summary>push</details>

### Procedures Continued

1. What register stores the return address?

   The answer can be found in the text.

   ><details><summary>Click for answer</summary>rax</details>

### Overwriting Variables

1. What is the minimum number of characters needed to overwrite the variable?

   If we look at the c script in the first overflow folder we can see the buffer has 14 bytes.

   VARIABLES SCRIPT

   This means we must use at least 15 bytes of data in order to overwrite the variable.

   VARIABLES OVERFLOW

   ><details><summary>Click for answer</summary>15</details>

### Overwriting Function Pointers

1. Invoke the special function()



   ><details><summary>Click for answer</summary></details>

### Buffer Overflows

1. Use the above method to open a shell and read the contents of the secret.txt file.


   ><details><summary>Click for answer</summary></details>

### Buffer Overflow 2 

1. Use the same method to read the contents of the secret file!

   

   ><details><summary>Click for answer</summary></details>
