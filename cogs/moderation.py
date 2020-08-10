import discord
from discord.ext import commands
import asyncio


def modlog_embed(title: str, victim: discord.Member, moderator: discord.Member, reason: str = "No reason given") -> discord.Embed:
    embed = discord.Embed(title=title, color=discord.Color.red())
    embed.set_author(name=victim.display_name, icon_url=victim.avatar_url)
    embed.add_field(name="User", value=victim.mention)
    embed.add_field(name="Moderator", value=moderator.mention)
    embed.add_field(name="Reason", value=reason)
    return embed


class Moderation(commands.Cog):

    def __init__(self, client):
        self.client = client

    # Events
    @commands.Cog.listener()
    async def on_ready(self):
        print("Cog <moderation.py> is online.")

    # Commands
    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount: int):
        await ctx.channel.purge(limit=amount + 1)
        msg = await ctx.send(f"{amount} messages cleared by {ctx.author.mention}.")
        await asyncio.sleep(5)
        try:
            await msg.delete()
        except discord.NotFound:
            pass

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        """Kick a specified user, with an optional reason"""
        try:
            await member.kick(reason=reason)
        except commands.CommandInvokeError:
            await ctx.send("That user can't be kicked")
            return None

        embed = modlog_embed("User kicked", member, ctx.author, reason)
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Moderation(client))
