![Data Exfiltration Banner](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/dataxexfilt/Data_Exfiltration_Banner.png)

<p align="center">
   <img src="https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/dataxexfilt/Data_Exfiltration_Cover.png" alt="Data Exfiltration Logo">
</p>

# Data Exfiltration

This guide contains the answer and steps necessary to get to them for the [Data Exfiltration](https://tryhackme.com/r/room/dataxexfilt) room.

## Table of contents

- [Data Exfiltration](#data-exfiltration)
- [Exfiltration using TCP socket](#exfiltration-using-tcp-socket)
- [Exfiltration using SSH](#exfiltration-using-ssh)
- [Exfiltrate using HTTP(S)](#exfiltrate-using-http(s))
- [Exfiltration using ICMP](#exfiltration-using-icmp)
- [DNS Configurations](#dns-configurations)
- [Exfiltration over DNS](#exfiltration-over-dns)
- [DNS Tunneling](#dns-tunneling)

### Data Exfiltration

1. In which case scenario will sending and receiving traffic continue during the connection?



   ><details><summary>Click for answer</summary></details>

2. In which case scenario will sending and receiving traffic be in one direction?



   ><details><summary>Click for answer</summary></details>

3. In the next task, we will be discussing how data exfiltration over the TCP socket works!



   ><details><summary>Click for answer</summary></details>

### Exfiltration using TCP socket

1. Exfiltration using TCP sockets relies on ____________ protocols!



   ><details><summary>Click for answer</summary></details>

2. Now apply what we discussed to exfiltrate data over the TCP socket! Once you exfiltrate data successfully, hitCompletedto move on to the next task!



   ><details><summary>Click for answer</summary></details>

### Exfiltration using SSH

1. All packets sent using the Data Exfiltration technique over SSH are encrypted! (T=True/F=False)



   ><details><summary>Click for answer</summary></details>

2. Replicate the steps to transfer data over the SSH client. Once you transfer the file successfully, hitCompletedand move on to the next task!



   ><details><summary>Click for answer</summary></details>

### Exfiltrate using HTTP(S)

1. Check the Apache log file onweb.thm.comand get the flag!



   ><details><summary>Click for answer</summary></details>

2. When you visit thehttp://flag.thm.com/flagwebsite through the uploader machine via the HTTP tunneling technique, what is the flag?



   ><details><summary>Click for answer</summary></details>

### Exfiltration using ICMP

1. In which ICMP packet section can we include our data?



   ><details><summary>Click for answer</summary></details>

2. Follow the technique discussed in this task to establish a C2 ICMP connection between JumpBox and ICMP-Host. Then execute the "getFlag" command. What is the flag?



   ><details><summary>Click for answer</summary></details>

### DNS Configurations

1. Once the DNS configuration works fine, resolve theflag.thm.comdomain name. What is the IP address?



   ><details><summary>Click for answer</summary></details>

### Exfiltration over DNS

1. What is the maximum length for the subdomain name (label)?



   ><details><summary>Click for answer</summary></details>

2. The Fully Qualified FQDN domain name must not exceed ______characters.



   ><details><summary>Click for answer</summary></details>

3. Execute the C2 communication over the DNS protocol of theflag.tunnel.com. What is the flag?



   ><details><summary>Click for answer</summary></details>

### DNS Tunneling

1. When the iodine connection establishes to Attacker, run theifconfigcommand. How many interfaces are? (including the loopback interface)



   ><details><summary>Click for answer</summary></details>

2. What is the network interface name created by iodined?



   ><details><summary>Click for answer</summary></details>

3. Use the DNS tunneling to prove your access to the webserver,http://192.168.0.100/test.php. What is the flag?



   ><details><summary>Click for answer</summary></details>

