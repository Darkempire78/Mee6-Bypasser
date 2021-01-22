import discord
import json

from discord.ext import commands
from discord.ext.commands import has_permissions

# ------------------------ COGS ------------------------ #  

class RemoveCog(commands.Cog, name="remove command"):
    def __init__(self, bot):
        self.bot = bot

# ------------------------------------------------------ #  

    @commands.command(name = 'remove')
    @has_permissions(administrator = True)
    async def remove (self, ctx, levelNumber):

        # Trying set levelnumber to int
        try:
            levelNumber = int(levelNumber)
        except:
            embed = discord.Embed(title=f"**ERROR**", description=f"The level number must be a number\nFollow the example : ``{self.bot.command_prefix}remove <Level number>``", color=0xe00000) # Red
            embed.set_footer(text="Bot Created by Darkempire#8245")
            return await ctx.channel.send(embed=embed)

        # Read json file
        with open("roles.json", "r+") as roleFile:
            data = json.load(roleFile)
            try:
                # Remove
                numberOfLevelReward = -1
                for x in data["roles"]:
                    numberOfLevelReward += 1
                    if x["level"] == levelNumber:
                        del data["roles"][numberOfLevelReward]
                        newdata = data
            except:
                embed = discord.Embed(title=f"**ERROR**", description=f"The level number is not valid.", color=0xe00000) # Red
                embed.set_footer(text="Bot Created by Darkempire#8245")
                return await ctx.channel.send(embed=embed)

            
            newdata = json.dumps(data, indent=4, ensure_ascii=False)
        
        #  Write new json file
        with open("roles.json", "w") as roleFile:
            roleFile.write(newdata)
        
        embed = discord.Embed(title=f"**SUCCESS**", description=f"The role reward has been remove.", color=0x1eb823) # Green
        embed.set_footer(text="Bot Created by Darkempire#8245")
        await ctx.channel.send(embed=embed)

# ------------------------ BOT ------------------------ #  

def setup(bot):
    bot.add_cog(RemoveCog(bot))