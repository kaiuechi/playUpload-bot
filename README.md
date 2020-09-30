           _                         _                 _       _           _   
     _ __ | | __ _ _   _ /\ /\ _ __ | | ___   __ _  __| |     | |__   ___ | |_ 
    | '_ \| |/ _` | | | / / \ \ '_ \| |/ _ \ / _` |/ _` |_____| '_ \ / _ \| __|
    | |_) | | (_| | |_| \ \_/ / |_) | | (_) | (_| | (_| |_____| |_) | (_) | |_ 
    | .__/|_|\__,_|\__, |\___/| .__/|_|\___/ \__,_|\__,_|     |_.__/ \___/ \__|
    |_|            |___/      |_|                                              


## What does Play Upload Bot do?

Here: Description of what the bot does

## How to Install

Clone this repo, then install required libraries:

* `pip install -r requirements.txt`
* Install `ffmeg` for your operating system -- [more info](https://github.com/adaptlearning/adapt_authoring/wiki/Installing-FFmpeg)

Then setup your configuration file, `config.py` (see below on details for configuration)

## How to Configure

Edit `config.py` as a Python file, and add in the values for the following variables:

* `TOKEN` = 'token' #create a discord bot token -- follow the instructions here [here](https://discordpy.readthedocs.io/en/latest/discord.html)
* `BOT_COMMAND_PREFIX` = '/' #prefix for bot commands
* `FFMPEG_EXE_LOC` = "./ffmpeg.exe" #location of ffmpeg (.exe on Windows) in relation to ./cog/ dir
* `ROLE_RESTRICT` = 'commandrestrict' #exact name of role required to invoke playUpload command (case sensitive)
* `ROLE_RESTRICT_COG` = 'cogrestrict' #exact name of role required to load and unload Cogs (case sensitive)
* `ACCEPTED_FILE_EXT` = [".mp3", ".wav", ".mp4"] #list of file extensions playUpload command recognizes and downloads.  You should be able to add any other filetype that ffmpeg can convert to PCM to this list without issue

## How to Run

If the first time you run it you get an error message `discord.errors.LoginFailure: Improper token has been passed` 
then you probably have not set up your own configuration file -- see _How to Configure_, above.

