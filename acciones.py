from equipamiento import *
from seres import *
import random as r
from os import system

caminos=[
    'pelea','pelea','pelea','pelea','pelea','pelea','pelea',
    'evento','evento','evento',
    'cofre',
    'descanso','descanso','descanso',
    'recarga','recarga','recarga',
    'mercader','mercader','mercader']
eventos=['herrero','vidaPorEquipamiento','aumentoStats','elegirEquipamiento','lastimarse','pociones']
efectos=['vida+','vida-','armadura+','armadura-','danio+', 'danio-','agilidad+','agilidad-']



def generadorEquipamiento(heroe):
    try:
        lista=['espadas', 'armaduras', 'anillos']
        tipos=r.choice(lista)
        seleccionado=r.choice(equipamientoTotal[tipos])
    except IndexError:
        try:
            lista.remove(tipos)
            tipos=r.choice(lista)
            seleccionado=r.choice(equipamientoTotal[tipos])
        except IndexError:
            lista.remove(tipos)
            tipos=r.choice(lista)
            seleccionado=r.choice(equipamientoTotal[tipos])
    equipamientoTotal[tipos].remove(seleccionado)
    return seleccionado, tipos

def equipar(heroe, equipando):
    if equipando.equiparEn == "arma":
        equiparEn=equipando.equiparEn
        heroe.Equipado(equiparEn, danio=equipando.danio, agilidad=equipando.agilidad,nombre=equipando.nombreEquipamiento)
    elif equipando.equiparEn == "armadura":
        equiparEn=equipando.equiparEn
        heroe.Equipado(equiparEn, armadura=equipando.armadura, agilidad=equipando.agilidad, vida=equipando.vida, nombre=equipando.nombreEquipamiento)
    elif equipando.equiparEn == "anillo":
        equiparEn=equipando.equiparEn
        heroe.Equipado(equiparEn, armadura=equipando.armadura, agilidad=equipando.agilidad, vida=equipando.vida, danio=equipando.danio, nombre=equipando.nombreEquipamiento)
    else:
        print("No se equipo nada")



def generadorEnemigos(tipo):
    clase='vacio'
    if tipo=='debil':
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
    elif tipo=='fuerte':
        try:
            clase=r.choice(enemigosFuertes)
            eleccion=r.choice(clase)
            clase.remove(eleccion)
        except IndexError:
            try:
                enemigosDebiles.remove(clase)
                clase=r.choice(enemigosFuertes)
                eleccion=r.choice(clase)
                clase.remove(eleccion)
            except IndexError:
                enemigosDebiles.remove(clase)
                clase=r.choice(enemigosFuertes)
                eleccion=r.choice(clase)
                clase.remove(eleccion)
    elif tipo == 'boss':
        eleccion=r.choice(enemigosBoses)
    if clase == troll:
        clase='troll'
    elif clase == esqueleto:
        clase='esqueleto'
    elif clase == perro:
        clase='perro'
    if clase == animal:
        clase='animal'
    elif clase == gigante:
        clase='gigante'
    elif clase == mago:
        clase='mago'
    if eleccion =='Dragon Anciano':
        clase='dragon'
    elif eleccion == 'Ogro de roca':
        clase='ogroPiedra'
    elif eleccion =='Ninja antiguo jackie chan':
        clase='ninja'
    else:
        print(f"No entro en ninguna clase: {clase}")
    enemigo=eleccion
    enemigo=Enemigo(enemigo, clase)
    return enemigo

