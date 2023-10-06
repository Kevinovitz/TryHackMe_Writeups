![Title Banner](https://tryhackme.com/img/banners/default_tryhackme.png)

<p align="center">
   <img src="https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/NAME/_Cover.png" alt="TITLE Logo">
</p>

# TITLE

This guide contains the answer and steps necessary to get to them for the [TITLE](https://tryhackme.com/room/NAME) room.

## Table of contents

- [Introduction](#introduction)
- [Symmetric Encryption](#symmetric-encryption)
- [Asymmetric Encryption](#asymmetric-encryption)
- [Diffie-Hellman Key Exchange](#diffie-hellman-key-exchange)
- [Hashing](#hashing)
- [PKI and SSL/TLS](#pki-and-ssl/tls)
- [Authenticating with Passwords](#authenticating-with-passwords)
- [Cryptography and Data - Example](#cryptography-and-data---example)

### Introduction

1. 


### Symmetric Encryption

1. You have received the following encrypted message:

   “Xjnvw lc sluxjmw jsqm wjpmcqbg jg wqcxqmnvw; xjzjmmjd lc wjpm sluxjmw jsqm bqccqm zqy.” Zlwvzjxj Zpcvcol

   You can guess that it is a quote. Who said it?

   We can use the Quipquip site to try and decode the message.

   INTRODCUTION NAME

   ><details><summary>Click for answer</summary>Miyamoto Musashi</details>

### Asymmetric Encryption

1. Decrypt the file quote01 encrypted (using AES256) with the key s!kR3T55 using gpg. What is the third word in the file?

   ```cmd
   gpg --output task02/quote01.txt --decrypt task02/quote01.txt.gpg
   ```

   SYMMETRIC QUOTE 1

   ><details><summary>Click for answer</summary>waste</details>

1. Decrypt the file quote02 encrypted (using AES256-CBC) with the key s!kR3T55 using openssl. What is the third word in the file?

   ```cmd
   openssl enc -aes-256-cbc -d -in task02/quote02 -out task02/quote02.txt
   ```

   SYMMETRIC QUOTE 2

   ><details><summary>Click for answer</summary>science</details>

3. Decrypt the file quote03 encrypted (using CAMELLIA256) with the key s!kR3T55 using gpg. What is the third word in the file?

   ```cmd
   gpg --output task02/quote03.txt --decrypt task02/quote03.txt.gpg
   ```

   SYMMETRIC QUOTE 3

   ><details><summary>Click for answer</summary>understand</details>

### Diffie-Hellman Key Exchange




### Hashing




### PKI and SSL/TLS




### Authenticating with Passwords




### Cryptography and Data - Example 



1. 

   

   ><details><summary>Click for answer</summary></details>
