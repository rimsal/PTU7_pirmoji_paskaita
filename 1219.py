# sarasas = [4, 3, 2, 1]
#
# sarasas_2 = []
# for skaicius in sarasas:
#     sarasas_2.append(skaicius ** 2)
#
# print(sarasas_2)
#
# sarasas = [4, 3, 2, 1]
# naujas = map(lambda x: x**2, sarasas)
# print(naujas)
#
# # <map object at 0x000001AA7B5D8048>
#
# print(list(naujas))
#
# data = "2000-03-25"
# y, m, d = map(int, data.split("-"))
#
# print(y)
# print(m)
# print(d)
#
# skaiciai = "4, 3, 2, 1"
# p, a, t, k = map(float, skaiciai.split(", "))
# print(p, a, t, k)
#
# sarasas = [4, 3, 2, 1]
#
# def daugiau_nei_2(sarasas):
#     sarasas_2 = []
#     for skaicius in sarasas:
#         if skaicius > 2:
#             sarasas_2.append(skaicius)
#     return sarasas_2
#
# print(daugiau_nei_2(sarasas))
#
# sarasas = [4, 3, 2, 1]
# naujas = filter(lambda x: x > 2, sarasas)
# print(list(naujas))
#
# import calendar
#
# metai = list(range(1900, 2150))
# naujas = list(filter(calendar.isleap, metai))
# print(naujas)
#
# from functools import reduce
#
# sarasas = [4, 3, 2, 1]
# naujas = reduce(lambda x, y: x + y, sarasas)
# print(naujas)
#
# sarasas = [4, 3, 2, 1, 5, 6, 7, 10, 9, 8]
#
# print(sum(sarasas))
#
# # 55
#
# print(min(sarasas))
#
# # 1
#
# print(max(sarasas))
#
# from statistics import mean, median
#
# sarasas = [2, 9, 10, 39, 45]
#
# print(mean(sarasas))
#
# # 21
#
# print(median(sarasas))
#
# sarasas = [4, 3, 2, 1]
# naujas = [x**2 for x in sarasas]
# print(naujas)
#
# # [16, 9, 4, 1]
# sarasas = [4, 3, 2, 1]
# naujas = [x for x in sarasas if x > 2]
# print(naujas)
#
# sarasas = list(range(20))
#
# def lyginiai(sarasas):
#     naujas = []
#     for skaicius in sarasas:
#         if skaicius % 2 == 0:
#             naujas.append(skaicius)
#     return naujas
#
# print(lyginiai(sarasas))
#
# sarasas = list(range(20))
# lyginiai = (x for x in sarasas if x % 2 == 0)
#
# print()
#
# sarasas = [2.5, 2, "Labas", True, 5, 7, 8, 2.8, "Vakaras"]
#
# int_kiekis = sum(type(c) is int for c in sarasas)
# print(int_kiekis)
#
# # 4
#
# str_kiekis = sum(type(c) is str for c in sarasas)
# print(str_kiekis)
#
# # 2
# sarasas = [2.5, 2, "Labas", True, 5, 7, 8, 2.8, "Vakaras"]
# bool_kiekis = sum(type(c) is bool for c in sarasas)
# print(bool_kiekis)
#
# # 1
#
# float_kiekis = sum(type(c) is float for c in sarasas)
# print(float_kiekis )
#
# sarasas = [4, 3, 2, 1, 5, 6, 7, 10, 9, 8]
#
# sarasas.sort()
# print(sarasas)
#
# # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# naujas = sorted(sarasas)
# print(naujas)
#
# # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# sarasas.sort(reverse=True)
# print(sarasas)
#
# # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
#
# naujas = sorted(sarasas, reverse=True)
# print(naujas)
#
# tuple_sarasas = (4, 3, 2, 1, 5, 6, 7, 10, 9, 8)
#
# # tuple_sarasas.sort()
# # # AttributeError: 'tuple' object has no attribute 'sort'
#
# naujas = sorted(tuple_sarasas)
# print(naujas)
#
# zodynas = {"Vardas": "Donatas", "Pavardė": "Noreika", "Amžius": None}
# surusiuotas = sorted(zodynas)
#
# print(surusiuotas)
#
# # ['Amžius', 'Pavardė', 'Vardas']
#
# sarasas = [-2, 5, -4, 7, -5, 9]
# surusiuotas = sorted(sarasas)
# print(surusiuotas)
#
# # [-5, -4, -2, 5, 7, 9]
#
# sarasas = [-2, 5, -4, 7, -5, 9]
# surusiuotas = sorted(sarasas, key=abs)
# print(surusiuotas)
#
# # [-2, -4, 5, -5, 7, 9]

class Darbuotojas:
    def __init__(self, vardas, pavarde, atlyginimas):
        self.vardas = vardas
        self.pavarde = pavarde
        self.atlyginimas = atlyginimas

    def __repr__(self):
        return (f"({self.vardas}, {self.pavarde}, {self.atlyginimas})")

d1 = Darbuotojas("Tadas", "Rutkauskas", 1500)
d2 = Darbuotojas("Domas", "Radzevičius", 2000)
d3 = Darbuotojas("Rokas", "Ramanauskas", 1000)
sarasas = [d1, d2, d3]

def rusiavimas(darbuotojas):
    return darbuotojas.vardas

surusiuotas = sorted(sarasas, key=rusiavimas)
print(surusiuotas)

#[(Domas, Radzevičius, 2000), (Rokas, Ramanauskas, 1000), (Tadas, Rutkauskas, 1500)]

surusiuotas = sorted(sarasas, key=lambda e: e.atlyginimas)
print(surusiuotas)

# [(Rokas, Ramanauskas, 1000), (Tadas, Rutkauskas, 1500), (Domas, Radzevičius, 2000)]

from operator import attrgetter
surusiuotas = sorted(sarasas, key=attrgetter("atlyginimas"))
print(surusiuotas)

# [(Rokas, Ramanauskas, 1000), (Tadas, Rutkauskas, 1500), (Domas, Radzevičius, 2000)
