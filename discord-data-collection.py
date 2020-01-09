#Setup
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd 
import discord
from discord.ext import commands
from discord.ext.commands import bot
import json
import datetime
import random
import os, sys, traceback, asyncio
from datetime import datetime
bot = commands.Bot(command_prefix=".")
scope = ['https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
gc = gspread.authorize(creds)
sh = gc.open("Calamari Cove Data Collection")
wks1 = sh.worksheet("Sheet1")
wks2 = sh.worksheet("Sheet2")
with open('setup.json') as f:
    data = json.loads(f.read())


@bot.event
async def on_ready():
    print("Bot connected")

@bot.command()
async def graph(ctx):
    if ctx.message.author.id == data["ownerid"]:
      #link = data["link"] + str(random.randint(100000000,20000000000)) 
      embed = discord.Embed(title = "Here ya go!", description = "A graph of activity", colour = discord.Colour.blue())
      embed.set_footer(text="Try again in a few minutes if it fails, Google can be slow sometimes")
      embed.set_image(url=data["link"])
      embed.set_thumbnail(url=data["link"])
      await ctx.channel.send(embed=embed)
    else:
        await ctx.channel.send("An error has occured. Either you're missing permissions or the world is ending. Error Code DCH-01")





@bot.event
async def on_message(message):
    author = str(message.author)
    content = str(message.content)
    userid = str(message.author.id) 
    messageid = str(message.id)
    time = str(message.created_at)
    link = str(message.jump_url)
    channel = str(message.channel)
    row = [userid,author,content,time,messageid,link,channel]
    wks1.insert_row(row, 2)
    date1 = str(datetime.date(datetime.now()))
    date2 = wks2.cell(2, 1).value
    date2 = date2.replace("'", '')
    if date1 == date2:
        daytotal = (wks2.cell(2, 2).value)
        daytotal = int(daytotal)
        daytotal = daytotal+1
        wks2.update_cell(2, 2, daytotal)
    else:
        row = [date1, 0]
        wks2.insert_row(row, 2)
    await bot.process_commands(message)
    



    
    


























bot.run(data["discordtoken"])
