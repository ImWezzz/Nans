import discord, asyncio, os
from discord.ui import Select, View
from discord.ext import commands
from midb import Database

db = Database(path="/database", tables=["main", "guilds", "users"])

async def get_prefix(client, message: discord.Message):
    if not message.guild:
        return '-'
    return db.get(f"{message.guild.id}.prefix", "guilds") or "-" 

bot = commands.Bot(
    help_command=None,
    case_insensitive=True,
    command_prefix=get_prefix,
    owner_ids=[664261902712438784, 759233882926350346],
    strip_after_prefix=True,
    intents=discord.Intents.all(),
    activity=discord.Activity(type=discord.ActivityType.listening, name="-help")
)

async def main():
    for file in os.listdir('./cogs'):
        if file.endswith('.py'):
            await bot.load_extension(f'cogs.{file[:-3]}')
    async with bot:
        await bot.start("TOKEN")

@bot.check
async def guild_only(ctx: commands.Context):
    if ctx.guild is None:
        return
    return ctx.guild != None

if __name__ == "__main__":
    asyncio.run(main())
