import discord
import os
import random
from discord import app_commands
from discord.ext import commands
from features.mensajes.lolball import eightball

from settings import logger
TEST_GUILD_ID = int(os.getenv("TEST_GUILD_ID"))  
class comandos(commands.Cog):
    def __init__(self,bot:commands.bot)->None:
        self.bot=bot
        bot.tree.add_command(self.hola, guild=discord.Object(id=TEST_GUILD_ID))
        bot.tree.add_command(self.credits, guild=discord.Object(id=TEST_GUILD_ID))
        bot.tree.add_command(self.coin, guild=discord.Object(id=TEST_GUILD_ID))
        bot.tree.add_command(self.magicball,guild=discord.Object(id=TEST_GUILD_ID) )

    @app_commands.command(name="holaa", description="Envia un saludo")
    async def hola(self, interaction: discord.Interaction):
        await interaction.response.send_message(f"hola mundo", ephemeral=False)

     # Evento al entrar un nuevo miembro
    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):
        try:
            if member.guild.system_channel:
                await member.guild.system_channel.send(
                    f'Hola {member.name}, ¡bienvenido a la zona de testeo!'
                )
        except Exception as e:
            print(f"[ERROR] No se pudo enviar mensaje de bienvenida: {e}")

    # Slash command /coin

    @app_commands.command(name="coin", description="Tira una moneda")
    async def coin(self, interaction: discord.Interaction, msg: str):
        result = random.choice(["verdadero", "falso"])
        await interaction.response.send_message(f"{result}")

    # Slash command /magicball
    @app_commands.command(name="magicball", description="Pregunta algo a la bola mágica")
    async def magicball(self, interaction: discord.Interaction, pregunta: str):
        if not pregunta.endswith("?"):
            await interaction.response.send_message("¡Eso no parece una pregunta!", ephemeral=True)
            return
        resultado = random.choice(eightball)
        await interaction.response.send_message(f"La bola mágica dice: **{resultado}**")

    @app_commands.command(name="creditos", description="muestra una pantalla con los desarrolladores")
    async def credits(self, interaction: discord.Interaction):
        embed = discord.Embed(
            title="milenko bot",
            description="Pequeño bot con gran potencial",
            color=0x052fff
        )
        embed.set_author(name="Créditos")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/269286302141251585/812540021168013352/NO.png")
        embed.add_field(name="Beta dummies", value="Barry y Jordanox", inline=True)
        embed.add_field(name="Programador", value="Panconpan", inline=True)
        embed.add_field(name="GitHub", value="https://github.com/panconpan99/milenko_bot", inline=False)
        embed.set_footer(text="Con más cosas que agregar")
        
        await interaction.response.send_message(embed=embed)
async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(comandos(bot))

