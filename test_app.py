from app import ResponseReservation,sala1, sala2, sala3, sala4

def test_struct():
    nombre = 'Marcela'
    email = 'marcelamelgar@ufm.edu'
    movie = 'Cásate Conmigo'
    time = '14:05'
    entradas = 2
    asientoss = ['E1', 'E2']
    totals = entradas*65
    pago = 'tarjeta'
    res = ResponseReservation(name=nombre, correo=email, pelicula=movie, hora=time, ents=entradas, asientos=asientoss, total = totals, pag=pago)
    assert res == ResponseReservation(name='Marcela', correo='marcelamelgar@ufm.edu', pelicula='Cásate Conmigo', hora='14:05', ents=2, asientos=['E1', 'E2'], total=130, pag='tarjeta')

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