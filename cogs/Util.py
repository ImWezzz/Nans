from discord.ext import commands
from main import db
import discord
import sys
import datetime

class Util(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
    # Help
    @commands.hybrid_command(name="h")
    async def help(self, ctx: commands.Context, *, query: str = None):
        """Show this message"""
        await ctx.send_help(query)

    # Reverse
    @commands.hybrid_command(name="reverse")
    async def reverse(self, ctx: commands.Context, *, text: str):
        """Reverse a text"""
        await ctx.send(content=text[::-1])

    

async def setup(bot: commands.Bot):
    await bot.add_cog(Util(bot))
