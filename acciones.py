from equipamiento import *
from seres import *
import random as r



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

def critico():
    prob=r.random()
    if prob>0.3:
        return 1
    else:
        return 2,

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

def pelea(heroe, enemigo):
    auxAgilidadHeroe = heroe.agilidad
    auxAgilidadEnemigo = enemigo.agilidad
    escp=False
    while heroe.vida > 0 and enemigo.vida > 0 and escp==False:
        print(f'{heroe.nombre}                  {enemigo.nombre}\nHP: {heroe.vida}/{heroe.vidaMaxima}           HP: {enemigo.vida}/{enemigo.vidaMaxima}')
        print(f'Daño: {heroe.danio}              Daño: {enemigo.danio}\nArmadura: {heroe.armadura}          Armadura: {enemigo.armadura}')
        print(f'Agilidad: {heroe.agilidad}          Agilidad: {enemigo.agilidad}\n\n')
        opcion=int(input("Que vas a hacer?\n Atacar(1)\n Pocion(2)\n Intentar huir(3)\n Tu decision: "))
        if opcion == 1:
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
        if opcion==2:
            aux=heroe.UsarPocion()
            if aux == 0:
                ataque(enemigo=enemigo, heroe=heroe, atacando=2)
        if opcion==3:
            escape=(heroe.agilidad-enemigo.agilidad)/100
            if (0.5+escape)<r.random():
                escp=True
            else:
                ataque(enemigo=enemigo, heroe=heroe, atacando=3)
        if heroe.agilidad>enemigo.agilidad*2:
            ataque(heroe=heroe,enemigo=enemigo, atacando=4)
        if enemigo.agilidad>heroe.agilidad*2:
            ataque(enemigo=enemigo, heroe=heroe, atacando=5)
    if heroe.vida <= 0:
        print("Perdiste")
    if enemigo.vida <= 0:
        print("Ganaste")
    if escp==True:
        print(f'Te logras escapar de {enemigo.nombre}')

def generadorEnemigos():
    try:
        clase=r.choice(enemigosTotal)
        eleccion=r.choice(clase)
        clase.remove(eleccion)
    except IndexError:
        try:
            enemigosTotal.remove(clase)
            clase=r.choice(enemigosTotal)
            eleccion=r.choice(clase)
            clase.remove(eleccion)
        except IndexError:
            enemigosTotal.remove(clase)
            clase=r.choice(enemigosTotal)
            eleccion=r.choice(clase)
            clase.remove(eleccion)
    if clase == troll:
        clase='troll'
    elif clase == gigante:
        clase='gigante'
    elif clase == perro:
        clase='perro'
    else:
        print(f"No entro en ninguna clase: {clase}")
    enemigo=eleccion
    enemigo=Enemigo(enemigo, clase)
    return enemigo

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

def generadorCofre(seleccionado, tipos, heroe):
    print(f'Al abrir el cofre te encuentras con {seleccionado.nombreEquipamiento}')
    if tipos=='espadas':
        print(f"Daño: {seleccionado.danio}\nAgilidad: {seleccionado.agilidad}")
    elif tipos =='armaduras':
        print(f" Armadura: {seleccionado.armadura}\n Agilidad: {seleccionado.agilidad}\n Vida: {seleccionado.vida}")
    else:
        print(f" Armadura: {seleccionado.armadura}\n Agilidad: {seleccionado.agilidad}\n Vida: {seleccionado.vida}\n Daño: {seleccionado.danio}")
    eleccion= input(('deseas equiparlo? (y/n): '))
    if eleccion == 'y' or eleccion == 'Y':
        equipando=seleccionado
        equipar(heroe=heroe, equipando=equipando)
    elif eleccion=='n' or eleccion == 'N':
        print(f'Descartas {seleccionado.nombreEquipamiento} y sigues tu camino')

def generadorEvento(heroe): # opcion +daño o +armadura
    eventoVidaPorEquipamiento(heroe)
    #eventoAumentoStats(heroe)
    #eventoElegirEquipamiento(heroe)
    #eventoLastimarse(heroe)
    #eventoPociones(heroe)
    enter=input('Continuar...')
    pass


