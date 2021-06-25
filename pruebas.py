from os import remove
import random as r
from seres import *
from equipamiento import *

troll=['Troll de las montañas','Troll de las nieves','Troll de Twitter']
gigante=['Gigante come hombres','Gigante de escarcha','Carlos el gigante malvado']
perro=['Perrito malvado','Pluto con hambre','Firulais con rabia']
enemigosTotal=[troll, gigante, perro]
clase=r.choice(enemigosTotal)
eleccion=r.choice(clase)
print(eleccion)