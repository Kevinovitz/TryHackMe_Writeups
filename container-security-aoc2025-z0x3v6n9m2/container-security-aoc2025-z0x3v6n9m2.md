![Containers - DoorDasher's Demise Banner](https://tryhackme-images.s3.eu-west-1.amazonaws.com/room-icons/6228f0d4ca8e57005149c3e3-1762360735083)

<p align="center">
   <img src="https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/container-security-aoc2025-z0x3v6n9m2/Containers_-_DoorDasher's_Demise_Cover.png" alt="Containers - DoorDasher's Demise Logo">
</p>

# <img src="https://tryhackme-images.s3.amazonaws.com/room-icons/6228f0d4ca8e57005149c3e3-1762360425839" alt="image" style="vertical-align: middle;height: 50px;" /> Containers - DoorDasher's Demise | Advent of Cyber 2025 - Day 14

This guide contains the answer and steps necessary to get to them for the [Containers - DoorDasher's Demise](https://tryhackme.com/room/container-security-aoc2025-z0x3v6n9m2) room.

## Table of contents

- [Container Security](#container-security)

### Container Security

1.  What exact command lists running Docker containers?

    The answer to this question can be found in the text.

    ><details><summary>Click for answer</summary>docker ps</details>

2.  What file is used to define the instructions for building a Docker image?

    The answer to this question can be found in the text.

    ><details><summary>Click for answer</summary>dockerfile</details>

3.  What's the flag?

    We log into the `deployer` container by using:

    ```cmd
    docker exec -it deployer bash
    ```

    ![Deployer](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/container-security-aoc2025-z0x3v6n9m2/Containers_-_DoorDasher's_Demise_Deployer.png)

    Now we can look for our flag. There seems to something hidden in the root folder.

    ![Flag](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/container-security-aoc2025-z0x3v6n9m2/Containers_-_DoorDasher's_Demise_Flag.png)

    If we run the script found in the root folder we can restore the site.

    ![Restore](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/container-security-aoc2025-z0x3v6n9m2/Containers_-_DoorDasher's_Demise_Restore.png)

    ><details><summary>Click for answer</summary>THM{DOCKER_ESCAPE_SUCCESS}</details>

4.  Bonus Question: There is a secret code contained within the news site running on port 5002; this code also happens to be the password for the deployer user! They should definitely change their password. Can you find it?

    On the webpage served on port 5002, we can see a news article. There is some indication here to a multiple parts password hidden in the text.

    ![Password](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/container-security-aoc2025-z0x3v6n9m2/Containers_-_DoorDasher's_Demise_Password.png)

    ><details><summary>Click for answer</summary>DeployMaster2025!</details>

5.  Liked the content? We have plenty more where this came from! Try our [Container Vulnerabilities](https://tryhackme.com/room/containervulnerabilitiesDG) room.
