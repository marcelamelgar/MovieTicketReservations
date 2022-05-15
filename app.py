from flask import Flask, render_template, request
from jinja2 import FileSystemLoader, Environment
from typing import NamedTuple
import numpy as np
from info import Cine1, Cine2, Cine3, Cine4, Cine1P, Cine2P, Cine3P, Cine4P
from queue_stack import Queue, Stack, shuffle, Stack
from tree import Node, BinarySearchTree
from Graph import generate_edges, addEdge
from sort import mergeSort
from jump_search import jumpSearch
from collections import defaultdict
from graphviz import GraphVisualization
import random
import json

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
fixed_num = int
num_orden = [4234,9784,2349,6378,1093,2450,8765,7384,3673]
horas_brujas = ['10:15','13:05','15:45','16:22','18:30']
horas_casate = ['11:20','14:05','17:45']
horas_corazon = ['14:00','19:00']
horas_padrino = ['16:00','20:30','21:05']
horas_banishing = ['18:35','20:45','22:15','23:55']
horas_sing = ['16:20','17:30','21:15']
tree = BinarySearchTree()
graph = defaultdict(list)
G = GraphVisualization()

def directed_loop_graph(i):
    for j in sala1:
        if i == j:
            addEdge(graph,i,'sala1')
            addEdge(graph,'sala1',i)
            G.addEdge2('sala1', i)
            G.addEdge2(i, 'sala1')
    for h in sala2:
        if i == h:
            addEdge(graph,i,'sala2')
            addEdge(graph,'sala2',i)
            G.addEdge2('sala2', i)
            G.addEdge2(i, 'sala2')
    for o in sala3:
        if i == o:
            addEdge(graph,i,'sala3')
            addEdge(graph,'sala3',i)
            G.addEdge2('sala3', i)
            G.addEdge2(i, 'sala3')
    for p in sala4:
        if i == p:
            addEdge(graph,i,'sala4')
            addEdge(graph,'sala4',i)
            G.addEdge2('sala4', i)
            G.addEdge2(i, 'sala4')

for i in horas_brujas:
    addEdge(graph,'Cacería de Brujas',i)
    G.addEdge2('Cacería de Brujas', i)
    directed_loop_graph(i)
for i in horas_casate:
    addEdge(graph,'Cásate Conmigo',i)
    G.addEdge2('Cásate Conmigo', i)
    directed_loop_graph(i)
for i in horas_corazon:
    addEdge(graph,'Corazón de Fuego',i)
    G.addEdge2('Corazón de Fuego', i)
    directed_loop_graph(i)
for i in horas_padrino:
    addEdge(graph,'El Padrino 50 años',i)
    G.addEdge2('El Padrino 50 años', i)
    directed_loop_graph(i)
for i in horas_banishing:
    addEdge(graph,'El Exorcismo',i)
    G.addEdge2('El Exorcismo', i)
    directed_loop_graph(i)
for i in horas_sing:
    addEdge(graph,'Sing 2: ¡Ven y Canta de Nuevo!',i)
    G.addEdge2('Sing 2: ¡Ven y Canta de Nuevo!', i)
    directed_loop_graph(i)

# G.visualize()

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
                    "Thor: Love and Thunder - 8 de Julio", "Avatar 2 - 16 de Diciembre", "Lightyear - 17 de Junio", 
                    "Black Panther: Wakanda Forever - 11 de Noviembre", "Halloween Ends - 14 de Octubre"]   

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
        for funcion in graph['sala1']:
            if funcion == time:
                cine1 = Cine1()
        for funcion in graph['sala2']:
            if funcion == time:
                cine1 = Cine2()
        for funcion in graph['sala3']:
            if funcion == time:
                cine1 = Cine3()
        for funcion in graph['sala4']:
            if funcion == time:
                cine1 = Cine4() 
        
        return render_template("hora.html", cine1=cine1, time=time, texto=texto, texto2=texto2)

    horas = []
    print(generate_edges(graph))
    # G.visualize()
    if chosen_movie == 'brujas':
        movie = 'Cacería de Brujas'
        horas = graph['Cacería de Brujas']
    elif chosen_movie == 'casate':
        movie = 'Cásate Conmigo'
        horas = graph['Cásate Conmigo']
    elif chosen_movie == 'corazon':
        movie = 'Corazón de Fuego'
        horas = graph['Corazón de Fuego']
    elif chosen_movie == 'padrino':
        movie = 'El Padrino 50 años'
        horas = graph['El Padrino 50 años']
    elif chosen_movie == 'banishing':
        movie = 'El Exorcismo'
        horas = graph['El Exorcismo']
    elif chosen_movie == 'sing':
        movie = 'Sing 2: ¡Ven y Canta de Nuevo!'
        horas = graph['Sing 2: ¡Ven y Canta de Nuevo!']
    horas =  np.array(horas)
    return render_template("hora.html", movie = movie, horas = horas, chosen_movie = chosen_movie)

