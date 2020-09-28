import os
from os import path
import sys
import youtube_dl
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix = 'mj.')

@bot.event
async def on_ready():
    print("ready!")
    
@bot.command()
async def unloadCog(ctx, extName):
        bot.unload_extension(f"cogs.{extName}")

@bot.command()
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

bot.run('token')