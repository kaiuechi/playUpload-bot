import discord
from discord.ext import commands

class commandsGeneric(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        print("loaded commandsGeneric")
        
    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f"latency: {1000 * self.bot.latency}ms")
        print(f"commandsGeneric- latency: {1000 * self.bot.latency}ms")
        
def setup(bot):
    bot.add_cog(commandsGeneric(bot))