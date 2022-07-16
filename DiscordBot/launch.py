from discord.ext import commands  # импортируем из фреймворка класс commands.
import discord  # импортируем библиотеку discord.
from func import *
import os

bot = commands.Bot(command_prefix='.', intents=discord.Intents.all())

bot.remove_command('help')  # удаляет команду help ранее зарегистрированное когами.


@bot.event
async def on_ready():
    print('{0.user} запущен!'.format(bot))


async def open_acc(user):
    users = await get_bank()
    if user.bot is True:
        return
    if str(user.id) in users:
        return False
    else:
        users[str(user.id)] = {}
        users[str(user.id)]['wallet'] = 100
    write_json('jsons/bank.json', users)
    return True


async def get_bank():
    users = load_json('jsons/bank.json')
    return users


for filename in os.listdir("./cogs"):
    if filename.endswith(".py") and not filename.startswith("_"):
        bot.load_extension(f'cogs.{filename[:-3]}')

bot.run('Token')
