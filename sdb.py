import sqlite3
from sqlite3 import Error
import discord
from discord.ext import commands
from discord.ext.commands import bot

#Connecting
def dbconnect(dbf):
  try:
    conn = sqlite3.connect(dbf)
  except Error:
    print(Error)
  else:
    return conn
db = dbconnect('cherub.db')
cursor = db.cursor()
#Builds tables
async def deploy(guild):
  for channel in guild.text_channels:
    cursor.execute("create table if not exists C"+str(channel.id)+"(AuthorID text, Author text, Content text, MessageID text, Time text, Link text, Attachments text)")
  db.commit()

#Updates a cell of a given type from a guild (specified by ID)
async def update(table, cat, arg, guildid):
  cursor.execute("UPDATE "+table+" SET "+str(cat)+" = '"+str(arg)+"' WHERE GuildID = '"+str(guildid)+"'")
  db.commit()

#Selects and reads a cell
async def read(table, obj, guildid):
  cursor.execute("SELECT "+str(obj)+" FROM "+table+" WHERE GuildID='"+str(guildid)+"'")
  r = cursor.fetchall()
  return r