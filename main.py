#!/usr/bin/env python3

import discord
import random 
import asyncio
import time
import os
import sys
import json

from datetime import datetime
from discord.ext import commands
from discord.ext import tasks
from discord.ext.commands import AutoShardedBot as asb

started = False

class Greetings(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

class Mee6Bypasser(asb):
    def __init__(self):
        super().__init__(
            command_prefix=commands.when_mentioned_or("?"),
            case_insensitive=True
            intents=discord.Intents.all(), # remove this if you dont want to enable all intents
            help_command=None
        )
        
        self.remove_command("help")
        self.cog_blacklist = [
            "__init__.py",
            "functions.py"
        ]
        
        if not started:
            print("Loading cogs:")
            for file in os.listdir("./Cogs"):
                if file.endswith(".py") and not file in self.cog_blacklist:
                    try:
                        self.load_extension(f"Cogs.{file[:-3]}")
                        print(f"    Loaded '{file}'")
                    except Exception as e:
                        print(str(e))
            started = True # doing this so it doesnt load cogs every time its initialised

    async def on_connect(self):
        print("Connected")
    async def on_ready(self):
        print("Ready")
        await self.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name =f"{bot.get_prefix}help"))

if __name__ == "__main__":
    with open("configuration.json", "r") as f:
        config = json.load(f)
    bot = Mee6Bypasser()
    bot.run(config["token"])
