import os

import discord
from discord.ext import commands

from util.config import *

bot = commands.Bot(command_prefix=prefix)


def load_cogs(path: str):
    for filename in os.listdir(path):
        if filename.endswith(".py"):
            try:
                bot.load_extension(f"cogs.{filename[:-3]}")
            except commands.ExtensionFailed as e:
                print(f"Failed to load {e.name}:\n{e.original}")


@bot.event
async def on_ready():
    """This function runs when the bot starts up"""
    await bot.change_presence(status=discord.Status.online, activity=discord.Game(activity))

load_cogs("./cogs")
bot.run(token)
