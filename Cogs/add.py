import discord
import json

from discord.ext import commands
from discord.ext.commands import has_permissions

# ------------------------ COGS ------------------------ #  

class AddCog(commands.Cog, name="add command"):
    def __init__(self, bot):
        self.bot = bot

# ------------------------------------------------------ #  

    @commands.command(name = 'add')
    @has_permissions(administrator = True)
    async def add (self, ctx, levelNumber, roleId):

        # Trying set levelnumber to int
        try:
            levelNumber = int(levelNumber)
        except:
            embed = discord.Embed(title=f"**ERROR**", description=f"The level number must be a number\nFollow the example : ``{self.bot.command_prefix}add <Level number> <Role ID>``", color=0xe00000) # Red
            embed.set_footer(text="Bot Created by Darkempire#8245")
            return await ctx.channel.send(embed=embed)
        # Trying set role id to int
        try:
            roleId = int(roleId)
        except:
            embed = discord.Embed(title=f"**ERROR**", description=f"The role id must be a number\nFollow the example : ``{self.bot.command_prefix}add <Level number> <Role ID>``", color=0xe00000) # Red
            embed.set_footer(text="Bot Created by Darkempire#8245")
            return await ctx.channel.send(embed=embed)

        # Read json file
        with open("roles.json", "r+") as roleFile:
            data = json.load(roleFile)
            # Check if the role number exist already
            for x in data["roles"]:
                if (x["level"] == levelNumber):
                    embed = discord.Embed(title=f"**ERROR**", description=f"This level number is alread set.", color=0xe00000) # Red
                    embed.set_footer(text="Bot Created by Darkempire#8245")
                    return await ctx.channel.send(embed=embed)
            # Append
            data["roles"].append({"level": levelNumber, "id": roleId})
            newdata = json.dumps(data, indent=4, ensure_ascii=False)
        
        #  Write new json file
        with open("roles.json", "w") as roleFile:
            roleFile.write(newdata)
        
        embed = discord.Embed(title=f"**SUCCESS**", description=f"The role reward has been set.", color=0x1eb823) # Green
        embed.set_footer(text="Bot Created by Darkempire#8245")
        await ctx.channel.send(embed=embed)

# ------------------------ BOT ------------------------ #  

def setup(bot):
    bot.add_cog(AddCog(bot))