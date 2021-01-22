import discord
from discord.ext import commands, tasks
from discord.utils import get

import json
from mee6_py_api import API
from math import ceil


class CogTask(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.updateRoles.start()


    @tasks.loop(minutes=5)
    async def updateRoles(self):
        with open("configuration.json", "r") as configFile:
            config = json.load(configFile)

        for guildId in config["updateEachTime"]:
            guild = self.bot.get_guild(guildId)
            if guild:
                with open("roles.json", "r") as roleFile:
                    data = json.load(roleFile)

                mee6API = API(guild.id)
                pageNumber = ceil(len(guild.members)/100)
                for i in range(pageNumber):
                    leaderboard_page = await mee6API.levels.get_leaderboard_page(i)
                    for user in leaderboard_page["players"]:
                        # If user in the guild
                        if int(user["id"]) in [guildMember.id for guildMember in guild.members]:
                            # Add role
                            for x in data["roles"]:
                                if x["level"] <= user["level"]:
                                    if x["id"] not in [roleId for roleId in [guildMember.roles for guildMember in guild.members if guildMember.id == int(user["id"])]]: # Check if user has not the role
                                        getrole = get(guild.roles, id = x["id"])
                                        member = [guildMember for guildMember in guild.members if guildMember.id == int(user["id"])]
                                        await member[0].add_roles(getrole)
                                elif config["removePreviousRewards"] == True:
                                    if x["id"] in [roleId for roleId in [guildMember.roles for guildMember in guild.members if guildMember.id == int(user["id"])]]: # Check if user has the role
                                        getrole = get(guild.roles, id = x["id"])
                                        member = [guildMember for guildMember in guild.members if guildMember.id == int(user["id"])]
                                        await member[0].remove_roles(getrole)
                

    @updateRoles.before_loop
    async def before_updateRoles(self):
        await self.bot.wait_until_ready()

def setup(bot):
    bot.add_cog(CogTask(bot))