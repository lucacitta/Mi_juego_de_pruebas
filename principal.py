from acciones import Caminos, equipar, pelea
from seres import *
from equipamiento import *




nombre = input("Como te llamaras?: ")
#nombre= 'luca'
clase = input("Ingrese su clase:\n'tanque' 'asesino' 'soldado' : ")
#clase='tanque'
heroe = Protagonista(nombre, clase)
heroe.ActualizarStats()

troll_1=Enemigo(nombre='Carlos el Troll',clase="troll")
perro_1=Enemigo(nombre='Pluto malvado', clase="perro")
gigante_1=Enemigo(nombre='Tipo Grande', clase="gigante")

elecciones = 0
while elecciones != 5:
    Caminos(heroe=heroe)
    #elecciones+=1
