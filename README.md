# Cherub
NOTE: Google API Keys are needed. Please choose the "download as JSON" option when creating your keys, and then rename the file "credentials.json" and put it in the same folder as the rest of this repository.

Cherub is an open-source Discord bot that pulls data from Discord servers and writes to Google Sheets.
Please note that this is not currently ready to be downloaded and used. It functions, but you'll need to create a credentials.json and setup.json file, and configure it correctly in order to make it work. A full usable release will be available soon

# Features
- Collects Discord messages with metadata
- Collects message counts and determines usage data

# Feature Plans
✔ Have the graphs actually embed within Discord (Google Sheets is a pain to work with)
- Improve data sorting to allow for more efficient data interpretation for other projects. 
      EX) If you were to use this data for a machine learning chatbot, differentiating between messages from #general and #bot-commands               would consume a considerable amount of time
✔ Setup wizard and documentation for installation and setup
X ~~Error code compilation, solutions, and other documentation~~
This is no longer necessary as the code has been sufficiently error tested and there is a setup wizard. I can add in error codes and               other documentation if enough people request it though

# Next Feature to be added:
Rewrite of the program to remove Google Sheets API, as it's request limit disables accurate logging.

# Setup Instructions
1. Download the latest version from releases
2. Create a Google API User and generate your keys as a JSON file. Rename the .json file "credentials.json"
3. Make a Discord Bot User and save the token somewhere
4. Run setup.exe, then discord-data-collection.exe
      * If you don't have a Google Sheets Graph URL yet, or you do not wish to have one, press enter when it asks for the URL, the program         will work. To make a Graph URL, create a graph with the data you'd like to be included in the graph, hover your mouse over the             graph, click the three dots, press share, ***deselect the rest of your spreadsheet***, and share the graph as an image. Make sure           it's not an interactive image, or it will not embed on Discord.
      * Alternatively, for experienced users you can configure setup.json manually, just define the variables "discordtoken" for the bot           token, "link" for the Graph URL, and "sheetname" for the sheet name.You can also run either setup or discord-data-collection from           their .py versions

# Social Media
- Patreon: https://patreon.com/jumpyvonvagabond
- Discord: https://discord.gg/calamari, username: @Jumpy♡#0150
- Twitter: @j_umpy
