from discord.ext import commands
import discord


class avatar(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('avatar ready')

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def avatar(self, ctx, user_id: int):
        try:
            user = await self.bot.fetch_user(user_id)
        except discord.NotFound:
            embed = discord.Embed(
                description='❌ Usuário não encontrado', color=discord.Color.blue())
            await ctx.reply(embed=embed, mention_author=False)
            return
        except discord.HTTPException:
            embed = discord.Embed(
                description='❌ Erro na busca', color=discord.Color.blue())
            await ctx.reply(embed=embed, mention_author=False)
            return
        if user.avatar is None:
            embed = discord.Embed(
                description='❌ Usuário não possui avatar', color=discord.Color.blue())
            await ctx.reply(embed=embed, mention_author=False)
            return
        else:
            avatar_url = user.avatar.url

        embed = discord.Embed(title=f'Avatar de {user.name}', description=f'{user.mention}', colour=discord.Colour.blue())
        embed.set_image(url=avatar_url)
        await ctx.reply(embed=embed, mention_author=False)


async def setup(bot):
    await bot.add_cog(avatar(bot))
