![The Game Banner](https://cdn-images.tryhackme.com/room-icons/62ff64c3c859dc0042b2b9f6-1741182038652)

<p align="center">
   <img src="https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/hfb1thegame/The_Game_Cover.png" alt="The Game Logo">
</p>

# <img src="https://cdn-images.tryhackme.com/room-icons/78f10e9c93abc65cba953f3873bf514bf6e343597fbd9d6524a9543a1ec631ea.618b3fa52f0acc0061fb0172-1747849942798" alt="image" style="vertical-align: middle;height: 50px;" /> The Game

This guide contains the answer and steps necessary to get to them for the [The Game](https://tryhackme.com/room/hfb1thegame) room.

## Table of contents

- [Task 1 - The Game](#task-1---the-game)

### Task 1 - The Game

1.  What is the flag?

    I first tried opening the executable to see what this would give us (in a sandbox environment of course). This didn't give us anything unfortunately.

    ![Program](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/hfb1thegame/The_Game_Program.png)

    Next I tried opening the executable in a hex editor. Here I tried looking from any text fragments resembling the flag (e.g., "THM").

    ![Flag](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/hfb1thegame/The_Game_Flag.png)

    ><details><summary>Click for answer</summary>THM{I_CAN_READ_IT_ALL}</details>