def pelea(heroe, enemigo):
    system('cls')
    auxAgilidadHeroe = heroe.agilidad
    auxAgilidadEnemigo = enemigo.agilidad
    escp=False
    while heroe.vida > 0 and enemigo.vida > 0 and escp==False:
        print(f'{heroe.nombre}                  {enemigo.nombre}\nHP: {heroe.vida}/{heroe.vidaMaxima}           HP: {enemigo.vida}/{enemigo.vidaMaxima}')
        print(f'Daño: {heroe.danio}              Daño: {enemigo.danio}\nArmadura: {heroe.armadura}          Armadura: {enemigo.armadura}')
        print(f'Agilidad: {heroe.agilidad}          Agilidad: {enemigo.agilidad}\n\n')
        opcion=input("Que vas a hacer?\n Atacar(1)\n Pocion(2)\n Intentar huir(3)\n Tu decision: ")
        opcion=verificar("numero",opcion,3)
        system('cls')
        if opcion == '1':
            if auxAgilidadHeroe > auxAgilidadEnemigo:
                aux = ((auxAgilidadHeroe-auxAgilidadEnemigo)/100)
                if (0.5+aux)>r.random():
                    ataque(heroe=heroe,enemigo=enemigo, atacando=0)
                else:
                    ataque(enemigo=enemigo,heroe=heroe, atacando=1)
            elif auxAgilidadHeroe < auxAgilidadEnemigo:
                aux = ((auxAgilidadEnemigo-auxAgilidadHeroe)/100)
                if (aux+0.5)>r.random():
                    ataque(enemigo=enemigo,heroe=heroe, atacando=1)
                else:
                    ataque(heroe=heroe,enemigo=enemigo, atacando=0)
            else:
                if 0.5<r.random():
                    ataque(heroe=heroe,enemigo=enemigo, atacando=0)
                else:
                    ataque(enemigo=enemigo,heroe=heroe, atacando=1)
        if opcion=='2':
            aux=heroe.UsarPocion()
            if aux == 0:
                ataque(enemigo=enemigo, heroe=heroe, atacando=2)
        if opcion=='3':
            escape=(heroe.agilidad-enemigo.agilidad)/100
            if (0.5+escape)<r.random():
                escp=True
            else:
                print('Intentas escaparte, pero eres alcanzado por el enemigo')
                ataque(enemigo=enemigo, heroe=heroe, atacando=3)
        if heroe.agilidad>=enemigo.agilidad*2 and opcion=='1':
            ataque(heroe=heroe,enemigo=enemigo, atacando=4)
        elif enemigo.agilidad>=heroe.agilidad*2 and opcion=='1':
            ataque(enemigo=enemigo, heroe=heroe, atacando=5)
        if escp==True:
            print(f'\nTe logras escapar de {enemigo.nombre}')
        elif heroe.vida <= 0:
            print("Fuiste Derrotado por el enemigo")
        elif enemigo.vida <= 0:
            print(f"\nGanaste la pelea contra {enemigo.nombre}")
            drop(heroe=heroe, enemigo=enemigo)




