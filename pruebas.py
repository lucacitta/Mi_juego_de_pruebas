from os import remove
import random as r
from seres import *
from equipamiento import *

troll=['Troll de las montañas','Troll de las nieves','Troll de Twitter']
gigante=['Gigante come hombres','Gigante de escarcha','Carlos el gigante malvado']
perro=['Perrito malvado','Pluto con hambre','Firulais con rabia']
enemigosDebiles=[troll, perro]
enemigosFuertes=[gigante]
try:
    clase=r.choice(enemigosDebiles)
    eleccion=r.choice(clase)
    clase.remove(eleccion)
except IndexError:
    try:
        enemigosDebiles.remove(clase)
        clase=r.choice(enemigosDebiles)
        eleccion=r.choice(clase)
        clase.remove(eleccion)
    except IndexError:
        enemigosDebiles.remove(clase)
        clase=r.choice(enemigosDebiles)
        eleccion=r.choice(clase)
        clase.remove(eleccion)
clase=str(clase)
#print(clase)
enemigo=Enemigo(eleccion,clase)
print(enemigo.clase)
