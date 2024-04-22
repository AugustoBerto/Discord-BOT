from discord.ext import commands
import asyncio

mx = 35


class clear(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('clear ready')

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def limparchat(self, ctx, amount=1):
        if amount <= mx:
            await ctx.channel.purge(limit=amount)
            if amount <= 1:
                await ctx.channel.purge(limit=1)
                message1 = await ctx.send(f'Ei {ctx.message.author.mention}, Deletei {amount} mensagens para você :)')
                await asyncio.sleep(5)
                await message1.delete()
            else:
                await ctx.channel.purge(limit=1)
                message2 = await ctx.send(f'Ei {ctx.message.author.mention}, Deletei {amount} mensagens para você :)')
                await asyncio.sleep(5)
                await message2.delete()
        else:
            await ctx.channel.purge(limit=1)
            message3 = await ctx.send(f'Ops!! Sinto muito {ctx.message.author.mention}, só consigo deletar até {mx} mensagens por vez :(')
            await asyncio.sleep(10)
            await message3.delete()
            return


async def setup(bot):
    await bot.add_cog(clear(bot))
