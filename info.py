import numpy as np

def horarios(movie):
    horas = []
    if movie == 'brujas':
        horas = [['10:15'],['13:05'],['15:45'],['16:22'],['18:30']]
    elif movie == 'casate':
        horas = [['11:20'],['14:05'],['17:45']]
    elif movie == 'corazon':
        horas = [['14:00'],['19:00']]
    elif movie == 'padrino':
        horas = [['16:00'],['20:30'],['21:05']]
    elif movie == 'banishing':
        horas = [['18:35'],['20:45'],['22:15'],['23:55']]
    elif movie == 'sing':
        horas = [['16:20'],['17:30'],['21:15']]
    return horas

print(horarios('brujas'))
print(horas)