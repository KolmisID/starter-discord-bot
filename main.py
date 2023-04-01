
import os
import pandas
import uvloop
import asyncio
import cachetools
import psutil
import disnake
from disnake.ext import commands
import config

intents = disnake.Intents.all()
intents.members = True
bot = commands.Bot(command_prefix=config.PREFIX, intents=intents, help_command=None)
# загрузка комманд
for filename in os.listdir('./commands'):
    if filename.endswith('.py'):
        bot.load_extension(f'commands.{filename[:-3]}')
#загрузка ивентов
for filename in os.listdir('./events'):
    if filename.endswith('.py'):
        bot.load_extension(f'events.{filename[:-3]}')			

bot.run(config.TOKEN)