import discord
import aiocron
import os
from latidos import mantener_vivo
from discord.ext import commands, tasks
import asyncio

client = discord.Client()
nro_canal = 406991565546979331
 
@client.event
async def on_ready():
    print("logeado mediante usuario {0.user}".format(client))
    send_message.start()
    #client.user a string
 
 
@client.event
async def on_message(message):

    # if message.author == client.user:
    #   return

    if message.content.startswith("carrier"):
        await message.channel.send("lis carrir ni sirvin")


@tasks.loop(hours=24)
async def send_message():
    canal = client.get_channel(nro_canal)
    print("enviando mensaje recordatorio")
    await canal.send("recordatorio!")

# await canal.send("lis carrir ni sirvin")


@send_message.before_loop
async def before():
    await client.wait_until_ready()
    print("Finished waiting")

 
#para mensajes de alarma en determinado hora o dia
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

mantener_vivo()
client.run(TOKEN)
 

 

 

 