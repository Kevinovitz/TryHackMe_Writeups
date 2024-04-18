![Burp Suite: Intruder Banner](https://assets.tryhackme.com/room-banners/burpsuite.svg)

<p align="center">
   <img src="https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/burpsuiteintruder/Burpsuite_Intruder_Cover.png" alt="Burp Suite: Intruder Logo">
</p>

# Burp Suite: Intruder

This guide contains the answer and steps necessary to get to them for the [Burp Suite: Intruder](https://tryhackme.com/room/burpsuiteintruder) room.

## Table of contents

- [Intruder What is Intruder?](#intruder-what-is-intruder)
- [Attack Types Sniper](#attack-types-sniper)
- [Attack Types Battering Ram](#attack-types-battering-ram)
- [Attack Types Pitchfork](#attack-types-pitchfork)
- [Attack Types Cluster Bomb](#attack-types-cluster-bomb)
- [Intruder Payloads](#intruder-payloads)
- [Practical Example](#practical-example)
- [Practical Challenge](#practical-challenge)
- [Extra Mile CSRF Token Bypass](#extra-mile-csrf-token-bypass)

### Intruder What is Intruder?


1. Which section of the Options sub-tab allows you to control what information will be captured in the Intruder results?

   The answer can be found in the text.
  
   ><details><summary>Click for answer</summary>Attack Results</details>
   
2. In which Intruder sub-tab can we define the "Attack type" for our planned attack?

   The answer can be found in the text.
  
   ><details><summary>Click for answer</summary>Positions</details>
   
### Attack Types Sniper


1. If you were using Sniper to fuzz three parameters in a request, with a wordlist containing 100 words, how many requests would Burp Suite need to send to complete the attack?

   The answer will be the numbers of parameters x the number of words in the list (3*100).
  
   ><details><summary>Click for answer</summary>300</details>

2. How many sets of payloads will Sniper accept for conducting an attack?

   The answer can be found in the text.
  
   ><details><summary>Click for answer</summary>1</details>

3. Sniper is good for attacks where we are only attacking a single parameter, aye or nay?

   The answer can be found in the text.
  
   ><details><summary>Click for answer</summary>Aye</details>

### Attack Types Battering Ram

As a hypothetical question: you need to perform a Battering Ram Intruder attack on the example request above.

If you have a wordlist with two words in it (admin and Guest) and the positions in the request template look like this:
username=§pentester§&password=§Expl01ted§

1. What would the body parameters of the first request that Burp Suite sends be?

   The answer can be found in the text.
  
   ><details><summary>Click for answer</summary>username=admin&password=admin</details>

### Attack Types Pitchfork

1. What is the maximum number of payload sets we can load into Intruder in Pitchfork mode?

   The answer can be found in the text.
  
   ><details><summary>Click for answer</summary>20</details>

### Attack Types Cluster Bomb

We have three payload sets. The first set contains 100 lines; the second contains 2 lines; and the third contains 30 lines.

1. How many requests will Intruder make using these payload sets in a Cluster Bomb attack?

   The answer is the number of entries in each payload times the others (2x30x100).
  
   ><details><summary>Click for answer</summary>6000</details>

### Intruder Payloads

1. Which payload type lets us load a list of words into a payload set?

   The answer is the number of entries in each payload times the others (2x30x100).
  
   ><details><summary>Click for answer</summary>Simple list</details>

2. Which Payload Processing rule could we use to add characters at the end of each payload in the set?

   The answer is the number of entries in each payload times the others (2x30x100).
  
   ><details><summary>Click for answer</summary>Add suffix</details>

### Practical Example

First we head over to the web page, setup Firefox and Burpsuite to intercept the request, and send the request to Intruder.

```cmd
http://10.10.53.19/support/login
```

In the positions tab we select the pitchfork method and make sure to select the correct parameters.

![Positions](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/burpsuiteintruder/Burpsuite_Intruder_Example_Positions.png)

In the payloads tab we set the first set as a simple list and load the usernames list we downloaded. We then set the second set as a simple list and load the passwords list we downloaded.

![Payloads](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/burpsuiteintruder/Burpsuite_Intruder_Example_Payloads.png)

Now we can start the attack and let it run for a while. After it is done we must sort the results. In this case on length as the status is the same for successfull and invalid attempts.

![Credentials](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/burpsuiteintruder/Burpsuite_Intruder_Example_Credentials.png)

We can try these credentials on the login page to see if we can log in.

![Log In](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/burpsuiteintruder/Burpsuite_Intruder_Example_Log_in.png)

### Practical Challenge

1. Which attack type is best suited for this task?

   Since we only have one element we need to substitute we can use the sniper attack method.
  
   ><details><summary>Click for answer</summary>Sniper</details>

Configure an appropriate position and payload (the tickets are stored at values between 1 and 100), then start the attack.

You should find that at least five tickets will be returned with a status code of 200, indicating that they exist.

Either using the Response tab in the Attack Results window or by looking at each successful (i.e. 200 code) request manually in your browser, find the ticket that contains the flag.

2. What is the flag?

   After logging in we can click on one of the tickets. Then we can capture its request.
   
   ![Ticket](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/burpsuiteintruder/Burpsuite_Intruder_Challenge_Ticketpng.png)
   
   After capturing the request and sending it to Intruder, we must select the correct positions. In this case the ID after the URL. Also make sure to change the attack method to sniper.
   
   ![Position](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/burpsuiteintruder/Burpsuite_Intruder_Challenge_Position.png)
   
   In the payloads tab we set the payload to a numbers set. And we set the options to a list from 1-100 in steps of 1.
   
   ![Payloads](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/burpsuiteintruder/Burpsuite_Intruder_Challenge_Payloads.png)
   
   After the attack has completed we must sort the results. This time we can sort on the status code (which should be 200). We see several entries. Clicking on each one enables us to view the rendere response.
   
   ![Flag](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/burpsuiteintruder/Burpsuite_Intruder_Challenge_Flag.png)

   ><details><summary>Click for answer</summary>THM{MTMxNTg5NTUzMWM0OWRlYzUzMDVjMzJl}</details>

### Extra Mile CSRF Token Bypass

To bruteforce the admin panel, we need to use a macro.

First, we navigate to the correct webpage `http://10.10.53.19/admin/login` and the capture the request and send it to Intruder.

We then only select 'username' and 'password' as our positions. Deselect the session and login token if selected.

![Positions](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/burpsuiteintruder/Burpsuite_Intruder_Extra_Positions.png)

Next we navigate to Project options -> Sessions -> Macros -> Add. 

In the list that pops up, we should be able to select the request for the admin/login page. Otherwise we need to visit it manually.

![Macro](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/burpsuiteintruder/Burpsuite_Intruder_Extra_Macro.png)

Then we navigate to Project options -> Sessions -> Session Handling Rules -> Add. 

In the scope tab we only select Intruder as the tool scope and add our URL `http://10.10.53.19/` to the URL scope (suite scope didn't work, probably because it wasn't set).

![Rules](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/burpsuiteintruder/Burpsuite_Intruder_Extra_Rules.png)

In the details tab we must add a new action. Select run a macro. In this window select the macros we created and use update only the following parameters and cookies.

![Action](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/burpsuiteintruder/Burpsuite_Intruder_Extra_Action.png)

Now we start the attack and we should see responses with a 302 status code. This time we sort on the length again and find out candidate.

![Hit](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/burpsuiteintruder/Burpsuite_Intruder_Extra_Hit.png)

Trying the credentials gives us access to the admin panel.

![Admin](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/burpsuiteintruder/Burpsuite_Intruder_Extra_Admin.png)