def ataque(heroe, enemigo, atacando):
    if atacando == 0:
        danioVerdadero=heroe.danio-enemigo.defensa
        crit=critico()
        if crit == 1:
            print(f'{heroe.nombre} ataca, causando {danioVerdadero} puntos de daño')
            enemigo.vidaPerdida += danioVerdadero
        else:
            print(f'{heroe.nombre}, golpea con un ataque critico, causando {danioVerdadero*2} puntos de daño')
            enemigo.vidaPerdida += heroe.danio*2
        enemigo.ActualizarEnemigos()
        if enemigo.vida > 0:
            danioVerdadero=enemigo.danio-heroe.defensa
            print(f'{enemigo.nombre} ataca, causando {danioVerdadero} puntos de daño')
            heroe.vidaPerdida += danioVerdadero
            heroe.ActualizarStats()
    elif atacando ==1:
        danioVerdadero=enemigo.danio-heroe.defensa
        print(f'{enemigo.nombre} ataca, causando {danioVerdadero} puntos de daño')
        heroe.vidaPerdida += danioVerdadero
        heroe.ActualizarStats()
        if heroe.vida > 0:
            danioVerdadero=heroe.danio-enemigo.defensa
            crit=critico()
            if crit == 1:
                print(f'{heroe.nombre} ataca, causando {danioVerdadero} puntos de daño')
                enemigo.vidaPerdida += danioVerdadero
            else:
                print(f'{heroe.nombre}, golpea con un ataque critico, causando {danioVerdadero*2} puntos de daño')
                enemigo.vidaPerdida += danioVerdadero*2
            enemigo.ActualizarEnemigos()
    elif atacando ==2:
        danioVerdadero=enemigo.danio-heroe.defensa
        print(f'{enemigo.nombre} ataca, causando {danioVerdadero} puntos de daño')
        heroe.vidaPerdida += danioVerdadero
        heroe.ActualizarStats()
    elif atacando==3:
        danioVerdadero=enemigo.danio-heroe.defensa
        print(f'{enemigo.nombre} ataca mientras intentas escapar, causando {danioVerdadero*2} puntos de daño, ya que te alcanza de espaldas')
        heroe.vidaPerdida += danioVerdadero
        heroe.ActualizarStats()
    elif atacando==4:
        danioVerdadero=heroe.danio-enemigo.defensa
        crit=critico()
        if crit == 1:
            print(f'{heroe.nombre} realiza un ataque extra por su agilidad, causando {danioVerdadero} puntos de daño ')
            enemigo.vidaPerdida += danioVerdadero
        else:
            print(f'{heroe.nombre}, realiza un ataque extra por su agilidad y encima critico, causando {danioVerdadero*2} puntos de daño')
            enemigo.vidaPerdida += danioVerdadero*2
        enemigo.ActualizarEnemigos()
    elif atacando==5:
        danioVerdadero=enemigo.danio-heroe.defensa
        print(f'{enemigo.nombre} realiza un ataque extra por su agilidad, causando {danioVerdadero} puntos de daño')
        heroe.vidaPerdida += danioVerdadero
        heroe.ActualizarStats()

def critico():
    prob=r.random()
    if prob>0.3:
        return 1
    else:
        return 2,

def drop(heroe, enemigo):
    if enemigo.clase=='perro':
        oroGanado=r.randrange(3,8)
    elif enemigo.clase=='troll':
        oroGanado=r.randrange(6,11)
    elif enemigo.clase=='esqueleto':
        oroGanado=r.randrange(6,11)
    elif enemigo.clase=='gigante':
        oroGanado=r.randrange(15,20)
    elif enemigo.clase=='animal':
        oroGanado=r.randrange(11,19)
    elif enemigo.clase=='mago':
        oroGanado=r.randrange(9,22)
    heroe.oro+=oroGanado
    print(f'Al derrotar a {enemigo.nombre}, obtubiste {oroGanado} monedas de oro, monedas totales {heroe.oro}')



def Caminos(heroe):
    creados=0
    opcion1='Nada'
    opcion2='Nada'
    while creados != 2:
        opcion=r.choice(caminos)
        if heroe.auxCamino==True:   #Asegura una pelea la primera vez
            heroe.auxCamino=False
            opcion='pelea'
        if opcion==opcion1:         #No permite caminos repetidos
            continue
        if opcion=='pelea':                     #Pelea
            fuerza=['fuerte','debil']
            poder=r.choice(fuerza)
            if poder == 'fuerte':
                print(f'En el camino {creados+1} hay un mounstruo bastante fuerte')
            if poder == 'debil':
                print(f'En el camino {creados+1} hay un mounstruo el cual no parece muy poderoso')
        elif opcion=='evento':                  #Evento
            print(f'En el camino {creados+1} no sabes que te podras encontrar:')
        elif opcion=='cofre':                   #Cofre
            print(f'En el camino {creados+1} ves un gran cofre dorado')
        elif opcion=='descanso':                #Descanso
            print(f'En el camino {creados+1} ves una hoguera, donde podrias descansar')
        elif opcion=='recarga':                 #Recarga pociones
            print(f'En el camino {creados+1} observas un caldero, con el cual recargar tus pociones')
        elif opcion=='mercader':
            print(f'En el camino {creados+1} ves un carro tirado de caballos, podria ser un mercader errante')
        creados +=1
        if creados==1:
            opcion1=opcion
        else:
            opcion2=opcion
    eleccionCamino=input('Elija por cual camino desea avanzar(1/2): ')
    eleccionCamino=verificar('numero',eleccionCamino,2)
    if eleccionCamino=='1':
        opcion=opcion1
    elif eleccionCamino=='2':
        opcion=opcion2
    system('cls')
    if opcion=='pelea':
        enemigo=generadorEnemigos(poder)
        pelea(heroe,enemigo)
    elif opcion=='evento':
        generadorEvento(heroe)
    elif opcion=='cofre':
        seleccionado,tipos=generadorEquipamiento(heroe)
        generadorCofre(seleccionado=seleccionado,tipos=tipos, heroe=heroe)
    elif opcion=='descanso':
        print('Decides descansar junto a la hoguera, recuperando toda tu vida y poniendote de buen humor, es importante estar de buen humor')
        heroe.vida=heroe.vidaMaxima
    elif opcion=='recarga':
        print(f'Logras rellenar tus viales de pociones, volviendo a tener {heroe.pocionesMaximas} pociones a dispocision.')
        heroe.pociones=heroe.pocionesMaximas
    elif opcion=='mercader':
        mercader(heroe)
    enter()
    system('cls')

