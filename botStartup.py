import os
from os import path
import sys
import discord
from discord.ext import commands

import config

bot = commands.Bot(command_prefix = config.BOT_COMMAND_PREFIX)

@bot.event
async def on_ready():
    print("ready!")
    
@bot.command()
@commands.has_role(config.ROLE_RESTRICT_COG)
async def unloadCog(ctx, extName):
        bot.unload_extension(f"cogs.{extName}")

@bot.command()
@commands.has_role(config.ROLE_RESTRICT_COG)
async def loadCog(ctx, extName):
        bot.load_extension(f"cogs.{extName}")

#load all cogs in /cogs/
cogdir = "./cogs/"
for filename in os.listdir(cogdir):
    print(f"found file: {filename}")
    if filename.endswith(".py"):
        filename = filename[:-3]
        print(f"loading {filename}")
        bot.load_extension(f"cogs.{filename}")

bot.run(config.TOKEN)