from _datetime import datetime
#
# zen = '''The Zen of Python, by Tim Peters
#
# Beautiful is better than ugly.
# Explicit is better than implicit.
# Simple is better than complex.
# Complex is better than complicated.
# Flat is better than nested.
# Sparse is better than dense.
# Readability counts.
# Special cases aren't special enough to break the rules.
# Although practicality beats purity.
# Errors should never pass silently.
# Unless explicitly silenced.
# In the face of ambiguity, refuse the temptation to guess.
# There should be one-- and preferably only one --obvious way to do it.
# Although that way may not be obvious at first unless you're Dutch.
# Now is better than never.
# Although never is often better than *right* now.
# If the implementation is hard to explain, it's a bad idea.
# If the implementation is easy to explain, it may be a good idea.
# Namespaces are one honking great idea -- let's do more of those!'''


# 1. Sukurti failą tekstas.txt su tekstu:

# with open("failas.txt", 'w') as failas:
#     failas.write(zen)

# 2. Atspausdintų tekstą iš sukurto failą:
# with open("failas.txt", 'r') as failas:
#     print(failas.read())

# 3. Paskutinėje sukurto failo eilutėje pridėtų šiandien datą:

# with open('failas.txt', 'a') as failas:
#     failas.write("\n" + str(datetime.datetime.today()))

# 4. Sunumeruoti visas failo teksto eilutes (kiekvienos pradžioje pridėti skaičių):

# naujas = ""
# skaicius = 1
# with open('failas.txt', 'r') as failas:
#     for eilute in failas:
#         naujas += str(skaicius) + " " + eilute
#         skaicius += 1
#
# with open('failas.txt', 'w') as failas:
#     failas.write(naujas)

# 5. Sukurtame faile eilutę "Beautiful is better than ugly." pakeisti į "Gražu yra geriau nei bjauru.":

# pakeitimas = ""
#
# with open('failas.txt', 'r') as failas:
#     pakeitimas = failas.read()
#
# pakeitimas = pakeitimas.replace("3 Beautiful is better than ugly.", "3 Gražu yra geriau nei bjauru.")
#
# with open('failas.txt', 'w', encoding="UTF-8") as failas:
#     failas.write(pakeitimas)


# 6. Atspausdintų visą failo tekstą atbulai:

# zen = ""
#
# with open("failas1.txt", 'r') as failas:
#      print(str(failas.read()[::-1]))


# 7. Atspausdintų, kiek failo tekste yra žodžių, skaičių, didžiųjų ir mažųjų raidžių:

# with open("failas1.txt", 'r') as failas:
#     pakeitimas = failas.read()
#
# skaiciai = len([x for x in pakeitimas if x.isdigit()])
# didziosios = len([x for x in pakeitimas if x.isupper()])
# mazosios = len([x for x in pakeitimas if x.islower()])
#      print(skaiciai, didziosios, mazosios, len(pakeitimas.split()))



# 8. Nukopijuotų visą sukurto failą tekstą į naują failą, tik DIDŽIOSIOMIS RAIDĖMIS:
#

# with open('failas1.txt', 'r', encoding="UTF-8") as nuskaitomas_failas:
#     with open('failas2.txt', "w", encoding="UTF-8") as irasomas_failas:
#         irasomas_failas.write(nuskaitomas_failas.read(upper)))

# BIUDZETO SUDARYMAS

import pickle
def nuskaityti_is_failo():
    try:
        with open("didzioji_knyga.pkl", 'rb') as file:
            knyga = pickle.load(file)
    except:
        knyga = []
    return knyga
def irasyti_i_faila(masyvas):
    with open('didzioji_knyga.pkl', 'wb') as file:
        pickle.dump(masyvas, file)
knyga = nuskaityti_is_failo()
while True:
    veiksmas = int(input("""1 - įvesti pajamas/išlaidas
2 - parodyti pajamas/išlaidas
3 - balansas
0 - išeiti
"""))
    match veiksmas:
        case 1:
            suma = float(input("Įveskite sumą: "))
            knyga.append(suma)
            irasyti_i_faila(knyga)
        case 2:
            print("Knyga:", knyga)
        case 3:
            print("Balansas", sum(knyga))
        case 0:
            print("Viso gero")
            break
        case _:
            print("nėra tokio veiksmo")
