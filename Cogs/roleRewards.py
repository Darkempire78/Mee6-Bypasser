import discord
import json

from discord.ext import commands

# ------------------------ COGS ------------------------ #  

class RoleRewardsCog(commands.Cog, name="roleRewards command"):
    def __init__(self, bot):
        self.bot = bot

# ------------------------------------------------------ #  

    @commands.command(name = 'rolerewards', aliases = ["rr", "show", "rolelist"])
    async def rolerewards(self, ctx):

        # Read json file
        with open("roles.json", "r") as roleFile:
            data = json.load(roleFile)
            levelList = [x["level"] for x in data["roles"]]
        # Sort the list
        levelList.sort()

        embedContent = ""
        for levelListNumber in levelList:
            for x in data["roles"]:
                if levelListNumber == x["level"]:
                    embedContent = embedContent + f"Level : **{levelListNumber}** > Role reward : <@&" + str(x["id"]) + ">\n"

        embed = discord.Embed(title=f"**MEE6 ROLE REWARDS :**", description=f"{embedContent}", color=0x1eb823) # Green
        embed.set_footer(text="Bot Created by Darkempire#8245")
        await ctx.channel.send(embed=embed)

# ------------------------ BOT ------------------------ #  

def setup(bot):
    bot.add_cog(RoleRewardsCog(bot))