import discord
from discord.ext import commands
import datetime
import os
import random
from urllib import parse, request
import re
from dotenv import load_dotenv

bot = commands.Bot(command_prefix='<', description="Bot d'Assistance")
load_dotenv()
TOKEN = os.getenv('token')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user.name} s\'est connecté au discord !')

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Salut {member.name}, bienvenue sur f"{ctx.guild.name}"!'
    )

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    brooklyn_99_quotes = [
        'j\'suis humain à 💯%.',
        'Jackpot!',
        (
            'Cool. Cool cool cool cool cool cool cool, '
            ' Pas cool Pas cool Pas cool Pas cool Pas cool Pas cool.'
        ),
    ]

@client.event
async def on_message(message):
    if 'joyeux anniversaire' in message.content.lower():
        await message.channel.send('WHOUOUO JOYEUX ANNIV\'! 🎈🎉')


@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def info(ctx):
    embed = discord.Embed(title=f"{ctx.guild.name}", description="le serveur :", timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
    embed.add_field(name="Serveur crée le ", value=f"{ctx.guild.created_at}")
    embed.add_field(name="Propriétaire ", value=f"{ctx.guild.owner}")
    embed.add_field(name="Région du serveur", value=f"{ctx.guild.region}")
    embed.add_field(name="ID du serveur", value=f"{ctx.guild.id}")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/699981231835709573/699982688404111400/OIPKTR3L0LD.jpg")

    await ctx.send(embed=embed)

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Streaming(name="un truc de ouf", url="https://www.youtube.com/channel/UC8kTw7zUbP5QMTG0jCLjKMg"))
    print('J\'suis pret papa')



bot.run('Token')
