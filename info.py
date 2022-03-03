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
    cuatro = np.array([['4'],['0'],['0'],['X'],['0'],['0'],['0']])
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
    tres = np.array([['3'],['0'],['0'],['0'],['0'],['0'],['0']])
    cuatro = np.array([['4'],['0'],['0'],['0'],['0'],['0'],['0']])
    cinco = np.array([['5'],['0'],['0'],['0'],['0'],['0'],['0']])
    seis = np.array([['6'],['0'],['0'],['0'],['0'],['0'],['0']])
    siete = np.array([['7'],['0'],['0'],['0'],['0'],['0'],['0']])
    ocho = np.array([['8'],['0'],['0'],['0'],['0'],['0'],['0']])

    cine3 = np.hstack((num,uno))
    cine3 = np.hstack((cine3,dos))
    cine3 = np.hstack((cine3,tres))
    cine3 = np.hstack((cine3,cuatro))
    cine3 = np.hstack((cine3,cinco))
    cine3 = np.hstack((cine3,seis))
    cine3 = np.hstack((cine3,siete))
    cine3 = np.hstack((cine3,ocho))
    return cine3

def Cine4():
    num = np.array([['O'], ['A'], ['B'], ['C'], ['D'], ['E'], ['F']])
    uno = np.array([['1'],['X'],['0'],['0'],['0'],['0'],['0']])
    dos = np.array([['2'],['X'],['0'],['0'],['X'],['0'],['0']])
    tres = np.array([['3'],['X'],['X'],['0'],['X'],['0'],['0']])
    cuatro = np.array([['4'],['0'],['X'],['0'],['X'],['0'],['0']])
    cinco = np.array([['5'],['0'],['X'],['0'],['X'],['0'],['X']])
    seis = np.array([['6'],['0'],['0'],['0'],['X'],['0'],['X']])
    siete = np.array([['7'],['X'],['0'],['0'],['X'],['0'],['0']])
    ocho = np.array([['8'],['X'],['0'],['0'],['X'],['0'],['0']])

    cine3 = np.hstack((num,uno))
    cine3 = np.hstack((cine3,dos))
    cine3 = np.hstack((cine3,tres))
    cine3 = np.hstack((cine3,cuatro))
    cine3 = np.hstack((cine3,cinco))
    cine3 = np.hstack((cine3,seis))
    cine3 = np.hstack((cine3,siete))
    cine3 = np.hstack((cine3,ocho))
    return cine3

def Cine1P():
    num = np.array([['OO'], ['A0'], ['B0'], ['C0'], ['D0'], ['E0'], ['F0']])
    uno = np.array([['O1'],['A1'],['B1'],['C1'],['D1'],['E1'],['F1']])
    dos = np.array([['O2'],['A2'],['0X'],['C2'],['D2'],['E2'],['F2']])
    tres = np.array([['O3'],['A3'],['0X'],['C3'],['D3'],['E3'],['F3']])
    cuatro = np.array([['O4'],['A4'],['B4'],['C4'],['D4'],['E4'],['F4']])
    cinco = np.array([['O5'],['A5'],['B5'],['C5'],['D5'],['0X'],['F5']])
    seis = np.array([['O6'],['A6'],['B6'],['C6'],['D6'],['0X'],['F6']])
    siete = np.array([['O7'],['A7'],['B7'],['C7'],['D7'],['0X'],['F7']])
    ocho = np.array([['O8'],['A8'],['B8'],['C8'],['D8'],['0X'],['F8']])

    cine1 = np.hstack((num,uno))
    cine1 = np.hstack((cine1,dos))
    cine1 = np.hstack((cine1,tres))
    cine1 = np.hstack((cine1,cuatro))
    cine1 = np.hstack((cine1,cinco))
    cine1 = np.hstack((cine1,seis))
    cine1 = np.hstack((cine1,siete))
    cine1 = np.hstack((cine1,ocho))
    return cine1

