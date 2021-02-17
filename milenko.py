import os
import discord 
from dotenv import load_dotenv
from discord.ext import commands
from discord.ext.commands import CommandNotFound

bot = commands.Bot(command_prefix='#', help_command=None)

@bot.event
async def on_ready():
    print("listo")


load_dotenv()
key=os.getenv('DISCORD_TOKEN')
bot.run(key)