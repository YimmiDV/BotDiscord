import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

botsaso = commands.Bot(command_prefix="/",intents=intents)

@botsaso.event
async def on_ready():
    print(f"hola se ha iniciado el bot {botsaso.user}")

@botsaso.command()
async def hola(ctx):
    await ctx.send(f"hola mucho gusto yo soy {botsaso.user}")

botsaso.run("pon tu TOKEN aqui")