def eventoVidaPorEquipamiento(heroe):
    print('Encuentras una antigua fuente de una mujer, arrodillada con un caliz en sus manos y una inscripcion en idioma antiguo')
    enter=input('Continuar...')
    print('Al acercarte y ponerte tus lentes, lees el mensaje y lo traduces en algo como "Entregadme lo importante de la vida" ')
    eleccion=int(input('Piensas en el acertijo y se te ocurren varias soluciones\nLa familia *Ofrecer sangre* (1)\nLa salud *Verter una pocion* (2)\nNo hacer nada (3)\nTu decision: '))
    if eleccion==1:
        heroe.vida-=(heroe.vida/5)
        objeto, tipo = generadorEquipamiento(heroe)
        print('Realizas un corte en tu mano y se escucha un sonido extraño')
        enter=input('Continuar...')
        print(f'La estatua se parte en dos y encuentras {objeto.nombreEquipamiento}')
        equipar(heroe,objeto)
        print('Luego sigues tu camino')
    elif eleccion ==2:
        heroe.pociones-= 1
        print('Viertes el contenido de uno de tus viales de pociones en el caliz')
        enter=input('Continuar...')
        print('Sin embargo, nada sucede y decides seguir tu camino')
    elif eleccion==3:
        print('Decides no arriesgarte y sigues tu camino')

def eventoAumentoStats(heroe):
    azar=r.random()
    if azar<=0.25:
        eleccion=input('Te encuentras un caldero, con restos de una pocion y un libro con el titulo "Secretos de la vida"\nDeseas tomar el resto de la pocion?(y/n): ')
        if eleccion == 'y' or eleccion == 'Y':
            heroe.vidaExtra+=50
            print('Tomas los restos de la pocion y te sientes rejuvenecido (Vida Maxima +50)\nLuego sigues tu camino')
            enter=input('Continuar...')
        elif eleccion=='n' or eleccion=='N':
            print('Decides no arriesgarte y sigues tu camino')
            enter=input('Continuar...')
    elif azar>0.25 and azar<0.5:
        eleccion=input('Te encuentras un caldero, con restos de una pocion y un libro con el titulo "Secretos de la guerra"\nDeseas tomar el resto de la pocion?(y/n: )')
        if eleccion == 'y' or eleccion == 'Y':
            heroe.danioExtra+=20
            print('Tomas los restos de la pocion y te sientes poderoso (Danio + 20) \nLuego sigues tu camino')
            enter=input('Continuar...')
        elif eleccion=='n' or eleccion=='N':
            print('Decides no arriesgarte y sigues tu camino')
            enter=input('Continuar...')
    elif azar>0.5 and azar<0.75:
        eleccion=input('Te encuentras un caldero, con restos de una pocion y un libro con el titulo "Secretos del precoz"\nDeseas tomar el resto de la pocion?(y/n): ')
        if eleccion == 'y' or eleccion == 'Y':
            heroe.armaduraExtra+=30
            print('Tomas los restos de la pocion y te sientes poderoso, como si aguantases mas (Armadura + 30) \nLuego sigues tu camino')
            enter=input('Continuar...')
        elif eleccion=='n' or eleccion=='N':
            print('Decides no arriesgarte y sigues tu camino')
            enter=input('Continuar...')
    elif azar>0.25 and azar<0.5:
        eleccion=input('Te encuentras un caldero, con restos de una pocion y un libro con el titulo "Secretos de las sombras"\nDeseas tomar el resto de la pocion?(y/n): ')
        if eleccion == 'y' or eleccion == 'Y':
            heroe.agilidadExtra+=30
            print('Tomas los restos de la pocion y te sientes mas ligero, casi como si tus pies no tocaran el suelo (Agilidad + 30) \nLuego sigues tu camino')
            enter=input('Continuar...')
        elif eleccion=='n' or eleccion=='N':
            print('Decides no arriesgarte y sigues tu camino')
            enter=input('Continuar...')

def eventoElegirEquipamiento(heroe):
    opcion1, tipo1=generadorEquipamiento(heroe)
    opcion2, tipo2=generadorEquipamiento(heroe)
    print('Ves la estatua de un angel, observas que en cada una de sus manos tiene un equipamiento')
    enter=input('Continuar...')
    eleccion=int(input(f'En su mano izquierda ves {opcion1.nombreEquipamiento}(1) y en su mano derecha {opcion2.nombreEquipamiento}(2), cual deseas recoger? (1/2): '))
    if eleccion==1:
        print(f'Al recoger {opcion1.nombreEquipamiento}, ves como el angel cierra su otra mano, impidiendote obtener {opcion2.nombreEquipamiento}')
        equipar(heroe,opcion1)
    elif eleccion==2:
        print(f'Al recoger {opcion2.nombreEquipamiento}, ves como el angel cierra su otra mano, impidiendote obtener {opcion1.nombreEquipamiento}')
        equipar(heroe,opcion2)

