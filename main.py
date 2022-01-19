import discord
import aiocron
import os
from latidos import mantener_vivo
from discord.ext import commands, tasks
import asyncio
import random

client = discord.Client()
nro_canal = 791515934237917244
nro_general = 828489491450560603
nro_echoes = 719244116713799702
nro_shaxi = 724373714535186472
val = True

#que haga un ua de variable duracion y mayusculas
#uaa, ua,  uaAAa, uaAA, uaAa

cMensajes = 0 #esto podria no hardcodearse, iterar => getUa
listaUA = ["ua","UaA", "UaA", "Uaa", "UAaA", "UAAaA", "UaaA", "UaaAA", "UaAaA", "uAaa", "uaAa", "uaaA", "uaaa" 
]


listaQuien = [ #problema de ser siempre lo mismo
  "qin ti priginti prrin",
  "who asked you, little doggie"
]
""" 
def generar_listaUA():
  size =
  cualA = flip coin 
  lista = []
  for 1 to size do:
    lista.append(cualA)
  
  return lista
"""

def getUa():
  cantidadA = random.randint(1,4)
  
  pal = "u"
  i = 0
  while i < cantidadA: ## ua, uaaa, uaaa
    pal = pal + "a"
    i += 1
  ##convierto en mayuscula una letra determinada, tambien podria agregarse que sea una funcion y tome parametro para volver randomar el numero de mayusculas
  indiceMayuscula = random.randint(0, len(pal) - 1)
  pal[indiceMayuscula] = pal[indiceMayuscula].upper()
  return pal



def pick_ele(lista):
  nroRand = random.randint(0,  len(lista) - 1)
  
  return lista[nroRand]

def ruleta_magica(): #problema de spam
  return random.randint(0,  10)
   
def no_estaPresente(id):
  return id not in presentes

@client.event
async def on_ready():
    print("logeado mediante usuario {0.user}".format(client))
  #  send_message.start()
    #client.user a string
 
presentes = []
usuarios_ignorar = []
@client.event
async def on_message(message):
    global val
    global presentes
    global resultado
    id_persona = message.author.id

    if message.content == "carrier" and no_estaPresente(id_persona):
        presentes.append(id_persona)
        await message.channel.send("lis carrir ni sirvin")

    if (message.content == "ua"):
       await message.channel.send(pick_ele(listaUA))       
    #    await message.channel.send('UA {}'.format(message.author.name)) 

    if (id_persona == nro_shaxi) and (ruleta_magica() > 1):
       await message.channel.send(pick_ele(listaQuien))
 

    if message.content == "quien" and no_estaPresente(id_persona):
      presentes.append(id_persona)
      await message.channel.send("quien te conoce")

    #if message.author.id == 141937575999963136 and "system" not in presentes:
      #presentes.append("system")
     # await message.channel.send("System claimed") 
     
    #if (message.content.startwith == "ignorar"):
    #  presentes.append(message.content[8>])
    
# await canal.send("lis carrir ni sirvin")
""""
@tasks.loop(minutes=2)
async def contar_tiempo():
  global val
  val = not val

 
@tasks.loop(minutes=1)
async def send_message():
    canal = client.get_channel(nro_canal)
    print("enviando mensaje recordatorio")
    await canal.send("recordatorio!")

# await canal.send("lis carrir ni sirvin")
 

@send_message.before_loop
async def before():
    await client.wait_until_ready()
    print("Finished waiting")
"""
 
#para mensajes de alarma en determinado hora o dia
@aiocron.crontab("2 6 * * *") #se reinicia cada 6 am
async def cornjob4():
  
  presentes.clear()


@aiocron.crontab('46 * * * *')
async def cornjob1():
  cliente = client.get_channel(406991565546979331)
  await cliente.send('Hour Cron Test1')


@aiocron.crontab('47 * * * *') 
async def cornjob2():
    cliente = client.get_channel(406991565546979331)
    await cliente.send('Hour Cron Test2')


@aiocron.crontab('48 * * * *')
async def cornjob3():
    cliente = client.get_channel(406991565546979331)
    await cliente.send('Hour Cron Test3')
 

TOKEN = os.environ['pasapalabra']  # enviroment variable
cornjob1.start()
cornjob2.start()
cornjob3.start()
cornjob4.start() 

mantener_vivo()
client.run(TOKEN)