import json

token = input("Enter Discord Bot Token\n")
prefix = input("Enter Bot Prefix\n")
url = input("Enter Google Sheets Graph URL\n")
sheetname = input("Enter the name of the Google Sheet you wish to use, make sure it is shared with your Google Bot User\n")

data = {
    'prefix': prefix,
    'discordtoken': token,
    'link': url,
    'sheetname': sheetname
}
with open('setup.json', 'w') as f:
  json.dump(data, f)