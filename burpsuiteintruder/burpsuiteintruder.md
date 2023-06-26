![Burp Suite: Intruder Banner]()

<p align="center">
   <img src="https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/burpsuiteintruder/Burp_Suite_Intruder_Cover.png" alt="Burp Suite: Intruder Logo">
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




### Practical Challenge

1. Which attack type is best suited for this task?

   Since we only have one element we need to substitute we can use the sniper attack method.
  
   ><details><summary>Click for answer</summary>Sniper</details>

Configure an appropriate position and payload (the tickets are stored at values between 1 and 100), then start the attack.

You should find that at least five tickets will be returned with a status code of 200, indicating that they exist.

Either using the Response tab in the Attack Results window or by looking at each successful (i.e. 200 code) request manually in your browser, find the ticket that contains the flag.

2. What is the flag?

   

### Extra Mile CSRF Token Bypass



1. 

   

   ><details><summary>Click for answer</summary></details>
