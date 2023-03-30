import discord
from discord.ext import commands
from main import db

class Mod(commands.Cog):
        
        # Ban
        @commands.bot_has_guild_permissions(ban_members=True)
        @commands.has_guild_permissions(ban_members=True)
        @commands.hybrid_command(name="ban")
        @discord.app_commands.describe(member="Select a member", reason="Write the reason")
        async def ban(self, ctx: commands.Context, member: discord.Member, reason = "No reason"):
            """Ban a guild user"""
            if member.id == ctx.author.id:
                return await ctx.send("You can't do that")
            if member.id == ctx.guild.owner_id:
                return await ctx.send("Cannot ban the server owner")
            if member.id == ctx.bot.user.id:
                return await ctx.send("Why?")
            if member.guild_permissions.administrator:
                return await ctx.send("You can't ban administrators")
            if member.top_role.position >= ctx.author.top_role.position:
                return await ctx.send("The member has a higher role than yours")
            if member.top_role.position >= ctx.guild.me.top_role.position:
                return await ctx.send("The user has a higher role than mine.")
            try:
                await member.ban(reason=reason)
                await ctx.send(f"**{member._user.name}#{member.discriminator}** was banned")
            except:
                await ctx.send("Cannot ban the member")


        # Unban
        @commands.bot_has_guild_permissions(ban_members=True)
        @commands.has_guild_permissions(ban_members=True)
        @commands.hybrid_command(name="unban")
        @discord.app_commands.describe(user="User", reason="Reason")
        async def unban(self, ctx: commands.Context, user: discord.User, reason="No reason"):
            """Unban a user from this server"""
            try:
                await ctx.guild.fetch_ban(user)
            except: 
                return await ctx.send("The user is not banned")
            try:
                await ctx.guild.unban(user, reason=reason)
                await ctx.send(f"**{user.name}#{user.discriminator}** was unbanned")
            except:
                return await ctx.send("Cannot unban the user")


        # Kick
        @commands.bot_has_guild_permissions(kick_members=True)
        @commands.has_guild_permissions(kick_members=True)
        @commands.hybrid_command(name="kick")
        @discord.app_commands.describe(member="Select a member", reason="Write the reason")
        async def kick(self, ctx: commands.Context, member: discord.Member, reason = "No reason"):
            """Kick a guild user"""
            if member.id == ctx.author.id:
                return await ctx.send("You can't do that")
            if member.id == ctx.guild.owner_id:
                return await ctx.send("Cannot kick the server owner")
            if member.id == ctx.bot.user.id:
                return await ctx.send("Why?")
            if member.guild_permissions.administrator:
                return await ctx.send("You can't kick administrators")
            if member.top_role.position >= ctx.author.top_role.position:
                return await ctx.send("The member has a higher role than yours")
            if member.top_role.position >= ctx.guild.me.top_role.position:
                return await ctx.send("The user has a higher role than mine.")
            try:
                await member.kick(reason=reason)
                await ctx.send(f"**{member._user.name}#{member.discriminator}** it was kicked")
            except:
                await ctx.send("Cannot kick the member")


        # ----> Channel | Lock & UnLock <----

        #@commands.hybrid_group(name="channel")
        #async def channel(self, ctx: commands.Context):
        #    """Lock or unlock an channel"""


        # Lock
        @commands.bot_has_guild_permissions(manage_channels=True, manage_roles=True)
        @commands.has_guild_permissions(manage_channels=True, manage_roles=True)
        @commands.hybrid_command(name="lock")
        @discord.app_commands.describe(channel="Select a channel")
        async def lock(self, ctx: commands.Context, channel: discord.TextChannel = None):
            """Lock a channel"""
            if channel is None:
                channel = ctx.channel
            if not channel.permissions_for(ctx.guild.default_role).send_messages:
                await channel.set_permissions(ctx.guild.default_role, send_messages=False)
            await ctx.send(f":lock: **Channel {channel.mention} has been locked**")


        # Unlock
        @commands.bot_has_guild_permissions(manage_channels=True, manage_roles=True)
        @commands.has_guild_permissions(manage_channels=True, manage_roles=True)
        @commands.hybrid_command(name="unlock")
        @discord.app_commands.describe(channel="Select a channel")
        async def unlock(self, ctx: commands.Context, channel: discord.TextChannel = None):
            """Unlock a channel"""
            if channel is None:
                channel = ctx.channel
            if not channel.permissions_for(ctx.guild.default_role).send_messages:
                await channel.set_permissions(ctx.guild.default_role, send_messages=True)
            await ctx.send(f":unlock: **Channel {channel.mention} has been unlocked**")

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

async def setup(bot: commands.Bot):
    await bot.add_cog(Mod(bot))
