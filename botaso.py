import discord
import random
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

@botsaso.command()
async def emoji(ctx):
    emojis = random.choice(["😀", "😂", "🥳", "😎", "👻", "😍", "😇", "😜","🥶","🤑"])
    await ctx.send(emojis)

@botsaso.command()
async def motivaciones(ctx):
    frases = [
        "¡Sigue adelante, lo estás haciendo genial!",
        "¡Nunca es tarde para aprender algo nuevo!",
        "El éxito llega para quienes trabajan duro.",
        "Recuerda, te mereces lo mejor"
    ]
    await ctx.send(random.choice(frases))

@botsaso.command()
async def meme(ctx):
    memes = [
        "https://i.imgflip.com/2/1otk96.jpg",
        "https://i.blogs.es/d86db0/meme-fry-1/1366_2000.jpg",
        "https://e00-elmundo.uecdn.es/assets/multimedia/imagenes/2018/03/28/15222363072573.jpg"
    ]
    await ctx.send(random.choice(memes))
@botsaso.command()
async def moneda(ctx):
    resultado = random.choice(["Cara", "Cruz"])
    await ctx.send(f"Resultado: {resultado}")


botsaso.run("token")