def eventoLastimarse(heroe):
    azar=r.random()
    if azar<=0.25:
        print('Activas una trampa y una flecha te impacta en tu brazo izquierdo')
        enter=input('Continuar...')
        print(f'Logras quitarla, pero perdiste bastante sangre (vida - {heroe.vida/4})')
        heroe.vida-=(heroe.vida/4)
        enter=input('Continuar...')
    elif azar>0.25 and azar<=0.5:
        print(f'Una de tus heridas se infecta, sobreviviras, por el momento...(vida - {heroe.vida/3} )')
        heroe.vida-=(heroe.vida/3)
        enter=input('Continuar...')
    elif azar>0.5 and azar<=0.75:
        print(f'Te patinas con una cascara de banana *Si, hasta aca mi imaginacion* (vida - {heroe.vida/4})')
        heroe.vida-=(heroe.vida/4)
        enter=input('Continuar...')
    else:
        print(f'Una serpiente logra morderte sorpresivamente, por suerte no era venenosa (vida - {heroe.vida/10})')
        heroe.vida-=(heroe.vida/10)
        enter=input('Continuar...')

def eventoPociones(heroe):
    print('Ves un anciano a lo lejos y decides acercarte a el')
    enter=input('Continuar...')
    print('Al llegar te das cuenta que es Tusam, el gran mago\nEl te mira con una sonrisa y decide hacerte un regalo')
    regalo=int(input('Puedes elegir entre llevar una pocion extra (1), o aumentar su efecto curativo(2)\nQue decides?(1/2) '))
    if regalo==1:
        heroe.pociones+=1
        heroe.pocionesMaximas+=1
        print(f'Tusam asiente, ahora puedes llevar {heroe.pocionesMaximas} pociones, tienes {heroe.pociones} llenas')
        enter=input('Continuar...')
    elif regalo==2:
        heroe.pocionesCuracion+=40
        print(f'Tusam asiente, ahora tus pociones regeneran {heroe.pocionesCuracion}')
        enter=input('Continuar...')

def Caminos(heroe):
    creados=0
    while creados != 2:
        aleatorio=r.random()
        if aleatorio<=0.2:                      #Pelea
            opcion='pelea'
            print(f'En el camino {creados+1}, hay un mounstruo al cual eliminar')
        elif aleatorio>0.2 and aleatorio<0.4:   #Evento
            opcion='evento'
            print(f'En el camino {creados+1} no sabes que te podras encontrar:')
        elif aleatorio>0.4 and aleatorio<0.6:   #Cofre
            print(f'En el camino {creados+1}, ves un gran cofre dorado')
            opcion='cofre'
        elif aleatorio>0.6 and aleatorio<0.8:   #Descanso
            print(f'En el camino {creados+1}, ves una hoguera, donde podrias descansar')
            opcion='descanso'
        else:                                   #Recarga pociones
            print(f'En el camino {creados+1}, observas un caldero, con el cual recargar tus pociones')
            opcion='recarga'
        creados +=1
        if creados==1:
            opcion1=opcion
        else:
            opcion2=opcion
    eleccionCamino=int(input('Elija por cual camino desea avanzar(1/2): '))
    if eleccionCamino==1:
        opcion=opcion1
    elif eleccionCamino==2:
        opcion=opcion2
    if opcion=='pelea':
        enemigo=generadorEnemigos()
        pelea(heroe,enemigo)
    elif opcion=='evento':
        generadorEvento(heroe)
    elif opcion=='cofre':
        seleccionado,tipos=generadorEquipamiento(heroe)
        generadorCofre(seleccionado=seleccionado,tipos=tipos)
    elif opcion=='descanso':
        print('Decides descansar junto a la hoguera, recuperando toda tu vida y poniendote de buen humor, es importante estar de buen humor')
        heroe.vida=heroe.vidaMaxima
    elif opcion=='recarga':
        print(f'Logras rellenar tus viales de pociones, volviendo a tener {heroe.pocionesMaximas} pociones a dispocision.')
        heroe.pociones=heroe.pocionesMaximas


