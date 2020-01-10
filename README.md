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
- Setup wizard and documentation for installation and setup
- Error code compilation, solution, and other documentation

# Next Feature to be added:
Setup Wizard. The setup wizard shouldn't take long to complete, it'll just be irritating to update it every time I make a new release, so I'm going to try to finalize most customizable options and then configure a setup wizard.
