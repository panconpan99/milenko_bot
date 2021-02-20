import os
import discord 
from dotenv import load_dotenv
import random
import youtube_dl
from discord.ext import commands
from features.youtube_request import *
from features.mensajes.message import MESSAGES
from features.mensajes.lolball import eightball

intents = discord.Intents().all()
bot = commands.Bot(command_prefix = '!')

@bot.event
async def on_ready():
    print("ready")

@bot.event
async def on_member_join(member):
    print("entre")
    await member.channel.send(
    f'hola {member.name}, biemvenido a la zona de testeo')

@bot.event
async def on_command_error(ctx,error):
    if isinstance(error,commands.MissingRequiredArgument) or isinstance(error,commands.CommandNotFound):
        msg = await ctx.send(random.choice(MESSAGES))


@bot.command(name= 'test', help = 'prueba de test')
async def test(ctx):
    await ctx.send("funciona")

@bot.command()
async def hagalo_usted_mismo(ctx):
    await ctx.send("chao jasmina")

#suerte

@bot.command(help = "tira una moneda")
async def coin(ctx,* ,msg):
    var=["verdadero","falso"]
    await ctx.send("{}".format(random.choice(var)))

@bot.command(help = "prueba tu suerte")
async def magicball(ctx,* ,msg):
    choice = await ctx.send("la bola magica dice  '{}' ".format(random.choice(eightball)))


#finder

@bot.command()
async def youtube(ctx, *, search):
    result = youtube_request(search)
    msg = await ctx.send(result)
    await msg.add_reaction("🗑️")


@bot.event
async def on_reaction_add(reaction, user):
    user_list =await reaction.users().flatten()
    msg = reaction.message
    emoji = reaction.emoji
    if  emoji=="🗑️" and user_list[0].bot == True and user_list[1].bot == False:
        await msg.delete()

#music

@bot.command(pass_context = True, help = 'soon')
async def play(ctx):
    if not ctx.author.voice:
        print("entre")
        channel =discord.utils.get(guild.voice_channels)
        await channel.connect()


@bot.command(pass_context = True, help = 'soon')
async def leave(ctx):
    voice_client = ctx.message.guild.voice_client
    await voice_client.disconnect()


load_dotenv()
key=os.getenv('DISCORD_TOKEN')
bot.run(key)