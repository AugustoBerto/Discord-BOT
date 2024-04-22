from discord.ext import commands


class send(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('send ready')

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def send(self, ctx, channel, *, content):
        if channel == "here":
            channel = ctx.channel
        else:
            channel = self.bot.get_channel(int(channel))

        await channel.send(content)
        await ctx.message.delete()

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def sendpv(self, ctx, user_id, *, content):
        user = await self.bot.fetch_user(user_id)
        await ctx.message.delete()
        await user.send(content)


async def setup(bot):
    await bot.add_cog(send(bot))
