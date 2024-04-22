from discord.ext import commands


class ready(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Logged in as {0.user}'.format(self.bot))
        try:
            synced = await self.bot.tree.sync()
            print(f"Synced {len(synced)} command(s)")
        except Exception as e:
            print(e)

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Envie todos os argumentos necessários")
        elif isinstance(error, commands.CommandNotFound):
            await ctx.send("Comando desconhecido")
        elif isinstance(error, commands.BadArgument):
            await ctx.send("Argumentos inválidos")
        else:
            raise error


async def setup(bot):
    await bot.add_cog(ready(bot))
