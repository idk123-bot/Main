import os
import discord
import time
import asyncio
import logging
from discord.ext import commands
from dotenv import load_dotenv
from Utils.Logger import setup_logging
from Bot import (
    Ping,
    Calculator,
    Rps,
)

setup_logging()
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="$", intents=intents)
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")


@bot.event
async def on_ready():
    CHANNEL_ID = int(os.getenv("DISCORD_CHANNEL"))
    channel = bot.get_channel(CHANNEL_ID)
    if channel:
        await channel.send("I Am Ready!")
        await asyncio.sleep(
            1
        )  # Wait a moment to ensure the message is sent before logging
        await channel.send("I hope you enjoy the games! Type $help for commands.")
        logging.info(f"{bot.user} has connected to Discord!")
    else:
        logging.error("Could not find the channel to send the ready message.")


Ping.setup(bot)
Calculator.setup(bot)
Rps.setup(bot)

bot.run(TOKEN)
