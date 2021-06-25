class Equipamiento():
    def __init__(self, nombreEquipamiento, ocupa):
        self.nombreEquipamiento=nombreEquipamiento
        if ocupa == "arma":
            self.equiparEn = "arma"
        elif ocupa == "armadura":
            self.equiparEn = "armadura"
        elif ocupa == "anillo":
            self.equiparEn = "anillo"
        else:
            print(f"Error, que ocupa {self.nombreEquipamiento}?")


class Arma(Equipamiento):
    def __init__(self, nombreEquipamiento, ocupa, danioArma, agilidadArma):
        super().__init__(nombreEquipamiento, ocupa)
        self.danio=danioArma
        self.agilidad=agilidadArma


class Armor(Equipamiento):
    def __init__(self, nombreEquipamiento, ocupa,armaduraArmor, agilidadArmor, vidaArmor):
        super().__init__(nombreEquipamiento, ocupa)
        self.armadura=armaduraArmor
        self.agilidad=agilidadArmor
        self.vida=vidaArmor


class Anillo(Equipamiento):
    def __init__(self, nombreEquipamiento, ocupa, danioAnillo, vidaAnillo, agilidadAnillo, armaduraAnillo):
        super().__init__(nombreEquipamiento, ocupa)
        self.danio=danioAnillo
        self.vida=vidaAnillo
        self.agilidad=agilidadAnillo
        self.armadura=armaduraAnillo


#EQUIPAMIENTO

espadaOscura=Arma("Espada Oscura",ocupa="arma",danioArma=30,agilidadArma=10)
espadaVeloz=Arma("Espada Veloz",ocupa="arma",danioArma=20,agilidadArma=20)
armasTotales=[espadaOscura,espadaVeloz]


armaduraNegra=Armor("Armadura Negra",ocupa="armadura", armaduraArmor=20, agilidadArmor=15, vidaArmor=50)
armaduraBlanca=Armor("Armadura Blanca",ocupa="armadura", armaduraArmor=40, agilidadArmor=0, vidaArmor=80)
armadurasTotales=[armaduraNegra, armaduraBlanca]

anilloDoran=Anillo("Anillo De Doran", ocupa="anillo", danioAnillo=10, vidaAnillo=40, agilidadAnillo=10, armaduraAnillo=40)
anilloSauron=Anillo("Anillo De Sauron", ocupa="anillo", danioAnillo=20, vidaAnillo=80, agilidadAnillo=20, armaduraAnillo=0)
anillosTotales=[anilloDoran, anilloSauron]

equipamientoTotal={'espadas':armasTotales, 'armaduras':armadurasTotales, 'anillos':anillosTotales}