![Towel on the Sunbed Banner](https://cdn-images.tryhackme.com/room-icons/5dbea226085ab6182a2ee0f7-1785251659750)

<p align="center">
   <img src="https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/hh-towelonthesunbed-61271709/Towel_on_the_Sunbed_Cover.png" alt="Towel on the Sunbed Logo">
</p>

# <img src="https://cdn-images.tryhackme.com/room-icons/5dbea226085ab6182a2ee0f7-1785251667401" alt="image" style="vertical-align: middle;height: 50px;" /> Towel on the Sunbed

This guide contains the answer and steps necessary to get to them for the [Towel on the Sunbed](https://tryhackme.com/room/hh-towelonthesunbed-61271709) room.

<h2>Table of contents</h2>

- [Task 1 - Hacker Holidays: Day 8](#task-1---hacker-holidays-day-8)

### Task 1 - Hacker Holidays: Day 8

1.  What is the flag?

    Judging from the challenge description, we are looking at a "race condition" exploit. Meaning if we can make multiple request in rapid enough succession, the server might not properly handle them and process them all.

    If we go the the machine ip and port listed, we are greeted with a login page.

    ![Login](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/hh-towelonthesunbed-61271709/Towel_on_the_Sunbed_Login.png)

    Lets create a new account to see what we are working with.

    We can claim our free Ponze on this page and we need 150 to access the vault. After claiming we get 50, but we cannot claim anymore today.

    ![Claim](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/hh-towelonthesunbed-61271709/Towel_on_the_Sunbed_Claim.png)

    Unfortunately, we can't exploit the race condition anymore, because it simply returns an error.

    So we create another account and try again. This time we use Burpsuite to capture the request and block it from executing in our browser.

    ![Capture](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/hh-towelonthesunbed-61271709/Towel_on_the_Sunbed_Capture.png)

    Now that the request is captured, drop the actual request and send it to burpsuite repeater.

    Add this tab to a new group and duplicate the request a few times. 10 should be enough to test.

    ![Duplicate](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/hh-towelonthesunbed-61271709/Towel_on_the_Sunbed_Duplicate.png)

    Make sure to enable 'last-byte' sync in the send settings.

    ![Settings](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/hh-towelonthesunbed-61271709/Towel_on_the_Sunbed_Settings.png)

    Now we the requests. From the response window, we can see we actually got more than one claim. So the race condition was used successfully. From the history, we can see that not all requests were accepted.

    ![Reward](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/hh-towelonthesunbed-61271709/Towel_on_the_Sunbed_Reward.png)

    After refreshing the page, we see we now have access to the vault!
    
    ![Vault](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/hh-towelonthesunbed-61271709/Towel_on_the_Sunbed_Vault.png)

    ><details><summary>Click for answer</summary>THM{t0w3l_0n_th3_sunb3d_d0ubl3_sp3nt}</details>
