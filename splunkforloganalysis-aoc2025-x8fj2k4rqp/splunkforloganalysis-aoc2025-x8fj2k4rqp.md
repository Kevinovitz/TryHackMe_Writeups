![Splunk Basics - Did you SIEM? Banner](https://tryhackme-images.s3.eu-west-1.amazonaws.com/room-icons/5f9c7574e201fe31dad228fc-1762631417696)

<p align="center">
   <img src="https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/splunkforloganalysis-aoc2025-x8fj2k4rqp/Splunk_Basics_-_Did_you_SIEM_Cover.png" alt="Splunk Basics - Did you SIEM? Logo">
</p>

# <img src="https://tryhackme-images.s3.amazonaws.com/room-icons/5e8dd9a4a45e18443162feab-1762518888961" alt="image" style="vertical-align: middle;height: 50px;" /> Splunk Basics - Did you SIEM? | Advent of Cyber 2025 - Day 3

This guide contains the answer and steps necessary to get to them for the [Splunk Basics - Did you SIEM?](https://tryhackme.com/room/splunkforloganalysis-aoc2025-x8fj2k4rqp) room.

## Table of contents

- [Log Analysis with Splunk](#log-analysis-with-splunk)

### Log Analysis with Splunk

1.  What is the attacker IP found attacking and compromising the web server?

    First we filter the correct dataset:

    ```cmd
    index=main sourcetype="web_traffic"
    ```

    If we now look at the IP addresses found, we see there is one standing out in numbers from the rest. This might be our attacker.

    ![Ip](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/splunkforloganalysis-aoc2025-x8fj2k4rqp/Splunk_Basics_-_Did_you_SIEM_Ip.png)

    ><details><summary>Click for answer</summary>198.51.100.55</details>

2.  Which day was the peak traffic in the logs? (Format: YYYY-MM-DD)

    We can show a time chart of events and sort them by the amount.

    ```cmd
    index=main sourcetype="web_traffic" 
    timechart span=1d count 
    sort by count 
    reverse
    ```

    ![Day](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/splunkforloganalysis-aoc2025-x8fj2k4rqp/Splunk_Basics_-_Did_you_SIEM_Day.png)

    ><details><summary>Click for answer</summary>2025-10-12</details>

3.  What is the count of Havij user_agent events found in the logs?

    We can either click on the user_agent field on the left or we can filter the dataset using:

    ```cmd
    user_agent="*Havij*
    ```

    ![Useragent](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/splunkforloganalysis-aoc2025-x8fj2k4rqp/Splunk_Basics_-_Did_you_SIEM_Useragent.png)

    ><details><summary>Click for answer</summary>993</details>

4.  How many path traversal attempts to access sensitive files on the server were observed?

    To look for path traversal attempts, we can look at logs where the attackers used ".." in the url. We also narrow down on our previously found attacker IP.

    ```cmd
    index=main sourcetype="web_traffic" client_ip="198.51.100.55" AND path="*..*"
    ```

    ![Path](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/splunkforloganalysis-aoc2025-x8fj2k4rqp/Splunk_Basics_-_Did_you_SIEM_Path.png)

    ><details><summary>Click for answer</summary>658</details>

5.  Examine the firewall logs. How many bytes were transferred to the C2 server IP from the compromised web server?



    ><details><summary>Click for answer</summary></details>

6.  If you enjoyed today's room, check out theIncident Handling With Splunkroom to learn more about analyzing logs with Splunk.
