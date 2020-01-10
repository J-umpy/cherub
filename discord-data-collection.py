#Modules
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import discord
from discord.ext import commands
from discord.ext.commands import bot
import json
import datetime
import random
import os, sys, traceback, asyncio
from datetime import datetime

#Setup
with open('setup.json') as f:
    data = json.loads(f.read())
bot = commands.Bot(command_prefix=data["prefix"])
bot.remove_command("help")
scope = ['https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
gc = gspread.authorize(creds)
sh = gc.open("Calamari Cove Data Collection")
wks1 = sh.worksheet("Sheet1")
wks2 = sh.worksheet("Sheet2")


@bot.event
async def on_ready():
    print("Bot connected")

@bot.command()
async def help(ctx):
    embed = discord.Embed(title = "Welcome to the Help Center!", description = "Help", colour = discord.Colour.blue())
    embed.set_footer(text="Bot by Jumpy♡#0150")
    embed.add_field(name="Commands", value=".graph: Displays a graph of server activity, if configured properly", inline=False)
    embed.add_field(name="Configuration", value="For configuration support contact me or check the github page")
    embed.add_field(name="Contact Me", value="Discord: Jumpy♡#0150\nTwitter: j_umpy")
    await ctx.channel.send(embed=embed)


@bot.command()
async def graph(ctx):
    link = data["link"]
    embed = discord.Embed(title = "Here ya go!", description = "A graph of activity", colour = discord.Colour.blue())
    embed.set_footer(text="Try again in a few minutes if it fails, Google can be slow sometimes.")
    embed.set_image(url=link)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/533774631102971904/664988197830262814/insiderbot.png")
    await ctx.channel.send(embed=embed)

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
