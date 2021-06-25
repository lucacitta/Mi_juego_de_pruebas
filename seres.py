from acciones import *

class Seres:
    def __init__(self, nombre):
        self.nombre=nombre
        self.vidaPerdida=0

    def Atributos(self, vida, danio, agilidad, armadura, vidaMaxima):
        self.vidaMaxima=vidaMaxima
        self.vida=vida
        self.danio=danio
        self.agilidad=agilidad
        self.armadura=armadura
        self.defensa=self.armadura*0.2


class Protagonista(Seres):
    def __init__(self, nombre, clase):
        super().__init__(nombre)
        self.clase=clase

        self.hayArmaEquipada=False
        self.hayAnilloEquipado=False
        self.hayArmaduraEquipada=False

        self.pocionesMaximas=2
        self.pociones=2
        self.pocionesCuracion=80

        self.vidaRegenerada=0
        self.vidaExtra=0

        self.vidaAnillo=0
        self.vidaArmadura=0

        self.danioAnillo=0
        self.danioArma=0
        self.danioExtra=0

        self.armaduraArmadura=0
        self.armaduraAnillo=0
        self.armaduraExtra=0

        self.agilidadExtra=0
        self.agilidadAnillo=0
        self.agilidadArma=0
        self.agilidadArmadura=0

    def Equipado(self, equiparEn, nombre, danio=0, vida=0, agilidad=0, armadura=0):
        if equiparEn == "arma":
            while self.hayArmaEquipada==False:
                self.nombreActual="Ninguna"
                self.danioArma="0"
                self.agilidadArma="0"
                break
            if self.hayArmaEquipada==False:
                self.danioArma = danio
                self.agilidadArma = agilidad
                self.nombreActual = nombre
                self.hayArmaEquipada=True
                self.ActualizarStats()
                print(f"Se equipo {self.nombreActual}")
                enter=input('Continuar...')
            else:
                print(f"Arma actual: {self.nombreActual}\n daño: {self.danioArma}\n agilidad: {self.agilidadArma}")
                print(f"Nueva arma: {nombre}\n daño: {danio}\n agilidad: {agilidad}")
                equipar=input("Desea cambiar de arma? (y/n): ")
                if equipar == "y" or equipar == "Y":
                    self.danioArma = danio
                    self.agilidadArma = agilidad
                    self.nombreActual = nombre
                    self.ActualizarStats()
                    print(f"Se equipo {self.nombreActual}")
                    enter=input('Continuar...')
                else:
                    print("No se cambio el arma equipada")
                    enter=input('Continuar...')
        elif equiparEn == "armadura":
            while self.hayArmaduraEquipada==False:
                self.nombreActual="Ninguna"
                self.armaduraArmadura="0"
                self.agilidadArmadura="0"
                self.vidaArmadura="0"
                break
            if self.hayArmaduraEquipada==False:
                self.nombreActual=nombre
                self.armaduraArmadura=armadura
                self.agilidadArmadura=agilidad
                self.vidaArmadura=vida
                self.hayArmaduraEquipada=True
                self.ActualizarStats()
                print(f"Se equipo {self.nombreActual}")
                enter=input('Continuar...')
            else:
                print(f"Armadura actual: {self.nombreActual}\n Armadura: {self.armaduraArmadura}\n Agilidad: {self.agilidadArmadura}\n Vida: {self.vidaArmadura}")
                print(f"Nueva armadura: {nombre}\n armadura: {armadura}\n agilidad: {agilidad}\n Vida: {vida}")
                equipar=input("Desea cambiar de armadura? (y/n): ")
                if equipar == "y" or equipar == "Y":
                    self.armaduraArmadura = armadura
                    self.agilidadArmadura = agilidad
                    self.vidaArmadura = vida
                    self.nombreActual = nombre
                    self.ActualizarStats()
                    print(f"Se equipo : {self.nombreActual}")
                    enter=input('Continuar...')
                else:
                    print("No se cambio la armadura equipada")
                    enter=input('Continuar...')
        elif equiparEn == "anillo":
            while self.hayAnilloEquipado==False:
                self.nombreActual="Ninguna"
                self.armaduraAnillo="0"
                self.agilidadAnillo="0"
                self.vidaAnillo="0"
                self.danioAnillo="0"
                break
            if self.hayAnilloEquipado==False:
                self.nombreActual=nombre
                self.armaduraAnillo=armadura
                self.agilidadAnillo=agilidad
                self.vidaAnillo=vida
                self.danioAnillo=danio
                self.hayAnilloEquipado=True
                self.ActualizarStats()
                print(f"Se equipo {self.nombreActual}")
                enter=input('Continuar...')
            else:
                print(f"Anillo actual: {self.nombreActual}\n Armadura: {self.armaduraAnillo}\n Agilidad: {self.agilidadAnillo}\n Vida: {self.vidaAnillo}\n Daño: {self.danioAnillo}")
                print(f"Nuevo anillo: {nombre}\n armadura: {armadura}\n agilidad: {agilidad}\n Vida: {vida}\n Daño: {danio}")
                equipar=input("Desea cambiar de anillo? (y/n): ")
                if equipar == "y" or equipar == "Y":
                    self.armaduraAnillo = armadura
                    self.agilidadAnillo = agilidad
                    self.vidaAnillo = vida
                    self.nombreActual = nombre
                    self.ActualizarStats()
                    print(f"Se equipo {self.nombreActual}")
                    enter=input('Continuar...')
                else:
                    print("No se cambio el anillo equipado")
                    enter=input('Continuar...')

    def UsarPocion(self):
        if self.pociones == 0:
            print('No le quedan mas pociones para utilizar')
            return 1
        else:
            self.pociones-=1
            self.vidaRegenerada += self.pocionesCuracion
            print(f'Se uso una pocion, queda {self.pociones}')
            return 0

    def ActualizarStats(self):
        if self.clase == "tanque":
            vidaMaxima=150+self.vidaAnillo+self.vidaArmadura+self.vidaExtra
            vida=vidaMaxima+self.vidaRegenerada-self.vidaPerdida
            if vida>vidaMaxima:
                vida = vidaMaxima
            danio=20+self.danioAnillo+self.danioArma+self.danioExtra
            agilidad=100+self.agilidadArmadura+self.agilidadAnillo+self.agilidadArma+self.agilidadExtra
            armadura=60+self.armaduraAnillo+self.armaduraArmadura+self.armaduraExtra
            self.Atributos(vida=vida, danio=danio, agilidad=agilidad, armadura=armadura, vidaMaxima=vidaMaxima)
        elif self.clase == "asesino":
            vidaMaxima=80+self.vidaAnillo+self.vidaArmadura+self.vidaExtra
            vida=vidaMaxima+self.vidaRegenerada-self.vidaPerdida
            if vida>vidaMaxima:
                vida = self.vidaMaxima
            danio=50+self.danioAnillo+self.danioArma+self.danioExtra
            agilidad=40+self.agilidadArmadura+self.agilidadAnillo+self.agilidadArma+self.agilidadExtra
            armadura=20+self.armaduraAnillo+self.armaduraArmadura+self.armaduraExtra
            self.Atributos(vida=vida, danio=danio, agilidad=agilidad, armadura=armadura, vidaMaxima=vidaMaxima)
        elif self.clase == "soldado":
            vidaMaxima=100+self.vidaAnillo+self.vidaArmadura+self.vidaExtra
            vida=vidaMaxima+self.vidaRegenerada-self.vidaPerdida
            if vida>vidaMaxima:
                vida = self.vidaMaxima
            danio=30+self.danioAnillo+self.danioArma+self.danioExtra
            agilidad=20+self.agilidadArmadura+self.agilidadAnillo+self.agilidadArma+self.agilidadExtra
            armadura=40+self.armaduraAnillo+self.armaduraArmadura+self.armaduraExtra
            self.Atributos(vida=vida, danio=danio, agilidad=agilidad, armadura=armadura, vidaMaxima=vidaMaxima)
        else:
            print("Error, no se hay clase")


