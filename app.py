from re import S
from flask import Flask, render_template, request
from jinja2 import FileSystemLoader, Environment
from typing import NamedTuple
import numpy as np
from info import Cine1, Cine2, Cine3, Cine4, Cine1P, Cine2P, Cine3P, Cine4P
from queue_stack import Queue, Stack, shuffle, Stack
import random

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
editar = ''
num_orden = [4234,9784,2349,6378,1093,2450,8765,7384,3673]

class ResponseReservation(NamedTuple):
  name: str
  correo: str
  pelicula: str
  hora: str
  ents: int
  asientos: list
  total: int
  pag: str
  order: int

@app.route("/", methods=["GET", "POST"])
def cartelera():
    fins = []
    futureMovies = ["Franco Escamilla: Payaso - 28 de Abril", "Dr. Strange en el Multiverso de Locura - 4 de Mayo", 
                    "Thor: Love and Thunder - 8 de Julio", "Avatar 2 - 16 de Diciembre"]   

    ran = shuffle(futureMovies)
    print("ASI ESTRAN AL QUEUE:")
    print(ran)

    q = Queue()
    for i in range(len(ran)):
        q.add_element(ran[i])
    print("ASI SALEN DEL QUEUE:")
    q.display()

    for i in q.queue:
        fin = i
        fins.append(fin)

    return render_template("cartelera.html", fins=fins)

@app.route("/menu", methods=["GET", "POST"])
def menu():
    fins_stack_food = []
    fins_stack_combos = []
    comida = ["/static/poporopo.png", "/static/soda.png", 
                    "/static/nachos.png", "/static/hotdog.png", 
                    "/static/fries.png", "/static/dulces.png"] 

    combos = ["/static/cp1.png", "/static/cp2.png", "/static/cp3.png",
                    "/static/cp4.png", "/static/cp5.png", "/static/cp6.png", "/static/cp7.png"]  

    ran_comida = shuffle(comida)
    ran_combos = shuffle(combos)
    print("ASI ESTRAN AL STACK:")
    print(ran_comida)
    print("ASI ESTRAN AL STACK:")
    print(ran_combos)

    s_food = Stack()
    for i in range(len(ran_comida)):
        s_food.push_element(ran_comida[i])
    print("ASI SALEN DEL STACK")    
    s_food.display()

    for i in s_food.stack:
        fin_stack = i
        fins_stack_food.append(fin_stack)

    s_combos = Stack()
    for i in range(len(ran_combos)):
        s_combos.push_element(ran_combos[i])
    print("ASI SALEN DEL STACK")
    s_combos.display()

    for i in s_combos.stack:
        fin_stack_combo = i
        fins_stack_combos.append(fin_stack_combo)

    return render_template("menu.html", fins_stack_food=fins_stack_food, fins_stack_combos=fins_stack_combos)

@app.route("/hora/<chosen_movie>", methods=["GET","POST"])
def read_movie(chosen_movie):
    global movie
    if request.method == "POST":
        global time
        time = request.form.get("gethorario")
        texto = "la hora escogida fue: "
        texto2 = "esta es la disponibilidad de la sala: "
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

        for i in range(len(cine1)):
            for j in range(len(cine1[i])):
                if cine1[i][j] in chequeados:
                    cine1[i][j] = '0X'
        
        for k in chequeados:
            entradas += 1

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
        nombre = request.form.get("getnombre")
        email = request.form.get("getemail")
        pago = request.form.get("getpago")

    return render_template("reservationInfo.html", movie=movie, time=time, entradas=entradas, chequeados=chequeados, nombre=nombre, pago=pago, email=email)

@app.route("/reserve", methods=["GET", "POST"])
def reservation():
    global movie
    global nombre
    global time
    global entradas
    global chequeados
    global pago
    global email
    global editar
    global num_orden

    s= 0

    while s == 0:
        assign_number = random.randint(1000,9999)
        exist_count = num_orden.count(assign_number)

        if exist_count > 0:
            s = 0
        elif exist_count == 0:
            fixed_num = assign_number
            num_orden.append(fixed_num)
            s += 1

    res = ResponseReservation(name=nombre, correo=email, pelicula=movie, hora=time, ents=entradas, asientos=chequeados, total = entradas*65, pag=pago, order=fixed_num)

    if request.method == "POST":
        dato = request.form.get('edita')

        if dato == 'nombre':
            editar = 'nombre'
        elif dato == 'email':
            editar = 'email'
        elif dato == 'pago':
            editar = 'pago'

    return render_template("reservation.html", nombre=nombre, movie=movie, time=time, entradas=entradas, chequeados=chequeados, pago=pago, email=email, total=entradas*65, editar=editar, order=fixed_num)

@app.route("/edit", methods=["GET", "POST"])
def edit():
    global pago
    global email
    global editar
    global nombre

    if request.method == "POST":
        cambio = request.form.get("getnombres")

        if editar == 'nombre':
            nombre = cambio
        if editar == 'pago':
            pago = cambio
        if editar == 'email':
            email = cambio

    res = ResponseReservation(name=nombre, correo=email, pelicula=movie, hora=time, ents=entradas, asientos=chequeados, total = entradas*65, pag=pago)
    
    return render_template("edit.html", pago=pago, email=email, nombre=nombre, editar=editar)

if __name__ == "__main__":
    app.run(host="0.0.0.0",port = 8000,debug=True)