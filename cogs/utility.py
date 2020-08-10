import discord
from discord.ext import commands


class Utility(commands.Cog):

    def __init__(self, client):
        self.client = client

    # Functions

    # Events
    @commands.Cog.listener()
    async def on_ready(self):
        print("Cog <Utility.py> is online.")

    @commands.command(aliases=["git"])
    async def github(self, ctx):
        """Links the github for the bot"""
        await ctx.send("Here is the github for the bot:\nhttps://github.com/justsomeonenamedalex/RulerBot")


def setup(client):
    client.add_cog(Utility(client))
