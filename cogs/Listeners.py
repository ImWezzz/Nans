from discord.ext import commands

class Listeners(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_command_error(self, ctx: commands.Context, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(f"Missing **{error.param.name}** parameter")
        elif isinstance(error, commands.MemberNotFound):
            await ctx.send(f"Member not found")
        elif isinstance(error, commands.UserNotFound):
            await ctx.send(f"User not found")
        elif isinstance(error, commands.MissingPermissions):
            await ctx.send(f"Missing **{', '.join(list(map(lambda s: f'`{s}`', error.missing_permissions)))}** permissions")
        elif isinstance(error, commands.ChannelNotFound):
            await ctx.send(f"Channel not found")
        elif isinstance(error, commands.RoleNotFound):
            await ctx.send(f"Role not found")
        elif isinstance(error, commands.BotMissingPermissions):
            await ctx.send(f"I missing **{', '.join(list(map(lambda s: f'`{s}`', error.missing_permissions)))}** permissions")
        else:
            raise error
    
    @commands.Cog.listener()
    async def on_ready(self):
        print(f"Successfully connected! \n In: {self.bot.user.name} \n Servers: {len(self.bot.guilds)} \n Users: {len(self.bot.users)} \n Commands: {len(self.bot.commands)} \n Ping: {round(self.bot.latency, 2) * 1000}ms")
        await self.bot.tree.sync()

# setup
async def setup(bot: commands.Bot):
    await bot.add_cog(Listeners(bot))
