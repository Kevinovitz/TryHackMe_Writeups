![Breaking RSA Banner](https://assets.tryhackme.com/img/banners/default_tryhackme.png)

<p align="center">
   <img src="https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/breakrsa/Breaking_Rsa_Cover.png" alt="Breaking RSA Logo">
</p>

# Breaking RSA

This guide contains the answer and steps necessary to get to them for the [Breaking RSA](https://tryhackme.com/room/breakrsa) room.

### Capture the flag

1. How many services are running on the box?

   Using nmap will give us the running services.

   ```console
   nmap -sS -sV 10.10.97.159 -Pn -p-
   ```

   ![Nmap](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/breakrsa/Breaking_Rsa_Nmap.png)

   ><details><summary>Click for answer</summary>2</details>

2. What is the name of the hidden directory on the web server? (without leading '/')

   We can use multiple tools for this task. I will use `dirsearch` here.

   ```console
   dirsearch -u 10.10.97.159:80 -w /usr/share/wordlists/seclists/Discovery/Web-Content/directory-list-2.3-medium.txt -r
   ```

   ![Directory](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/breakrsa/Breaking_Rsa_Directory.png)

   This gives us a hidden directory which happens to contain an id_rsa key.

   ><details><summary>Click for answer</summary>development</details>

3. What is the length of the discovered RSA key? (in bits)

   To find details about the key, we can use `ssh-keygen`.

   ```console
   ssh-keygen -l -f Downloads/id_rsa.pub 
   ```

   ![Length](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/breakrsa/Breaking_Rsa_Length.png)

   ><details><summary>Click for answer</summary>1096</details>

4. What are the last 10 digits of n? (where 'n' is the modulus for the public-private key pair)

   To get the components of the public key we can use the suggested python module 'pydryptodome'.

   First we must convert the public key to PEM format using `ssh-keygen`.

   ```console
   ssh-keygen -e -f id_rsa.pub -m pem
   ```

   Now we can use the following python code to extract the modulus 'n':

   ```python
   from Crypto.PublicKey import RSA
   key_encoded='''<id_rsa key here>'''


   pubkey = RSA.importKey(key_encoded)
   print(f"Modulus n is: {pubkey.n}")
   print(f"Constant e is: {pubkey.e}")
   ```

   ![Modulus](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/breakrsa/Breaking_Rsa_Modulus.png)

   ><details><summary>Click for answer</summary>1225222383</details>

5. Factorize n into prime numbers p and q

   The provided script didn't work as the modulus was too large to be handled by it. Modifying it also didn't work, so I used a different script.

   ```python
   def isqrt(n):
	x=n
	y=(x+n//x)//2
	while(y<x):
		x=y
		y=(x+n//x)//2
	return x
   def fermat(n):
      t0=isqrt(n)+1
      counter=0
      t=t0+counter
      temp=isqrt((t*t)-n)
      while((temp*temp)!=((t*t)-n)):
         counter+=1
         t=t0+counter
         temp=isqrt((t*t)-n)
      s=temp
      p=t+s
      q=t-s
      return p,q

   print("Enter the number to factor of form (p*q):	")
   n=int(input())
   p,q=fermat(n)
   print("Your first number   : ",int(p))
   print("Your Second number  : ",int(q))
   ```

   Now we can enter the modulus we acquired and we are given 'p' and 'q'.

   ![Factorized](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/breakrsa/Breaking_Rsa_Factorized.png)

   ><details><summary>Click for answer</summary></details>

6. What is the numerical difference between p and q?

   The previous script also outputs the differences between the two factors.

   ><details><summary>Click for answer</summary>1502</details>

7. Generate the private key using p and q (take e = 65537)

   I first tried using openssl, without any success. So I used the pycryptodome library to create a python script to help me with this.

   ```python
   from Crypto.PublicKey import RSA

   # Specify the factors
   p = <first prime>
   q = <second prime>
   e = 65537

   # Calculate n and d
   n = p * q
   phi = (p - 1) * (q - 1)
   d = pow(e, -1, phi)

   # Create the RSA key object
   key = RSA.construct((n, e, int(d)))

   # Export the private key to a PEM file
   with open("private_key.pem", "wb") as f:
      f.write(key.export_key())
   ```

   Add both primes we found in the previous step and generate the private key.

   ```console
   python genpkey.py
   ```

   ![Private Key](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/breakrsa/Breaking_Rsa_Private_Key.png)

8. What is the flag?

   Now that we have the private key, we can use it to ssh into the machine. From the hidden directory we also learned that root login was enabled.

   First restrict usage of the private keu with `chmod`:

   ```console
   chmod 600 private_key.pem
   ```

   Now we can ssh into the machine as root with:

   ```console
   ssh root@10.10.97.159 -i private_key.pem
   ```

   ![Ssh](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/breakrsa/Breaking_Rsa_Ssh.png)

   ![Flag](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/breakrsa/Breaking_Rsa_Flag.png)

   ><details><summary>Click for answer</summary>breakingRSAissuperfun20220809134031</details>