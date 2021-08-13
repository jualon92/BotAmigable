from flask import Flask
from threading import Thread # thread separado para que ambos corran al mismo tiempo

app = Flask('')

@app.route('/')
def home():
    return "sigo despierto!"

def run():
  app.run(host='0.0.0.0',port=8080)

def mantener_vivo(): #corre el srv
    t = Thread(target=run)
    t.start()