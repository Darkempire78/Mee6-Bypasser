import discord
from discord.ext import commands
from discord.utils import get

import json
from mee6_py_api import API
from math import ceil


class CogLeaderboard(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command(name = "leaderboard",
                    usage="")
    @commands.guild_only()
    @commands.cooldown(1, 2, commands.BucketType.member)
    async def leaderboard(self, ctx):

        waitMessage = await ctx.channel.send("Please wait during the update...")
        # Check roles json
        with open("roles.json", "r") as roleFile:
            data = json.load(roleFile)
        # Check config json
        with open("configuration.json", "r") as configFile:
            config = json.load(configFile)

        mee6API = API(ctx.guild.id)
        pageNumber = ceil(len(ctx.guild.members)/100)
        for i in range(pageNumber):
            leaderboard_page = await mee6API.levels.get_leaderboard_page(i)
            for user in leaderboard_page["players"]:
                # If user in the guild
                if int(user["id"]) in [guildMember.id for guildMember in ctx.guild.members]:
                    # Add role
                    for x in data["roles"]:
                        if x["level"] <= user["level"]:
                            if x["id"] not in [roleId for roleId in [guildMember.roles for guildMember in ctx.guild.members if guildMember.id == int(user["id"])]]: # Check if user has not the role
                                getrole = get(ctx.guild.roles, id = x["id"])
                                member = [guildMember for guildMember in ctx.guild.members if guildMember.id == int(user["id"])]
                                await member[0].add_roles(getrole)
                        elif config["removePreviousRewards"] == True:
                            if x["id"] in [roleId for roleId in [guildMember.roles for guildMember in ctx.guild.members if guildMember.id == int(user["id"])]]: # Check if user has the role
                                getrole = get(ctx.guild.roles, id = x["id"])
                                member = [guildMember for guildMember in ctx.guild.members if guildMember.id == int(user["id"])]
                                await member[0].remove_roles(getrole)
        await waitMessage.delete()
        embed = discord.Embed(title=f"**LEADERBOARD :**", description=f"Everyone has been updated.", color=0x1eb823) # Green
        embed.set_footer(text="Bot Created by Darkempire#8245")
        await ctx.channel.send(embed=embed)


def setup(bot):
    bot.add_cog(CogLeaderboard(bot))