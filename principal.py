from acciones import Caminos, equipar, mercader, pelea
from seres import *
from equipamiento import *
import os
import random as r



#nombre = input("Como te llamaras?: ")
nombre= 'luca'
#clase = input("Ingrese su clase:\n'tanque' 'asesino' 'soldado' : ")
clase='tanque'
heroe = Protagonista(nombre, clase)
heroe.ActualizarStats()

troll_1=Enemigo(nombre='Carlos el Troll',clase="troll")
perro_1=Enemigo(nombre='Pluto malvado', clase="perro")
gigante_1=Enemigo(nombre='Tipo Grande', clase="gigante")


elecciones = 0
primera=True
while elecciones != 5 and heroe.vida>0:
    Caminos(heroe=heroe)
    #elecciones+=1
if heroe.vida>0:
    print('Felicidades, lograste ganar el minijuego')
elif heroe.vida<=0:
    print('No fuiste capaz de dominar la mazmorra, loser...')
enter=input('Finalizar...')


#os.system('cls')


