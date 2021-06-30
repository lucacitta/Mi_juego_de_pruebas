from acciones import *
from os import system

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

        self.oro=0

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

        self.auxCamino=True

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
            else:
                system('cls')
                print(f"Arma actual: {self.nombreActual}           Nueva arma: {nombre}\n       daño: {self.danioArma}                            daño: {danio}\n    agilidad: {self.agilidadArma}                         agilidad: {agilidad}")
                equipar=input(" \nDesea cambiar de arma? (y/n): ")
                if equipar == "y" or equipar == "Y":
                    self.danioArma = danio
                    self.agilidadArma = agilidad
                    self.nombreActual = nombre
                    self.ActualizarStats()
                    print(f"Se equipo {self.nombreActual}")
                else:
                    print("No se cambio el arma equipada")
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
            else:
                system('cls')
                print(f"Armadura actual: {self.nombreActual}            Nueva armadura: {nombre}\n      Armadura: {self.armaduraArmadura}                                 Armadura: {armadura}\n      Agilidad: {self.agilidadArmadura}                                  Agilidad: {agilidad}\n       Vida: {self.vidaArmadura}                                      Vida: {vida}")
                equipar=input("\nDesea cambiar de armadura? (y/n): ")
                if equipar == "y" or equipar == "Y":
                    self.armaduraArmadura = armadura
                    self.agilidadArmadura = agilidad
                    self.vidaArmadura = vida
                    self.nombreActual = nombre
                    self.ActualizarStats()
                    print(f"Se equipo : {self.nombreActual}")
                else:
                    print("No se cambio la armadura equipada")
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
            else:
                system('cls')
                print(f"Anillo actual: {self.nombreActual}              Nuevo anillo: {nombre}\n        Armadura: {self.armaduraAnillo}                               Armadura: {armadura}\n        Agilidad: {self.agilidadAnillo}                               Agilidad: {agilidad}\n          Vida: {self.vidaAnillo}                                   Vida: {vida}\n          Daño: {self.danioAnillo}                                   Daño: {danio}")
                equipar=input("\nDesea cambiar de anillo? (y/n): ")
                if equipar == "y" or equipar == "Y":
                    self.armaduraAnillo = armadura
                    self.agilidadAnillo = agilidad
                    self.vidaAnillo = vida
                    self.nombreActual = nombre
                    self.ActualizarStats()
                    print(f"Se equipo {self.nombreActual}")
                else:
                    print("No se cambio el anillo equipado")

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
            agilidad=20+self.agilidadArmadura+self.agilidadAnillo+self.agilidadArma+self.agilidadExtra
            if agilidad<0:
                agilidad=0
            armadura=60+self.armaduraAnillo+self.armaduraArmadura+self.armaduraExtra
            self.Atributos(vida=vida, danio=danio, agilidad=agilidad, armadura=armadura, vidaMaxima=vidaMaxima)
        elif self.clase == "asesino":
            vidaMaxima=80+self.vidaAnillo+self.vidaArmadura+self.vidaExtra
            vida=vidaMaxima+self.vidaRegenerada-self.vidaPerdida
            if vida>vidaMaxima:
                vida = self.vidaMaxima
            danio=50+self.danioAnillo+self.danioArma+self.danioExtra
            agilidad=40+self.agilidadArmadura+self.agilidadAnillo+self.agilidadArma+self.agilidadExtra
            if agilidad<0:
                agilidad=0
            armadura=20+self.armaduraAnillo+self.armaduraArmadura+self.armaduraExtra
            self.Atributos(vida=vida, danio=danio, agilidad=agilidad, armadura=armadura, vidaMaxima=vidaMaxima)
        elif self.clase == "soldado":
            vidaMaxima=100+self.vidaAnillo+self.vidaArmadura+self.vidaExtra
            vida=vidaMaxima+self.vidaRegenerada-self.vidaPerdida
            if vida>vidaMaxima:
                vida = self.vidaMaxima
            danio=30+self.danioAnillo+self.danioArma+self.danioExtra
            agilidad=20+self.agilidadArmadura+self.agilidadAnillo+self.agilidadArma+self.agilidadExtra
            if agilidad<0:
                agilidad=0
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

    def ActualizarEnemigos(self):
        if self.clase == "troll":
            vidaMaxima=100
            vida, danio, agilidad, armadura=vidaMaxima-self.vidaPerdida, 20, 20, 30
            self.Atributos(vida=vida,danio=danio,agilidad=agilidad,armadura=armadura, vidaMaxima=vidaMaxima)
        elif self.clase == "perro":
            vidaMaxima=50
            vida, danio, agilidad, armadura=vidaMaxima-self.vidaPerdida, 25, 40, 20
            self.Atributos(vida=vida,danio=danio,agilidad=agilidad,armadura=armadura, vidaMaxima=vidaMaxima)
        elif self.clase =="esqueleto":
            vidaMaxima=70
            vida, danio, agilidad, armadura=vidaMaxima-self.vidaPerdida, 30, 20, 30
            self.Atributos(vida=vida,danio=danio,agilidad=agilidad,armadura=armadura, vidaMaxima=vidaMaxima)
        elif self.clase == "gigante":
            vidaMaxima=200
            vida, danio, agilidad, armadura=vidaMaxima-self.vidaPerdida, 30, 10, 60
            self.Atributos(vida=vida,danio=danio,agilidad=agilidad,armadura=armadura, vidaMaxima=vidaMaxima)
        elif self.clase == "animal":
            vidaMaxima=180
            vida, danio, agilidad, armadura=vidaMaxima-self.vidaPerdida, 40, 30, 10
            self.Atributos(vida=vida,danio=danio,agilidad=agilidad,armadura=armadura, vidaMaxima=vidaMaxima)
        elif self.clase == "mago":
            vidaMaxima=80
            vida, danio, agilidad, armadura=vidaMaxima-self.vidaPerdida, 50, 25, 0
            self.Atributos(vida=vida,danio=danio,agilidad=agilidad,armadura=armadura, vidaMaxima=vidaMaxima)


            self.Atributos(vida=vida,danio=danio,agilidad=agilidad,armadura=armadura, vidaMaxima=vidaMaxima)

        else:
            print("No se encuentra la clase seleccionadad")

troll=['Troll de las montañas','Troll de las nieves','Troll de Twitter']
perro=['Perrito malvado','Pluto con hambre','Firulais con rabia']           
esqueleto=['Carlos el huesos','Esqueleto malvado','Esqueleto Hambriento']

enemigosDebiles=[troll, perro, esqueleto]


gigante=['Gigante come hombres','Gigante de escarcha','Juan el gigante malvado']
animal=['Oso pardo', 'Mamut', 'Pantera negra']
mago=['Mandraque el mago', 'Veigar el mago oscuro', 'El mago oscuro']           

enemigosFuertes=[gigante, animal, mago]