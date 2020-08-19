import discord
import json

from discord.ext import commands
from discord.ext.commands import has_permissions

# ------------------------ COGS ------------------------ #  

class RemovePreviousRewardsCog(commands.Cog, name="removePreviousRewards command"):
    def __init__(self, bot):
        self.bot = bot

# ------------------------------------------------------ #  

    @commands.command(name = 'removepreviousrewards', aliases = ["rpr", "settings"])
    @has_permissions(administrator = True)
    async def rolerewards (self, ctx, trueOrFalse):

        # Read json file
        with open("configuration.json", "r") as configFile:
            data = json.load(configFile)
        
        trueOrFalse = trueOrFalse.lower()
        if trueOrFalse == "false":
            data["removePreviousRewards"] = False
        elif trueOrFalse == "true":
            data["removePreviousRewards"] = True   
        else:
            embed = discord.Embed(title=f"**ERROR**", description=f"The removePreviousRewards setting must be true or false\nFollow the example : ``{self.bot.command_prefix}removePreviousRewards <true/false>``", color=0xe00000) # Red
            embed.set_footer(text="Bot Created by Darkempire#8245")
            return await ctx.channel.send(embed=embed)

        # Write in the json file
        newdata = json.dumps(data, indent=4, ensure_ascii=False)
        with open("configuration.json", "w") as configFile:
            configFile.write(newdata)

        embed = discord.Embed(title=f"**SETTINGS :**", description=f"RemovePreviousRewards setting has been modified.", color=0x1eb823) # Green
        embed.set_footer(text="Bot Created by Darkempire#8245")
        await ctx.channel.send(embed=embed)

# ------------------------ BOT ------------------------ #  

def setup(bot):
    bot.add_cog(RemovePreviousRewardsCog(bot))