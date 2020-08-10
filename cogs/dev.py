import discord
from discord.ext import commands

# Dev stuff
# DO NOT TOUCH THIS FILE UNLESS YOU HAVE TO


class Dev(commands.Cog):

    def __init__(self, client):
        self.client = client

    # Events
    @commands.Cog.listener()
    async def on_ready(self):
        """Runs when the cog is loaded, so i know it's working"""
        print(f"Cog <dev.py> is online.")

    # Commands
    @commands.is_owner()
    @commands.command(hidden=True)
    async def load(self, ctx, extension: str):
        """Loads a cog"""
        try:
            self.client.load_extension(f"cogs.{extension}")
            await ctx.send(f"{extension} loaded.")

        except commands.NoEntryPointError as e:
            # Runs if the cog has no entry point
            # Not sure if I need this but I might as well cover everything
            await ctx.send(f"Extension {e.name} has no entry point.")

        except commands.ExtensionFailed as e:
            # Runs if there is an error in the code
            await ctx.send(f"Failed to load extension {e.name}, due to a code error:\n`{e.original}`")

        except commands.ExtensionAlreadyLoaded as e:
            await ctx.send(f"Extension {e.name} is already loaded.")

        except commands.ExtensionNotFound as e:
            await ctx.send(f"Extension {e.name} not found.")

    @commands.is_owner()
    @commands.command(hidden=True)
    async def unload(self, ctx, extension: str):
        """Unloads a cog"""
        try:
            self.client.unload_extension(f"cogs.{extension}")
            await ctx.send(f"{extension} unloaded.")

        except commands.ExtensionFailed as e:
            # Runs if there is an error in the code
            await ctx.send(f"Failed to unload extension {e.name}, due to a code error:\n`{e.original}`")

        except commands.ExtensionNotLoaded as e:
            await ctx.send(f"Extension {e.name} is not loaded")

        except commands.ExtensionNotFound as e:
            await ctx.send(f"Extension {e.name} not found.")

    @commands.is_owner()
    @commands.command(hidden=True)
    async def reload(self, ctx, extension: str):
        """Unloads, then loads a cog"""
        # TODO: do this by invoking the other commands
        # Unload the cog
        try:
            self.client.unload_extension(f"cogs.{extension}")
            await ctx.send(f"{extension} unloaded.")

        except commands.ExtensionFailed as e:
            await ctx.send(f"Failed to unload extension {e.name}, due to a code error:\n`{e.original}`")

        except commands.ExtensionNotLoaded as e:
            await ctx.send(f"Extension {e.name} is not loaded")

        except commands.ExtensionNotFound as e:
            await ctx.send(f"Extension {e.name} not found.")

        # Load the cog
        try:
            self.client.load_extension(f"cogs.{extension}")
            await ctx.send(f"{extension} loaded.")

        except commands.NoEntryPointError as e:
            # Not sure if I need this but I might as well cover everything
            await ctx.send(f"Extension {e.name} has no entry point.")

        except commands.ExtensionFailed as e:
            await ctx.send(f"Failed to load extension {e.name}, due to a code error:\n`{e.original}`")

    @commands.is_owner()
    @commands.command(aliases=["shutdown"], hidden=True)
    async def off(self, ctx):
        """Safely shuts down the bot"""
        await ctx.send("Bot shutting down")

        await self.client.change_presence(status=discord.Status.offline)
        await self.client.logout()

    @commands.command(hidden=True)
    async def ping(self, ctx):
        """Returns the latency of the bot in ms"""
        await ctx.send(f"Pong! `{round(self.client.latency*1000)}ms`")
        print(f"Pong! {round(self.client.latency*1000)}ms")


def setup(client):
    client.add_cog(Dev(client))
