import os
import discord
from dotenv import load_dotenv
import commands

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

# Definir intents
intents = discord.Intents.default()
intents.message_content = True

# Criar uma instância do bot com intents especificadas
bot = discord.Bot(intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user} Caminha por santuario...")

@bot.slash_command(name="benca", description="Peça bença a mãe...")
async def benca(ctx: discord.ApplicationContext):
    await commands.hello(ctx)

# Executar o bot
bot.run(os.getenv('TOKEN'))