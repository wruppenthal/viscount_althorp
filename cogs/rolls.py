import random
import numpy as np
import discord
from discord.ext import commands


class Rolls(commands.Cog, name="Stat Commands"):
    def __init__(self, bot):
        self.bot = bot


    #----------cog methods----------#

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def justify(self, ctx, dur : int, maxinf : int):
        """Returns infamy gained due to war goal justification."""
        days = round(np.random.normal(dur/2, dur*0.375))
        inf = round(maxinf*((dur - days)/dur))

        if inf > 0:
            if days <= 0:
                await ctx.send('Discovered immediately! Infamy accrued: {}'.format(maxinf))
            else:
                s = 'Discovered after {} days! Infamy accrued: {}'
                await ctx.send(s.format(max(0, round(days)), min((inf, maxinf))))
        else:
            await ctx.send('Fabrication not discovered.')


def setup(bot):
    bot.add_cog(Rolls(bot))
