import discord
from discord.ext import commands

class CustomDropdown(discord.ui.Select):
    def __init__(self):

        options = [
            discord.SelectOption(label='Utility'),
            discord.SelectOption(label='Information'),
            discord.SelectOption(label='Moderation'),
        ]

        super().__init__(placeholder='Select a category', min_values=1, max_values=1, options=options)
    
    async def callback(self, interaction: discord.Interaction):
        VALUE = interaction.data['values'][0]
        print(VALUE)
        if VALUE =="Utility":
            embed = discord.Embed(colour=1399944)
            embed.set_author(name="Util commands")
            embed.description = "**</help:0> -> Help command \n </reverse:0> -> Reverse a text \n </say:0> -> I repeat your text**"
            await interaction.response.edit_message(embed=embed)

        elif VALUE =="Information":
                embed = discord.Embed(colour=1399944)
                embed.title = "Information commands"
                embed.description = "**</userinfo:0> -> Get a user information \n </serverinfo:0> -> Get the server information \n </channel:0> -> Get a channel information \n </role:0> -> Get a role information \n </botinfo:0> -> Get the bot information \n </ping:0> -> Show my ping \n </avatar:0> -> Get a user avatar \n </icon:0> -> Get the server icon**"
                await interaction.response.edit_message(embed=embed)

        elif VALUE=="Moderation":
            try:
                embed = discord.Embed(colour=1399944)
                embed.title = "Moderation commands"
                embed.description = "**</ban:0> -> Ban a user from the guild \n </unban:0> -> Unban a user from the guild \n </kick:0> -> Kick a user from the guild \n </lock:0> -> Lock a channel \n </unlock:0> -> Unlock a channel \n </prefix:0> -> Set a new prefix in this server**"
                await interaction.response.edit_message(embed=embed)
            except Exception as err:
                print(err)
        try:
                pass
        except Exception as err:
                print(err)

class DropdownView(discord.ui.View):
    def __init__(self):
        super().__init__()

        self.add_item(CustomDropdown())
