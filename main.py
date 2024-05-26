import os
import discord
from dotenv import load_dotenv

load_dotenv()
token = os.getenv("token")

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'{self.user} está caminhando por santuario...')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(token)
