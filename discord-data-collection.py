#Modules
import discord
from discord.ext import tasks, commands
from discord.ext.commands import bot
import json
import sqlite3
from sqlite3 import Error
import sdb
import asyncio

#Setup
db = sdb.dbconnect('cherub.db')
cursor = db.cursor()
with open('config.json') as f:
    data = json.loads(f.read())
try:
    data['config']
except:
    token = input("\nPlease enter your Discord Bot's Token\n")  
    guildid = input("\nPlease enter the ID of the server you'd like to monitor\n")
    d = {'prefix': '~', 'token': token, 'guildid': int(guildid), 'timer': 600.0, 'config': True}
    with open('config.json', 'w') as f:
        json.dump(d, f, indent=4)
async def get_prefix(bot, message):
  prefix = data['prefix']
  if prefix == None:
    prefix = '~'
  return commands.when_mentioned_or(prefix)(bot, message)
bot = commands.Bot(command_prefix=get_prefix, case_insensitive=True, help_command=None)
r = input("What would you like to do?\n1) Run Cherub\n2) Delete User Data\n")
if r == '2':
    r = input("Enter the ID of the user you'd like to delete the data of\n")
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
    c = cursor.fetchall()
    for channel in c:
        cursor.execute("DELETE FROM "+channel[0]+" WHERE AuthorID='"+r+"'")
        db.commit()
    db.close()
    db = sdb.dbconnect('cherub.db')
    cursor = db.cursor()


@bot.event
async def on_ready():
    guild = bot.get_guild(data['guildid'])
    await sdb.deploy(guild)
    print("Bot connected")
    writer.start()

@bot.command()
async def help(ctx):
    embed = discord.Embed(title = "Welcome to the Help Center!", description = "Help", colour = discord.Colour.blue())
    embed.set_footer(text="Bot by Jumpy♡#0150")
    embed.add_field(name="Configuration", value="For configuration support contact me or check the [GitHub page](https://github.com/J-umpy/cherub)", inline=False)
    embed.add_field(name="Remember", value="Always shut down the bot with the shutdown command to prevent data loss", inline=False)
    embed.add_field(name="Contact Me", value="Discord: Jumpy♡#0150\nTwitter: @j_umpy", inline=False)
    await ctx.channel.send(embed=embed)

@bot.command(aliases=["die"])
async def shutdown(ctx):
    db.commit()
    db.close()
    raise SystemExit

@bot.event
async def on_command_error(ctx, exception):
    error = getattr(exception, "original", exception)
    if isinstance(error, commands.CommandNotFound):
        return


async def write():
    db.commit()

@tasks.loop(seconds=data['timer'])
async def writer():
    async with asyncio.Lock():
        await write()
@writer.after_loop
async def on_write_cancel():
    print("Writing remaining data...")
    if writer.is_being_cancelled():
        await write()
        print("Write successful. Loop has ended.")

@bot.event
async def on_message(message):
    await bot.wait_until_ready()
    author = str(message.author)
    content = str(message.content)
    userid = str(message.author.id) 
    messageid = str(message.id)
    time = str(message.created_at)
    link = str(message.jump_url)
    if len(message.attachments) != 0:
        attachments = message.attachments[0].url
    else:
        attachments = 0
    row = (userid,author,content,messageid,time,link,attachments)
    cursor.execute("INSERT INTO C"+str(message.channel.id)+"(AuthorID, Author, Content, MessageID, Time, Link, Attachments) VALUES(?, ?, ?, ?, ?, ?, ?)", row)
    await bot.process_commands(message)
bot.run(data["token"])