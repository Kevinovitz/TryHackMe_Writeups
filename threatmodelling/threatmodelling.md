![Threat Modelling Banner](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/threatmodelling/Threat_Modelling_Banner.png)

<p align="center">
   <img src="https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/threatmodelling/Threat_Modelling_Cover.png" alt="Threat Modelling Logo">
</p>

# Threat Modelling

This guide contains the answer and steps necessary to get to them for the [Threat Modelling](https://tryhackme.com/room/threatmodelling) room.

## Table of contents

- [Threat Modelling Overview](#threat-modelling-overview)
- [Modelling with MITRE ATT&CK](#modelling-with-mitre-att&ck)
- [Mapping with ATT&CK Navigator](#mapping-with-att&ck-navigator)
- [DREAD Framework](#dread-framework)
- [STRIDE Framework](#stride-framework)
- [PASTA Framework](#pasta-framework)

### Threat Modelling Overview

1. What is a weakness or flaw in a system, application, or process that can be exploited by a threat?

   The answer can be found in the text.

   ><details><summary>Click for answer</summary>Vulnerability</details>

2. Based on the provided high-level methodology, what is the process of developing diagrams to visualise the organisation's architecture and dependencies?

   The answer can be found in the text.

   ><details><summary>Click for answer</summary>Asset identification</details>

3. What diagram describes and analyses potential threats against a system or application?

   The answer can be found in the text.

   ><details><summary>Click for answer</summary>Attack tree</details>

### Modelling with MITRE ATT&CK

1. What is the technique ID of "Exploit Public-Facing Application"?

   After opening the link to the "Exploit Public Facing Applications" technique, we can see the number in the details pane.

   ![Mitre Technique](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/threatmodelling/Threat_Modelling_Mitre_Technique.png)

   ><details><summary>Click for answer</summary>T1190</details>

2. Under what tactic does this technique belong?

   On the same page, we can find which tactis this technique belongs to.

   ><details><summary>Click for answer</summary>Initial Access</details>

### Mapping with ATT&CK Navigator

1. How many MITRE ATT&CK techniques are attributed to APT33?

   After creating a new enterprise layer, use the search function to search for APT33. Then select all techniques associated with them. You can also click view to go the the MITRE page about this group. However, new techinques may have been added which gives a wrong total. Instead look at the amount of selected techniques in the top bar.

   ![Mitre Apt33](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/threatmodelling/Threat_Modelling_Mitre_Apt33.png)

   ><details><summary>Click for answer</summary>31</details>

2. Upon applying the IaaS platform filter, how many techniques are under the Discovery tactic?

   Close the search field and open the filter field. Here deselect everything except for IaaS. Now we can see how many techniques are left under the Discovery Technique.

   ![Mitre Iaas](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/threatmodelling/Threat_Modelling_Mitre_Iaas.png)

   ><details><summary>Click for answer</summary>13</details>

### DREAD Framework

1. What DREAD component assesses the potential harm from successfully exploiting a vulnerability?

   The answer can be found in the text.

   ><details><summary>Click for answer</summary>Damage</details>

2. What DREAD component evaluates how others can easily find and identify the vulnerability?

   The answer can be found in the text.

   ><details><summary>Click for answer</summary>Discoverability</details>

3. Which DREAD component considers the number of impacted users when a vulnerability is exploited?

   The answer can be found in the text.

   ><details><summary>Click for answer</summary>Affected Users</details>

### STRIDE Framework

1. What foundational information security concept does the STRIDE framework build upon?

   The answer can be found in the text.

   ><details><summary>Click for answer</summary>CIA Triad</details>

2. What policy does Information Disclosure violate?

   The answer can be found in the text.

   ><details><summary>Click for answer</summary>Confidentiality</details>

3. Which STRIDE component involves unauthorised modification or manipulation of data?

   The answer can be found in the text.

   ><details><summary>Click for answer</summary>Tampering</details>

4. Which STRIDE component refers to the disruption of the system's availability?

   The answer can be found in the text.

   ><details><summary>Click for answer</summary>Denial of Service</details>

5. Provide the flag for the simulated threat modelling exercise.

   After opening the site, we click on the door to begin.
   
   ![Stride Game](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/threatmodelling/Threat_Modelling_Stride_Game.png)

   After going through all required departments (skipping the CEO room and cafeteria), we need to answer some questions for the report.

   Most of the answers can be found in the text above.
   
   ![Stride Q1](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/threatmodelling/Threat_Modelling_Stride_Q1.png)

   ![Stride Q2](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/threatmodelling/Threat_Modelling_Stride_Q2.png)

   ![Stride Q3](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/threatmodelling/Threat_Modelling_Stride_Q3.png)

   ![Stride Q4](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/threatmodelling/Threat_Modelling_Stride_Q4.png)

   If we answered everything correctly, we are given the flag!

   ![Stride Flag](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/threatmodelling/Threat_Modelling_Stride_Flag.png)

   ><details><summary>Click for answer</summary>THM{m0d3ll1ng_w1th_STR1D3}</details>

### PASTA Framework

1. In which step of the framework do you break down the system into its components?

   The answer can be found in the text.

   ><details><summary>Click for answer</summary>Decompose the application</details>

2. During which step of thePASTAframework do you simulate potential attack scenarios?

   The answer can be found in the text.

   ><details><summary>Click for answer</summary>Analyse the attacks</details>

3. In which step of thePASTAframework do you create an inventory of assets?

   The answer can be found in the text.

   ><details><summary>Click for answer</summary>Define the Technical Scope</details>

4. Provide the flag for the simulated threat modelling exercise.

   After opening the site we are given a task. 

   ![Pasta G1](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/threatmodelling/Threat_Modelling_Pasta_G1.png)

   For this we need to head to the Strategic Planning room.

   ![Pasta G2](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/threatmodelling/Threat_Modelling_Pasta_G2.png)

   For this we need to head to the System Architecture room.

   ![Pasta G3](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/threatmodelling/Threat_Modelling_Pasta_G3.png)

   For this we need to head to the Software Development room.

   ![Pasta G4](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/threatmodelling/Threat_Modelling_Pasta_G4.png)

   For this we need to head to the Information Security room.

   ![Pasta G5](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/threatmodelling/Threat_Modelling_Pasta_G5.png)

   For this we need to head to the Strategic Planning room.

   After going through all required departments (skipping the CEO room and cafeteria), we need to answer some questions for the report.

   Pay close attention to what has been said by the departments.

   ![Pasta Q1](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/threatmodelling/Threat_Modelling_Pasta_Q1.png)

   ![Pasta Q2](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/threatmodelling/Threat_Modelling_Pasta_Q2.png)

   ![Pasta Q3](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/threatmodelling/Threat_Modelling_Pasta_Q3.png)

   ![Pasta Q4](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/threatmodelling/Threat_Modelling_Pasta_Q4.png)

   ![Pasta Q5](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/threatmodelling/Threat_Modelling_Pasta_Q5.png)

   ![Pasta Q6](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/threatmodelling/Threat_Modelling_Pasta_Q6.png)

   ![Pasta Q7](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/threatmodelling/Threat_Modelling_Pasta_Q7.png)

   If we answered everything correctly, we are given the flag!

   ![Pasta Flag](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/threatmodelling/Threat_Modelling_Pasta_Flag.png)

   ><details><summary>Click for answer</summary>THM{c00k1ng_thr34ts_w_P4ST4}</details>