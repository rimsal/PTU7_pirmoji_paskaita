# funkcija
'''
def pasisveikinti(vardas):
    print('Sveiki,', vardas)

pasisveikinti("Rima")
pasisveikinti("Sauliau")

def kvadratas(skaicius):
    return skaicius ** 2

print(kvadratas(6))



def skaiciu_suma(skaicius1=2, skaicius2=2, skaicius3=1):
    suma = skaicius1 + skaicius2
    rezultatas = suma * skaicius3
    return rezultatas

print(skaiciu_suma(5, 2))
print(skaiciu_suma(5, 2, 6))
print(skaiciu_suma(skaicius1=5, skaicius2=6, skaicius3=9))
print(skaiciu_suma(5))


def kvadratai(*args):
    for skaicius in args:
        print(skaicius ** 2)

kvadratai(4, 9, 2, 1)
kvadratai(1)
kvadratai()


def kvadratai(*args):
    suma = 0
    for skaicius in args:
         suma += skaicius3
     return suma

print(kvadratai(4, 9, 2, 1))
print(kvadratai(1))

rezultas = kvadratai(4, 9, 2, 1)
print(rezultas)



def spausdinti(**kwargs):
    for x in kwargs.items():
        print(x)
        #arba
        print(kwargs)

spausdinti(vardas='Rima', amzius=45, daiktas='Raktas')



def spausdinti(skaicius1, skaicius2, *args):
    return(skaicius1 + skaicius2) + sum(args)

print(spausdinti(2, 2))


#funkcijos aprašymas

def suma(a, b):
    #'''     #funkcijos_aprašymas
    #Ši funkcija sudeda du skaicius
    #:param a: pirmas skaicius
    #:param b: antras skaicius
    #:return: skaiciu a + b suma
    #'''

    #return a + b
'''

N.D.

# 4.1.1

def skaiciu_suma(skaicius1=2, skaicius2=2, skaicius3=1):
    suma = skaicius1 + skaicius2
    rezultatas = skaicius1 + skaicius2 + skaicius3
    return rezultatas

    print(skaiciu_suma(5, 2, 6))



# 4,1.2

def skaiciu_suma(skaicius1, skaicius2, skaicius3):
    rezultatas = (skaicius1 + skaicius2 + skaicius3)
    return rezultatas


print(skaiciu_suma(2, 5, 4))


# 4.1.3


def didz_skaiciu(*args):
    didis = 0
    for skaicius in args:
        if skaicius > didis:
            didis = skaicius
    return(didis)


skaicius = (4, 9, 2, 1)

print(didz_skaiciu(4, 9, 21, 11))


# 4.1.4

zodziai: str = ['Labas vakaras, Lietuva']
print(zodziai[::-1])
'''

#4.1.5

# def info(masyvas):
#     x = 0
#     y = 0
#     z = 0
#     for c in masyvas:
#         if c.isdigit():
#             z += 1
#         if c.isupper():
#             x += 1
#         if c.islower():
#             y += 1
#     print(f"Didžiosios {x}, Mažosios {y}, Skaičiai {z}")
#
# info("Labas vakaras 21543")




#
# print("Input a string: ")
# str1 = input()
#
# no_of_ucase, no_of_lcase = 0,0
#
# for c in str1:
#     if c>='A' and c<='Z':
#         no_of_ucase += 1
#     if c>='a' and c<='z':
#         no_of_lcase += 1
#     if c>='0' and c<='0':
# print("Input string is", str1)
# print("Total number of uppercase letters: ", no_of_ucase)
# print("Total number of lowercase letters: ", no_of_lcase)

# ASMENS KODO PATIKRINIMAS

def gauti_kontrolini(asmens_kodas):
    kodas = str(asmens_kodas)





