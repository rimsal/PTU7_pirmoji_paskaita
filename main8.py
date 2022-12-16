# 1 UZDUOTIS
# class Automobilis:
#     def __init__(self, metai, modelis, kuro_tipas):
#         self.metai = metai
#         self.modelis = modelis
#         self. kuro_tipas = kuro_tipas
#         print(self.metai, self.modelis, self.kuro_tipas)

#     def vaziuoti(self):
#         print("Važiuoja")
#
#     def stoveti(self):
#         print("Priparkuota")
#
#     def pildyti_degalu(self):
#         print("Degalai įpilti")
#
# class Elektromobilis(Automobilis):
#     def pildyti_degalu(self):
#         print("Baterija įkrauta")
#
#     def vaziuoti_autonomiskai(self):
#         print("Važiuoja autonomiškai")
#
#
# auto = Automobilis(2022, "Audi", "benzinas")
# auto.vaziuoti()
# auto.stoveti()
# auto.pildyti_degalu()
# print("------------")
# auto1 = Automobilis(2014, "VW", "dyzelis")
# print("------------")
# auto2 = Elektromobilis(2021, "Tesla", "elektra")
# auto2.vaziuoti_autonomiskai()
# auto2.stoveti()
# auto2.pildyti_degalu()
# print(auto.metai, auto.modelis, auto.kuro_tipas)
# print(auto1.metai, auto1.modelis, auto1.kuro_tipas)
# print(auto2.metai, auto2.modelis, auto2.kuro_tipas)

# 2 UZDUOTIS

# import datetime
#
# class Darbuotojas:
#     def __init__(self, vardas, valandos_ikainis, dirba_nuo):
#         self.vardas = vardas
#         self.valandos_ikainis = valandos_ikainis
#         self.dirba_nuo = dirba_nuo
#         self.data = datetime.datetime.strptime(dirba_nuo, "%Y-%m-%d")
#
#     def _isdirbo_dienu(self):
#          dirba_dienu = datetime.datetime.today() - self.data
#          return dirba_dienu.days
#
#     def paskaiciuoti_atlyginima(self):
#         return self._isdirbo_dienu() * self.valandos_ikainis * 8
#
# class NormalusDarbuotojas(Darbuotojas):
#
#     def paskaiciuoti_atlyginima(self):
#         return super().paskaiciuoti_atlyginima() / 7*5
#
#
# darbuotojas1  = Darbuotojas("Darius", 10, "2022-03-10")
# darbuotojas2 = NormalusDarbuotojas("Romas", 7, "2022-03-10")
# print("Darius", darbuotojas1._isdirbo_dienu())
# print(darbuotojas1.paskaiciuoti_atlyginima())
# print("Romas", darbuotojas2._isdirbo_dienu())
# print(darbuotojas2.paskaiciuoti_atlyginima())

# 3UZDUOTIS
class Irasas:
    def __init__(self, suma):
        self.suma = suma

class PajamuIrasas(Irasas):
    def __init__(self, suma, siuntejas, papildoma_info):
        super().__init__(suma)
        self.siuntejas = siuntejas
        self.papildoma_info = papildoma_info

class IslaiduIrasas(Irasas):
    def __init__(self, suma, atsiskaitymo_budas, isigyta_preke_paslauga):
        super().__init__(suma)
        self.atsiskaitymo_budas = atsiskaitymo_budas
        self.isigyta_preke_paslauga = isigyta_preke_paslauga

class Biudzetas():
    def __init__(self):
        self.zurnalas = []

    def ivesti_pajamas(self, suma, siuntejas, papildoma_informacija):
        pajamu_irasas = PajamuIrasas(suma, siuntejas, papildoma_informacija)
        self.zurnalas.append(pajamu_irasas)

    def ivesti_islaidas(self, suma, atsiskaitymo_budas, isigyta_preke_paslauga):
        islaidu_irasas = IslaiduIrasas(suma, atsiskaitymo_budas, isigyta_preke_paslauga)
        self.zurnalas.append(islaidu_irasas)

    def gauti_biudzeto_balansa(self):
        balansas = 0
        for irasas in self.zurnalas:
            if isinstance(irasas, PajamuIrasas):
                balansas += irasas.suma
            if isinstance(irasas, IslaiduIrasas):
                balansas -= irasas.suma
        return balansas

    def gauti_ataskaita(self):
        for irasas in self.zurnalas:
            if isinstance(irasas, PajamuIrasas):
                print(f"Pajamos: {irasas.suma} {irasas.siuntejas} {irasas.papildoma_info}")
            if isinstance(irasas, IslaiduIrasas):
                print(f"Išlaidos: {irasas.suma} {irasas.atsiskaitymo_budas} {irasas.isigyta_preke_paslauga}")

mano_biudzetas = Biudzetas()

while True:
    print("Pasirinkite veiksmą: ")
    print("1 - Įvesti pajamas")
    print("2 - Įvesti išlaidas")
    print("3 - Gauti balansą")
    print("4 - Gauti ataskaitą")
    print("0 - Išeiti iš programos")
    pasirinkimas = input()
    if pasirinkimas == "1":
        print("Įveskite pajamas: ")
        suma = int(input("Suma: "))
        siuntejas = input("Siuntėjas: ")
        papildoma_informacija = input("Papildoma informacija: ")
        mano_biudzetas.ivesti_pajamas(suma, siuntejas, papildoma_informacija)
        print("Pajamos įvestos sėkmingai!")
    if pasirinkimas == "2":
        print("Įveskite išlaidas: ")
        suma = int(input("Suma: "))
        atsiskaitymo_budas = input("Atsiskaitymo būdas: ")
        isigyta_preke_paslauga = input("Įsigyta prekė/paslauga: ")
        mano_biudzetas.ivesti_islaidas(suma, atsiskaitymo_budas, isigyta_preke_paslauga)
        print("Išlaidos įvestos sėkmingai!")
    if pasirinkimas == "3":
        print(f"Sąskaitos balansas: {mano_biudzetas.gauti_biudzeto_balansa()}")
    if pasirinkimas == "4":
        mano_biudzetas.gauti_ataskaita()
    if pasirinkimas == "0":
        break