class Enemigo(Seres):
    def __init__(self, nombre, clase):
        super().__init__(nombre)
        self.vidaPerdida=0
        self.clase=clase
        self.ActualizarEnemigos()

    def Drop(self):
        pass

    def ActualizarEnemigos(self):
        if self.clase == "troll":
            vidaMaxima=100
            vida=vidaMaxima-self.vidaPerdida
            danio=40
            agilidad=30
            armadura=30
            self.Atributos(vida=vida,danio=danio,agilidad=agilidad,armadura=armadura, vidaMaxima=vidaMaxima)
        elif self.clase == "perro":
            vidaMaxima=40
            vida=vidaMaxima-self.vidaPerdida
            danio=25
            agilidad=40
            armadura=20
            self.Atributos(vida=vida,danio=danio,agilidad=agilidad,armadura=armadura, vidaMaxima=vidaMaxima)
        elif self.clase == "gigante":
            vidaMaxima=200
            vida=vidaMaxima-self.vidaPerdida
            danio=20
            agilidad=10
            armadura=60
            self.Atributos(vida=vida,danio=danio,agilidad=agilidad,armadura=armadura, vidaMaxima=vidaMaxima)
        else:
            print("No se encuentra la clase seleccionadad")

troll=['Troll de las montañas','Troll de las nieves','Troll de Twitter']
gigante=['Gigante come hombres','Gigante de escarcha','Carlos el gigante malvado']
perro=['Perrito malvado','Pluto con hambre','Firulais con rabia']
enemigosTotal=[troll, gigante, perro]