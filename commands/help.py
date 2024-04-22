from discord.ext import commands
from commands.clear import mx
import discord


class help(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('help ready')

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def help(self, ctx):
        embed = discord.Embed(
            title='Comandos do BOT', description='**AQUI ESTÂO TODOS OS COMANDOS:**', color=discord.Color.blue())

        embed.add_field(name='!avatar (user_id)',
                        value='Busca o avatar de um usuário através do ID', inline=False)
        embed.add_field(name='!limparchat (Value)',
                        value=f'Limpa determinado numero de mensagens do chat (Max={mx})', inline=False)
        embed.add_field(name='!send (channel_id / here)(message)',
                        value='Envia uma mensagem no chat através do ID, "here" envia no chat atual', inline=True)
        embed.add_field(name='!sendpv (user_id)(message)',
                        value='Envia uma mensagem no privado de um usuário através do ID', inline=True)

        await ctx.send(embed=embed)


async def setup(bot):
    await bot.add_cog(help(bot))
