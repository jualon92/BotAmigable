

import aiocron
from personas import shaxi, juani
from fabricaUA import getUa
import os
from latidos import mantener_vivo
from discord.ext import commands
import random
import requests
import aiohttp
import json
from mercado import get_item_price, get_plex_price, obtener_historia

nro_canal = 791515934237917244
nro_general = 828489491450560603
nro_echoes = 719244116713799702
val = True
presentes = []
usuarios_ignorar = []
cMensajes = 0

bot = commands.Bot(command_prefix='!')


listaQuien = [  # data deberia tener su import
    "qin ti priginti prrin",
    "who asked you, little doggie"
]

  
# command implementa !help con resumen de comandos, y utiliza prefijo

# personas se juntan a elegir quien le toca primero y a quien ultimo aleatoriamente
@bot.command(name="rank_random", help="devuelve ranking entre nombres aleatorio => rank_random p1 p2 p3...")
async def tirar_dado(ctx, *argv):
    contador = 0
    personasLista = ""
    # personasLista = f"{nombre} \n"
    listaNueva = random.sample(argv, len(argv))  # agregar un titulo dificulta
    for arg in listaNueva:
        # podria utilizarse lista.index(ele). pero con contador ya empieza ranking en 1
        contador = contador + 1
        # nombre = arg
        fraseNueva = f"{str(contador)} puesto: {arg} \n"
        # fraseNueva = str(contador) + " puesto: " + " " + nombre  +    "\n"
        personasLista = personasLista + fraseNueva
    await ctx.send(personasLista)


@bot.command(name="plex", help="precio de plex en Eve Online desde api ")
async def obtener_plex_precio(ctx):
    await get_plex_price(ctx)
     

@bot.command(name="precio", help="precio de item en Eve Online desde api ")
async def obtener_item_precio(ctx, *args):
    await get_item_price(ctx, *args)
    

@bot.command(name="history", help="precio de item en Eve Online desde api ")
async def obtener_history(ctx, id):
    await obtener_historia(ctx,id)
    

@bot.event  # listener mensajes
async def on_message(message):
    global val
    global presentes
    global resultado
    id_persona = message.author.id
    mensaje_dicho = message.content

    # si no es persona ya hablada por hoy
    if mensaje_dicho == "carrier" and id_persona not in presentes:
        presentes.append(id_persona)
        await message.channel.send("lis carrir ni sirvin")

    if (message.content == "ua"):
        await message.channel.send(getUa())

    if (shaxi.tiene_id(id_persona)) and (shaxi.tiene_malasuerte()):
        await message.channel.send(shaxi.get_joke())

    # testing
    # if (juani.tiene_id(id_persona)) and (juani.tiene_malasuerte()):
    # await message.channel.send(juani.get_joke())

    if "quien" in mensaje_dicho and id_persona not in presentes:
        presentes.append(id_persona)
        # string interp
        await message.channel.send(f"quien te conoce,  {message.author.name}")

    await bot.process_commands(message)  # necesario para no ser bloqueante

 # para mensajes de alarma en determinado hora o dia


@aiocron.crontab("2 6 * * *")  # se reinicia cada 6 am
async def cornjob1():
    presentes.clear()


TOKEN = os.environ['pasapalabra']  # enviroment variable
cornjob1.start()


mantener_vivo()
bot.run(TOKEN)
