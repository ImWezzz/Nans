from discord.ext import commands
from main import db
import discord
import sys

class Information(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

            # ----> User <----

    #@commands.hybrid_group(name="user")
    #async def user(self, ctx: commands.Context):
    #    """Show user information"""

    # Info
    @commands.hybrid_command(name="userinfo")
    @discord.app_commands.describe(member="Select a member")
    async def userinfo(self, ctx: commands.Context, member: discord.Member = None): 
        """Display user information"""
        if member is None:
            member = ctx.author
        if member.activity is None:
            print(f"{member.activity} tiene esa mierda")
        embed = discord.Embed(colour=1399944)
        embed.set_thumbnail(url=member.display_avatar)
        embed.set_author(name=f"{member.name}#{member.discriminator}", icon_url=member.display_avatar)
        embed.description = f"**ID:** {member.id} \n **Nickname:** {member.nick} \n **Status:** {member.status} \n **Bot:** {member.bot} \n **Color:** {member.color} \n\n **・Joined**\n **Discord:** <t:{round(member.created_at.timestamp())}:R> \n **Server:** <t:{round(member.joined_at.timestamp())}:R>"

        await ctx.send(embed=embed)

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

    # Roles 
    @commands.hybrid_command(name="roles")
    @discord.app_commands.describe(member="Select a member")
    async def roles(self, ctx: commands.Context, member: discord.Member = None):
        """Get user roles"""
        await ctx.defer()
        if member is None:
            member = ctx.author
        embed = discord.Embed(colour=1399944)
        embed.set_author(name=f"{member.name}#{member.discriminator}", icon_url=member.display_avatar)
        embed.description = f"- {len(member.roles) if member else '0'} Roles\n{' • '.join(list(map(lambda r: r.mention, member.roles))) if member else 'No roles'}"

        await ctx.send(embed=embed)
            
            # ----> Server <----
        
    #@commands.hybrid_group(name="server")
    #async def server(self, ctx: commands.Context):
    #        """Show server information"""
    
        # Info

    @commands.hybrid_command(name="serverinfo")
    async def serverinfo(self, ctx: commands.Context):
        """Get the server info"""
        await ctx.defer()
        embed = discord.Embed(colour=1399944)
        embed.set_thumbnail(url=ctx.guild.icon.url if ctx.guild.icon else None)
        embed.set_author(name=ctx.guild.name, icon_url=ctx.guild.icon)
        embed.description = f"**ID:** {ctx.guild.id} \n **Owner:** <@{ctx.guild.owner_id}> \n **Created:** <t:{round(ctx.guild.created_at.timestamp())}:R> \n **Members:** {ctx.guild.member_count} \n **Channels:** {len(ctx.guild.channels)} \n **Roles:** {len(ctx.guild.roles)} "

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

    # Role
    @commands.hybrid_command(name="role")
    @discord.app_commands.describe(role='Choose the role')
    async def role(self, ctx: commands.Context, role: discord.Role):
        """Get a role info"""
        await ctx.defer()
        embed = discord.Embed(colour=1399944)
        embed.set_thumbnail(url=ctx.guild.icon.url if ctx.guild.icon else None)
        embed.set_author(name=ctx.guild.name, icon_url=ctx.guild.icon)
        embed.description = f"**Name:** {role.name} \n **ID:** {role.id} \n **Position:** {role.position} \n **Color:** {role.color} \n **Created:** <t:{round(role.created_at.timestamp())}:R>"

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
        embed.description = f"**Name:** {channel.name} \n **ID:** {channel.id} \n **Type:** {channel.type} \n **Position:** {channel.position} \n **Created:** <t:{round(ctx.channel.created_at.timestamp())}:R>"
        
        await ctx.send(embed=embed)

            # ----> Bot <----

    #@commands.hybrid_group(name="bot")
    #async def bot(self, ctx: commands.Context):
    #        """Show bot information"""

    # Ping
    @commands.hybrid_command(name="ping", aliases=["latency"])
    async def ping(self, ctx: commands.Context):
        """Show my ping"""
        await ctx.send(f"My ping is **{round(self.bot.latency, 2) * 1000}ms**")
    
    # Info
    @commands.hybrid_command(name="botinfo", aliases=["stats"])
    async def stats(self, ctx: commands.Context):
        """Get the bot info"""
        await ctx.defer()
        embed = discord.Embed(colour=1399944)
        embed.set_thumbnail(url=self.bot.user.display_avatar)
        embed.title = f"{ctx.bot.user.name}'s stats"
        embed.description = f"-> **Stats** \n\n **Servers:** {len(self.bot.guilds)} \n **Users:** {len(self.bot.users)} \n **Commands:** {len(self.bot.commands)} \n\n **Developer:** [Wez#9777](https://discord.com/users/759233882926350346) \n **Discord.py version:** {discord.__version__} \n **Python version:** {sys.version.split(' ')[0]} \n\n -> **Links** \n [Invite](https://dsc.gg/willow-bot) \n [Support](https://discord.gg/ynNWwPRgv2) \n [Website](https://willowbot.munlai.fun) \n [Vote for me](https://top.gg/bot/779489579392040960/vote)"

        await ctx.send(embed=embed)

async def setup(bot: commands.Bot):
    await bot.add_cog(Information(bot))
