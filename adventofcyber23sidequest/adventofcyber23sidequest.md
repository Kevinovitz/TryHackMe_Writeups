![Advent of Cyber '23 Side Quest Banner](https://tryhackme-images.s3.amazonaws.com/user-uploads/6093e17fa004d20049b6933e/room-content/8d1eef4732f7fc206539fb68abdabc5d.svg)

<p align="center">
   <img src="https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber23sidequest/Advent_of_Cyber_23_Side_Quest_Cover.png" alt="Advent of Cyber '23 Side Quest Logo">
</p>

# Advent of Cyber '23 Side Quest

This guide contains the answer and steps necessary to get to them for the [Advent of Cyber '23 Side Quest](https://tryhackme.com/room/adventofcyber23sidequest) room.

## Table of contents

- [Flag submissions](#flag_submissions)
- [The Key You get this one for free!](#the_key_you_get_this_one_for_free)

### Flag submissions

1. Side Quest Challenge 1 Flag 

   The key has been split into four parts. There of these must be found in TryHackMe's socials. These can be found [here](https://tryhackme.com/room/adventofcyber2023) in task 3.
   
   The first part can be found on their Twitter page.
   
   ![Key1 Part1](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber23sidequest/Aoc_Side_Quests_Key1_Part1.png)
   
   The second part can be found on their Discord server in the aoc-2023-side-quest channel. Luckily for us, it has been pinned.

   ![Key1 Part2 2](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber23sidequest/Aoc_Side_Quests_Key1_Part2_2.png)

   ![Key1 Part2 1](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber23sidequest/Aoc_Side_Quests_Key1_Part2_1.png)
   
   The third part can be found on their LinkedIn page.

   ![Key1 Part3](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber23sidequest/Aoc_Side_Quests_Key1_Part3.png)
   
   The fourth and final part has been given to us in task 5 of this room.
   
   ![Key1 Part4](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber23sidequest/Aoc_Side_Quests_Key1_Part4.png)
   
   Now we can combine these snippets into 1 QR code with the site on task 5.
   
   ![Key1 Link](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber23sidequest/Aoc_Side_Quests_Key1_Link.png)
   
   To get our flag we must complete the room.

   ><details><summary>Click for answer</summary>1-1f9548f131522e85ea30e801dfd9b1a4e526003f9e83301faad85e6154ef2834</details>

2. Side Quest Challenge 2 Flag 

   The second key can be found in the machine of day 6 as we can read from the final question.
   
   Start the machine and the game when it is loaded.
   
   ![Key2 Game Intro](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber23sidequest/Aoc_Side_Quests_Key2_Game_Intro.png)
   
   We need to find a glitch that will give us the key we are looking for. 
   
   At first I tried to see if there are any openings in the edges where I could get through but got no luck.
   
   The only other thing we really can do is change our name and with it the memory values of the game.
   
   Lets check the shop and see what we buy. Maybe we have to look at the stuff we can't buy/isn't listed. This can be done by changing our name to have our inventory contain all possible characters or we can try them in the shop.
   
   A is not listed which we would expect, the other correct IDs are E and F. These two are out of stock.
   
   ![Key2 Shop A](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber23sidequest/Aoc_Side_Quests_Key2_Shop_A.png)
   
   However, ID A tells us we dont' have enough money. Which is weird, since we have a lot.
   
   ![Key2 Shop E](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber23sidequest/Aoc_Side_Quests_Key2_Shop_E.png)
   
   Lets try to add these items manually using the name switcher.
   
   ![Key2 Name Test](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber23sidequest/Aoc_Side_Quests_Key2_Name_Test.png)
   
   Apparently A is some sort of yeti token, E is a blue nutcracker, and F is a TryHackMe ball.
   
   ![Key2 Inventory Test](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber23sidequest/Aoc_Side_Quests_Key2_Inventory_Test.png)
   
   A is of interest as we could have bought it with money. Checking the shopkeeper again, we are told we don't have the real one. Which we can indeed buy.

   ![Key2 Shop Fake](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber23sidequest/Aoc_Side_Quests_Key2_Shop_Fake.png)
   
   We need more money. The most money we can get is probably by using the last letter 'z' four times.
   
   Lets change our name so our coin count becomes 'zzzz'.
   
   ![Key2 Name Money](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber23sidequest/Aoc_Side_Quests_Key2_Name_Money.png)
   
   Lets see if we can buy the real token this time.
   
   Use ID A to buy the unlisted token.
   
   ![Key2 Inventory Token](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber23sidequest/Aoc_Side_Quests_Key2_Inventory_Token.png)
   
   Success!
   
   We also see a glitch appear. The Ghost of the Christmas Glitch!
   
   The glitch sees we have the real token and has a riddle for us.
   
   ![Key2 Glitch Text 1](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber23sidequest/Aoc_Side_Quests_Key2_Glitch_Text_1.png)
   
   ![Key2 Glitch Text 2](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber23sidequest/Aoc_Side_Quests_Key2_Glitch_Text_2.png)
   
   ![Key2 Glitch Text 3](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber23sidequest/Aoc_Side_Quests_Key2_Glitch_Text_3.png)
   
   ![Key2 Glitch Text 4](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber23sidequest/Aoc_Side_Quests_Key2_Glitch_Text_4.png)
   
   ![Key2 Glitch Text 5](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber23sidequest/Aoc_Side_Quests_Key2_Glitch_Text_5.png)
   
   Looks like there are 4 conditions we must meet.
   
   - Our name must be: Snowball
   - Our coins count must be 31337
   - The shopkeeper must be named: MIDAS
   - The name switcher must be named: TED
   
   We can't do all this at once, since we need a null character at the end of each variable.
   
   First we must get more coins to change our name. Then we name the name switcher 'Ted' using `My name here1234123412341234Ted`.
   
   ![Key2 Memory Ted](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber23sidequest/Aoc_Side_Quests_Key2_Memory_Ted.png)
   
   Then we do the same with the shopkeeper using `My name here1234Midas`.
   
   ![Key2 Memory Midas](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber23sidequest/Aoc_Side_Quests_Key2_Memory_Midas.png)
   
   We need 31337 coins. Lets convert this into hexadecimal and then to text (keep in mind the game is using little-endian notation).
   
   ![Key2 Conversion Coins](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber23sidequest/Aoc_Side_Quests_Key2_Conversion_Coins.png)
   
   However, we still need to change our own name afterwards, decreasing our coin count.
   
   So we must add and extra 8 coins, since 'Snowball' consists of 8 characters (31345).
   
   ![Key2 Conversion Coins 2](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber23sidequest/Aoc_Side_Quests_Key2_Conversion_Coins_2.png)
   
   This gives us a value of 'qz'.
   
   First change the last digit of the coin counter to a null value and then to 'qz'.
   
   ```cmd
   My name here123
   My name hereqz
   ```
   
   ![Key2 Memory Coins](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber23sidequest/Aoc_Side_Quests_Key2_Memory_Coins.png)
   
   Finally, we change our characters name to 'Snowball'.
   
   ![Key2 Memory Name](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber23sidequest/Aoc_Side_Quests_Key2_Memory_Name.png)
   
   All condition are met. Now we must input some secret code. I have no idea what it is, but we can look it up only.
   
   ![Key2 Secret Code](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber23sidequest/Aoc_Side_Quests_Key2_Secret_Code.png)
   
   It seems to be a cheat code for the game Contra.
   
   Back in the game we input the cheat code omitting 'start'.
   
   Everything starts to glitch out even more and we stumble upon the yeti who has a message for us.
   
   ![Key2 Link.gif](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/adventofcyber23sidequest/Aoc_Side_Quests_Key2_Link.gif)
   
   To get our flag we must complete the room.
   
   ><details><summary>Click for answer</summary></details>

3. Side Quest Challenge 3 Flag 



   ><details><summary>Click for answer</summary></details>

4. Side Quest Challenge 4 Flag 

   

   ><details><summary>Click for answer</summary></details>
   
### The Key You get this one for free!

1. How many QR code pieces was the Challenge 1 Key divided into?  

   We get the last piece of the first key in this task. This mean we now have four pieces to make up our first QR code.
   
   On the site provided to us in this task, we can combine the pieces into one code and get the link to the first challenge.

   ><details><summary>Click for answer</summary>4</details>
