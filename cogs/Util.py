from discord.ext import commands
from main import db
from utils.views import DropdownView
import discord
import sys
import datetime

class Util(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
    # Help
    @commands.hybrid_command(name="help")
    async def help(self, ctx: commands.Context):
        """Commands list"""

        embed = discord.Embed(colour=1399944)
        embed.set_thumbnail(url=self.bot.user.display_avatar)
        embed.set_author(name="Commands list")
        embed.description = f"**Hi! If you want to see my list of commands use the menu below** \n\n **Total commands: {len(self.bot.commands)}** \n\n [Invite](https://dsc.gg/willow-bot) • [Support](https://discord.gg/ynNWwPRgv2) • [Website](https://willowbot.munlai.fun)"
        miview = DropdownView()
        await ctx.send(embed=embed, view=miview)

    # Reverse
    @commands.hybrid_command(name="reverse")
    async def reverse(self, ctx: commands.Context, *, text: str):
        """Reverse a text"""
        await ctx.send(content=text[::-1])

    # Say
    @commands.hybrid_command(namd="say")
    async def say(self, ctx: commands.Context, *, text: str):
        """I repeat your message"""
        await ctx.send(content=text)

async def setup(bot: commands.Bot):
    await bot.add_cog(Util(bot))
