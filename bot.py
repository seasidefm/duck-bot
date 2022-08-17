from datetime import datetime
import os

import discord
from discord import Message

from commands import get_commands

TOKEN = os.environ.get("DISCORD_TOKEN")

client = discord.Client()


@client.event
async def on_ready():
    print("Logged in as")
    print(client.user.name)
    print(client.user.id)
    print("------")

    print("Setting bot presence")

    activity = discord.Game(name="?help")
    await client.change_presence(status=discord.Status.online, activity=activity)

    print("Setup done!")



COMMANDS = get_commands()


@client.event
async def on_message(message: Message):
    if message.content.startswith("?"):
        command, *arg_string = message.content.split(" ", 1)
        arg_string = arg_string[0] if arg_string else ""
        print(f"Command {command} called by {message.author.name}")
        if COMMANDS.get(command):
            reply = await COMMANDS[command](message, arg_string)
            await message.channel.send(reply)


client.run(TOKEN)
