import discord
from discord.ext import commands

class CustomDropdown(discord.ui.Select):
    def __init__(self):
        options = [
            discord.SelectOption(label='Utility', description='Get util commands'),
            discord.SelectOption(label='Information', description='Get information commands'),
            discord.SelectOption(label='Moderation', description='Get moderation commands'),
        ]

        super().__init__(placeholder='Select a category', min_values=1, max_values=1, options=options)
    
    async def callback(self, interaction: discord.Interaction):
        VALUE = interaction.data['values'][0]
        print(VALUE)
        if VALUE =="Utility":
            embed = discord.Embed(colour=14474460)
            embed.set_author(name="Util commands")
            embed.description = "> **Total: 3 commands | Prefix and Slash** \n\n **Command ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ Description \n </help:0>‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ Commands list \n </say:0>‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ I repetar your text \n </reverse:0>‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ Reverse your text**"
            await interaction.response.edit_message(embed=embed)

        elif VALUE =="Information":
                embed = discord.Embed(colour=14474460)
                embed.set_author(name="Information commands")
                embed.description = "> **Total: 8 commands | Prefix & Slash** \n\n**Command ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ Description \n </userinfo:0>‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ Get a user information \n </serverinfo:0> ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ Get the server information \n </botinfo:0>‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ Get the bot info \n </icon:0>‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ Get the server icon \n </ping:0>  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ Show my ping \n </channel:0> ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ Get a channel information \n </avatar:0> ‎ ‎ ‎ ‎ ‎‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ Get a user avatar**"
                await interaction.response.edit_message(embed=embed)

        elif VALUE=="Moderation":
            try:
                embed = discord.Embed(colour=14474460)
                embed.set_author(name="Moderation commands")
                embed.description = "> **Total: 6 commands | Prefix & Slash** \n\n**Command** ㅤㅤㅤㅤㅤ**Description \n</ban:0>ㅤㅤㅤㅤㅤㅤㅤㅤBan a user form this guild \n </unban:0>ㅤ ㅤㅤㅤㅤㅤㅤUnban a user from this guild \n </kick:0>ㅤㅤㅤㅤㅤㅤㅤㅤKick a user from this guild \n </lock:0>ㅤㅤㅤㅤㅤㅤㅤㅤLock a channel \n </unlock:0>ㅤㅤㅤㅤㅤㅤㅤUnlock a channel \n </prefix:0>ㅤㅤㅤㅤㅤㅤㅤSet a new prefix in this guild**"
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
