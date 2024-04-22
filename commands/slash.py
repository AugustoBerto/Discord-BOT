from discord.ext import commands
from discord import app_commands
import discord


class slash(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('slash ready')

    @app_commands.command(name="say")
    async def say(self, interaction: discord.Interaction, message: str):
        await interaction.response.send_message(f"{interaction.user.name} disse: `{message}`")


async def setup(bot):
    await bot.add_cog(slash(bot))
