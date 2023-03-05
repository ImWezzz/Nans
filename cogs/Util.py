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
        
    # Avatar 
    @commands.hybrid_command(name="avatar", aliases=["pfp"])
    @discord.app_commands.describe(member="Select a member")
    async def avatar(self, ctx: commands.Context, member: discord.Member = None):
        """Get a user avatar"""
        await ctx.defer()
        if member is None:
            member = ctx.author
        embed = discord.Embed(colour=1399944)
        embed.set_author(name=f"{member.name}#{member.discriminator}", icon_url=member.display_avatar)
        embed.set_image(url=member.display_avatar)
        
        await ctx.send(embed=embed) 

    # Userinfo
    @commands.hybrid_command(name="userinfo", aliases=["user"])
    async def avatar(self, ctx: commands.Context, member: discord.Member = None): 
        """Display user information"""
        if member is None:
            member = ctx.author

        embed = discord.Embed(colour=1399944)
        embed.set_thumbnail(url=member.display_avatar)
        embed.set_author(name=f"{member.name}#{member.discriminator}", icon_url=member.display_avatar)
        embed.description = f"\n **Information** \n**User:** {member.name}#{member.discriminator} `{member.id}` \n **Nick:** {member.nick} \n **Avatar:** [Click aquí](https://discord.com/users/{member.id}) \n\n **Created:** <t:{round(member.created_at.timestamp())}:R> \n **Joined:** <t:{round(member.joined_at.timestamp())}:R>"

        await ctx.send(embed=embed)

    # Ping
    @commands.hybrid_command(name="ping", aliases=["latency"])
    async def ping(self, ctx: commands.Context):
        """Show my ping"""
        await ctx.send(f"My ping is **{round(self.bot.latency, 2) * 1000}ms**")
    
    # Help
    @commands.hybrid_command(name="h")
    async def help(self, ctx: commands.Context, *, query: str = None):
        """Show this message"""
        await ctx.send_help(query)

    # Serverinfo
    @commands.hybrid_command(name="serverinfo")
    async def serverinfo(self, ctx: commands.Context):
        """Get server information"""
        await ctx.defer() # reinicia pelotudo de mierda pe che bldo posta capo deaaa ndeaahh
        embed = discord.Embed(colour=1399944)
        embed.set_thumbnail(url=ctx.guild.icon.url if ctx.guild.icon else None)
        embed.title = f"{ctx.guild.name} information"
        embed.description = f"**ID:** {ctx.guild.id} \n **Owner:** <@{ctx.guild.owner_id}> \n **Created:** <t:{round(ctx.guild.created_at.timestamp())}:R> \n **Members:** {ctx.guild.member_count} \n **Channels:** {len(ctx.guild.channels)} \n **Roles:** {len(ctx.guild.roles)} "

        await ctx.send(embed=embed)

    # Channel
    @commands.hybrid_command(name="channel")
    @discord.app_commands.describe(channel='Choose the channel')
    async def channel(self, ctx: commands.Context, channel: discord.abc.GuildChannel = None):
        """Get a channel info"""
        channel = channel or ctx.channel
        await ctx.defer()
        embed = discord.Embed(colour=1399944)
        embed.set_author(name=ctx.guild.name, icon_url=ctx.guild.icon)
        embed.set_thumbnail(url=ctx.guild.icon.url if ctx.guild.icon else None)
        embed.description = f"**Name:** {channel.name} \n **ID:** {channel.id} \n **Type:** {channel.type} \n **Position:** {channel.position} \n **Created:** <t:{round(ctx.channel.created_at.timestamp())}:R> \n **Is NSFW:** {channel.is_nsfw}"
        
        await ctx.send(embed=embed)

    # Role
    @commands.hybrid_command(name="role")
    @discord.app_commands.describe(role='Choose the role')
    async def role(self, ctx: commands.Context, role: discord.Role):
        """Get a role info"""
        await ctx.defer()
        embed = discord.Embed(colour=9999999)
        embed.set_thumbnail(url=ctx.guild.icon.url if ctx.guild.icon else None)
        embed.set_author(name=ctx.guild.name, icon_url=ctx.guild.icon)
        embed.description = f"**Name:** {role.name} \n **ID:** {role.id} \n **Position:** {role.position} \n **Color:** {role.color} \n **Created:** <t:{round(role.created_at.timestamp())}:R>"

        await ctx.send(embed=embed)

    # Icon
    @commands.hybrid_command(name="icon")
    async def icon(self, ctx: commands.Context):
        """Get the server icon"""
        if not ctx.guild.icon:
            return await ctx.send("The server has no icon")
        await ctx.defer()
        embed = discord.Embed(colour=1399944)
        embed.set_author(name=ctx.guild.name, icon_url=ctx.guild.icon.url)
        embed.set_image(url=ctx.guild.icon.url)

        await ctx.send(embed=embed)

    # Bot Info
    @commands.hybrid_command(name="botinfo", aliases=["stats"])
    async def stats(self, ctx: commands.Context):
        """Get the bot info"""
        await ctx.defer()
        embed = discord.Embed(colour=1399944)
        embed.set_thumbnail(url=self.bot.user.display_avatar)
        embed.title = f"{ctx.bot.user.name} stats"
        embed.description = f"• **Stats** \n **Servers:** {len(self.bot.guilds)} \n **Users:** {len(self.bot.users)} \n **Commands:** {len(self.bot.commands)} \n\n  • **Development** \n **Discord.py:** {discord.__version__} \n **Python:** {sys.version.split(' ')[0]} \n\n • **Developer** \n [Wez#9777](https://discord.com/users/759233882926350346) \n\n • **Links** \n [Invite](https://dsc.gg/willow-bot) • [Support](https://discord.gg/ynNWwPRgv2)"

        await ctx.send(embed=embed)

    # 

async def setup(bot: commands.Bot):
    await bot.add_cog(Util(bot))
