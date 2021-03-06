from app import ResponseReservation,sala1, sala2, sala3, sala4,num_orden
from queue_stack import shuffle, Stack, Queue
from tree import BinarySearchTree, Node
from sort import mergeSort
from jump_search import jumpSearch
from Graph import addEdge, generate_edges
from collections import defaultdict

def test_struct():
    nombre = 'Marcela'
    email = 'marcelamelgar@ufm.edu'
    movie = 'Cásate Conmigo'
    time = '14:05'
    entradas = 2
    asientoss = ['E1', 'E2']
    totals = entradas*65
    pago = 'tarjeta'
    orden = 5398
    res = ResponseReservation(name=nombre, correo=email, pelicula=movie, hora=time, ents=entradas, asientos=asientoss, total = totals, pag=pago, order = orden)
    assert res == ResponseReservation(name='Marcela', correo='marcelamelgar@ufm.edu', pelicula='Cásate Conmigo', hora='14:05', ents=2, asientos=['E1', 'E2'], total=130, pag='tarjeta', order=5398)

def test_sala():
    hora = '18:30'
    if hora in sala1:
        cine1 = 'sala1'
    elif hora in sala2:
        cine1 = 'sala2'
    elif hora in sala3:
        cine1 = 'sala3'
    elif hora in sala4:
        cine1 = 'sala4'
    assert cine1 == 'sala4'

def test_horas():
    pelicula = 'brujas'
    if pelicula == 'brujas':
        movie = 'Cacería de Brujas'
        horas = [['10:15'],['13:05'],['15:45'],['16:22'],['18:30']]
    elif pelicula == 'casate':
        movie = 'Cásate Conmigo'
        horas = [['11:20'],['14:05'],['17:45']]
    elif pelicula == 'corazon':
        movie = 'Corazón de Fuego'
        horas = [['14:00'],['19:00']]
    elif pelicula == 'padrino':
        movie = 'El Padrino 50 años'
        horas = [['16:00'],['20:30'],['21:05']]
    elif pelicula == 'banishing':
        movie = 'El Exorcismo'
        horas = [['18:35'],['20:45'],['22:15'],['23:55']]
    elif pelicula == 'sing':
        movie = 'Sing 2: ¡Ven y Canta de Nuevo!'
        horas = [['16:20'],['17:30'],['21:15']]
    assert movie == 'Cacería de Brujas'
    assert horas == [['10:15'],['13:05'],['15:45'],['16:22'],['18:30']]

def test_seat():
    entradas = 0
    asientoss = ['E1', 'E2']
    for k in asientoss:
            entradas += 1
    assert entradas == 2

def test_queue():
    inicial  = ["Franco Escamilla: Payaso - 28 de Abril", "Dr. Strange en el Multiverso de Locura - 4 de Mayo", 
                    "Thor: Love and Thunder - 8 de Julio", "Avatar 2 - 16 de Diciembre"]
    ran = shuffle(inicial)
    q = Queue()
    q.add_element("Avatar 2 - 16 de Diciembre")
    assert len(q.queue) == 1
    assert len(inicial) == len(ran)
    assert all([a == b for a, b in zip(inicial, ran)])   

def test_stack():
    s_food = Stack()
    s_food.push_element("/static/hotdog.png")
    assert len(s_food.stack) == 1

def test_tree():
    tree = BinarySearchTree()
    tree.insert(tree.root, 3)
    tree.insert(tree.root, 5)
    tree.insert(tree.root, 1)
    assert tree.search(tree.root, 3)
    assert tree.delete(tree.root, 1)

def test_sort():
    try_array = [3,1,7,2,45,21,34]
    try_array = mergeSort(try_array)
    primero = try_array[0]
    ultimo = try_array[-1]
    medio = try_array[3]
    assert primero == 1
    assert ultimo == 45
    assert medio == 7

def test_jump_search():
    try_array2 = mergeSort(num_orden)
    largo = len(try_array2)
    buscar1 = 1093
    buscar2 = 8765
    index = jumpSearch(try_array2, buscar1, largo)
    index2 = jumpSearch(try_array2, buscar2, largo)
    assert index == 0
    assert index2 == 7

def test_grafo():
    graph = defaultdict(list)
    addEdge(graph,'Punto A','Punto B')
    addEdge(graph,'Punto B','Punto C')
    addEdge(graph,'Punto B','Punto A')
    generate_edges(graph)
    resultado = graph['Punto A']
    loop = graph['Punto B']
    assert resultado[0] == 'Punto B'
    assert loop[0] == 'Punto C'
    assert loop[1] == 'Punto A'