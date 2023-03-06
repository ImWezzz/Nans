from discord.ext import commands
from main import db
import discord
import sys
import datetime

class Util(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
    # Prefix
    @commands.hybrid_command(name="prefix")
    @commands.has_permissions(manage_guild=True)
    @discord.app_commands.describe(new_prefix="The new prefix to set")
    async def prefix(self, ctx: commands.Context, new_prefix: str):
        """Set a new prefix"""
        if not new_prefix:
            return await ctx.send("Missing new prefix argument.")
        if len(new_prefix) >= 6:
            return await ctx.send("The prefix cannot exceed **6 characteres**")
        await ctx.defer()
        db.set(f"{ctx.guild.id}.prefix", new_prefix, "guilds")
        await ctx.send(f"**Prefix channged to:** `{new_prefix}`") 
        
    # Help
    @commands.hybrid_command(name="h")
    async def help(self, ctx: commands.Context, *, query: str = None):
        """Show this message"""
        await ctx.send_help(query)

async def setup(bot: commands.Bot):
    await bot.add_cog(Util(bot))
