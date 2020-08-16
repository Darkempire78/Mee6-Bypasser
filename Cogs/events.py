import discord
import random 
import asyncio
import time
import os
import datetime

from datetime import datetime
from discord.ext import commands

# ------------------------ COGS ------------------------ #  

class EventsCog(commands.Cog, name="EventsCog"):
    def __init__(self, bot):
        self.bot = bot

# ------------------------------------------------------- #

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            jour = round(error.retry_after/86400)
            heure = round(error.retry_after/3600)
            minute = round(error.retry_after/60)
            if jour > 0:
                await ctx.send('This command has a cooldown, be sure to wait for '+str(jour)+ "day(s)")
            elif heure > 0:
                await ctx.send('This command has a cooldown, be sure to wait for '+str(heure)+ " hour(s)")
            elif minute > 0:
                await ctx.send('This command has a cooldown, be sure to wait for '+ str(minute)+" minute(s)")
            else:
                await ctx.send(f'This command has a cooldown, be sure to wait for {error.retry_after:.2f} second(s)')
        if isinstance(error, (commands.MissingRole, commands.MissingAnyRole)):
            await ctx.send("You do not have the required permission to place this order..")
        else:
            print(error)

# ------------------------ BOT ------------------------ #  

def setup(bot):
    bot.add_cog(EventsCog(bot))