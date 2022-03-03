from mailbox import NoSuchMailboxError
from flask import Flask, render_template, request, url_for, redirect
from jinja2 import Template, FileSystemLoader, Environment
from typing import Dict, Text
import numpy as np
from info import Cine1, Cine2, Cine3, Cine4, Cine1P, Cine2P, Cine3P, Cine4P

domain = "0.0.0.0:5000/"
number = 0
templates = FileSystemLoader('templates')
environment = Environment(loader = templates)

app = Flask(__name__)

sala1 = ['10:15', '11:20', '14:00', '16:00', '18:35']
sala2 = ['13:05','14:05', '19:00', '20:30', '16:20']
sala3 = ['15:45', '17:45', '21:05', '20:45', '17:30']
sala4 = ['16:22', '18:30', '22:15', '23:55', '21:15']
pos = []
chequeados = []
time = ''
movie = ''
entradas = 0
pago = ''
nombre = ''
email = ''

@app.route("/", methods=["GET", "POST"])
def cartelera():
    return render_template("cartelera.html")

@app.route("/hora/<chosen_movie>", methods=["GET","POST"])
def read_movie(chosen_movie):
    global movie
    if request.method == "POST":
        global time
        time = request.form["gethorario"]
        texto = "la hora escogida fue: "
        texto2 = "esta es la disponibilidad de la sala: "
        print(time)
        if time in sala1:
            cine1 = Cine1()
        elif time in sala2:
            cine1 = Cine2()
        elif time in sala3:
            cine1 = Cine3()
        elif time in sala4:
            cine1 = Cine4() 
        
        return render_template("hora.html", cine1=cine1, time=time, texto=texto, texto2=texto2)

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
    return render_template("hora.html", movie = movie, horas = horas, chosen_movie = chosen_movie)

@app.route("/asiento/<time>", methods=["GET", "POST"])
def get_asiento(time):
    if time in sala1:
        cine1 = Cine1P()
    elif time in sala2:
        cine1 = Cine2P()
    elif time in sala3:
        cine1 = Cine3P()
    elif time in sala4:
        cine1 = Cine4P()
        
    if request.method == "POST":
        global chequeados
        global entradas
        done = "ingresar datos para reservacion >>"
        chequeados = request.form.getlist('asiento')
        chequeados = np.array(chequeados)
        print(chequeados)

        for i in range(len(cine1)):
            for j in range(len(cine1[i])):
                if cine1[i][j] in chequeados:
                    cine1[i][j] = '0X'
        
        for k in chequeados:
            entradas += 1
        print(entradas)

        return render_template("asiento.html",chequeados=chequeados, done=done, cine1=cine1)

    return render_template("asiento.html", time=time, cine1=cine1)

@app.route("/reservationinfo", methods=["GET", "POST"])
def reservationinfo():
    global movie
    global time
    global entradas
    global chequeados
    global nombre
    global pago
    global email

    if request.method == "POST":
        nombre = request.form["getnombre"]
        email = request.form["getemail"]
        pago = request.form["getpago"]

    return render_template("reservationInfo.html", movie=movie, time=time, entradas=entradas, chequeados=chequeados)

if __name__ == "__main__":
    app.run(host="0.0.0.0",port = 8000,debug=True)