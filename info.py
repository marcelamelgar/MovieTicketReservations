import numpy as np

def Cine1():
    num = np.array([['O'], ['A'], ['B'], ['C'], ['D'], ['E'], ['F']])
    uno = np.array([['1'],['0'],['0'],['0'],['0'],['0'],['0']])
    dos = np.array([['2'],['0'],['X'],['0'],['0'],['0'],['0']])
    tres = np.array([['3'],['0'],['X'],['0'],['0'],['0'],['0']])
    cuatro = np.array([['4'],['0'],['0'],['0'],['0'],['0'],['0']])
    cinco = np.array([['5'],['0'],['0'],['0'],['0'],['X'],['0']])
    seis = np.array([['6'],['0'],['0'],['0'],['0'],['X'],['0']])
    siete = np.array([['7'],['0'],['0'],['0'],['0'],['X'],['0']])
    ocho = np.array([['8'],['0'],['0'],['0'],['0'],['X'],['0']])

    cine1 = np.hstack((num,uno))
    cine1 = np.hstack((cine1,dos))
    cine1 = np.hstack((cine1,tres))
    cine1 = np.hstack((cine1,cuatro))
    cine1 = np.hstack((cine1,cinco))
    cine1 = np.hstack((cine1,seis))
    cine1 = np.hstack((cine1,siete))
    cine1 = np.hstack((cine1,ocho))
    return cine1

def Cine2():
    num = np.array([['O'], ['A'], ['B'], ['C'], ['D'], ['E'], ['F']])
    uno = np.array([['1'],['0'],['0'],['0'],['0'],['0'],['0']])
    dos = np.array([['2'],['0'],['0'],['0'],['0'],['0'],['0']])
    tres = np.array([['3'],['0'],['0'],['X'],['0'],['0'],['0']])
    cuatro = np.array([['4'],['0'],['0'],['x'],['0'],['0'],['0']])
    cinco = np.array([['5'],['X'],['0'],['0'],['0'],['X'],['0']])
    seis = np.array([['6'],['X'],['0'],['0'],['0'],['X'],['0']])
    siete = np.array([['7'],['X'],['0'],['0'],['0'],['0'],['0']])
    ocho = np.array([['8'],['0'],['0'],['0'],['0'],['X'],['0']])

    cine2 = np.hstack((num,uno))
    cine2 = np.hstack((cine2,dos))
    cine2 = np.hstack((cine2,tres))
    cine2 = np.hstack((cine2,cuatro))
    cine2 = np.hstack((cine2,cinco))
    cine2 = np.hstack((cine2,seis))
    cine2 = np.hstack((cine2,siete))
    cine2 = np.hstack((cine2,ocho))
    return cine2

def Cine3():
    num = np.array([['O'], ['A'], ['B'], ['C'], ['D'], ['E'], ['F']])
    uno = np.array([['1'],['0'],['0'],['0'],['0'],['0'],['0']])
    dos = np.array([['2'],['0'],['0'],['0'],['0'],['0'],['0']])
    tres = np.array([['3'],['0'],['0'],['X'],['0'],['0'],['0']])
    cuatro = np.array([['4'],['0'],['0'],['x'],['0'],['0'],['0']])
    cinco = np.array([['5'],['X'],['0'],['0'],['0'],['X'],['0']])
    seis = np.array([['6'],['X'],['0'],['0'],['0'],['X'],['0']])
    siete = np.array([['7'],['X'],['0'],['0'],['0'],['0'],['0']])
    ocho = np.array([['8'],['0'],['0'],['0'],['0'],['X'],['0']])

    cine3 = np.hstack((num,uno))
    cine3 = np.hstack((cine3,dos))
    cine3 = np.hstack((cine3,tres))
    cine3 = np.hstack((cine3,cuatro))
    cine3 = np.hstack((cine3,cinco))
    cine3 = np.hstack((cine3,seis))
    cine3 = np.hstack((cine3,siete))
    cine3 = np.hstack((cine3,ocho))
    return cine3