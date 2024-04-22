from discord.ext import commands
from configparser import ConfigParser
import discord
import asyncio

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())
bot.remove_command('help')

auth = ConfigParser()
auth.read('token.env')


async def main():
    async with bot:
        await bot.load_extension('commands.avatar')
        await bot.load_extension('commands.clear')
        await bot.load_extension('commands.help')
        await bot.load_extension('commands.send')
        await bot.load_extension('commands.slash')
        await bot.load_extension('tasks.ready')
        await bot.start(auth['default']['TOKEN_ID'])

asyncio.run(main())
