![Encryption - Crypto 101 Banner](https://assets.tryhackme.com/room-banners/crypto.png)

<p align="center">
   <img src="https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/encryptioncrypto101/Encryption_Crypto_101_Cover.png" alt="Encryption - Crypto 101 Logo">
</p>

# Encryption - Crypto 101

This guide contains the answer and steps necessary to get to them for the [Encryption - Crypto 101](https://tryhackme.com/room/encryptioncrypto101) room.

## Table of contents

- [Key terms](#key-terms)
- [Why is Encryption important?](#why-is-encryption-important?)
- [Crucial Crypto Maths](#crucial-crypto-maths)
- [Types of Encryption](#types-of-encryption)
- [RSA - Rivest Shamir Adleman](#rsa---rivest-shamir-adleman)
- [Digital signatures and Certificates](#digital-signatures-and-certificates)
- [SSH Authentication](#ssh-authentication)
- [PGP, GPG and AES](#pgp-gpg-and-aes)

### Key terms

1. I agree not to complain too much about how theory heavy this room is.

2. Are SSH keys protected with a passphrase or a password?

   The answer can be found in the text.

   ><details><summary>Click for answer</summary>passphrase</details>

### Why is Encryption important?

1. What does SSH stand for?

   Looking up SSH gives us what it stands for.

   ><details><summary>Click for answer</summary>Secure Shell</details>

2. How do webservers prove their identity?

   This can be found in the text.

   ><details><summary>Click for answer</summary>Certificates</details>

3. What is the main set of standards you need to comply with if you store or process payment card details?

   These standards are noted in the Payment Card Industry Data Security Standards. This can be found through a search.

   ><details><summary>Click for answer</summary>PCI-DSS</details>

### Crucial Crypto Maths

1. What's 30 % 5?

   Dividing 30 by 5 gives us 6. So it is divisible by 5 and the remainder is 0.

   ><details><summary>Click for answer</summary>0</details>

2. What's 25 % 7

   25 isn't divisible by 7. Closest we can get is 3*7=21. So the remainder is 4

   ><details><summary>Click for answer</summary>4</details>

3. What's 118613842 % 9091

   Dividing 118613842 by 9091 gives us a large decimal number, so it isn't divisible by 9091. If we take all that is after the comma and multiply it with 9091 we get 3565. This would be the remainder.

   ><details><summary>Click for answer</summary>3565</details>

### Types of Encryption

1. Should you trust DES? Yea/Nay

   From the text we can gather DES is not considere secure anymore.

   ><details><summary>Click for answer</summary>Nay</details>

2. What was the result of the attempt to makeDESmore secure so that it could be used for longer?

   This we must research!

   ><details><summary>Click for answer</summary>triple DES</details>

3. Is it ok to share your public key? Yea/Nay

   Only the private key must be kept private.

   ><details><summary>Click for answer</summary>Yea</details>

### RSA - Rivest Shamir Adleman

1. p = 4391, q = 6659. What is n?

   n is the product of p and q, so we need to multiply p and q to get our answer.

   ><details><summary>Click for answer</summary>29239669</details>

2. I understand enough about RSA to move on, and I know where to look to learn more if I want to.

### Digital signatures and Certificates

1. Who is TryHackMe's HTTPS certificate issued by?

   We can find the website's certificate by clicking on the padlock icon in the address bar. This already shows us who verified the website. CLicking on more information should give us the name we are after.

   ![Certificates Issuer](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/encryptioncrypto101/Encryption_Crypto_101_Certificates_Issuer.png)

   ><details><summary>Click for answer</summary>E1</details>

### SSH Authentication

1. I recommend giving this a go yourself. Deploy a VM, like [Linux Fundamentals 2](https://tryhackme.com/room/linuxfundamentalspart2) and try to add an SSH key and log in with the private key.

   If you want to try, use the following commands:

   ```console
   ssh-keygen
   -> To generate the private and public key pair.

   cat id_rsa > authorized_keys
   or
   ssh-copy-id
   -> To copy the public key into the authorized_keys file
   ```

   Now create a folder on the target machine `.ssh` and place the public key and authorized_keys file in it.

   Now you can log in with your private key using:

   ```console
   ssh -i <private key file> <username>@<ip>
   ```
   
2. Download the SSH Private Key attached to this room.

3. What algorithm does the key use?

   After downloading the file, we can make a guess of the used algorithm by looking at its file name. This can be checked by opening the file.

   ![Ssh Key](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/encryptioncrypto101/Encryption_Crypto_101_Ssh_Key.png)

   ><details><summary>Click for answer</summary>RSA</details>

4. Crack the password with John The Ripper and rockyou, what's the passphrase for the key?

   First we must convert the key into a suitable format for John.

   ```console
   ssh2john idrsa_rsa sshhash.txt

   john --wordlist=/usr/share/wordlists/rockyou.txt sshhash.txt
   ```

   ><details><summary>Click for answer</summary>delicious</details>

### PGP, GPG and AES

1. Time to try some GPG. Download the archive attached and extract it somewhere sensible.

2. You have the private key, and a file encrypted with the public key. Decrypt the file. What's the secret word?

   We must use `gpg` to decrypt the file. Since we have the key, we can import it into `gpg`.

   ```console
   gpg --import tryhackme.key
   ```

   Now we can decrypt the message.

   ```console
   gpg --decrypt message.gpg
   ```

   ![Gpg Secret Message](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/encryptioncrypto101/Encryption_Crypto_101_Gpg_Secret_Message.png)

   ><details><summary>Click for answer</summary>Pineapple</details>
