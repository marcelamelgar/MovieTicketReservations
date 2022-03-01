from flask import Flask, render_template, request, url_for, redirect
from jinja2 import Template, FileSystemLoader, Environment
from typing import Dict, Text
import numpy as np

domain = "0.0.0.0:5000/"
number = 0
templates = FileSystemLoader('templates')
environment = Environment(loader = templates)

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def cartelera():
    return render_template("cartelera.html")

@app.route("/hora/<chosen_movie>", methods=["GET","POST"])
def read_movie(chosen_movie):
    if request.method == "POST":
        time = request.form["gethorario"]
        print(time)
        return redirect(url_for('read_movie'), time = time)
    horas = []
    if chosen_movie == 'brujas':
        movie = 'Cacería de Brujas'
        horas = [['10:15'],['13:05'],['15:45'],['16:22'],['18:30']]
    elif chosen_movie == 'casate':
        movie = 'Cásate Conmigo'
        horas = [['11:20'],['14:05'],['17:45']]
    elif chosen_movie == 'corazon':
        movie = 'Corazón de Fuego'
        horas = [['14:00'],['19:00']]
    elif chosen_movie == 'padrino':
        movie = 'El Padrino 50 años'
        horas = [['16:00'],['20:30'],['21:05']]
    elif chosen_movie == 'banishing':
        movie = 'El Exorcismo'
        horas = [['18:35'],['20:45'],['22:15'],['23:55']]
    elif chosen_movie == 'sing':
        movie = 'Sing 2: ¡Ven y Canta de Nuevo!'
        horas = [['16:20'],['17:30'],['21:15']]
    horas =  np.array(horas)
    return render_template("hora.html", movie = movie, horas = horas)

@app.route("/asiento", methods=["GET", "POST"])
def get_asiento():
    return render_template("asiento.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0",port = 8000,debug=True)