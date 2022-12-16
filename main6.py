
# import pickle
#
# while True:
#     veiksmas = int(input("Pasirinkite veiksmą: 1 - peržiūrėti, 2 - įrašyti, 3 - išeiti"))
#     if veiksmas == 1:
#         try:
#             with open("zmones.pkl", 'rb') as failas:
#                 print(pickle.load(failas))
#         except:
#             print("Nėra tokio failo")
#             with open("zmones.pkl", 'wb') as failas:
#                 zmones = []
#                 pickle.dump(zmones, failas)
#     if veiksmas == 2:
#         with open("zmones.pkl", 'rb') as failas:
#             zmones = pickle.load(failas)
#             vardas = input("Įveskite naują vardą")
#             with open("zmones.pkl", 'wb') as failas:
#                 zmones.append(vardas)
#                 pickle.dump(zmones, failas)
#     if veiksmas == 3:
#         print("Programa baigta")
#         break
#
# class Automobilis:
#     def __init__(self, marke, modelis):
#         self.marke = marke
#         self.modelis = modelis
#
# automobiliai = [Automobilis("Toyota", "Avensis"), Automobilis("Toyota", "Corolla"), Automobilis("Toyota", "Camry")]
#
# with open("automobilis.pkl", "wb") as failas:
#     pickle.dump(automobiliai, failas)
#
# with open("automobilis.pkl", "rb") as failas:
#     automobiliai = pickle.load(failas)
#     for automobilis in automobiliai:
#         print("Markė", automobilis.marke)
#         print("Modelis", automobilis.modelis)



# N.M.
# 1 užduotis
from _datetime import datetime

zen = '''The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!'''


# 1.1 Sukurti failą tekstas.txt su tekstu:
#
# with open("failas.txt", 'w') as failas:
#     failas.write(zen)
#
# # 1,2. Atspausdintų tekstą iš sukurto failą:
# with open("failas.txt", 'r') as failas:
#     print(failas.read())
#
# # 1,3. Paskutinėje sukurto failo eilutėje pridėtų šiandien datą:
#
# with open('failas.txt', 'a') as failas:
#     failas.write("\n" + str(datetime.today()))
#
# # 1,4. Sunumeruoti visas failo teksto eilutes (kiekvienos pradžioje pridėti skaičių):
#
# naujas = ""
# skaicius = 1
# with open('failas.txt', 'r') as failas:
#     for eilute in failas:
#         naujas += str(skaicius) + " " + eilute
#         skaicius += 1
#
# with open('failas.txt', 'w') as failas:
#     failas.write(naujas)
#
# # 1,5. Sukurtame faile eilutę "Beautiful is better than ugly." pakeisti į "Gražu yra geriau nei bjauru.":
#
# zen = ""
#
# with open('failas.txt', 'r', encoding="UTF-8") as failas:
#     pakeitimas = failas.read()
#
# pakeitimas = pakeitimas.replace("Beautiful is better than ugly.", "Gražu yra geriau nei bjauru.")
#
# with open('failas.txt', 'w', encoding="UTF-8") as failas:
#     failas.write(pakeitimas)

#
# # 1,6. Atspausdintų visą failo tekstą atbulai:
#
# zen = ""
#
# with open("failas1.txt", 'r') as failas:
#      print(str(failas.read()[::-1]))
#
#
# # 1,7. Atspausdintų, kiek failo tekste yra žodžių, skaičių, didžiųjų ir mažųjų raidžių:

# with open("failas1.txt", 'r') as failas:
#     pakeitimas = failas.read()
#
# skaiciai = len([x for x in pakeitimas if x.isdigit()])
# didziosios = len([x for x in pakeitimas if x.isupper()])
# mazosios = len([x for x in pakeitimas if x.islower()])
# print(skaiciai, didziosios, mazosios, len(pakeitimas.split()))



# 1,8. Nukopijuotų visą sukurto failą tekstą į naują failą, tik DIDŽIOSIOMIS RAIDĖMIS:
# zen = ""
#
# with open('failas1.txt', 'r', encoding="UTF-8") as nuskaitomas_failas:
#     with open('tekstas_didziosiomis.txt', "w", encoding="UTF-8") as irasomas_failas:
#         irasomas_failas.write(nuskaitomas_failas.read().upper())

# 2 UŽDUOTIS
# while True:
#     ivestas = input("Įveskite tekstą: ")
#     tekstas += ivestas + "\n"
#     if not ivestas:
#         break
#
# failo_pav = input("Įveskite failo pavadinimą")
#
# with open(f"{failo_pav}.txt", 'w') as file:
#     file.write(tekstas)

#  3 užduotis ?????
#
import os
from datetime import datetime

# 1 Ant darbalaukio sukurtų naują katalogą "Mano Katalogas"

try:
    os.chdir('C:\\Users\\Donoras\\Desktop')
    os.mkdir("Naujas katalogas")
except:
    "Toks katalogas jau yra"

os.chdir('C:\\Users\\Donoras\\Desktop\\Naujas katalogas')

# 2 Jame sukurtų failą "data.txt", kurios tektas - šiandienos data ir laikas

with open("data.txt", "w") as failas:
    failas.write(str(datetime.today()))

# 3 Atspaudintų, kada naujas failas buvo modifikuotas ir kiek jis užima baitų
os.chdir('C:\\Users\\Donoras\\Desktop\\Naujas katalogas')

print("Sukūrimo data:", datetime.fromtimestamp(os.stat("data.txt").st_ctime))
print("Failo dytis:", os.stat("data.txt").st_size)


# # 4, MINIBIUDZETO SUDARYMAS
#
# import pickle
# def nuskaityti_is_failo():
#     try:
#         with open("didzioji_knyga.pkl", 'rb') as file:
#             knyga = pickle.load(file)
#     except:
#         knyga = []
#     return knyga
# def irasyti_i_faila(masyvas):
#     with open('didzioji_knyga.pkl', 'wb') as file:
#         pickle.dump(masyvas, file)
# knyga = nuskaityti_is_failo()
# while True:
#     veiksmas = int(input("""1 - įvesti pajamas/išlaidas
# 2 - parodyti pajamas/išlaidas
# 3 - balansas
# 0 - išeiti
# """))
#     match veiksmas:
#         case 1:
#             suma = float(input("Įveskite sumą: "))
#             knyga.append(suma)
#             irasyti_i_faila(knyga)
#         case 2:
#             print("Knyga:", knyga)
#         case 3:
#             print("Balansas", sum(knyga))
#         case 0:
#             print("Viso gero")
#             break
#         case _:
#             print("nėra tokio veiksmo")
