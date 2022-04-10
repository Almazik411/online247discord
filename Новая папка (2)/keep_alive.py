from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')

def index():
    return "Creado por Fleik#1111 y Ar$06#0006"

def run():
    app.run(host="0.0.0.0", port=8080)

def keep_alive():
    server = Thread(target=run)
    server.start()


