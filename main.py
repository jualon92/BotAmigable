import discord
import aiocron
from personas import shaxi, juani
from fabricaUA import getUa
import os
from latidos import mantener_vivo
from discord.ext import commands, tasks
import asyncio
import random
from discord.ext import commands
import requests
import json
from mercado import *

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

 #Main
@client.event
async def on_ready():
    print("logeado mediante usuario {0.user}".format(client))
    #  send_message.start()
    # client.user a string


#command implementa !help con resumen de comandos, y utiliza prefijo
bot = commands.Bot(command_prefix='!')



#personas se juntan a elegir quien le toca primero y a quien ultimo aleatoriamente
@bot.command(name="rank_random", help="devuelve ranking entre nombres aleatorio => rank_random p1 p2 p3...")
async def tirar_dado(ctx, *argv):
  contador = 0
  personasLista = ""
   #personasLista = f"{nombre} \n"
  listaNueva = random.sample(argv, len(argv))  #agregar un titulo dificulta
  for arg in  listaNueva:
    contador = contador + 1 #podria utilizarse lista.index(ele). pero con contador ya empieza ranking en 1
    #nombre = arg
    fraseNueva = f"{str(contador)} puesto: {arg} \n"
    #fraseNueva = str(contador) + " puesto: " + " " + nombre  +    "\n"
    personasLista =  personasLista + fraseNueva
  await ctx.send(personasLista)



# Se piden datos de mercado de mmorpg de cotizacion de moneda virtual  
@bot.command(name="plex", help="precio de plex en Eve Online desde api ")
async def obtener_plex_precio(ctx):
  # obtengo objeto Response
   response_API = requests.get("https://api.evemarketer.com/ec/marketstat/json?typeid=44992&usesystem=30000142")  
   data = response_API.json() #
   listaBuy = data[0].get("buy")
   listaSell = data[0].get("sell") 
  
   precioCompraAVG = (listaBuy.get("avg") * 500) / 1000000000 # convencion es hablar de  1.3Billones 
   precioVentaAVG = listaSell.get("avg") * 500  / 1000000000
    
   mensajePlexCompra =  f" Jita (4:4) \nPlex para la Compra: {precioCompraAVG:.2f} Millones"
   mensajePlexVenta = f"Plex para la Venta:   {precioVentaAVG:.2f} Millones"
   await ctx.send(mensajePlexCompra + "\n" +  mensajePlexVenta )
 
  
#Ideas a implementar
#subio o bajo un producto en comparacion a la semana o mes pasado? estaria bueno implementarlo de alguna manera
#conseguir el precio de cualquier item sin tener que entrar al juego




@client.event #listener mensajes
async def on_message(message):
    global val
    global presentes
    global resultado
    id_persona = message.author.id
    mensajeDicho = message.content.lower()

    if (message.author == client.user):# que respuesta del mismo bot no trigeree una respuesta
      return  
    
    # si no es persona ya hablada por hoy
    if mensajeDicho == "carrier" and id_persona not in presentes:
        presentes.append(id_persona)
        await message.channel.send("lis carrir ni sirvin")

    if (mensajeDicho == "ua"):
      # await message.channel.send(pick_ele(listaUA))     #elige de lista de ua hardcodeada al azar
        # genera un ua de random largo, mezcla mayus y minus
        await message.channel.send(getUa())
    #    await message.channel.send('UA {}'.format(message.author.name))

    if (shaxi.tiene_id(id_persona)) and (shaxi.tiene_malasuerte()):
        await message.channel.send(shaxi.get_joke())
      
    #testing  
    ##if (juani.tiene_id(id_persona)) and (juani.tiene_malasuerte()):
    ##    await message.channel.send(juani.get_joke())

    if "quien" in mensajeDicho and id_persona not in presentes: 
        presentes.append(id_persona)
        # string interp
        await message.channel.send(f"quien te conoce,  {message.author.name}")

    
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
bot.run(TOKEN)
 
client.run(TOKEN)
 
