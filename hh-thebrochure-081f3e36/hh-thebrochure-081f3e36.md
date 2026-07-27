![The Brochure Banner](https://cdn-images.tryhackme.com/room-icons/5dbea226085ab6182a2ee0f7-1784882148570)

<p align="center">
   <img src="https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/hh-thebrochure-081f3e36/The_Brochure_Cover.png" alt="The Brochure Logo">
</p>

# <img src="https://cdn-images.tryhackme.com/room-icons/5e9c5d0148cf664325c8a075-1784923108816" alt="image" style="vertical-align: middle;height: 50px;" /> The Brochure

This guide contains the answer and steps necessary to get to them for the [The Brochure](https://tryhackme.com/room/hh-thebrochure-081f3e36) room.

## Table of contents

- [Task 2 - Hacker Holidays: Day 0](#task-2---hacker-holidays-day-0)

### Task 2 - Hacker Holidays: Day 0

1.  What is the flag?

    First thing I tried after downloading the borchure image was checking for any hidden content.

    ```console
    file thebrochure.png
    exiftools thebrochure.png
    strings thebrochure.png
    ```

    None which returned anything. 

    I then continued to look at the image itself and noticed a mention of an Instagram account.

    Looking for this account only, gave me a hit.

    ![Instagram](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/hh-thebrochure-081f3e36/The_Brochure_Instragram.png)

    I looked through the posts, its comments, source page for hidden clues etc. Nothing.

    The other clue left behind on the brochure was something about Vera the concierge.

    Looking at some of the followers on the instragram account, we find one that might lead us to the hidden social media account of the concierge.

    This account has several post with short pieces of, likely, base64 encoded text.

    ![Vera](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/hh-thebrochure-081f3e36/The_Brochure_Vera.png)

    Combining these strings in cyber chef yields us our first flag!

    ![Flag](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/hh-thebrochure-081f3e36/The_Brochure_Flag.png)

    ><details><summary>Click for answer</summary>THM{V3r@s_aCC0unt_h4s_b33n_f0und!}</details>

