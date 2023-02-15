import discord
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Access environment variables
BOT_TOKEN = os.getenv('BOT_TOKEN')

intents = discord.Intents().all()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"Logged in as {client.user.name}")

@client.event
async def on_voice_state_update(member, before, after):
    if after.channel is not None:
        if member != client.user:  # Exclude the bot itself
            channel = after.channel
            members = channel.members
            print(f"Users in {channel.name}:")
            for member in members:
                print(member.name)

client.run(BOT_TOKEN)
