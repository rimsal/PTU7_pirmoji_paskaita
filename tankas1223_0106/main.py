from tankas1223_0106.judejimas import Taikinys
from tankas1223_0106.tankas import Tankas

tankas = Tankas()
taikinys = Taikinys()
Taskai = 100

while Taskai != 0:  # Programa veiks kol taškai nesibaigs.
    print("Judesiai:")
    print("w: aukštyn, s: žemyn, a: kairėn, d: dešinėn")
    print("b: Boom, i: informacija, q: išeiti")
    print(f"x: {tankas.x}, y: {tankas.y}")
    x = str(input("Tavo pasirinkimas: "))
    Taskai -= 10

    if x == 'w':
        tankas.judeti('aukštyn')
    elif x == 's':
        tankas.judeti('žemyn')
    elif x == 'a':
        tankas.judeti('kairėn')
    elif x == 'd':
        tankas.judeti('dešinėn')
    elif x == 'b':
        if tankas.sauti(taikinys.x, taikinys.y):
            print('Pataikei')
            Taskai += 50  # Pataikius pridedami 50 taškų
            taikinys.atkurta()  # Per naują nustatomas taikinys
    elif x == 'i':
        tankas.info()
    elif x == "q":
        print("GG")
        print(f"Targets Hit: {tankas.suviu_skaicius}")
        break
    elif x == "c":
        print(f"{taikinys.x}: {taikinys.y}")

print("Taškai baigėsi, ko dar nori?")







# while True:
#     tankas.info()
#     if tankas.ar zaidimo pabaiga():
#         print("Žaidimo pabaiga")
#         break
#     choise = input("w - pirmyn \ns - atgal \na - kairėn \nd - dešinėn \nx - šauti \ne - išeiti \n")
#     math choise:
#         case "w":
#             tankas.pirmyn()
#          case "s":
#             tankas.atgal()
#         case "a":
#             tankas.kairėn()
#          case "d":
#             tankas.dešinėn()
#          case "x":
#             tankas.šūvis()
#          case "e":
#             print("Viso gero!")
#             break
