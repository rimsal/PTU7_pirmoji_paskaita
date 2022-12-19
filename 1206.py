# I.I
'''
masyvas = [5, 6, 8, "Tomas", [2, 3, 1], True]

print(masyvas[3])
masyvas.append("Saulė")
print(masyvas)
masyvas.pop(2)
print(masyvas)
masyvas[-2] = False
print(masyvas)


# I.2

skaiciai = []
while True:
    a = int(input("Įveskite skaičių: "))
    if a > 0:
        print(a)
        skaiciai.append(a)
    if a < 0:
        print(suma)
    break

# I.3

l = []

for x in range(5):
    zodis = input('Iveskite zodi:')
    l.append(zodis)

for n in l:
    print(l.index(n)+1, n, f"Raidziu: {len(n)}")

#I.4

import random

for x in range(3):
    skaicius = random.randint(1, 6)
    print(random.randint(1, 6))
    if skaicius == 5
        print("pralaimejai")
        break

import random
skaiciai = []
for x in range(3):
    skaicius = random.randint(1, 6)
    print(skaicius)
    skaiciai.append(skaicius)
if 5 in skaiciai:
    print("Pralaimėjai")
else:
    print("Laimėjai")
'''
 #ne/keliamieji metai

metai = int(input("Įveskite metus "))

if (metai % 4 == 0 and metai % 100 != 0) and (metai % 400 == 0):
     print('Keliamieji')
else:
     print("Nekeliamieji")
