import discord
import os
from replit import db
from latidos import mantener_vivo
client = discord.Client()

@client.event 
async def on_ready():
  print("logeado mediante usuario {0.user}".format(client)) 
  #client.user a string


@client.event
async def on_message(message):
  
 # if message.author == client.user:
 #   return
  
  if  message.content.startswith("carrier"):
    await message.channel.send("lis carrir ni sirvin")

TOKEN = os.environ['pasapalabra'] # enviroment variable

mantener_vivo()
client.run(TOKEN)
 
