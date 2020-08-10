import discord
from discord.ext import commands
import asyncio


class Errors(commands.Cog):

    def __init__(self, client):
        self.client = client

    # Events
    @commands.Cog.listener()
    async def on_ready(self):
        print("Cog <Errors.py> is online.")

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        """Proper handling for errors in commands"""

        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Please pass in all required arguments.")
            print(f"{ctx.author.mention} had error '{error}' in command '{ctx.message.content}'")

        elif isinstance(error, commands.CommandNotFound):
            print(f"{ctx.author.mention} had error '{error}' in command '{ctx.message.content}'")

        elif isinstance(error, commands.MissingPermissions):
            await ctx.send("You do not have permission to run that command.")
            print(f"{ctx.author.mention} had error '{error}' in command '{ctx.message.content}'")

        elif isinstance(error, commands.CommandInvokeError):
            await ctx.send(f"The bot was unable to run the command for the following reason:\n{error}")

        else:
            print(f"{ctx.author.mention} had error '{error}' in command '{ctx.message.content}'")


def setup(client):
    client.add_cog(Errors(client))
