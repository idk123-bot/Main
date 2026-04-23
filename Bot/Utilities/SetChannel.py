# Bot/Utilities/SetChannel.py
import discord
from discord.ext import commands
from Utils.Config import (
    add_allowed_channel,
    remove_allowed_channel,
    get_allowed_channels,
)
from Utils.Logger import setup_logging

logging = setup_logging()


def setup(bot):
    @bot.command(name="setchannel", aliases=["SetChannel", "SETCHANNEL"])
    @commands.has_permissions(administrator=True)
    async def set_channel(ctx, channel: discord.TextChannel = None):
        """Add a channel where the bot can send announcements."""
        if channel is None:
            channel = ctx.channel

        add_allowed_channel(ctx.guild.id, channel.id)
        await ctx.send(f"✅ {channel.mention} added to allowed channels!")
        logging.info(f"{ctx.author} added {channel.name} in {ctx.guild.name}")

    @bot.command(name="removechannel", aliases=["RemoveChannel", "REMOVECHANNEL"])
    @commands.has_permissions(administrator=True)
    async def remove_channel(ctx, channel: discord.TextChannel = None):
        """Remove a channel from allowed channels."""
        if channel is None:
            channel = ctx.channel

        remove_allowed_channel(ctx.guild.id, channel.id)
        await ctx.send(f"🗑️ {channel.mention} removed from allowed channels!")
        logging.info(f"{ctx.author} removed {channel.name} in {ctx.guild.name}")

    @bot.command(name="channels", aliases=["Channels", "CHANNELS"])
    @commands.has_permissions(administrator=True)
    async def list_channels(ctx):
        """List all allowed channels for this server."""
        channels = get_allowed_channels(ctx.guild.id)
        if not channels:
            await ctx.send("No channels set! Use `!setchannel #channel` to add one.")
            return

        mentions = []
        for cid in channels:
            channel = ctx.guild.get_channel(cid)
            if channel:
                mentions.append(channel.mention)

        await ctx.send(f"📋 Allowed channels: {', '.join(mentions)}")
