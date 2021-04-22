import discord
import json

from discord.ext import commands
from discord.utils import get

from datetime import datetime

from mee6_py_api import API

# ------------------------ COGS ------------------------ #  

class OnMessageCog(commands.Cog, name="on message"):
    def __init__(self, bot):
        self.bot = bot

# ------------------------------------------------------ #  

    @commands.Cog.listener()
    async def on_message(self, message):

        if (message.author.bot):
            return

        # Check config json
        with open("configuration.json", "r") as configFile:
            config = json.load(configFile)

        if config["updateEachMessage"]:
            # Find guild id
            guild_id = message.guild.id
            mee6API = API(guild_id)
            
            # Check user level
            user_id = message.author.id
            userLevel = await mee6API.levels.get_user_level(user_id)

            if userLevel is None:
                date = datetime.datetime.now().strftime("%x %X")
                return print(f"{date} The search for the player's level failed.")

            # Check roles json
            with open("roles.json", "r") as roleFile:
                data = json.load(roleFile)
            
            # Add role
            for x in data["roles"]:
                if x["level"] <= userLevel:
                    if x["id"] not in [y.id for y in message.author.roles]: # Check if user has not the role
                        getrole = get(message.guild.roles, id = x["id"])
                        await message.author.add_roles(getrole)

                        # Remove previous roles
                        if config["removePreviousRewards"]:
                            for userRole in message.author.roles:
                                if (userRole.id in [roleReward["id"] for roleReward in data["roles"]]) and userRole.id != x["id"]:
                                    getrole = get(message.guild.roles, id = x["id"])
                                    await message.author.remove_roles(getrole)


                # elif config["removePreviousRewards"] == True:
                #     if x["id"] in [y.id for y in message.author.roles]:
                #         getrole = get(message.guild.roles, id = x["id"])
                #         await message.author.remove_roles(getrole)

# ------------------------ BOT ------------------------ #  

def setup(bot):
    bot.add_cog(OnMessageCog(bot))

