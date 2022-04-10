from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')

def index():
    return "Creado por ! 𝐊𝐨𝐢𝐧𝐲𝐚𝐫𝐅𝐢𝐤#6060"

def run():
    app.run(host="0.0.0.0", port=8080)

def keep_alive():
    server = Thread(target=run)
    server.start()


