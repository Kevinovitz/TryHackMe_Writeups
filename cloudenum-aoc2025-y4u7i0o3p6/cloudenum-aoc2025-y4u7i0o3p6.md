![AWS Security - S3cret Santa Banner](https://tryhackme-images.s3.eu-west-1.amazonaws.com/room-icons/5ed5961c6276df568891c3ea-1764054644335)

<p align="center">
   <img src="https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/cloudenum-aoc2025-y4u7i0o3p6/AWS_Security_-_S3cret_Santa_Cover.png" alt="AWS Security - S3cret Santa Logo">
</p>

# <img src="https://tryhackme-images.s3.amazonaws.com/room-icons/5ed5961c6276df568891c3ea-1761886566945" alt="image" style="vertical-align: middle;height: 50px;" /> AWS Security - S3cret Santa | Advent of Cyber 2025 - Day 23

This guide contains the answer and steps necessary to get to them for the [AWS Security - S3cret Santa](https://tryhackme.com/room/cloudenum-aoc2025-y4u7i0o3p6) room.

## Table of contents

- [Introduction](#introduction)
- [IAM: Users, Roles, Groups and Policies](#iam-users-roles-groups-and-policies)
- [Practical: Enumerating a User's Permissions](#practical-enumerating-a-users-permissions)
- [Assuming Roles](#assuming-roles)
- [Grabbing a file from S3](#grabbing-a-file-from-s3)

### Introduction

1.  Run aws sts get-caller-identity. What is the number shown for the "Account" parameter?

    We will be running `aws sts get-caller-identity` to get the information about the configure user.

    ![User](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/cloudenum-aoc2025-y4u7i0o3p6/AWS_Security_-_S3cret_Santa_User.png)

    ><details><summary>Click for answer</summary>123456789012</details>

### IAM: Users, Roles, Groups and Policies

1.  What IAM component is used to describe the permissions to be assigned to a user or a group?

    The answer to this question can be found in the text.

    ><details><summary>Click for answer</summary>policy</details>

### Practical: Enumerating a User's Permissions

1.  What is the name of the policy assigned to sir.carrotbane?

    We can list the inline policies for his account using:

    ```cmd
    aws iam list-user-policies --user-name sir.carrotbane
    ```

    ![Policy](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/cloudenum-aoc2025-y4u7i0o3p6/AWS_Security_-_S3cret_Santa_Policy.png)

    ><details><summary>Click for answer</summary>SirCarrotbanePolicy</details>

### Assuming Roles

1.  Apart from GetObject and ListBucket, what other action can be taken by assuming the bucketmaster role?

    We need to see what action can be performed by the role 'bucketmaster'. Using the following command:

    ```cmd
    aws iam get-role-policy --policy-name BucketMasterPolicy --role-name bucketmaster
    ```

    ![Role](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/cloudenum-aoc2025-y4u7i0o3p6/AWS_Security_-_S3cret_Santa_Role.png)

    ><details><summary>Click for answer</summary>ListAllMyBuckets</details>

### Grabbing a file from S3

1.  What are the contents of the cloud_password.txt file?

    First, we need to assume the 'bucketmaster' role. This can be done using the following commands:

    ```cmd
    aws sts assume-role --role-arn arn:aws:iam::123456789012:role/bucketmaster --role-session-name TBFC

    export AWS_ACCESS_KEY_ID="ASIARZPUZDIKGOANAAGV"
    export AWS_SECRET_ACCESS_KEY="agHlyxjLjO73hsoieB4Txt0bM3aT7IpBsI/TjcdH"
    export AWS_SESSION_TOKEN="FQoGZXIvYXdzEBYaDie4xs35h+TC1csNaJQa1r0xD45kuAInHsDMyTGWu4pEOYgF0mUERVcyRAKwP9WjiPe5nxDyxOUwC9hFw83hJyO72quNSb3knuBNAAcyUkYP9DKyu2Z7SOWygKm8p+YEsNpKlprK4oo0gncd3nGCoALJ7YLJylUbIN5x8oHKAAZwhUhwqkSJpUghJMVxN6Ur611+b4r1fALMl0VcyNcgwVt0aDNa7J8HSXMykuIksT5+1Bl1xn5nz7aa7jWW+jnRFzJ4703dIpiIieQlhAWxJdSe04v59tUjWItUgHLV/JaFta1yQz3hyZ7UcxfSHC5kZKUkTbJmwcapgdZqyt0="

    aws sts get-caller-identity
    > Check what role we are using.
    ```

    ![Assume Role](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/cloudenum-aoc2025-y4u7i0o3p6/AWS_Security_-_S3cret_Santa_Assume_Role.png)

    Now we can list all available S3 bucket using:

    ```cmd
    aws s3api list-buckets
    ```

    ![Buckets](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/cloudenum-aoc2025-y4u7i0o3p6/AWS_Security_-_S3cret_Santa_Buckets.png)

    One of these buckets might contain some interesting information. Lets list the object in this secret bucket.

    ```cmd
    aws s3api list-objects --bucket easter-secrets-123145
    ```

    ![Objects](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/cloudenum-aoc2025-y4u7i0o3p6/AWS_Security_-_S3cret_Santa_Objects.png)

    The should download the password file and see what is inside.

    ```cmd
    aws s3api get-object --bucket easter-secrets-123145 --key cloud_password.txt cloud_password.txt

    cat cloud_password.txt
    ```

    ![Flag](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/cloudenum-aoc2025-y4u7i0o3p6/AWS_Security_-_S3cret_Santa_Flag.png)

    ><details><summary>Click for answer</summary>THM{more_like_sir_cloudbane}</details>
