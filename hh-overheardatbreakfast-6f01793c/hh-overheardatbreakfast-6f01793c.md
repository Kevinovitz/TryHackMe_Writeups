![Overheard at Breakfast Banner](https://cdn-images.tryhackme.com/room-icons/5dbea226085ab6182a2ee0f7-1785251494686)

<p align="center">
   <img src="https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/hh-overheardatbreakfast-6f01793c/Overheard_at_Breakfast_Cover.png" alt="Overheard at Breakfast Logo">
</p>

# <img src="https://cdn-images.tryhackme.com/room-icons/5dbea226085ab6182a2ee0f7-1785251499374" alt="image" style="vertical-align: middle;height: 50px;" /> Overheard at Breakfast

This guide contains the answer and steps necessary to get to them for the [Overheard at Breakfast](https://tryhackme.com/room/hh-overheardatbreakfast-6f01793c) room.

## Table of contents

- [Task 1 - Hacker Holidays: Day 6](#task-1---hacker-holidays-day-6)

### Task 1 - Hacker Holidays: Day 6

1.  What is the flag?

    Looking through the conversation, one thing that pops out is the social media profile linking tool. Lets do some 'research' to find out what tool this is.

    ![Tool](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/hh-overheardatbreakfast-6f01793c/Overheard_at_Breakfast_Tool.png)

    Gravatar sounds exactly what we are after. We can use a page to identify our gravatar profile url if we know the profiles email address (which they so kindly provided for us).

    ![Search](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/hh-overheardatbreakfast-6f01793c/Overheard_at_Breakfast_Search.png)
    
    Looks like we found the hidden profile. Here we also find a string that might be our flag.

    ![Profile](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/hh-overheardatbreakfast-6f01793c/Overheard_at_Breakfast_Profile.png)

    This string is probably base64 encoded. Lets decode it to reveal our flag.
    
    ![Flag](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/hh-overheardatbreakfast-6f01793c/Overheard_at_Breakfast_Flag.png)

    ><details><summary>Click for answer</summary>THM{S3creT_Pr0fil3_H4s_b33n_Ident1fi3d}</details>