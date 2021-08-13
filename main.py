import discord
import os
from replit import db
from latidos import mantener_vivo
import schedule
import time
from discord.ext import commands, tasks

client = discord.Client()
 
 

@client.event 
async def on_ready():
  print("logeado mediante usuario {0.user}".format(client)) 
  send_message.start()
  #client.user a string
   
@client.event
async def on_message(message):
  
 # if message.author == client.user:
 #   return
  
  if  message.content.startswith("carrier"):
    await message.channel.send("lis carrir ni sirvin")


@tasks.loop(seconds=29)
async def send_message():
   canal = client.get_channel(406991565546979331)
   print("enviando mensaje recordatorio")
   await canal.send("recordatorio!")
 # await canal.send("lis carrir ni sirvin")

@send_message.before_loop
async def before():
    await client.wait_until_ready()
    print("Finished waiting")

  
TOKEN = os.environ['pasapalabra'] # enviroment variable

mantener_vivo()
client.run(TOKEN)
 
