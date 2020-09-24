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
        
    @commands.command()
    async def purge(self, ctx, amount = 5):
        amount = amount + 1 #compensating for the calling command
        await ctx.channel.purge(limit=amount)
        print(f"commandsGeneric- user {ctx.author} purged {amount - 1} messages")
        
def setup(bot):
    bot.add_cog(commandsGeneric(bot))