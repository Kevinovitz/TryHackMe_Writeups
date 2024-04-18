![Risk Management Banner](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/seriskmanagement/Risk_Management_Banner.png)

<p align="center">
   <img src="https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/seriskmanagement/Risk_Management_Cover.png" alt="Risk Management Logo">
</p>

# Risk Management

This guide contains the answer and steps necessary to get to them for the [Risk Management](https://tryhackme.com/room/seriskmanagement) room.

## Table of contents

- [Introduction](#introduction)
- [Basic Terminology](#basic-terminology)
- [Risk Assessment Methodologies](#risk-assessment-methodologies)
- [Respond to Risk](#respond-to-risk)
- [Monitor Risk](#monitor-risk)
- [Putting It All Together](#putting-it-all-together)

### Introduction

1. You have registered to attend a local workshop about offensive cyber security tools. The workshop requires the attendees to bring their own laptops. This workshop is critical for you, and you want to get the most out of it. Your laptop is good and reliable; however, as with any electronic device, there is always a chance, no matter how minuscule, that something might go wrong and it would fail.You decide to carry an extra laptop; if your main laptop fails, the second laptop will be ready. What would you call this response to risk?

   The answer to this question can be found in the text.

   ><details><summary>Click for answer</summary>Risk Reduction</details>

2. You think your laptop has never failed before, and the chances of failing now are too slim. You decide not to take any extra actions. What do you call this response to risk?

   The answer to this question can be found in the text.

   ><details><summary>Click for answer</summary>Risk acceptance</details>

### Basic Terminology

1. What do you call the potential for a loss or an incident that may harm the confidentiality, integrity or availability of an organisation’s information assets?

   The answer to this question can be found in the text.

   ><details><summary>Click for answer</summary>Risk</details>

2. What do you call a weakness an attacker could exploit to gain unauthorised access to a system or data?

   The answer to this question can be found in the text.

   ><details><summary>Click for answer</summary>Vulnerability</details>

3. What do you consider a business laptop?

   The answer to this question can be found in the text.

   ><details><summary>Click for answer</summary>Asset</details>

4. Ransomware has become a lucrative business. From the perspective of legal business, how do you classify ransomware groups?

   The answer to this question can be found in the text.

   ><details><summary>Click for answer</summary>Threat</details>

### Risk Assessment Methodologies

1. What is the name of the risk assessment methodology developed by NIST?

   The answer to this question can be found in the text.

   ><details><summary>Click for answer</summary>NIST SP 800-30</details>

### Respond to Risk

1. Click on View Site. Decide whether each of the suggested safeguards (controls) is justified. Follow the instructions to retrieve the flag.

   For eacht safeguard we must calculate the ALE before and after implementation. Subtract them from each other as well as the cost of the safe guard to find out if the safeguard is justified.

   We will use 1 to notate values before implementation of the safeguard and 2 for after.

   $ALE1 = (AssetValue * EF1) * ARO1$

   $SafeguardValue = ALE1 - ALE2 - SafeguardCost$

   ![Respond 1](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/seriskmanagement/Risk_Management_Respond_1.png)

   $ALE1 = (2000 * 0,5) * 2$

   $ALE2 = (2000 * 0,1) * 2$

   $SafeguardValue = 2000 - 400 - 20 = 1580$

   The value is positive, so it is justified to implement.

   ![Respond 2](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/seriskmanagement/Risk_Management_Respond_2.png)

   $ALE1 = (10000 * 0,25) * 0,35$

   $ALE2 = (2000 * 0) * 0,35$

   $SafeguardValue = 875 - 0 - 400 = 475$

   The value is positive, so it is justified to implement.

   ![Respond 3](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/seriskmanagement/Risk_Management_Respond_3.png)

   $ALE1 = (2000 * 0,5) * 0,25$

   $ALE2 = (2000 * 0,1) * 0,5$

   $SafeguardValue = 250 - 100 - 1500 = 1350$

   The value is negative, so it is not justified to implement.

   ><details><summary>Click for answer</summary>THM{Excellent_Risk_Management}</details>

### Monitor Risk

1. You want to confirm whether the new policy enforcing laptop disk encryption is helping mitigate data breach risk. What is it that you are monitoring in this case?

   The answer to this question can be found in the text.

   ><details><summary>Click for answer</summary>Effectiveness</details>

2. You are keeping an eye on new regulations and laws. What is it that you are monitoring?

   The answer to this question can be found in the text.

   ><details><summary>Click for answer</summary>Compliance</details>

### Putting It All Together

1. Click on View Site and follow the instructions to retrieve the flag. Remember that your decision should be based on the value of the safeguard to the organisation, which is calculated as follows: ValueofSafeguard = ALEbeforeSafeguard − ALEafterSafeguard − AnnualCostSafeguard

   ![Together Screen 1](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/seriskmanagement/Risk_Management_Together_Screen_1.png)
   
   ![Together Control 1 Laptop](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/seriskmanagement/Risk_Management_Together_Control_1_Laptop.png)
   
   (2500 * 1) * 0,05

   (2500 * 0,06) *8* 0,05

   125 - 7,5 - 45 = 72,5

   The value is positive, so it is justified to implement.

   ![Together Screen 2](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/seriskmanagement/Risk_Management_Together_Screen_2.png)

   ![Together Control 2 Workstation](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/seriskmanagement/Risk_Management_Together_Control_2_Workstation.png)

   (3000 * 0,7) * 0,2

   (3000 * 0) * 0,2

   420 - 0 - 200 = 220

   The value is positive, so it is justified to implement.

   ![Together Control 2 Phone](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/seriskmanagement/Risk_Management_Together_Control_2_Phone.png)
   
   (1250 * 1) * 0,35

   (1250 * 0,4) * 0,35

   437,5 - 175 - 10 = 252,5

   The value is positive, so it is justified to implement.

   ![Together Screen 3](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/seriskmanagement/Risk_Management_Together_Screen_3.png)

   ![Together Control 3 Office](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/seriskmanagement/Risk_Management_Together_Control_3_Office.png)

   (20000 * 1) * 0,1

   (20000 * 0,15) * 0,1

   2000 - 300 - 750 = 950

   The value is positive, so it is justified to implement.

   ![Together Control 3 Workstation](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/seriskmanagement/Risk_Management_Together_Control_3_Workstation.png)

   (3000 * 0,1) * 0,05

   (3000 * 0) * 0,05

   15 - 0 - 250 = -235

   The value is negative, so it is not justified to implement.

   ![Together Control 3 Laptop](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/seriskmanagement/Risk_Management_Together_Control_3_Laptop.png)

   (2500 * 1) * 0,2

   (2500 * 0,24) * 0,2

   500 - 120 - 75 = 305

   The value is positive, so it is justified to implement.

   ![Together Control 3 Workstation 2](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/seriskmanagement/Risk_Management_Together_Control_3_Workstation_2.png)

   (3000 * 0,85) * 0,35

   (3000 * 0,05) * 0,35

   595 - 52,5 - 75 = 467,5

   The value is positive, so it is justified to implement.

   ><details><summary>Click for answer</summary>THM{OFFICE_RISK_MANAGED}</details>