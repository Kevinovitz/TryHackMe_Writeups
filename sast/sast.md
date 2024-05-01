![SAST Banner](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/sast/SAST_Banner.png)

<p align="center">
   <img src="https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/sast/SAST_Cover.png" alt="SAST Logo">
</p>

# SAST

This guide contains the answer and steps necessary to get to them for the [SAST](https://tryhackme.com/r/room/sast) room.

## Table of contents

- [Code Review](#code-review)
- [Manual Code Review](#manual-code-review)
- [Automated Code Review](#automated-code-review)
- [Rechecking our Application with SAST Tools](#rechecking-our-application-with-sast-tools)
- [SAST in the Development Cycle](#sast-in-the-development-cycle)

### Code Review

The answers to the following questions can be found in the text.

1. Are automated code reviews a substitute for manual reviewing? (yea/nay)

   ><details><summary>Click for answer</summary>Nay</details>

2. What type of code review will run faster? (Manual/Automated)

   ><details><summary>Click for answer</summary>Automated</details>

3. What type of code review will be more thorough? (Manual/Automated)

   ><details><summary>Click for answer</summary>Manual</details>

### Manual Code Review

1. Local File Inclusion (LFI) attacks are made possible by the misuse of one of the following functions in PHP: require() include() require_once() include_once(). Answer the following questions using `grep` to search for LFI vulnerabilities only on the.php files in the html/ directory of thesimple-webappproject.

2. Which of the mentioned functions is used in the project? (Include the parenthesis at the end of the function name)

   After navigating to `/home/ubuntu/Desktop/simple-webapp/html`, we can search for any reference to these functions in the files using `grep`.

   ```console
   grep -r -n --include \*.php 'require('
   grep -r -n --include \*.php 'include('
   grep -r -n --include \*.php 'require_once('
   grep -r -n --include \*.php 'include_once('
   ```

   MANUAL

   Looks like only one of the functions is present in the .php files.

   ><details><summary>Click for answer</summary>include()</details>

3. How many instances of the function found in question 2 exist in your project's code?

   This we can find in the previous image, by counting the instances found.

   ><details><summary>Click for answer</summary>9</details>

4. Only one of the function's instances is vulnerable to LFI. Remember that for LFI to be present, the attacker must be able to manipulate a part of what is sent to the vulnerable function. The vulnerable instance must contain some reference to a GET or POST parameter or other manipulable inputs.What file contains the vulnerable instance?

   Again from the previous image, we can see one instance that uses a GET or POST command.

   ><details><summary>Click for answer</summary>view.php</details>

5. What line in the file found on the previous question is vulnerable to LFI?

   The `grep` command we used displays the line on which this function is used.

   ><details><summary>Click for answer</summary>22</details>

### Automated Code Review

All of the answers for the question below can be found in the text.

1. Does SAST require a running instance of the application for analysis? (yea/nay)

   ><details><summary>Click for answer</summary>Nay</details>

2. What kind of analysis would likely flag dead code segments?

   ><details><summary>Click for answer</summary>Structural Analysis</details>

3. What kind of analysis would likely detect flaws in configuration files?

   ><details><summary>Click for answer</summary>Configuration Analysis</details>

4. What kind of analysis is similar to grepping the code in search of flaws?

   ><details><summary>Click for answer</summary>Semantics Analysis</details>

### Rechecking our Application with SAST Tools

1. What type of error occurs when the tool reports on a vulnerability that isn't present in the code?

   This can be found in the text.

   ><details><summary>Click for answer</summary>False Positive</details>

2. How many errors are reported after annotating the code as instructed in this task and re-running Psalm?

   First we need to add the piece of code into the `db.php` file, just before the `db_query` function.

   RECHECKING ADD

   Now we can re-run psalm and the number of error founds will be listed at the bottom.

   ```console
   ./vendor/bin/psalm --no-cache --taint-analysis
   ```

   RECHECKING ERRORS

   ><details><summary>Click for answer</summary>9</details>

### SAST in the Development Cycle

1. For this task's questions, we will analyse an old version ofReciPHP, a small open-source app. Before continuing, make sure to open thereciphp.code-workspaceicon on your desktop. This will open a VS Code workspace where the project is already loaded for you. VS Code will take around 3 minutes to load, so be patient.

2. How many problems in total are detected by Semgrep in this project?

   After opening the vscode workspace, we can see the number of errors in the window at the bottom.

   DEVELOPMENT

   ><details><summary>Click for answer</summary>27</details>

3. How many problems are detected in theshowrecipe.inc.phpfile?

   This number is reported in the left pane.

   ><details><summary>Click for answer</summary>8</details>

4. Open showrecipe.inc.php. There are two types of problems being reported by Semgrep in this file. One is identified as "tainted-sql-string" and refers to possible SQL injections.What other problem identifier is reported by Semgrep in this file? (Write the id reported by Semgrep)

   After opening the file, we can see two types listed at the bottom (in the previous image).

   ><details><summary>Click for answer</summary>echoed-request</details>

5. What type of vulnerability is associated with the problem identifier on the previous question?

   Hovering over said error, we are told what type of vulnerability this is related to.

   ><details><summary>Click for answer</summary>Cross-site scripting</details>

