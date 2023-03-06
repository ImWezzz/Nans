import discord, asyncio, os
from discord.ext import commands
from midb import Database

db = Database(path="/database", tables=["main", "guilds", "users"])

async def get_prefix(client, message: discord.Message):
    if not message.guild:
        return 'w!'
    return db.get(f"{message.guild.id}.prefix", "guilds") or "w!" 

bot = commands.Bot(
    case_insensitive=True,
    command_prefix=get_prefix,
    owner_ids=[664261902712438784, 759233882926350346],
    strip_after_prefix=True,
    intents=discord.Intents.all(),
    activity=discord.Activity(type=discord.ActivityType.listening, name="Wez ;3")
)

async def main():
    for file in os.listdir('./cogs'):
        if file.endswith('.py'):
            await bot.load_extension(f'cogs.{file[:-3]}')
    async with bot:
        await bot.start("TOKEN")

@bot.event
async def on_guild_join(guild: discord.Guild) -> None:
    channel = await bot.fetch_channel(1057367206066921582)

    await channel.send(f"""\n Name: {guild.name}
        ID: {guild.id}
        Owner: <@{guild.owner_id}>
        Created: <t:{round(guild.created_at.timestamp())}> <t:{round(guild.created_at.timestamp())}:D>
        Members: {guild.member_count} 
        Channels: {len(guild.channels)}
        Roles: {len(guild.roles)} 

        Ahora estoy en: {len(bot.guilds)} servers con {len(bot.users)} users
    """)
    
@bot.check
async def guild_only(ctx: commands.Context):
    if ctx.guild is None:
        return
    return ctx.guild != None

if __name__ == "__main__":
    asyncio.run(main())
