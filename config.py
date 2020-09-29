TOKEN = 'token' #discord bot token

BOT_COMMAND_PREFIX = '/' #prefix for bot commands

FFMPEG_EXE_LOC = "./ffmpeg.exe" #location of ffmpeg exe in relation to /cog/ dir

ROLE_RESTRICT = 'commandrestrict' #exact name of role required to invoke playUpload command (case sensitive)

ROLE_RESTRICT_COG = 'cogrestrict' #exact name of role required to load and unload Cogs (case sensitive)

ACCEPTED_FILE_EXT = [".mp3", ".wav", ".mp4"] #list of file extensions playUpload command recognizes and downloads
#you should be able to add any other filetype that ffmpeg can convert to PCM to this list without issue