def generadorCofre(seleccionado, tipos, heroe):
    print(f'Al abrir el cofre te encuentras con {seleccionado.nombreEquipamiento}')
    if tipos=='espadas':
        print(f"Daño: {seleccionado.danio}\nAgilidad: {seleccionado.agilidad}")
    elif tipos =='armaduras':
        print(f" Armadura: {seleccionado.armadura}\n Agilidad: {seleccionado.agilidad}\n Vida: {seleccionado.vida}")
    else:
        print(f" Armadura: {seleccionado.armadura}\n Agilidad: {seleccionado.agilidad}\n Vida: {seleccionado.vida}\n Daño: {seleccionado.danio}")
    eleccion= input(('deseas equiparlo? (y/n): '))
    eleccion=verificar('y/n',eleccion)
    if eleccion == True:
        equipando=seleccionado
        equipar(heroe=heroe, equipando=equipando)
    elif eleccion==False:
        print(f'Descartas {seleccionado.nombreEquipamiento} y sigues tu camino')

def mercader(heroe):
    opcion1, opcion2, opcion3= r.choice(equipamientoTotal['espadas']), r.choice(equipamientoTotal['armaduras']), r.choice(equipamientoTotal['anillos'])
    precio1, precio2, precio3= r.randrange(10,20), r.randrange(10,20), r.randrange(10,20)
    comprado1, comprado2, comprado3=False,False,False
    alcanzo=False
    while alcanzo==False:
        print('Te encuentras con un extraño sujeto en una carreta, al verte se detiene y hace señas llamandote\nVas hacia el y te saluda diciendo "welcome stranger" con una voz tenebrosa')
        print('En el momento que te saluda comienza a mostrarte 3 mercancias que podrian interesarte\n')
        print(
            f'Opcion 1, Precio: {precio1}        Opcion 2, Precio: {precio2}         Opcion 3, Precio: {precio3}\n'
            f'{opcion1.nombreEquipamiento}           {opcion2.nombreEquipamiento}               {opcion3.nombreEquipamiento}\n'
            f'Agillidad: {opcion1.agilidad}               Agilidad: {opcion2.agilidad}                  Agilidad: {opcion3.agilidad}\n'
            f'Armadura: 0                  Armadura: {opcion2.armadura}                   Armadura: {opcion3.armadura}\n'
            f'Vida: 0                        Vida: {opcion2.vida}                      Vida: {opcion3.vida}\n'
            f'Daño: {opcion1.danio}                       Daño: 0                       Daño: {opcion3.danio}\n'
            )
        eleccion=input(f'Si deseas y puedes comprar alguna pieza de equipamiento elige (1/2/3) o si no deseas comprar nada (4)\nOro actual={heroe.oro}\nTu respuesta: ')
        eleccion=verificar('numero',eleccion,4)
        print('\n')
        if eleccion=='1':
            if comprado1==True:
                print('Ya has comprado este objeto')
                alcanzo=False
            else:
                if heroe.oro>=precio1:
                    heroe.oro-=precio1
                    equipar(heroe=heroe, equipando=opcion1)
                    equipamientoTotal['espadas'].remove(opcion1)
                    comprado1=True
                    alcanzo=True
                else:
                    print(f'No tienes el dinero suficiente para comprar {opcion1.nombreEquipamiento}')
                    enter()
        elif eleccion=='2':
            if comprado2==True:
                print('Ya has comprado este objeto')
                alcanzo=False
            else:
                if heroe.oro>=precio2:
                    heroe.oro-=precio2
                    comprado2=True
                    equipar(heroe=heroe, equipando=opcion2)
                    equipamientoTotal['armaduras'].remove(opcion2)
                    alcanzo=True
                else:
                    print(f'No tienes el dinero suficiente para comprar {opcion2.nombreEquipamiento}')
                    enter()
        elif eleccion=='3':
            if comprado3==True:
                print('Ya has comprado este objeto')
                alcanzo=False
            else:
                if heroe.oro>=precio3:
                    heroe.oro-=precio3
                    comprado3=True
                    equipar(heroe=heroe, equipando=opcion3)
                    equipamientoTotal['anillos'].remove(opcion3)
                    alcanzo=True
                else:
                    print(f'No tienes el dinero suficiente para comprar {opcion3.nombreEquipamiento}')
                    enter()
        elif eleccion=='4':
            alcanzo=True
            continue
        seguir=input('Desea seguir comprando? (y/n)\nSu respuesta: ')
        seguir=verificar('y/n',seguir)
        if seguir==True:
            alcanzo=False
        elif seguir==False:
            alcanzo=True
        system('cls')
    print('Saludas con desconfianza al extraño mercader y sigues tu camino')



