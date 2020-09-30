import discord
from discord.ext import commands

import sys
sys.path.append('../..')
import config

def check_file_ext(att_filename):
    fileValid = False
    for fileExt in config.ACCEPTED_FILE_EXT:
        if att_filename.endswith(fileExt):
            fileValid = True
    return fileValid

class playUpload(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        print("loaded playUpload")

    @commands.command()
    @commands.has_role(config.ROLE_RESTRICT)
    async def upload(self, ctx):

        print(f"playUpload- attachment {ctx.message.attachments} uploaded from {ctx.author}")
        for attach in ctx.message.attachments:
            if check_file_ext(attach.filename):
                print(f"playUpload- saving attachment {attach.filename}")
                await attach.save(attach.filename)

                query = attach.filename
                source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(query, executable=config.FFMPEG_EXE_LOC))
                ctx.voice_client.play(source, after=lambda e: print('Player error: %s' % e) if e else None)
                await ctx.send(f"playing file {attach.filename}")
                print(f"playUpload- playing file {attach.filename}")
            else:
                print(f"playUpload- {attach.filename} not saved, invalid file extension")
                await ctx.send("invalid file extension")


    @upload.before_invoke
    async def ensure_voice(self, ctx):
        if ctx.voice_client is None:
            if ctx.author.voice:
                await ctx.author.voice.channel.connect()
            else:
                await ctx.send("You are not connected to a voice channel.")
                raise commands.CommandError("Author not connected to a voice channel.")
        elif ctx.voice_client.is_playing():
            ctx.voice_client.stop()

    @upload.error
    async def upload_error(self, ctx, error):
        if isinstance(error, commands.MissingRole):
            await ctx.send(f"role {config.ROLE_RESTRICT} is required to run this command")

def setup(bot):
    bot.add_cog(playUpload(bot))
