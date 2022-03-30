import discord
import aiocron
from .personas import *
import os
from latidos import mantener_vivo
from discord.ext import commands, tasks
import asyncio
import random
from random import choice


client = discord.Client()
nro_canal = 791515934237917244
nro_general = 828489491450560603
nro_echoes = 719244116713799702
val = True
presentes = []
usuarios_ignorar = []
cMensajes = 0

listaQuien = [
    "qin ti priginti prrin",
    "who asked you, little doggie"
]

# que haga un ua de variable duracion y mayusculas
#uaa, ua,  uaAAa, uaAA, uaAa

# listaUA = ["ua","UaA", "UaA", "Uaa", "UAaA", "UAAaA", "UaaA", "UaaAA", "UaAaA", "uAaa", "uaAa", "uaaA", "uaaa"
# ] ##esta mejor que se genere por funciones, 1. se devuelve un uaa de random largo, y luego se vuelven mayusculas minusculas
def getPalabra(cantidadA):  # utilizar clases para ua estaria mejor
    pal = "u"
    i = 0
    while i < cantidadA:  # ua, uaaa, uaaa
        pal = pal + "a"
        i += 1
    return pal


def getUa():
    pal = getPalabra(random.randint(1, 5))  # largo palabra
    return getMayusculasRandom(pal)


def getMayusculasRandom(pal):  # devuelve mayus arbitrarias "hola" hOlA hoLA
    eleccionMayus = zip(pal.lower(), pal.upper())  # ("H","h"), ("O","o")
    # que eliga entre cada una y luego pase a string con join
    return "".join(map(choice, eleccionMayus))

 

def no_estaPresente(id):
    return id not in presentes



#Main
@client.event
async def on_ready():
    print("logeado mediante usuario {0.user}".format(client))
    #  send_message.start()
    # client.user a string


@client.event
async def on_message(message):
    global val
    global presentes
    global resultado
    id_persona = message.author.id
    mensajeDicho = message.content.lowerCase()

    # si no es persona ya hablada por hoy
    if mensajeDicho == "carrier" and no_estaPresente(id_persona):
        presentes.append(id_persona)
        await message.channel.send("lis carrir ni sirvin")

    if (mensajeDicho == "ua"):
      # await message.channel.send(pick_ele(listaUA))     #elige de lista de ua hardcodeada al azar
        # genera un ua de random largo, mezcla mayus y minus
        await message.channel.send(getUa())
    #    await message.channel.send('UA {}'.format(message.author.name))

    if (shaxi.tiene_id(id_persona)) and (shaxi.tiene_malasuerte):
        await message.channel.send(shaxi.get_joke())

    if mensajeDicho == "quien" and no_estaPresente(id_persona):
        presentes.append(id_persona)
        # string interp
        await message.channel.send(f"quien te conoce, {message.author.name}")

    # if message.author.id == 141937575999963136 and "system" not in presentes:
        # presentes.append("system")
       # await message.channel.send("System claimed")

    # if (message.content.startwith == "ignorar"):
    #  presentes.append(message.content[8>])

# await canal.send("lis carrir ni sirvin")


# para mensajes de alarma en determinado hora o dia
@aiocron.crontab("2 6 * * *")  # se reinicia cada 6 am
async def cornjob1():
    presentes.clear()


TOKEN = os.environ['pasapalabra']  # enviroment variable
cornjob1.start()


mantener_vivo()
client.run(TOKEN)
