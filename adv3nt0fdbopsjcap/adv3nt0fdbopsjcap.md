![The Return of the Yeti Banner](https://tryhackme-images.s3.amazonaws.com/user-uploads/6093e17fa004d20049b6933e/room-content/8d1eef4732f7fc206539fb68abdabc5d.svg)

<p align="center">
   <img src="https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/adv3nt0fdbopsjcap/Return_Of_The_Yeti_Cover.png" alt="The Return of the Yeti Logo">
</p>

# The Return of the Yeti

This guide contains the answer and steps necessary to get to them for the [The Return of the Yeti](https://tryhackme.com/room/adv3nt0fdbopsjcap) room.

### New Year, New Opportunities 

1. What's the name of the WiFi network in the PCAP?

   Opening the capture file in Wireshark may give us an insight into the networks captured. (Another way is using `aircrack-ng` as in question 2)
   
   !(Ssid)[https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/adv3nt0fdbopsjcap/Return_Of_The_Yeti_Ssid.png]
   
   A usefull addition to Wireshark would be to add a column that would display the SSID of the network.
   
   This can be done from the Edit -> Preferences menu -> Appearance -> Columns.
   
   Add a new value with the values listed below.
   
   !(Wireshark Columns)[https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/adv3nt0fdbopsjcap/Return_Of_The_Yeti_Wireshark_Columns.png]
   
   Another method is to look at the build in function to list WLAN addresses. Under "Wireless -> WLAN Traffic".
   
   WLAN
   
   WLAN NETWORKS

   ><details><summary>Click for answer</summary>FreeWifiBFC</details>

2. What's the password to access the WiFi network?

   If we filter our pcap file in Wireshark by the `eapol` protocol we can see if any WPA related packets are captured.
   
   !(Eapol Packets)[https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/adv3nt0fdbopsjcap/Return_Of_The_Yeti_Eapol_Packets.png]
   
   This indeed gives us two pair of hashes consisting of four keys. This also mean we can possible decrypt the packets to view the previously encrypted data.
   
   There are two methods I want to highlight here that we can use to extract the WPA wifi password.
   
   The first one is using `hashcat` and the second is by using `aircrack-ng`. Both require just a little preparation.
   
   ** Mehtode 1 Hashcat**
   
   Running `hashcat -h | grep WPA` we can see that hashcat is able to crack WPA hashes. 
   
   !(Hashcat Wpa)[https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/adv3nt0fdbopsjcap/Return_Of_The_Yeti_Hashcat_Wpa.png]
   
   The first thing we need to do is extract the wpa hashes from the capture file and put it in a format that hashcat understands.
   
   We can use `hcxtools` for this.
   
   ```cmd
   hcxpcapngtool VanSpy.pcapng -o wifihashes.txt
   ```
   
   !(Extract Hashes)[https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/adv3nt0fdbopsjcap/Return_Of_The_Yeti_Extract_Hashes.png]
   
   Checking the file, we can see it extracted two hashes. One for each of the EAPOL handshakes in our file.

   !(Wpa Keys)[https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/adv3nt0fdbopsjcap/Return_Of_The_Yeti_Wpa_Keys.png]

   Now that we have our hashes in a readable format, we can use Hashcat to crack it. **Note, this does require the used password to be in our wordlist.**
   
   ```cmd
   hashcat -m 22000 -w 3 wifihashes.txt /usr/share/wordlists/rockyou.txt
   ```
   
   !(Hashcat Password)[https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/adv3nt0fdbopsjcap/Return_Of_The_Yeti_Hashcat_Password.png]

   ** Mehtode 2 Aircrack-ng**
   
   `aircrack-ng` is able to crack the WPA keys directly from the capture file. However, using the file provided gives us an error as the utility can't parse `.pcapng` files.
   
   !(Aircrack Failed)[https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/adv3nt0fdbopsjcap/Return_Of_The_Yeti_Aircrack_Failed.png]
   
   So we must convert it to a `.cap` files using `tshark`.
   
   ```cmd
   tshark -r VanSpy.pcapng -w VanSpy.pcap -F libpcap
   ```
   
   !(Convert)[https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/adv3nt0fdbopsjcap/Return_Of_The_Yeti_Convert.png]
   
   Now we can try it again to get the wifi password.
   
   ```cmd
   aircrack-ng -w /usr/share/wordlists/rockyou.txt VanSpy.pcap  
   ```
   
   !(Aircrack Password)[https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/adv3nt0fdbopsjcap/Return_Of_The_Yeti_Aircrack_Password.png]   
   
   ><details><summary>Click for answer</summary>Christmas</details>

3. What suspicious tool is used by the attacker to extract a juicy file from the server?

   To look deeper at what has been done, we must decrypt the data somehow. 
   
   Luckily, we got hold of the WPA2 password. We can use this to decrypt the IEE 802.11 traffic.
   
   ADD DECRYPTION KEYS
   
   Now we can look further at the captured traffic. Something that looks interesting is the presence of RDP traffic. You can view this by filtering for "RDP" or "TPKT".
   
   RDP PACKETS
   
   Unfortunately, the rest of the data is encrypted as we can see with the "Continuation" messages. 
   
   We would need to somehow find the rsa private keys used to decrypt the data.
   
   After some research it is clear that we cannot decrypt the rdp stream without the private key. This might be a rabbit hole, but it feels like the RDP data is the way to go.
   
   Changing our tactics, we look further into the pcap file. At the bottom of the file we can see a lot of failed TCP handshakes.
   
   We can see a SYN packet is sent to various ports which is being met with a RST,ACK packet. But no ACK packet is sent back. This can be an indication of port scanning or bruteforcing.
   
   At the end we can see data is being pushed to a machine. Following this TCP stream gives us some valuable data! Apparently, someone had a powershell shell on the machine.
   
   FOLLOW TCP SHELL
   
   POWERSHELL tool
   
   Someone has been using a malicous tool on this machine as becomes apparent from the command history.

   ><details><summary>Click for answer</summary>Mimikatz</details>

4. What is the case number assigned by the CyberPolice to the issues reported by McSkidy?

   Looking through the commands issued in powershell we can see they exported a public and private certificate key using Mimikatz. This could have something to do with RDP.
   
   POWERSHELL EXPORT CERTIFICATE 
   
   More specifically, the .pfx file is of interest to us. Unfortunately, we can only see that the file was exported, but can't see or export the contents. 
   
   Or can we?
   
   POWERSHELL CERTIFICATE CONVERT 
   
   Here we can see the contents of the key itself! Lets re-create the private key from this.
   
   Note that the contents has been encoded into base64.
   
   Copy the contents to a file and convert it back from base64.
   
   ```cmd
   base64 -d privateb64.pfx > privatekey.pfx
   ```
   
   Opening the file, we get a password prompt. If you get an error, something probably went wrong copying the data or converting it.
   
   The password has been added by Mimikatz. Its default password is 'mimikatz'.
   
   PRIVATE KEY
   
   Unfortunately, Wireshark is unable to use a pfx formated certificate. We must convert it to PEM format or .cer.
   
   ```cmd
   openssl pkcs12 -in privatekey.pfx -out privatekey.cer -noenc
   ```
   
   Now we can import this certificate into Wireshark to decrypt TLS data.
   
   Edit -> Preferences -> Protocols -> TLS
   
   ADD TLS KEY
   
   We still don't get any meaningfull data. Something we can try is to have Wireshark use the TLS dissector to interpret the packets instead of TPKT.
   
   Select one of the "Continuation" packets -> Decode as. Now change current to "TLS".
   
   TLS DISSECTOR
   
   TLS DECRYPT
   
   Success! We decrypted the TLS traffic and have access to the RDP stream. 
   
   It would be easiest to replay what has been done through RDP. Luckily, we can use a tool called `pyrdp` to convert the rdp stream to a vieweable format, even a video file!
   
   Lets export the RDP data from Wireshark. 
   
   File -> Export PDUs to File. Select OSI layer 7 and click ok.
   
   EXPORT RDP
   
   Now save this as a separate pcap file.
   
   Next thing is to install pyrdp if not already available. Use the following guide to install.
   
   https://kalilinuxtutorials.com/pyrdp/
   
   Using the following command we can convert the pcap to a usable format for pyrdp.
   
   ```cmd
   pyrdp-convert -o output rdp-session.pcap
   ```
   
   We can now open the file using `pyrdp-player`. Or we can open a video file using the following command:
   
   ```cmd
   pyrdp-convert -o output -f mp4 rdp-session.pcap
   ```
   
   RDP VIDEO
   
   Looks like there is some email traffic regarding the case file.

   ><details><summary>Click for answer</summary>31337-0</details>

5. What is the content of the yetikey1.txt file?

   At the end of the 'stream' we can see the contents of the yetikey file is copied to the clipboard using powershell. This isn't vieweable in the video file.
   
   Luckily, `pyrdp` has the ability to display the keypresses during the stream.
   
   Eventually, we can see what the clipboard data is.
   
   YETIKEY

   ><details><summary>Click for answer</summary>1-1f9548f131522e85ea30e801dfd9b1a4e526003f9e83301faad85e6154ef2834</details>
