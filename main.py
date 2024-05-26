import os
import discord
from dotenv import load_dotenv

load_dotenv()
token = os.getenv("token")

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} caminha por santuario...')
    
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('/Olá'):
        await message.channel.send(f'olá {message.author}')

client.run(token)

