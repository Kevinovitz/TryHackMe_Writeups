![C2 Detection - Command & Carol Banner](https://tryhackme-images.s3.eu-west-1.amazonaws.com/room-icons/66c44fd9733427ea1181ad58-1766058806245)

<p align="center">
   <img src="https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/detecting-c2-with-rita-aoc2025-m9n2b5v8c1/C2_Detection_-_Command_%26_Carol_Cover.png" alt="C2 Detection - Command & Carol Logo">
</p>

# <img src="https://tryhackme-images.s3.amazonaws.com/room-icons/66c44fd9733427ea1181ad58-1761823947148" alt="image" style="vertical-align: middle;height: 50px;" /> C2 Detection - Command & Carol | Advent of Cyber 2025 - Day 22

This guide contains the answer and steps necessary to get to them for the [C2 Detection - Command & Carol](https://tryhackme.com/room/detecting-c2-with-rita-aoc2025-m9n2b5v8c1) room.

## Table of contents

- [Detecting C2 with RITA](#detecting-c2-with-rita)

### Detecting C2 with RITA

1.  How many hosts are communicating with malhare.net?

    First we need to prepare the logs for `rita` to analyze. This will be done using `zeek`.

    ```cmd
    zeek readpcap pcaps/rita_challenge.pcap  zeek_logs/rita_challenge
    ```

    We can now verify that the logs have been created.

    ![Preparation](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/detecting-c2-with-rita-aoc2025-m9n2b5v8c1/C2_Detection_-_Command_%26_Carol_Preparation.png)

    Now we import these logs into `rita`:

    ```cmd
    rita import --logs zeek_logs/rita_challenge/ --database ritachallenge
    ```

    ![Import](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/detecting-c2-with-rita-aoc2025-m9n2b5v8c1/C2_Detection_-_Command_%26_Carol_Import.png)

    And then we can run `rita` to analyze the logs.

    ```cmd
    rita view ritachallenge
    ```

    ![Dashboard](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/detecting-c2-with-rita-aoc2025-m9n2b5v8c1/C2_Detection_-_Command_%26_Carol_Dashboard.png)

    In the list we can see several hosts that er communicating with 'rabbithole.malhare.net'.

    ><details><summary>Click for answer</summary>6</details>

2.  Which Threat Modifier tells us the number of hosts communicating to a certain destination?

    Of these two modifiers, one states when it was first seen.

    ><details><summary>Click for answer</summary>prevalence</details>

3.  What is the highest number of connections to rabbithole.malhare.net?

    Looking through the entries with destination 'rabbithole.malhare.net', we can see on the right which one has the highest 'connection count'.

    ![Connections](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/detecting-c2-with-rita-aoc2025-m9n2b5v8c1/C2_Detection_-_Command_%26_Carol_Connections.png)

    ><details><summary>Click for answer</summary>40</details>

4.  Which search filter would you use to search for all entries that communicate to rabbithole.malhare.net with a beacon score greater than 70% and sorted by connection duration (descending)?

    We can use '?' in the search bar (after using '/') to find help if needed. We can simply add another search term with a space after our first one.
    
    To search for something greater than, we must use: `column:>value`. And sorting can be done using: `sort:column-order`.

    ![Sort](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/detecting-c2-with-rita-aoc2025-m9n2b5v8c1/C2_Detection_-_Command_%26_Carol_Sort.png)

    ><details><summary>Click for answer</summary>dst:rabbithole.malhare.net beacon:>70 sort:duration-desc</details>

5.  Which port did the host 10.0.0.13 use to connect to rabbithole.malhare.net?

    We don't need to filter the list as we don't have that many entries, but if we needed to, we could do so with:

    ```cmd
    src:10.0.0.13 dst:rabbithole.malhare.net
    ```

    The entry shows us the port used in the details pane.

    ![Port](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/detecting-c2-with-rita-aoc2025-m9n2b5v8c1/C2_Detection_-_Command_%26_Carol_Port.png)

    ><details><summary>Click for answer</summary>80</details>
