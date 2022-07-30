# bot.py
import os
import discord
from discord.ext import commands, tasks
import birthday_logic
import logging

logging.basicConfig(level=logging.INFO)

TOKEN = os.environ['DISCORD_TOKEN']
CHANNEL = os.environ['DISCORD_CHANNEL_ID']
client = discord.Client()

@client.event
async def on_ready():
    logging.debug(TOKEN)
    logging.debug(CHANNEL)
    logging.info(f'{client.user} has connected to Discord!')
    birthday_check_task.start()


@tasks.loop(seconds = 0, minutes=0, hours=24.0, count=None)
async def birthday_check_task():
    logging.info("Time to check our birthdays")
    channel = client.get_channel(int(CHANNEL))
    logging.debug(channel)
    users = birthday_logic.check_for_all_known_birthdays()
    logging.debug(users)
    for user in users:
        message = birthday_logic.generate_birthday_message(user)
        await channel.send(message)

client.run(TOKEN)
