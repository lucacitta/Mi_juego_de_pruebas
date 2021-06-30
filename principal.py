from acciones import Caminos, generadorEnemigos, inicio, pelea, enter, verificar
from seres import *
from equipamiento import *
from os import system
introduccion=input('Saltar introduccion?(y/n)\nTu respuesta: ')
introduccion=verificar('y/n', introduccion)
system('cls')
if introduccion==False:
    print('Bienvenido a "Inserte un buen nombre" por Luca Cittá Giordano.\n\n'
    'Este juego es un proyecto para poner en practica mis conocimientos en python, mas adelante se agregara interfaz grafica.\n\n'
    'El objetivo es lograr vencer al jefe de la mazmorra, para eso deberas explorar la misma hasta llegar a el.\n'
    'Todo se genera de manera aleatoria, recomiendo varios intentos.\n'
    'Hay mas de 20 piezas de equipamiento, mas de 20 enemigos (incluidos varios jefes finales) y varios caminos a elegir.\n'
    'Es posible que haya algun fallo, ya sea tipeo o de codigo, de encontrar alguno, se agradece el aviso para solucionarlo.\n'
    'Ahora si, que lo disfrutes :) \n')
enter()
heroe=inicio()
elecciones = 0
primera=True
cantidad=0
while elecciones != 10 and heroe.vida>0:
    print(f'Elijes {10-elecciones} veces antes de la pelea final\n')
    Caminos(heroe=heroe)
    elecciones+=1
if elecciones==10:
    print('Llegas al final de la mazmorra, es momento de pelear contra el boss, espero que estes preparado')
    enter()
    boss=generadorEnemigos('boss')
    pelea(heroe=heroe,enemigo=boss)
    enter()
if heroe.vida>0:
    print('Felicidades, lograste ganar el minijuego')
elif heroe.vida<=0:
    print('No fuiste capaz de dominar la mazmorra, loser...')
enter=input('Finalizar...')


#os.system('cls')