def generadorEvento(heroe):
    eleccion=r.choice(eventos)
    eventos.remove(eleccion)
    if eleccion=='herrero':
        eventoHerrero(heroe)
    elif eleccion=='vidaPorEquipamiento':
        eventoVidaPorEquipamiento(heroe)
    elif eleccion=='aumentoStats':
        eventoStats(heroe)
    elif eleccion=='elegirEquipamiento':
        eventoElegirEquipamiento(heroe)
    elif eleccion=='lastimarse':
        eventoLastimarse(heroe)
    elif eleccion=='pociones':
        eventoPociones(heroe)

def eventoHerrero(heroe):
    print('Ves una casa a lo lejos, al acercarte te das cuenta que se trata del hogar de un herrero')
    enter()
    print('Al llegar a la casa ves a un herrero trabajando que al ver tu equipamiento te observa y dice\n')
    print('* Deberia darte verguenza el estado de tus armas y armadura, por un modico precio podria arreglarlas*\n')
    alcanza=False
    while alcanza==False:
        seleccion=input(f'Elije que deseas hacer (Tienes {heroe.oro} monedas)\nAfilar armas Coste:10 monedas (1)\nReforzar armadura Coste:10 monedas (2)\nMejorar ambas coste:18 monedas (3)\nNo contratar sus servicios (4)\nTu respuesta: ')
        seleccion=verificar('numero',seleccion,4)
        if seleccion=='1':
            if heroe.oro>=10:
                heroe.danioExtra+=20
                print('El herrero afila amablemente tus armas y luego le entregas su paga (Daño +20).\nFinalmente, agradeces y sigues tu camino')
                heroe.oro-=10
                alcanza=True
            else:
                print('No tienes el oro suficiente')
        elif seleccion=='2':
            if heroe.oro>=10:
                heroe.armaduraExtra+=30
                print('El herrero refuerza amablemente tu armadura y luego le entregas su paga (Armadura +30).\nFinalmente, agradeces y sigues tu camino')
                heroe.oro-=10
                alcanza=True
            else:
                print('No tienes el oro suficiente')
        elif seleccion=='3':
            if heroe.oro>=18:
                heroe.danioExtra+=20
                heroe.armaduraExtra+=30
                print('El herrero mejora ambas partes de tu equipamiento y luego le entregas su paga (Daño +20--Armadura +30).\nFinalmente, agradeces y sigues tu camino')
                heroe.oro-=18
                alcanza=True
            else:
                print('No tienes el oro suficiente')
        elif seleccion=='4':
            alcanza=True
            print('Le dices al herrero que no solicitaras sus servicios y sigues tu camino mientras te observa con una mirada sobradora')

