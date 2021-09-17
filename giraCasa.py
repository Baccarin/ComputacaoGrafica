import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from flask import *
from wand.color import Color

casa = np.array([[ 0, 4,  4,  0,  0], #x
                     [ 2, 2,  0,  0,  2], #y
                     [ 0, 0,  0,  0,  0] #z=1
])


xCasa, yCasa, zCasa = casa

telhado = np.array([[ 0, 2,  4, 0, 0], #x
                      [ 2, 3  ,  2, 2, 2], #y
                      [ 0, 0  ,  0, 0, 0] #z=1
])

xTelhado, yTelhado, zTelhado = telhado

porta = np.array([[ 3, 3.5  ,  3.5, 3, 3], #x
                      [ 1  , 1  ,  0, 0, 1], #y
                      [ 0  , 0  ,  0, 0, 0] #z=1
])

xPorta, yPorta, zPorta = porta


janela = np.array([[ 0.5, 0.5  ,  1.5, 1.5, 0.5], #x
                      [ 0.5  , 1.5  ,  1.5, 0.5, 0.5], #y
                      [ 0  , 0  ,  0, 0, 0] #z=1
])

xJanela, yJanela, zJanela = janela


T = np.array([
              [np.cos(np.pi/2), -np.sin(np.pi/2), 2],
              [np.sin(np.pi/2), np.cos(np.pi/2), 0]
])

plt.plot(xCasa, yCasa, xTelhado, yTelhado, xPorta, yPorta, xJanela, yJanela, color = 'blue')
plt.axis('equal')
plt.show()


xCasaGirada, yCasaGirada = np.matmul(T,casa)
xTelhadoGirado, yTelhadoGirado = np.matmul(T,telhado)
xPortaGiraado, yPortaGirado = np.matmul(T,porta)
xJanelaGirado, yJanelaGirado = np.matmul(T,janela)

plt.plot(xCasaGirada, yCasaGirada, xTelhadoGirado, yTelhadoGirado, xPortaGiraado, yPortaGirado, xJanelaGirado, yJanelaGirado, color = 'green')
plt.axis('equal')
plt.show()