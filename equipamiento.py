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

#Armas
dagasDelViento=Arma("Dagas Del Viento",ocupa="arma",danioArma=5,agilidadArma=25)
dagasDeGoblin=Arma("Dagas De Goblin",ocupa="arma",danioArma=10,agilidadArma=20)
cuchilloDeManteca=Arma("Cuchillo De Manteca",ocupa="arma",danioArma=5,agilidadArma=5)

espadaOscura=Arma("Espada Oscura",ocupa="arma",danioArma=25,agilidadArma=5)
espadaDelReyArruinado=Arma("Espada Del Rey Arruinado", ocupa='arma',danioArma=30, agilidadArma=0)
espadaVeloz=Arma("Espada Veloz",ocupa="arma",danioArma=15,agilidadArma=15)

espadonDetol=Arma("Espadon Detol",ocupa="arma",danioArma=40,agilidadArma=-10)
espadonDelReyMomo=Arma("Espadon Del Rey Momo",ocupa="arma",danioArma=45,agilidadArma=-20)

armasTotales=[cuchilloDeManteca, dagasDelViento, dagasDeGoblin, espadaOscura, espadaVeloz, espadaDelReyArruinado, espadonDelReyMomo, espadonDetol]

#Armaduras
armaduraNegra=Armor("Armadura Negra",ocupa="armadura", armaduraArmor=30, agilidadArmor=0, vidaArmor=20)
armaduraBlanca=Armor("Armadura Blanca",ocupa="armadura", armaduraArmor=20, agilidadArmor=-10, vidaArmor=40)
armaduraPetrea=Armor('Armadura Petrea',ocupa="armadura", armaduraArmor=30, agilidadArmor=-15, vidaArmor=20)
armaduraDeColoso=Armor('Armadura De Coloso',ocupa="armadura", armaduraArmor=30, agilidadArmor=-20, vidaArmor=40)

cotaDeMallasVitales=Armor('Cota De Mallas Vitales',ocupa="armadura", armaduraArmor=10, agilidadArmor=20, vidaArmor=20)
cotaDeMallasDoradas=Armor('Cota De Mallas Doradas',ocupa="armadura", armaduraArmor=10, agilidadArmor=30, vidaArmor=10)
cotaDeMallasLigeras=Armor('Cota De Mallas Ligeras',ocupa="armadura", armaduraArmor=15, agilidadArmor=15, vidaArmor=20)

araposDeEsclavo=Armor('Arapos De Esclavo',ocupa="armadura", armaduraArmor=10, agilidadArmor=0, vidaArmor=0)


armadurasTotales=[armaduraNegra, armaduraBlanca, armaduraPetrea, armaduraDeColoso, cotaDeMallasVitales, cotaDeMallasDoradas, cotaDeMallasLigeras, araposDeEsclavo]

#Anillos
anilloDoran=Anillo("Anillo De Doran", ocupa="anillo", danioAnillo=15, vidaAnillo=15, agilidadAnillo=15, armaduraAnillo=15)
anilloSauron=Anillo("Anillo De Sauron", ocupa="anillo", danioAnillo=20, vidaAnillo=10, agilidadAnillo=20, armaduraAnillo=10)
anilloVital=Anillo("Anillo Vital", ocupa="anillo", danioAnillo=5, vidaAnillo=35, agilidadAnillo=10, armaduraAnillo=0)
anilloDelColoso=Anillo("Anillo Del Coloso", ocupa="anillo", danioAnillo=10, vidaAnillo=25, agilidadAnillo=-25, armaduraAnillo=30)
anilloDeLaHoja=Anillo("Anillo De La Hoja ", ocupa="anillo", danioAnillo=15, vidaAnillo=0, agilidadAnillo=20, armaduraAnillo=5)
anilloMVP=Anillo("Anillo M.V.P.", ocupa="anillo", danioAnillo=10, vidaAnillo=25, agilidadAnillo=20, armaduraAnillo=10)
anilloComun=Anillo("Anillo Comun", ocupa="anillo", danioAnillo=5, vidaAnillo=5, agilidadAnillo=5, armaduraAnillo=5)
anilloDeCasamiento=Anillo("Anillo De Casamiento", ocupa="anillo", danioAnillo=-10, vidaAnillo=-10, agilidadAnillo=-10, armaduraAnillo=-10)

anillosTotales=[anilloDoran, anilloSauron, anilloVital, anilloDelColoso, anilloDeLaHoja, anilloMVP, anilloComun, anilloDeCasamiento]

equipamientoTotal={'espadas':armasTotales, 'armaduras':armadurasTotales, 'anillos':anillosTotales}