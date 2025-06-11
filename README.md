# ERNR-randomizer-discordbot
Discordbot for getting random classes and boss for Elden Ring Night Reign

**How to get started**:

  1.Install Python and discord.py.
    https://www.python.org/downloads/release/python-3100/
    You can select, for example, the Windows installer (64-Bit) if that matches your system, download it, run the installer and follow the instructions there.
    Make sure you know the path to your python.exe to use it in command line later (/PATH/TO/YOUR/python.exe).

  2.Clone this repository.
    
  3.Install dependencies from requirements.txt.
    or just in command line /PATH/TO/YOUR/python.exe -m pip install discord 

**How to get a Discord bot token and enable intents**:
  log in to https://discord.com/developers/
    New Application
      Give it a name like "ERNR randomizer" and create
      From the left side of the page, open the "Bot" page
        You can set the bot public and set the "Message content intent" True
        ![image](https://github.com/user-attachments/assets/9ff73244-6b2e-4b48-aec3-a7dcfdb80452)
        Get the TOKEN from Bot page as well, by pressing the Reset Token -button. 
        **You need to add the TOKEN  to the randomiser_bot.py line 4** (change the DISCORD TOKEN to match your token):
        TOKEN = "DISCORD TOKEN"  # TODO Set your discord token here
        ![image](https://github.com/user-attachments/assets/58539c28-8988-4271-9e3e-786211fd4075)

        Save changes

**How to get a channel ID**:

  In your Discord settings, go to the "Advanced" page at the bottom of the settings list and enable the Developer mode.
  After that, you can right click a channel in you Discord server and see the "Copy channel ID" at the bottom. 
  **You need to add the channel ID  to the randomiser_bot.py line 5** (change the 1234567890 to match the channel ID):
        CHANNEL_ID = 1234567890  # TODO Set your discord channel ID here

**How to run the bot**:

  After that, you can run the bot from command line with: /PATH/TO/YOUR/python.exe randomiser_bot.py

**How to invite the bot to a server**:
  In discord.com/developers/ select your application and from the left side of the page open the OAuth2 page. 
  Under OAuth2 URL Generator select the bot
  ![image](https://github.com/user-attachments/assets/551dfbd5-014b-4cea-aeea-c263a14600c4)
  Under BOT PERMISSIONS select Send Messages and Manage Messages, then you can see the generated URL at the bottom of the page. Copy it and paste it into your browser, open the page, and select the server you want to add the bot to. 
