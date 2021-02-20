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


@bot.command(name= 'test', hidden=True)
async def test(ctx):
    await ctx.send("funciona")

@bot.command()
async def hagalo_usted_mismo(ctx):
    await ctx.send("chao jasmina")

#suerte

@bot.command(help = "Tira una moneda")
async def coin(ctx,* ,msg):
    var=["verdadero","falso"]
    await ctx.send("{}".format(random.choice(var)))

@bot.command(help = "Prueba tu suerte")
async def magicball(ctx,* ,msg):
    if msg[-1]=='?':
        choice = await ctx.send("la bola magica dice  '{}' ".format(random.choice(eightball)))
    else :
        await ctx.send("no es pregunta")


#finder

@bot.command(help = "busqueda en youtube")
async def youtube(ctx, *, search):
    result = youtube_request(search)
    msg = await ctx.send(result)
    await msg.add_reaction("🗑️")


@bot.event
async def on_reaction_add(reaction, user):
    user_list =await reaction.users().flatten()
    msg = reaction.message
    emoji = reaction.emoji
    if  emoji=="🗑️" and reaction.count > 1 and user_list[0].bot == True and user_list[1].bot == False:
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

@bot.command(help = 'Muestra los creditos del bot')
async def credits(ctx):
    blue_color = str("""```css\nThis is some colored Text```""")
    embed=discord.Embed(title="milenko bot",value = blue_color ,description="pequeño bot con gran potencial", color=0x052fff)
    embed.set_author(name="Creditos")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/269286302141251585/812540021168013352/NO.png")
    embed.add_field(name="Beta dummies", value="Barry y Jordanox", inline=True)
    embed.add_field(name="Programador", value="Panconpan", inline=True)
    embed.add_field(name="Github", value="https://github.com/panconpan99/milenko_bot", inline=False)
    embed.set_footer(text="Con mas cosas que agregar")
    await ctx.send(embed=embed)

load_dotenv()
key=os.getenv('DISCORD_TOKEN')
bot.run(key)