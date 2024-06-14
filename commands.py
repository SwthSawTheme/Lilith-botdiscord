import discord
import asyncio
from datetime import timedelta

async def hello(ctx: discord.ApplicationContext):
    embed = discord.Embed(
        title="Meus filhos...",
        description="A salvação não está na luz, está em vocês!",
        color=discord.Colour.red(),
    )
    
    embed.set_footer(text="Os senhores do inferno estão vindo para devorar nosso mundo...")
    embed.set_author(name="Filha do ódio", icon_url="https://assetsio.gnwcdn.com/diablo-4-max-level-lilith.jpg?width=1200&height=1200&fit=crop&quality=100&format=png&enable=upscale&auto=webp")
    embed.set_thumbnail(url="https://static.wikia.nocookie.net/diablo/images/5/52/Lilith_DIV_face2.jpg/revision/latest/scale-to-width-down/1200?cb=20230328014303")
    embed.set_image(url="https://images-ext-1.discordapp.net/external/c5eAZksU1MdpKAn9DyOxYjOZz_DdELNpj-pFF5W7uF8/https/sucodemanga.com.br/wp-content/uploads/2023/03/lilith-diablo-4-primeiro-gole.jpg?format=webp&width=1195&height=670")
 
    await ctx.respond(embed=embed)  # Enviar o embed com algum texto

async def on_member_join(member):
    channel = discord.utils.get(member.guild.channels, name="bem-vindo")  # Altere para o nome do canal desejado
    if channel:
        embed = discord.Embed(
            title="Entrou no Santuario",
            description=f"Bem-vindo(a) ao servidor, {member.mention}!",
            color=discord.Colour.green()
        )
        embed.set_thumbnail(url=member.avatar.url if member.avatar else member.default_avatar.url)
        embed.set_image(url="https://www.gamespot.com/a/uploads/original/1816/18167535/4163070-diablo-4-season-1-prepare-season-of-the-malignant-guide-feat.jpg")
        await channel.send(embed=embed)

async def on_member_remove(member):
    channel = discord.utils.get(member.guild.channels, name="bem-vindo")  # Altere para o nome do canal desejado
    if channel:
        embed = discord.Embed(
            title="Meu filho...sucumbiu a escuridão!",
            description=f"{member.name} deixou santuario.",
            color=discord.Colour.red()
        )
        embed.set_thumbnail(url=member.avatar.url if member.avatar else member.default_avatar.url)
        embed.set_image(url="https://www.pcinvasion.com/wp-content/uploads/2022/12/diablo-iv-release-date-leaked.webp?fit=1200%2C675")
        await channel.send(embed=embed)