import os
import discord 
from dotenv import load_dotenv
from discord import client, message, user
from discord.ext import commands
from discord.ext.commands import CommandNotFound

intents = discord.Intents().all()
bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print("listo")

@bot.command()
async def foo(ctx, arg):
    print("prueba")
    await ctx.send(arg)

@bot.command()
async def test(ctx):
    print("entro")
    await ctx.send("its works")

@bot.event
async def on_member_join(member):
    await member.channel.send("bienvenido a este sv de prueba")

@bot.event
async def on_message(message):
    if message.author == user :
        return
    if message.content == "hagalo usted mismo":
        await message.channel.send("chao jasmina")
    if message.content =="hola":
        await message.channel.send("pati mi cola")
    if message.content =="qlo":
        await message.channel.send("voh mismo")
    if message.content =="#dm":
        await message.author.send( "funciono, a medias")



load_dotenv()
key=os.getenv('DISCORD_TOKEN')
bot.run(key)