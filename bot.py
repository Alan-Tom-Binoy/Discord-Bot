#Bot.py
import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )
@client.event
async def on_message(message):
    if 'happy birthday' in message.content.lower():
        await message.channel.send('Thank You 🎈🎉')

    if 'what is your name?' in message.content.lower():
        await message.channel.send('')
    if 'when is your birthday' in message.content.lower():
        await message.channel.send('')
    if 'who created you' in message.content.lower():
        await message.channel.send('')
client.run(TOKEN)
