# 1.1
'''
skaicius = int(input("Įveskite skaičių: "))
ar_skaicius_teigiamas = skaicius > 0
print(type(ar_skaicius_teigiamas))

print(int(input("Įveskite skaičių: ")) > 0

#funkcija true or false

#1.2

import datetime
x = datetime.datetime.today()
print(x)

import datetime
now = datetime.datetime.now()
print(now - datetime.timedelta(days=5))
print(now + datetime.timedelta(hours=8))

import datetime
y = datetime.datetime(2019, 3, 8, 9, 57, 17)
print(y)


#1.3

import datetime
ivesta_data:str = input("Įveskite datą: ")
data: datetime = datetime.datetime.strptime(ivesta_data, "%Y-%m-%d")
skirtumas = (datetime.datetime.now() - data)

print("Nuo įvestos datos praėjo:")
print("Metų:", skirtumas.days // 365)
print("Menesių:", skirtumas.days // 365 * 12)

print(int(skirtumas.total_seconds() // 60), "Minucių")
print(int(skirtumas.total_seconds()), "Sekundzių")
print("")
print("Programos pabaiga")

#1.4
# tikrina klaidas

while True:
    try:
        skaicius = int(input("Įveskite skaičių: "))
        break
    except ValueError:
        print("Įvedėte ne skaičių")

ar_skaicius_teigiamas = skaicius > 0
print(type(ar_skaicius_teigiamas))


'''
#1.5

# tikrina klaidas


import datetime

while True:
        try:
                ivesta_data:str = input("Įveskite datą: ")
                data: datetime = datetime.datetime.strptime(ivesta_data, "%Y-%m-%d")
                break
        except ValueError as klaida:
                print("Neteisingai įvesta data. Bandykite dar kartą")
                print(klaida)

skirtumas = (datetime.datetime.now() - data)
print(ivesta_data)
print(skirtumas.days // 365, "Metų")
print(skirtumas.days // 30, "Menesių")
print(int(skirtumas.total_seconds() // 60), "Minucių")
print(int(skirtumas.total_seconds()), "Sekundzių")
print("")
print("Programos pabaiga")
