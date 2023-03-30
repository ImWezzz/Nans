import os
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

        embed = discord.Embed(colour=14474460)
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
    @commands.hybrid_command(name="say")
    async def say(self, ctx: commands.Context, *, text: str):
        """I repeat your message"""
        await ctx.send(content=text)

    # Invite
    @commands.hybrid_command(name="invite")
    async def say(self, ctx: commands.Context):
        """Get my invite"""
        embed = discord.Embed(colour=14474460)
        embed.set_thumbnail(url=self.bot.user.display_avatar)
        embed.title = "My invitation"
        embed.description = f"If you want to invite me to your server use this link \n Invite: https://dsc.gg/willow-bot \n Support server: https://discord.gg/ynNWwPRgv2"

        await ctx.send(embed=embed)


    # -------- > SubCommands <--------


        # ----> Image <----

    #@commands.hybrid_group(name="image")
    #async def image(self, ctx: commands.Context):
    #    """Create images OMG"""

    # Discordjs
    @commands.hybrid_command(name="discordjs")
    @discord.app_commands.describe(text="Text")
    async def discordjs(self, ctx: commands.Context, text: str):
        """Make a Discord.JS image"""

        embed = discord.Embed()
        embed.set_image(url=f"https://api.munlai.fun/image/discordjs?text={text[0:20]}")

        await ctx.send(embed=embed)

    # Simp
    @commands.hybrid_command(name="simp")
    @discord.app_commands.describe(user="User")
    async def simp(self, ctx: commands.Context, user: discord.Member = None):
        """Make a simp image"""
        if user is None:
            user = ctx.author
        embed = discord.Embed()
        embed.set_image(url=f"https://api.munlai.fun/image/simp?image={user.display_avatar}")

        await ctx.send(embed=embed)

    # Target
    @commands.hybrid_command(name="target")
    @discord.app_commands.describe(user="User")
    async def target(self, ctx: commands.Context, user: discord.Member = None):
        """Make a target image"""
        if user is None:
            user = ctx.author
        embed = discord.Embed()
        embed.set_image(url=f"https://api.munlai.fun/image/target?image={user.display_avatar}")

        await ctx.send(embed=embed)

    # Communism
    @commands.hybrid_command(name="communism")
    @discord.app_commands.describe(user="User")
    async def communism(self, ctx: commands.Context, user: discord.Member = None):
        """Make a communism image"""
        if user is None:
            user = ctx.author
        embed = discord.Embed()
        embed.set_image(url=f"https://api.munlai.fun/image/communism?image={user.display_avatar}")

        await ctx.send(embed=embed)

    # Rainbow/Gay
    @commands.hybrid_command(name="rainbow")
    @discord.app_commands.describe(user="User")
    async def rainbow(self, ctx: commands.Context, user: discord.Member = None):
        """Make a rainbow image"""
        if user is None:
            user = ctx.author
        embed = discord.Embed()
        embed.set_image(url=f"https://api.munlai.fun/image/gay?image={user.display_avatar}")

        await ctx.send(embed=embed)

    # Delete
    @commands.hybrid_command(name="delete")
    @discord.app_commands.describe(user="User")
    async def delete(self, ctx: commands.Context, user: discord.Member = None):
        """Make a delete image"""
        if user is None:
            user = ctx.author
        embed = discord.Embed()
        embed.set_image(url=f"https://api.munlai.fun/image/delete?image={user.display_avatar}")

        await ctx.send(embed=embed)

    # Beautiful
    @commands.hybrid_command(name="beautiful")
    @discord.app_commands.describe(user="User")
    async def beautiful(self, ctx: commands.Context, user: discord.Member = None):
        """OMG is beautiful :o"""
        if user is None:
            user = ctx.author
        embed = discord.Embed()
        embed.set_image(url=f"https://api.munlai.fun/image/beautiful?image={user.display_avatar}")

        await ctx.send(embed=embed)

    # Deepfry
    @commands.hybrid_command(name="deepfry")
    @discord.app_commands.describe(user="User")
    async def deepfry(self, ctx: commands.Context, user: discord.Member = None):
        """Make a deepfry image"""
        if user is None:
            user = ctx.author
        embed = discord.Embed()
        embed.set_image(url=f"https://api.munlai.fun/image/deepfry?image={user.display_avatar}")

        await ctx.send(embed=embed)

    # Invert
    @commands.hybrid_command(name="invert")
    @discord.app_commands.describe(user="User")
    async def invert(self, ctx: commands.Context, user: discord.Member = None):
        """Invert the colors of an avatar"""
        if user is None:
            user = ctx.author
        embed = discord.Embed()
        embed.set_image(url=f"https://api.munlai.fun/image/invert?image={user.display_avatar}")

        await ctx.send(embed=embed)

        # --------> Developer commands <--------

    # Eval
    @commands.is_owner()
    @commands.hybrid_command(name="eval")
    @discord.app_commands.describe(code="Code")
    async def eval(self, ctx: commands.Context, code: str):
        """Evaluate a code"""
        try:
            result = eval(code)
            await ctx.send(result)
        except Exception as e:
            await ctx.send(f'```py\n{e}```')

    # Reload
    @commands.is_owner()
    @commands.hybrid_command(name="reload")
    async def _reload(self, ctx: commands.Context, cog: str):
        await self.bot.reload_extension(f"cogs.{cog}")
        if os.path.exists(f"./cogs/{cog}.py"):
            return await ctx.send(f'**cogs.{cog}** was reloaded omg uwu')
        else:
            ctx.send("No es un cog bro :c")

async def setup(bot: commands.Bot):
    await bot.add_cog(Util(bot))
