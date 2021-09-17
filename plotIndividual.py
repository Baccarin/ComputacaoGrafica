import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from flask import *
from wand.color import Color

def plotCasa():
    casa = np.array([[ 0, 4,  4,  0,  0], #x
                        [ 2, 2,  0,  0,  2], #y
                        [ 0, 0,  0,  0,  0] #z=1
    ])

    xCasa, yCasa, zCasa = casa
    plt.plot(xCasa, yCasa, color = 'yellow')
    plt.axis('equal')
    plt.show()

def plotTelhado():
    telhado = np.array([[ 0, 2,  4, 0, 0], #x
                        [ 2, 3  ,  2, 2, 2], #y
                        [ 0, 0  ,  0, 0, 0] #z=1
    ])

    xTelhado, yTelhado, zTelhado = telhado
    plt.plot(xTelhado, yTelhado, color = 'blue')
    plt.axis('equal')
    plt.show()

def plotPorta():
    porta = np.array([[ 3, 3.5  ,  3.5, 3, 3], #x
                        [ 1  , 1  ,  0, 0, 1], #y
                        [ 0  , 0  ,  0, 0, 0] #z=1
    ])

    xPorta, yPorta, zPorta = porta
    plt.plot(xPorta, yPorta, color = 'green')
    plt.axis('equal')
    plt.show()

def plotJanela():
    janela = np.array([[ 0.5, 0.5  ,  1.5, 1.5, 0.5], #x
                        [ 0.5  , 1.5  ,  1.5, 0.5, 0.5], #y
                        [ 0  , 0  ,  0, 0, 0] #z=1
    ])

    xJanela, yJanela, zJanela = janela
    plt.plot(xJanela, yJanela, color = 'red')
    plt.axis('equal')
    plt.show()


plotCasa()
plotJanela()
plotPorta()
plotTelhado()