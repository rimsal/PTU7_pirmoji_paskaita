import random, math


class Tankas:

    def __init__(self):
        """
        Inicijuojam koordinates x ir y kad tankas stovi 0:0 pozicijoje
         ir yra atsisukęs į y teigiamą pusę arba į viršų.
         Inicijuoti šūvių kiekių ir šūvių kiekviena kryptimi kintamieji.
        """
        self.x = 0
        self.y = 0
        self.zingsnis = 'pirmyn'
        self.suvio_kryptis = {'pirmyn': 0, 'atgal': 0, 'kairen': 0, 'desinen': 0}
        self.suviu_skaicius = 0

    def judėti(self, pajudeti):
        """
           Funkcija atakinga už tanko judėjimą
        """
        self.zingsnis = pajudeti
        if pajudeti == 'pirmyn':
            self.y += 1  # Tankas pavažiavo į priekį
        elif pajudeti == 'atgal':
            self.y -= 1  # Tankas pavažiavo į atgal
        elif pajudeti == 'kairen':
            self.x -= 1  # Tankas pavažiavo į kairę
        elif pajudeti == 'desinen':
            self.x += 1  # Tankas pavažiavo į dešinę

    def sauti(self, taskasx, taskasy):
        """
        Tikrinimas vyksta pagal logiką kad jeigu tankas stovi pizicijoje
        kuri yra lygi taikinio x, arba taikinio y reikšmei,
        ir tanko kryptis atitinka logiką kad jis žiūri yra y arba x reikšmę
        atitinkamai, šūvis bus sėkmingas.
        :param taskasx: Taikinio pozicijos x reikšmė
        :param taskasy: Taikinio pozicijos y reikšmė
        :return: True jeigu pataikom į taikinį, kitu atveju, gražinam False
        """
        print('Šūvis!')

        self.suvio_kryptis[self.zingsnis] += 1
        if self.x == taskasx:
            if self.y < taskasy:
                if self.zingsnis == 'pirmyn':
                    self.suviu_skaicius += 1
                    return True
            else:
                if self.zingsnis == 'atgal':
                    self.suviu_skaicius += 1
                    return True
        if self.y == taskasy:
            if self.x < taskasx:
                if self.zingsnis == 'desinen':
                    self.suviu_skaicius += 1
                    return True
            else:
                if self.zingsnis == 'kairen':
                    self.suviu_skaicius += 1
                    return True

        return False

    def info(self):

        # Funkcija atsakinga už klasės informacijos atspausdinimą ekrane.
        # return : nieko
        print(f"Kryptis: {self.zingsnis}")
        print(f"Koordinatės: {self.x}:{self.y}")
        print(f"Šūvių iš viso: {sum(self.suvio_kryptis.values())}")
        print(f"{self.suvio_kryptis}")
        print((f"Taškai: {self.suviu_skaicius}"))
