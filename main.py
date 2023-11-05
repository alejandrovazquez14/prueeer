import discord
import os
import random
import requests
from discord.ext import commands


img_names = ['mem1.jpg', 'mem2.jpg', 'mem3.jpg', 'mem4.jpg', 'mem5.jpg', 'mem6.jpg']

intents = discord.Intents.default()
intents.message_content = True


bot = commands.Bot(command_prefix='', intents=intents)


def get_duck_image_url():
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']

def select_mem_image():
    # Probabilidades de rareza (70% normal y 30% raro)
    rareza = random.choices(['normal', 'raro'], weights=[0.7, 0.3])[0]
    
    if rareza == 'normal':
        return random.choice(img_names[:3])  # Imágenes normales (mem1, 2, 3)
    else:
        return random.choice(img_names[3:])  # Imágenes raras (mem4, 5, 6)

@bot.event
async def on_ready():
    print(f'Hemos iniciado sesión como {bot.user}')

@bot.command()
async def hola(ctx):
    author_name = ctx.author.display_name
    await ctx.send(f'Hola, {author_name}!')

@bot.command(name='mem')
async def mem(ctx):
    selected_image = random.choice(img_names)
    img_path = os.path.join('images', selected_image)
    if os.path.exists(img_path):
        with open(img_path, 'rb') as f:
            picture = discord.File(f)
        await ctx.send(file=picture)
    else:
        await ctx.send("La imagen no fue encontrada.")

@bot.command(name='duck')
async def duck(ctx):
    image_url = get_duck_image_url()
    await ctx.send(image_url)

bot.run("token")
