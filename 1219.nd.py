
# 1 UZDUOTIS:
# Sukurti programą, kuri:
#
# Prie kiekvieno sakinio "The Zen of Python" žodžio pridėtų šauktuką ir atspausdintų naują sakinį.
# Patarimai:
#
# Naudoti map (su lambda) arba comprehension, " ".join()

# sakinys = "The Zen of Python"
# print(sakinys)
#
# naujas = list(map(lambda x: x + "!", sakinys.split()))
#
# naujas2 = " ".join(naujas)
# # naujas = [x + "!" for x in sakinys.split()]
# print(naujas2)

# 2 UZDUOTIS

# from statistics import mean, median
# #
# # # Atliktų veiksmus su skaičiais iki 50:
# #
# skaiciai = list(range(51))
# # print(skaiciai)
# #
# # # Padaugintų visus sąrašo skaičius iš 10 ir atspausdintų:
# #
# # naujas = map(lambda x: x * 10, skaiciai)
# # print(list(naujas))
# #
# # # arba
# #
# # naujas = [x * 10 for x in skaiciai]
# # print(naujas)
# #
# # # Atrinktų iš sąrašo skaičius, kurie dalinasi iš 7 ir atspausdintų
# #
# # is_7 = filter(lambda x: x % 7 == 0, skaiciai)
# # print(list(is_7))
# #
# # # arba
# #
# # is_7 = [x for x in skaiciai if x % 7 == 0]
# # print(is_7)
# #
# # # Pakeltų visus sąrašo skaičius kvadratu ir atspausdintų
# #
# # kvadratu = list(map(lambda x: x ** 2, skaiciai))
# # print(list(kvadratu))
# #
# # # arba
# #
# kvadratu = [x ** 2 for x in skaiciai]
# print(kvadratu)
# #
# # # Su kvadratų sąrašu atliktų šiuos veiksmus: atspausdintų sumą,
# # # mažiausią ir didžiausią skaičių, vidurkį, medianą
# #
# print(sum(kvadratu))
# print(len(kvadratu))
# print(min(kvadratu))
# print(max(kvadratu))
# print(mean(kvadratu))
# print(median(kvadratu))
# #
# # # Surūšiuotų ir atspausdintų kvadratų sąrašą atbulai
# #
# atbulai = sorted(kvadratu, reverse=True)
# print(atbulai)

# 3 UZDUOTIS

sarasas = [2.5, 2, "Labas", True, 5, 7, 8, 2.8, "Vakaras"]
#
# # Paskaičiuotų ir atspausdintų visų sąrašo skaičių sumą
#
# suma = sum(filter(lambda x: type(x) is int or type(x) is float, sarasas))
# suma = [x for x in sarasas if type(x) in [int, float]]
# print(suma)
#
# # arba
#
# stringai = sum(x for x in sarasas if type(x) is int or type(x) is float)
# print(stringai)
#
# # Sudėtų ir atspausdintų visus sąrašo žodžius
# #
# sakinys = filter(lambda x: type(x) is str, sarasas)
# print(" ".join(sakinys))
# #
# # # arba
# #
# sakinys = [x for x in sarasas if type(x) is str]
# print(" ".join(sakinys))
#
# # Suskaičiuotų ir atspausdintų, kiek sąrašę yra loginių (boolean)
# # kintamųjų su True reikšme
#
# kiek = sum(filter(lambda x: type(x) is bool, sarasas))
# print(kiek)
#
# # arba
#
# kiek = sum([type(x) is bool for x in sarasas])
# print(kiek)

# 4 UZDUOTIS
#
from operator import attrgetter
#
# # Turėtų klasę Zmogus, su savybėmis vardas ir amzius
# # Klasėje būtų __repr__ metodas, kuris atvaizduotų vardą ir amžių
#
class Zmogus:
    def __init__(self, vardas, amzius):
        self.vardas = vardas
        self.amzius = amzius

    def __repr__(self):
        return (f"({self.vardas}, {self.amzius})")

# # Inicijuoti kelis Zmogus objektus su vardais ir amžiais
# # Įdėti sukurtus Zmogus objektus į naują sąrašą
#
z1 = Zmogus("Ana", 28)
z2 = Zmogus("Joana", 36)
z3 = Zmogus("Janis", 49)
#
sarasas = [z1, z2, z3]
#
# # Surūšiuotų ir atspausdintų sąrašo objektus pagal vardą
#
# surusiuotas = sorted(sarasas, key=lambda x: x.vardas)
# print(surusiuotas)
# #
# # # arba
# #
# surusiuotas = sorted(sarasas, key=attrgetter("vardas"))
# print(surusiuotas)
# #
# # # Surūšiuotų ir atspausdintų sąrašo objektus pagal vardą atbulai
# #
# surusiuotas = sorted(sarasas, key=attrgetter("vardas"), reverse=True)
# print(surusiuotas)
# #
# # # Surūšiuotų ir atspausdintų sąrašo objektus pagal amžių
# #
# surusiuotas = sorted(sarasas, key=attrgetter("amzius"))
# print(surusiuotas)
# #
# # # Surūšiuotų ir atspausdintų sąrašo objektus pagal amžių atbulai
# #
# surusiuotas = sorted(sarasas, key=attrgetter("amzius"), reverse=True)
# print(surusiuotas)

