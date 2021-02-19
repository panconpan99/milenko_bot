import os
import discord 
from dotenv import load_dotenv
import random
import youtube_dl
from discord.ext import commands

bot = commands.Bot(command_prefix = '!' )

@bot.event
async def on_ready():
    print("ready")

@bot.command()
async def test(ctx):
    await ctx.send("sim")

@bot.command()
async def hagalo_usted_mismo(ctx):
    await ctx.send("chao jasmina")

@bot.command(help_command= "tira una moneda")
async def coin(ctx,* ,msg):
    var=["verdadero","falso"]
    await ctx.send("{}".format(random.choice(var)))

#music


@bot.command(pass_context = True)
async def play(ctx, url_: str):
    voice = discord.utils.get(ctx.guild.voicechannel,name='general')
    voice = discord.utils.get(bot.voice_clients, guild = ctx.guild)
    await voice.connect()


load_dotenv()
key=os.getenv('DISCORD_TOKEN')
bot.run(key)