

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

async def get_data(link): #no bloqueante
  async with aiohttp.ClientSession() as session: # 
      async with session.get(link) as response: 
        return await response.json()
 
  
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
    def procesar_plex(numero): # es convencion que el precio sea 500 unidades de plex, en 1B. ej:1.3B
      return (numero * 500) /  1000000000  
    # obtengo objeto Response
     
    data = await get_data("https://api.evemarketer.com/ec/marketstat/json?typeid=44992&usesystem=30000142")  
    lista_buy = data[0].get("buy")
    lista_sell = data[0].get("sell")
    
  #convencion es hablar de  1.3Billones
    precio_compra_avg = procesar_plex(lista_buy.get("wavg"))   
    precio_venta_avg = procesar_plex(lista_sell.get("wavg"))
  
  #string, html
    mensaje_header = "Jita (4:4) -  x 500u Promedio Semanal"
    mensaje_plex_compra = f"\nPlex para la Compra: {precio_compra_avg:.2f} B"
    mensaje_plex_venta = f"\nPlex para la Venta:    {precio_venta_avg:.2f} B"
    await ctx.send(mensaje_header + mensaje_plex_venta + mensaje_plex_compra)



@bot.command(name="precio", help="precio de item en Eve Online desde api ")
async def obtener_item_precio(ctx, *args): 
    nombre_item = " ".join(args) 
    async def obtener_id():
    # obtengo id del item a buscar en api de id
      async with aiohttp.ClientSession() as session: # 
        async with session.get(f"https://www.fuzzwork.co.uk/api/typeid.php?typename={nombre_item}") as response: 
          return await response.json(content_type='text/html') #custom

    data_item = await obtener_id() 
    id_item = data_item.get("typeID")
    nombre_obtenido = data_item.get("typeName")
  
    #obtengo info del item
    data_mercado = await get_data(f"https://api.evemarketer.com/ec/marketstat/json?typeid={id_item}&usesystem=30000142")
        
    precio_compra_avg = int(data_mercado[0].get("buy").get("avg"))
    precio_venta_avg = int(data_mercado[0].get("sell").get("avg"))


  
    #logica, estaria mejor en import
    if (nombre_obtenido == "bad item"):  #si no existe aisar al usuario que escribio mal
      await ctx.send(f"item con nombre {nombre_item} no encontrado :(  ")
      
    elif precio_venta_avg > 0 : #si es encontrado, devolver valor de compra y venta
       await ctx.send(f"Precio promedio x unidad de {nombre_obtenido}\nPrecio venta: {precio_venta_avg}  \nPrecio compra: { precio_compra_avg}")
      
    else: #si existe pero api devuelve valor 0, mejor buscar en contratos p2p
      async with aiohttp.ClientSession() as session:   
        async with session.get(f"https://api.contractsappraisal.com/v1/prices/{id_item}?include_private=false&bpc=false&security=lowsec") as response: 
          if (response.status != 200):
             await ctx.send("item no encontrado")
          else:
            dato_contrato = await response.json()  #custom
            precio_venta_contrato = dato_contrato.get("median")
            await ctx.send(f"Consultando contratos precio promedio de {nombre_item}\nPrecio venta: {int(precio_venta_contrato) / 1000000000 } B")
    


def separar_partes(item, n_partes):
    item_str = str(item)
    partes = [item_str[i:i+n_partes]
              for i in range(0, len(item_str), n_partes)]  # [123,342,532]
    return " ".join(partes)  # 123 342 532


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