def eventoVidaPorEquipamiento(heroe):
    print('Encuentras una antigua fuente de una mujer, arrodillada con un caliz en sus manos y una inscripcion en idioma antiguo')
    enter()
    print('Al acercarte y ponerte tus lentes, lees el mensaje y lo traduces en algo como "Vuestra sangre sera recompensada" ')
    eleccion=input('Deseas arriesgarte y entregar un poco de tu sangre? (y/n)\nTu decision: ')
    eleccion=verificar('y/n',eleccion)
    if eleccion==True:
        heroe.vida-=(heroe.vida/5)
        objeto, tipo = generadorEquipamiento(heroe)
        print('Realizas un corte en tu mano y se escucha un sonido extraño')
        print(f'La estatua se parte en dos y encuentras {objeto.nombreEquipamiento}')
        enter()
        equipar(heroe,objeto)
        print('Luego sigues tu camino')
    elif eleccion==False:
        print('Decides no arriesgarte y sigues tu camino')

def eventoStats(heroe):
    opcion=input('Encuentras un caldero con restos de una pocion, podria ser beneficiosa o maligna, deseas beberla? (y/n)\nTu Respuesta:')
    opcion=verificar('y/n',opcion)
    if opcion==True:
        azar=r.choice(efectos)
        efectos.remove(azar)
        if azar=='vida+':
                heroe.vidaExtra+=50
                print('Tomas los restos de la pocion y te sientes rejuvenecido (Vida Maxima +50)\nLuego sigues tu camino')
        elif azar=='danio+':
                heroe.danioExtra+=10
                print('Tomas los restos de la pocion y te sientes poderoso (Danio + 10) \nLuego sigues tu camino')
        elif azar=='armadura+':
                heroe.armaduraExtra+=30
                print('Tomas los restos de la pocion y te sientes poderoso, como si aguantases mas (Armadura + 30) \nLuego sigues tu camino')
        elif azar=='agilidad+':
                heroe.agilidadExtra+=30
                print('Tomas los restos de la pocion y te sientes mas ligero, casi como si tus pies no tocaran el suelo (Agilidad + 30) \nLuego sigues tu camino')
        elif azar=='vida-':
                heroe.vidaExtra-=50
                print('Tomas los restos de la pocion y te sientes que te arde el estomago, no parece haber sido buena idea (Vida Maxima -50)\nLuego sigues tu camino')
        elif azar=='danio-':
                heroe.danioExtra-=10
                print('Tomas los restos de la pocion y te sientes con poca fuerza, casi no puedes levantar tu espada (Danio - 10) \nLuego sigues tu camino')
        elif azar=='armadura-':
                heroe.armaduraExtra-=30
                print('Tomas los restos de la pocion y te sientes debil, como si estuvieras enfermo (Armadura - 30) \nLuego sigues tu camino')
        elif azar=='agilidad+':
                heroe.agilidadExtra-30
                print('Tomas los restos de la pocion y te sientes pesado, casi como si salieras de un tenedor libre (Agilidad - 30) \nLuego sigues tu camino')
    elif opcion==False:
        print('Decides no arriesgarte a tomar una pocion que no conoces y sigues tu camino')

