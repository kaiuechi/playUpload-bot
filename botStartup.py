import os
from os import path
import sys
import youtube_dl
#!{sys.executable} -m pip install discord.py

import discord
from discord.ext import commands

bot = commands.Bot(command_prefix = 'mj.')

@bot.event
async def on_ready():
    print("ready!")

#load all cogs in /cogs/
cogdir = path.dirname(__file__) + "\cogs\\"
print(cogdir)
for filename in os.listdir(cogdir):
    print(f"found file: {filename}")
    if filename.endswith(".py"):
        filename = filename[:-3]
        print(f"loading {filename}")
        bot.load_extension(f"cogs.{filename}")

bot.run('NzU2NTcyODM1MTE1MzAzMDY0.X2TzXA.vsVj6Krkgknkb5po428kdRKMnFY')