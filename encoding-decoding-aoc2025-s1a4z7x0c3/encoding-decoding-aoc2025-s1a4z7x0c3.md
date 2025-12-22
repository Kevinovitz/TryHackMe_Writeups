![CyberChef - Hoperation Save McSkidy Banner](https://tryhackme-images.s3.eu-west-1.amazonaws.com/room-icons/68baea2454c82afe90fd7020-1761906977572)

<p align="center">
   <img src="https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/encoding-decoding-aoc2025-s1a4z7x0c3/CyberChef_-_Hoperation_Save_McSkidy_Cover.png" alt="CyberChef - Hoperation Save McSkidy Logo">
</p>

# <img src="https://tryhackme-images.s3.amazonaws.com/room-icons/68baea2454c82afe90fd7020-1761822112541" alt="image" style="vertical-align: middle;height: 50px;" /> CyberChef - Hoperation Save McSkidy

This guide contains the answer and steps necessary to get to them for the [CyberChef - Hoperation Save McSkidy](https://tryhackme.com/room/encoding-decoding-aoc2025-s1a4z7x0c3) room.

## Table of contents

- [First Lock - Outer Gate](#first-lock--outer-gate)
- [Second Lock - Outer Wall](#second-lock--outer-wall)
- [Third Lock - Guard House](#third-lock--guard-house)
- [Fourth Lock - Inner Castle](#fourth-lock--inner-castle)
- [Fifth Lock - Prison Tower](#fifth-lock--prison-tower)

### First Lock - Outer Gate

1.  What is the password for the first lock?

    First thing to note is the guard name. This is displayed in the chat “Cottontail”. This name encoded to base64 will be our username. 

    Now looking at the network traffic after opening the developer tools and refreshing the page we can see a question. If we encode this to base64 as well and put it in the chat, we are given the password which is base64 encoded. 

    ![Chat](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/encoding-decoding-aoc2025-s1a4z7x0c3/CyberChef_-_Hoperation_Save_McSkidy_Chat.PNG)

    Decoding this message gives us another partially encoded message with the password.

    ![First Password](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/encoding-decoding-aoc2025-s1a4z7x0c3/CyberChef_-_Hoperation_Save_McSkidy_First_Password.png)

    ><details><summary>Click for answer</summary>Iamsofluffy</details>

### Second Lock - Outer Wall

1.  What is the password for the second lock?

    Now we can login at the first lock with:

    Username: `Q290dG9uVGFpbA==`
    Password: `Iamsofluffy`

    ![Outer Gate](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/encoding-decoding-aoc2025-s1a4z7x0c3/CyberChef_-_Hoperation_Save_McSkidy_Outer_Gate.png)

    For the second lock, we see the guards name in the chat: 'CarrotHelm' which encoded to base64 is 'Q2Fycm90SGVsbQ=='.

    Now look in the network tab to find the magic question.

    ![Question2](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/encoding-decoding-aoc2025-s1a4z7x0c3/CyberChef_-_Hoperation_Save_McSkidy_Question2.png)

    Base64 encode this and send it in the chat. We will receive an encoded reply.

    ![Chat2](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/encoding-decoding-aoc2025-s1a4z7x0c3/CyberChef_-_Hoperation_Save_McSkidy_Chat2.png)

    Looking at the level login logic, we can see that the password is twice encoded to bas64.

    ![Level Logic2](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/encoding-decoding-aoc2025-s1a4z7x0c3/CyberChef_-_Hoperation_Save_McSkidy_Level_Logic2.png)

    Decoding it twice from base64 in CyberChef will give us our second password.

    ![Second Password](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/encoding-decoding-aoc2025-s1a4z7x0c3/CyberChef_-_Hoperation_Save_McSkidy_Second_Password.png)

    ><details><summary>Click for answer</summary>Itoldyoutochangeit!</details>

### Third Lock - Guard House

1.  What is the password for the third lock?

    Now we can login at the second lock with:

    Username: `Q2Fycm90SGVsbQ==`
    Password: `Itoldyoutochangeit!`

    ![Outer Wall](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/encoding-decoding-aoc2025-s1a4z7x0c3/CyberChef_-_Hoperation_Save_McSkidy_Outer_Wall.png)

    For the third lock, we see the guards name in the chat: 'LongEars' which encoded to base64 is 'TG9uZ0VhcnM='.

    This time there is no magic question and we have to ask the guard for the password. We can use 'Password please' encoded to Base64.

    ![Chat3](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/encoding-decoding-aoc2025-s1a4z7x0c3/CyberChef_-_Hoperation_Save_McSkidy_Chat3.png)

    From the level login logic, we can now see that the password is XOR encoded first and then encoded to base64. We need to reverse this to get the plaintext password.

    ![Level Logic3](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/encoding-decoding-aoc2025-s1a4z7x0c3/CyberChef_-_Hoperation_Save_McSkidy_Level_Logic3.png)

    We can also see the used key, which is 'cyberchef'.

    In Cyber using the from base64 recipe together with the key and a chained XOR recipe should give us the password.

    ![Third Password](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/encoding-decoding-aoc2025-s1a4z7x0c3/CyberChef_-_Hoperation_Save_McSkidy_Third_Password.png)

    ><details><summary>Click for answer</summary>BugsBunny</details>

### Fourth Lock - Inner Castle

1.  What is the password for the fourth lock?

    Now we can login at the third lock with:

    Username: `TG9uZ0VhcnM=`
    Password: `BugsBunny`

    ![Guard House](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/encoding-decoding-aoc2025-s1a4z7x0c3/CyberChef_-_Hoperation_Save_McSkidy_Guard_House.png)

    For the fourth lock, we see the guards name in the chat: 'Lenny' which encoded to base64 is 'TGVubnk='.

    Again, we ask the guard for the password encoded to Base64. Decoding its reply, doesn't realy look like Base64. The level login logic tells us why.

    ![Level Logic4](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/encoding-decoding-aoc2025-s1a4z7x0c3/CyberChef_-_Hoperation_Save_McSkidy_Level_Logic4.png)

    It seems to be hashed using md5. This cannot be reversed using CyberChef. But if it is a common word, it can be looked up using a tool such as '[Crackstation](https://crackstation.net/)'.

    ![Chat4](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/encoding-decoding-aoc2025-s1a4z7x0c3/CyberChef_-_Hoperation_Save_McSkidy_Chat4.png)

    ![Fourth Password](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/encoding-decoding-aoc2025-s1a4z7x0c3/CyberChef_-_Hoperation_Save_McSkidy_Fourth_Password.png)

    ><details><summary>Click for answer</summary>passw0rd1</details>

### Fifth Lock - Prison Tower

1.  What is the password for the fifth lock?

    Now we can login at the fourth lock with:

    Username: `TGVubnk=`
    Password: `passw0rd1`

    ![Inner Castle](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/encoding-decoding-aoc2025-s1a4z7x0c3/CyberChef_-_Hoperation_Save_McSkidy_Inner_Castle.png)

    For the fifth lock, we see the guards name in the chat: 'Carl' which encoded to base64 is 'Q2FybA=='.

    Again, we ask the guard for the password encoded to Base64. Decoding its reply, doesn't realy look like only Base64 either. The level login logic reveals us what has been done.

    ![Level Logic5](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/encoding-decoding-aoc2025-s1a4z7x0c3/CyberChef_-_Hoperation_Save_McSkidy_Level_Logic5.png)

    This time there are multiple options depending on the 'recipeID' variabel. In the network tab, we can see what this value is: "R3".

    ![Question5](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/encoding-decoding-aoc2025-s1a4z7x0c3/CyberChef_-_Hoperation_Save_McSkidy_Question5.png)

    This means we should look at the option where: `case "R3"`. 

    We see it is first encoded using XOR with key 'cyberchef'. Then it is encoded to Base64 and finally encoded using a ROT13 cypher. We need to reverse these steps using CyberChef.

    ![Chat5](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/encoding-decoding-aoc2025-s1a4z7x0c3/CyberChef_-_Hoperation_Save_McSkidy_Chat5.png)

    ![Fifth Password](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/encoding-decoding-aoc2025-s1a4z7x0c3/CyberChef_-_Hoperation_Save_McSkidy_Fifth_Password.png)


    ><details><summary>Click for answer</summary>51rBr34chBl0ck3r</details>

2.  What is the retrieved flag?

    Now we can login at the fifth lock with:

    Username: `Q2FybA==`
    Password: `51rBr34chBl0ck3r`

    ![Prison Tower](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/encoding-decoding-aoc2025-s1a4z7x0c3/CyberChef_-_Hoperation_Save_McSkidy_Prison_Tower.png)

    After breaching all these gates, we are given our flag.

    ![Flag](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/encoding-decoding-aoc2025-s1a4z7x0c3/CyberChef_-_Hoperation_Save_McSkidy_Flag.png)

    ><details><summary>Click for answer</summary>THM{M3D13V4L_D3C0D3R_4D3P7}</details>
