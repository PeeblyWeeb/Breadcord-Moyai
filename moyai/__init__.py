from discord.ext import commands

from bot import Bot, Module


class Moyai(Module):

    @commands.Cog.listener()
    async def on_ready(self):
        self.logger.info(self.bot.settings.moyai.users)

    @commands.Cog.listener()
    async def on_message(self, ctx):
        if self.bot.settings.moyai.enabled is False:
            return
        if ctx.author.id in self.bot.settings.moyai.users:
            await ctx.add_reaction('🗿')


async def setup(bot: Bot):
    await bot.add_cog(Moyai(__name__, bot))
