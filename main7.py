# OBJEKTAI/ CLASS

# class Kate:
#     def __int__(self, vardas, spalva):
#         self.vardas = vardas
#         self.spalva = spalva
#
#     def miaukseti(self):
#         print("Miau")
#
#     def __str__(self):
#         # return "objektas"
#         return f"Kate vardu {self.vardas}, jos spalva {self.spalva}"
#
# kate1 = Kate()
# kate2 = Kate()
# kate3 = Kate()
#
# kate1.miaukseti()
#
#
# print(kate1.spalva, kate1.vardas)
# print(kate2.spalva, kate2.vardas)
# print(kate3.vardas, kate3.spalva)
# print(kate1)

# NAMU DARBAI

# I.1 uzduotis

#
# class Sakinys:
#
#     def __init__(self, tekstas):
#         self.tekstas = tekstas
#
#     def atbulai(self):
#         return self.tekstas[::-1]
#
# PAPILDOMA INFO
#
#     def __repr__(self):
#         return self.tekstas
#
# masyvas = []
#
# for x in range(100):
#     objektas = Sakinys(f"Tekstas nr {x}")
#     masyvas.append(objektas)
#
# print(len(masyvas))
# IKI CIA


#     def didziosios(self):
#         return self.tekstas.upper()
#
#     def mazosios(self):
#         return self.tekstas.lower()
#
#     def gauti_zodi(self, eilesnr):
#         return self.tekstas.split()[eilesnr]
#
#     def numeriai(self, tekstas):
#         return self.tekstas.count(tekstas)
#
#     def kiek_yra(self):
#         skaiciai = len([x for x in self.tekstas if x.isdigit()])
#         didziosios = len([x for x in self.tekstas if x.isupper()])
#         mazosios = len([x for x in self.tekstas if x.islower()])
#         print(skaiciai, didziosios, mazosios, len(self.tekstas.split()))
#
#     def kiekiai(self, senas, naujas):
#         return self.tekstas.replace(senas, naujas)
#
# sakinys1 = Sakinys("programavimo mokykla Code Academy 321")
#
# print(sakinys1.atbulai())
# print(sakinys1.didziosios())
# print(sakinys1.mazosios())
# print(sakinys1.gauti_zodi(2))
# print(sakinys1.numeriai("a"))
# print(sakinys1.kiekiai('programavimo', 'kodavimo'))
# sakinys1.kiek_yra()



# 2 uzduotis

# SUKAKTIS

import datetime
import calendar

class Sukaktis:

    def __init__(self, metai=0, menuo=0, diena=0, valandos=0, minutes=0):
        self.data = datetime.datetime(metai, menuo, diena, valandos, minutes)

    def smulkiai(self):
        skirtumas = datetime.datetime.today() - self.data

        print(f"Praėjo metų: ", skirtumas.days // 365)
        print("Praėjo mėnesių: ", skirtumas.days / 365 * 12)
        print("Praėjo savaičių: ", skirtumas.days / 7)
        print("Praėjo dienų: ", skirtumas.days)
        print("Praėjo valandų: ", skirtumas.total_seconds() / 3600)
        print("Praėjo minučių: ", skirtumas.total_seconds() / 60)
        print("Praėjo sekundžių: ", skirtumas.total_seconds())

    def arKeliamieji(self):
        if calendar.isleap(year=2000):
            print("Keliamieji metai")

    def atimtiDienas(self, dienos):
        return self.data - datetime.timedelta(days=dienos)

    def pridetiDienas(self, dienos):
        return self.data + datetime.timedelta(days=dienos)

    def __str__(self):
        return (f"Data: {self.data.year}-{self.data.month}-{self.data.day}")


data1 = Sukaktis(2000, 9, 22)
data1.arKeliamieji()
data1.smulkiai()
print(data1.atimtiDienas(5))
print(data1.pridetiDienas(45))

