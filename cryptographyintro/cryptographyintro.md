![Introduction to Cryptography Banner](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/cryptographyintro/Introduction_Cryptography_Banner.png)

<p align="center">
   <img src="https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/cryptographyintro/Introduction_Cryptography_Cover.png" alt="Introduction to Cryptography Logo">
</p>

# Introduction to Cryptography

This guide contains the answer and steps necessary to get to them for the [Introduction to Cryptography](https://tryhackme.com/room/cryptographyintro) room.

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

1. You have received the following encrypted message:

   “Xjnvw lc sluxjmw jsqm wjpmcqbg jg wqcxqmnvw; xjzjmmjd lc wjpm sluxjmw jsqm bqccqm zqy.” Zlwvzjxj Zpcvcol

   You can guess that it is a quote. Who said it?

   We can use the Quipquip site to try and decode the message.

   ![Introduction Name](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/cryptographyintro/Introduction_Cryptography_Introduction_Name.png)

   ><details><summary>Click for answer</summary>Miyamoto Musashi</details>
   
### Symmetric Encryption

1. Decrypt the file quote01 encrypted (using AES256) with the key s!kR3T55 using gpg. What is the third word in the file?

   ```cmd
   gpg --output task02/quote01.txt --decrypt task02/quote01.txt.gpg
   ```

   ![Symmetric Quote 1](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/cryptographyintro/Introduction_Cryptography_Symmetric_Quote_1.png)

   ><details><summary>Click for answer</summary>waste</details>

1. Decrypt the file quote02 encrypted (using AES256-CBC) with the key s!kR3T55 using openssl. What is the third word in the file?

   ```cmd
   openssl enc -aes-256-cbc -d -in task02/quote02 -out task02/quote02.txt
   ```

   ![Symmetric Quote 2](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/cryptographyintro/Introduction_Cryptography_Symmetric_Quote_2.png)

   ><details><summary>Click for answer</summary>science</details>

3. Decrypt the file quote03 encrypted (using CAMELLIA256) with the key s!kR3T55 using gpg. What is the third word in the file?

   ```cmd
   gpg --output task02/quote03.txt --decrypt task02/quote03.txt.gpg
   ```

   ![Symmetric Quote 3](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/cryptographyintro/Introduction_Cryptography_Symmetric_Quote_3.png)

   ><details><summary>Click for answer</summary>understand</details>

### Asymmetric Encryption

1. Bob has received the file ciphertext_message sent to him from Alice. You can find the key you need in the same folder. What is the first word of the original plaintext?

   For this, we need the cipher text and Bob's private key.

   ```cmd
   openssl pkeyutl -decrypt -in ciphertext_message -inkey private-key-bob.pem -out plaintext.txt
   ```

   This will put the plaintext into a file for us to read.

   ![Assymetric Plaintext](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/cryptographyintro/Introduction_Cryptography_Assymetric_Plaintext.png)

   ><details><summary>Click for answer</summary>Perception</details>

2. Take a look at Bob’s private RSA key. What is the last byte of p?

   To view the real RSA variable we can use the following command:

   ```cmd
   openssl rsa -in private-key-bob.pem -text -noout
   ```

   The `p` variable will be prime1.

   ![Assymetric Bytes](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/cryptographyintro/Introduction_Cryptography_Assymetric_Bytes.png)

   ><details><summary>Click for answer</summary>e7</details>

3. Take a look at Bob’s private RSA key. What is the last byte of q?

   This can be found with the same command. `q` will be prime2.

   ><details><summary>Click for answer</summary>27</details>

### Diffie-Hellman Key Exchange

1. A set of Diffie-Hellman parameters can be found in the file dhparam.pem. What is the size of the prime number in bits?

   To view the real varibales of the Diffie-Hellman key, we can use the same command as in the previous task.

   ```cmd
   openssl dhparam -in dhparams.pem -text -noout
   ```

   ![Hellman Size](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/cryptographyintro/Introduction_Cryptography_Hellman_Size.png)

   ><details><summary>Click for answer</summary>4096</details>

3. What is the prime number’s last byte (least significant byte)?

   This can be found together with the previous question.

   ><details><summary>Click for answer</summary>4f</details>

### Hashing

1. What is the SHA256 checksum of the file order.json?

   Using `sha256sum` we can calculate the SHA-256 hash of the file.

   ```cmd
   sha256sum order.json
   ```

   ![Hashing Sha](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/cryptographyintro/Introduction_Cryptography_Hashing_Sha.png)

   ><details><summary>Click for answer</summary>2c34b68669427d15f76a1c06ab941e3e6038dacdfb9209455c87519a3ef2c660</details>

1. Open the file order.json and change the amount from 1000 to 9000. What is the new SHA256 checksum?

   After changing the content of the file, we can use the same command to re-calculate the hash.

   ![Hashing Change](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/cryptographyintro/Introduction_Cryptography_Hashing_Change.png)
   
   ```cmd
   sha256sum order.json
   ```

   ![Hashing Sha New](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/cryptographyintro/Introduction_Cryptography_Hashing_Sha_New.png)
   
   ><details><summary>Click for answer</summary>11faeec5edc2a2bad82ab116bbe4df0f4bc6edd96adac7150bb4e6364a238466</details>

3. Using SHA256 and the key 3RfDFz82, what is the HMAC of order.txt?

   Using the following command will give us the hash we are looking for.

   ```cmd
   hmac256 3RfDFz82 order.txt
   ```

   ![Hashing Hmac](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/cryptographyintro/Introduction_Cryptography_Hashing_Hmac.png)

   ><details><summary>Click for answer</summary>c7e4de386a09ef970300243a70a444ee2a4ca62413aeaeb7097d43d2c5fac89f</details>

### PKI and SSL/TLS

1. What is the size of the public key in bits?

   Using the following command we can view the contents of the certificate.

   ```cmd
   openssl x509 -in cert.pem -text -noout
   ```

   ![PKI Cert](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/cryptographyintro/Introduction_Cryptography_PKI_Cert.png)

   ><details><summary>Click for answer</summary>4096</details>

1. Till which year is this certificate valid?

   This can be found in the same image as the previous question.

   ><details><summary>Click for answer</summary>2039</details>

### Authenticating with Passwords

1. You were auditing a system when you discovered that the MD5 hash of the admin password is 3fc0a7acf087f549ac2b266baf94b8b1. What is the original password?

   We can use `hashcat` to crack the hash. Knowing it is an MD5 hash we use the following command:

   ```cmd
   hashcat -m 0 3fc0a7acf087f549ac2b266baf94b8b1 /usr/share/wordlists/rockyou.txt
   ```

   ![Authenticating Password](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/cryptographyintro/Introduction_Cryptography_Authenticating_Password.png)

   ><details><summary>Click for answer</summary>qwerty123</details>
