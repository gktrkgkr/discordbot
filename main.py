import discord
from discord.ext import commands
import music

cogs = [music]

client = commands.Bot(command_prefix="-", intents = discord.Intents.all())


for i in range(len(cogs)):
  cogs[i].setup(client)

client.run("ODkwNjQ0MjExODc0MDA5MTE5.YUyzDw.DWHWmuPyVc2RCkwdNfCpdPWSkLY")