def eventoElegirEquipamiento(heroe):
    opcion1, tipo1=generadorEquipamiento(heroe)
    opcion2, tipo2=generadorEquipamiento(heroe)
    print('Ves la estatua de un angel, observas que en cada una de sus manos tiene un equipamiento')
    enter()
    eleccion=input(f'En su mano izquierda ves {opcion1.nombreEquipamiento}(1) y en su mano derecha {opcion2.nombreEquipamiento}(2), cual deseas recoger? (1/2): ')
    eleccion=verificar('numero',eleccion,2)
    if eleccion=='1':
        print(f'Al recoger {opcion1.nombreEquipamiento}, ves como el angel cierra su otra mano, impidiendote obtener {opcion2.nombreEquipamiento}')
        equipar(heroe,opcion1)
    elif eleccion=='2':
        print(f'Al recoger {opcion2.nombreEquipamiento}, ves como el angel cierra su otra mano, impidiendote obtener {opcion1.nombreEquipamiento}')
        equipar(heroe,opcion2)

def eventoLastimarse(heroe):
    azar=r.random()
    if azar<=0.25:
        print('Activas una trampa y una flecha te impacta en tu brazo izquierdo')
        enter()
        print(f'Logras quitarla, pero perdiste bastante sangre (vida - {int(heroe.vida/4)})')
        heroe.vida-=int(heroe.vida/4)
    elif azar>0.25 and azar<=0.5:
        print(f'Una de tus heridas se infecta, sobreviviras, por el momento...(vida - {int(heroe.vida/3)} )')
        heroe.vida-=int(heroe.vida/3)
    elif azar>0.5 and azar<=0.75:
        print(f'Te patinas con una cascara de banana *Si, hasta aca mi imaginacion* (vida - {int(heroe.vida/4)})')
        heroe.vida-=int(heroe.vida/4)
    else:
        print(f'Una serpiente logra morderte sorpresivamente, por suerte no era venenosa (vida - {int(heroe.vida/10)})')
        heroe.vida-=int(heroe.vida/10)

def eventoPociones(heroe):
    print('Ves un anciano a lo lejos y decides acercarte a el')
    enter()
    print('Al llegar te das cuenta que es Tusam, el gran mago\nEl te mira con una sonrisa y decide hacerte un regalo')
    regalo=input('Puedes elegir entre llevar una pocion extra (1), o aumentar su efecto curativo(2)\nQue decides?(1/2) ')
    regalo=verificar('numero',regalo,2)
    if regalo=='1':
        heroe.pociones+=1
        heroe.pocionesMaximas+=1
        print(f'Tusam asiente, ahora puedes llevar {heroe.pocionesMaximas} pociones, tienes {heroe.pociones} llenas')
    elif regalo=='2':
        heroe.pocionesCuracion+=40
        print(f'Tusam asiente, ahora tus pociones regeneran {heroe.pocionesCuracion}')


def inicio():
    nombre = input("Como te llamaras?: ")
    nombre=verificar('nombre',nombre)
    system('cls')
    eleccion = input("Seleccione su clase:\n\n"
    "Soldado (1)                                Tanque (2)                            Asesino (3)\n"
    "Vida inicial=100                       Vida inicial=150                        Vida inicial=80\n"
    "Danio inicial=30                       Danio inicial=20                        Danio inicial=50\n"
    "Agilidad inicial=20                    Agilidad inicial=10                     Agilidad inicial=40\n"
    "Armadura inicial=20                    Armadura inicial=40                     Armadura asesino=5\n"
    "\nTu eleccion: "
    )
    eleccion=verificar('numero',eleccion,3)
    clase=eleccionClase(eleccion)
    system('cls')
    heroe = Protagonista(nombre, clase)
    heroe.ActualizarStats()
    return heroe

def enter():
    enter=input('Continuar...')

def eleccionClase(clase):
    if clase=='1':
        clase='soldado'
    elif clase=='2':
        clase='tanque'
    elif clase=='3':
        clase='asesino'
    print(f'Se a seleccionado correctamente la clase {clase}, mucha suerte.')
    enter()
    return clase

