import os
import discord 

import settings as func

from settings import setup_logging
from dotenv import load_dotenv
from discord.ext import commands
from features.youtube_request import *




class milenkobot(commands.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    async def on_ready(self):
        func.logging.info(f'---------------------------')
        func.logging.info(f'Ingresando como {self.user}')
        func.logging.info(f'bot id {self.user.id}')

        
    
    async def on_message(self,message) -> None:

        if message.author.bot or not message.guild :
            return False

        await self.process_commands(message)
    async def setup_hook(self)->None:

        for module in os.listdir(func.ROOT_DIR + '/cogs'):
            if module.endswith('.py'):
                try:
                    await self.load_extension(f"cogs.{module[:-3]}")
                    func.logger.info(f"cargado {module[:-3]}")
                except Exception as e:
                    func.logger.error(f"error al cargar {module[:-3]}.", exc_info=e)

        try:
           test_guild = discord.Object(id=TEST_GUILD_ID)
           synced= await self.tree.sync(guild=test_guild)
           func.logging.info(f' se han sincronizado : {len(synced)} comandos')
        except Exception as e:
            func.logging.error(f'error en : {e}')

class CommandCheck(discord.app_commands.CommandTree):
    async def interaction_check(self, interaction: discord.Interaction, /) -> bool:
        if not interaction.guild:
            await interaction.response.send_message("Este comando solo se aplica en servidores!")
            return False

        return True

setup_logging()

intents = discord.Intents().default()
intents.voice_states = True
intents.message_content = True
intents.guilds = True
bot= milenkobot(command_prefix='!',tree_cls=CommandCheck, intents= intents)



if __name__=="__main__":    
    load_dotenv()
    TEST_GUILD_ID = int(os.getenv("TEST_GUILD_ID"))
    key=os.getenv('DISCORD_TOKEN')
    bot.run(key)