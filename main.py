import os
import discord
from dotenv import load_dotenv
import commands

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

# Definir intents
intents = discord.Intents.all()  # Habilitar todos os intents

# Criar uma instância do bot com intents especificadas
bot = discord.Bot(intents=intents)

# Inicia o bot
@bot.event
async def on_ready():
    print(f"{bot.user} Caminha por santuario...")

# Comandos de barra
@bot.slash_command(name="benca", description="Peça bença a mãe...")
async def benca(ctx: discord.ApplicationContext):
    await commands.hello(ctx)
    
# Eventos de membros
@bot.event
async def on_member_join(member):
    await commands.on_member_join(member)

@bot.event
async def on_member_remove(member):
    await commands.on_member_remove(member)

# Executar o bot
bot.run(os.getenv('TOKEN'))