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