@app.route("/asiento/<time>", methods=["GET", "POST"])
def get_asiento(time):
    for funcion in graph['sala1']:
            if funcion == time:
                cine1 = Cine1P()
    for funcion in graph['sala2']:
            if funcion == time:
                cine1 = Cine2P()
    for funcion in graph['sala3']:
            if funcion == time:
                cine1 = Cine3P()
    for funcion in graph['sala4']:
            if funcion == time:
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
    global fixed_num

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
    
    as_list = chequeados.tolist()
    list_ob = []

    with open("reservations_done.json") as pf:
        list_ob = json.load(pf)

    list_ob.append({
        "numero": fixed_num,
        "nombre": nombre,
        "correo": email,
        "pelicula": movie,
        "hora": time,
        "entradas": entradas,
        "asientos": as_list,
        "total": entradas*65,
        "pago": pago
    })

    
    with open("reservations_done.json", "w") as json_file:
        json.dump(list_ob, json_file, indent=4, separators=(',',': '))

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
    global fixed_num

    if request.method == "POST":
        cambio = request.form.get("getnombres")

        if editar == 'nombre':
            nombre = cambio
        if editar == 'pago':
            pago = cambio
        if editar == 'email':
            email = cambio

    res = ResponseReservation(name=nombre, correo=email, pelicula=movie, hora=time, ents=entradas, asientos=chequeados, total = entradas*65, pag=pago, order=fixed_num)
    
    return render_template("edit.html", pago=pago, email=email, nombre=nombre, editar=editar)

@app.route("/admin", methods=["GET", "POST"])
def admin():
    global num_orden
    print(num_orden)
    global tree
    file = open('reservations_done.json')
    registro = json.load(file)
    file.close()

    num_orden = mergeSort(num_orden)
    print(num_orden)
    largo = len(num_orden)
    for reser in num_orden:
        tree.insert(tree.root, reser)
    print("TREE")    
    Node.visualization(tree.root)

    if request.method == "POST":
        buscado = int(request.form.get("getnumber"))
        index = jumpSearch(num_orden, buscado, largo)
        if index == -1:
            feedback = "Orden no se encuentra en el sistema!"
        else:
            print("ORDEN BUSCADA")
            print("Orden" , buscado, "en el espacio" ,"%.0f"%index)
            feedback = "Orden encontrada!"
        # tree.search(tree.root, buscado)
        # print("ORDEN BUSCADA")
        # print(tree.search(tree.root, buscado))

        for ing in range(len(registro)):
            if (buscado == registro[ing]["numero"]):
                en_nombre = registro[ing]["nombre"]
                en_correo = registro[ing]["correo"]
                en_pelicula = registro[ing]["pelicula"]
                en_hora = registro[ing]["hora"]
                en_entradas = registro[ing]["entradas"]
                en_asientos = registro[ing]["asientos"]
                en_total = registro[ing]["total"]
                en_pago = registro[ing]["pago"]
        return render_template("admin.html", buscado=buscado, en_nombre=en_nombre, en_correo=en_correo, en_pelicula=en_pelicula, en_hora=en_hora, en_entradas=en_entradas, en_asientos=en_asientos, en_total=en_total, en_pago=en_pago, feedback=feedback)
    return render_template("admin.html")

@app.route("/delete/<buscado>", methods=["GET", "POST"])
def delete_order(buscado):
    global tree
    global num_orden
    if request.method == "POST":
        tree.delete(tree.root, int(buscado))
        print("ARBOL CON ORDEN ELIMINADA")
        Node.visualization(tree.root)
    return render_template("delete.html", buscado=buscado, num_orden=num_orden)

if __name__ == "__main__":
    app.run(host="0.0.0.0",port = 8000,debug=True)