def Cine2P():
    num = np.array([['OO'], ['A0'], ['B0'], ['C0'], ['D0'], ['E0'], ['F0']])
    uno = np.array([['O1'],['A1'],['B1'],['C1'],['D1'],['E1'],['F1']])
    dos = np.array([['O2'],['A2'],['B2'],['C2'],['D2'],['E2'],['F2']])
    tres = np.array([['O3'],['A3'],['B3'],['0X'],['D3'],['E3'],['F3']])
    cuatro = np.array([['O4'],['A4'],['B4'],['0X'],['D4'],['E4'],['F4']])
    cinco = np.array([['O5'],['0X'],['B5'],['C5'],['D5'],['0X'],['F5']])
    seis = np.array([['O6'],['0X'],['B6'],['C6'],['D6'],['0X'],['F6']])
    siete = np.array([['O7'],['0X'],['B7'],['C7'],['D7'],['E7'],['F7']])
    ocho = np.array([['O8'],['A8'],['B8'],['C8'],['D8'],['0X'],['F8']])

    cine1 = np.hstack((num,uno))
    cine1 = np.hstack((cine1,dos))
    cine1 = np.hstack((cine1,tres))
    cine1 = np.hstack((cine1,cuatro))
    cine1 = np.hstack((cine1,cinco))
    cine1 = np.hstack((cine1,seis))
    cine1 = np.hstack((cine1,siete))
    cine1 = np.hstack((cine1,ocho))
    return cine1

def Cine3P():
    num = np.array([['OO'], ['A0'], ['B0'], ['C0'], ['D0'], ['E0'], ['F0']])
    uno = np.array([['O1'],['A1'],['B1'],['C1'],['D1'],['E1'],['F1']])
    dos = np.array([['O2'],['A2'],['B2'],['C2'],['D2'],['E2'],['F2']])
    tres = np.array([['O3'],['A3'],['B3'],['C3'],['D3'],['E3'],['F3']])
    cuatro = np.array([['O4'],['A4'],['B4'],['C4'],['D4'],['E4'],['F4']])
    cinco = np.array([['O5'],['A5'],['B5'],['C5'],['D5'],['E5'],['F5']])
    seis = np.array([['O6'],['A6'],['B6'],['C6'],['D6'],['E6'],['F6']])
    siete = np.array([['O7'],['A7'],['B7'],['C7'],['D7'],['E7'],['F7']])
    ocho = np.array([['O8'],['A8'],['B8'],['C8'],['D8'],['E8'],['F8']])

    cine1 = np.hstack((num,uno))
    cine1 = np.hstack((cine1,dos))
    cine1 = np.hstack((cine1,tres))
    cine1 = np.hstack((cine1,cuatro))
    cine1 = np.hstack((cine1,cinco))
    cine1 = np.hstack((cine1,seis))
    cine1 = np.hstack((cine1,siete))
    cine1 = np.hstack((cine1,ocho))
    return cine1

def Cine4P():
    num = np.array([['OO'], ['A0'], ['B0'], ['C0'], ['D0'], ['E0'], ['F0']])
    uno = np.array([['O1'],['0X'],['B1'],['C1'],['D1'],['E1'],['F1']])
    dos = np.array([['O2'],['0X'],['B2'],['C2'],['0X'],['E2'],['F2']])
    tres = np.array([['O3'],['0X'],['0X'],['C3'],['0X'],['E3'],['F3']])
    cuatro = np.array([['O4'],['A4'],['0X'],['C4'],['0X'],['E4'],['F4']])
    cinco = np.array([['O5'],['A5'],['0X'],['C5'],['0X'],['E5'],['0X']])
    seis = np.array([['O6'],['A6'],['B6'],['C6'],['0X'],['E6'],['0X']])
    siete = np.array([['O7'],['0X'],['B7'],['C7'],['0X'],['E7'],['F7']])
    ocho = np.array([['O8'],['0X'],['B8'],['C8'],['0X'],['E8'],['F8']])

    cine1 = np.hstack((num,uno))
    cine1 = np.hstack((cine1,dos))
    cine1 = np.hstack((cine1,tres))
    cine1 = np.hstack((cine1,cuatro))
    cine1 = np.hstack((cine1,cinco))
    cine1 = np.hstack((cine1,seis))
    cine1 = np.hstack((cine1,siete))
    cine1 = np.hstack((cine1,ocho))
    return cine1