class Tankas:
    pass


class Taikinys:
    """
    Klasė nurodyti taikinio savybėms ir funkcionalumui
    """
    def __init__(self):
        """
        Inicijuojam taikinio lokaciją kur x ir y kreikšmės bus sugeneruotos random rėžiuose nuo -5 iki 5
        """
        self.x = random.randint(-5, 5)
        self.y = random.randint(-5, 5)

    def atkurta(self):
        """
         Per naują nustatom taikinio lokaciją kur x ir y kreikšmės bus sugeneruotos random rėžiuose nuo -5 iki 5.
         Turėtų būti panaudojamas kai taikinys buvo sunaikintas.
         """
        self.x = random.randint(-5, 5)
        self.y = random.randint(-5, 5)

print("Sveiki, Taisyklės kaip žaisti")



