![Race Conditions - Toy to The World Banner](https://tryhackme-images.s3.eu-west-1.amazonaws.com/room-icons/62a7685ca6e7ce005d3f3afe-1763479569063)

<p align="center">
   <img src="https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/race-conditions-aoc2025-d7f0g3h6j9/Race_Conditions_-_Toy_to_The_World_Cover.png" alt="Race Conditions - Toy to The World Logo">
</p>

# <img src="https://tryhackme-images.s3.amazonaws.com/room-icons/62a7685ca6e7ce005d3f3afe-1763479664712" alt="image" style="vertical-align: middle;height: 50px;" /> Race Conditions - Toy to The World | Advent of Cyber 2025 - Day 20

This guide contains the answer and steps necessary to get to them for the [Race Conditions - Toy to The World](https://tryhackme.com/room/race-conditions-aoc2025-d7f0g3h6j9) room.

## Table of contents

- [Race Condition](#race-condition)

### Race Condition

1.  What is the flag value once the stocks are negative for SleighToy Limited Edition?

    Make sure to open Burpsuite, enable Foxy proxy's burp toggle, and turn of intercept in Burpsuite. Then log into the web portal using the given credentials. On this dashboard we select the toy, add it to our cart, click to checkout. Confirm the order and go to the orders screen.

    ![Checkout](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/race-conditions-aoc2025-d7f0g3h6j9/Race_Conditions_-_Toy_to_The_World_Checkout.png)

    We can see one items has been deducted and the new stock is 9. Now that we have created a legitimate purchase, head over to burpsuite and look for the POST request in the HTTP history list under the Proxy tab. Send this request over to Burpsuite Repeater.

    ![Send](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/race-conditions-aoc2025-d7f0g3h6j9/Race_Conditions_-_Toy_to_The_World_Send.png)

    Now we create the tab group as instructed and duplicate the original request about 15 times. Once that is done, select the 'send in parallel' method and click send.

    ![Repeater](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/race-conditions-aoc2025-d7f0g3h6j9/Race_Conditions_-_Toy_to_The_World_Repeater.png)

    After sending the requests, we can see that the stock is not in the negative.

    ![Flag1](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/race-conditions-aoc2025-d7f0g3h6j9/Race_Conditions_-_Toy_to_The_World_Flag1.png)

    ><details><summary>Click for answer</summary>THM{WINNER_OF_R@CE007}</details>

2.  Repeat the same steps as were done for ordering the SleighToy Limited Edition. What is the flag value once the stocks are negative for Bunny Plush (Blue)?

    Lets create another legitimate order, this time for the Bunny toy.

    ![Bunny](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/race-conditions-aoc2025-d7f0g3h6j9/Race_Conditions_-_Toy_to_The_World_Bunny.png)

    Look this request up again the the HTTP history list. Add it to Repeater. Now create anoth tab group and duplicate the original request 4 more times. Set the mode to parallel and send the requests.

    ![Send2](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/race-conditions-aoc2025-d7f0g3h6j9/Race_Conditions_-_Toy_to_The_World_Send2.png)

    ![Repeater2](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/race-conditions-aoc2025-d7f0g3h6j9/Race_Conditions_-_Toy_to_The_World_Repeater2.png)

    If we look at the orders, we can see that the stock for the bunny toy is also negative!

    ![Flag2](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/race-conditions-aoc2025-d7f0g3h6j9/Race_Conditions_-_Toy_to_The_World_Flag2.png)

    ><details><summary>Click for answer</summary>THM{WINNER_OF_Bunny_R@ce}</details>

3.  Feel free to check out the [Race Conditions](https://tryhackme.com/r/room/raceconditionsattacks) room if you enjoyed this task.
