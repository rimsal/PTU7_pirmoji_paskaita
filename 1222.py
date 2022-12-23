import re
# dirbsime su telefono numeriais, tokiais kaip +370 642 12321.

# pattern = re.compile(r'\+370\s\d{3}\s\d{5}')
#
# tekstas = '''Pirmas telefono numeris yra +370 123 12321,
#                 antras +370 321 10101.'''
# res = pattern.search(tekstas)
# print(res)

# Jei .search neranda mūsų šabloną atitinkančios simbolių sekos,
# res įgauna None reikšmę. Tam, kad ištraukti match reikšmę,
# naudojame .group() metodą:

# print(res.group())

# search metodas nepalaiko daugiau negu 1 reikšmės suradimo
# tekste, norint surasti visas, naudojamas metodas findall:
# findall grąžina surastus atitikmenis sąraše.

# res = pattern.findall(tekstas)
# print(res)

# funkciją, kuri patikrintų, ar pateiktas el. pašto adresas
# atitinka standartus:

# def validate_email(input):
#     email_regex = re.compile(r'^[a-zA-Z0-9._%-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$')
#     result = email_regex.search(input)
#     if result:
#         return True
#     return False

# print(validate_email('kazkoks@email.lt'))
# print(validate_email('neteisingas@@email.lt'))

# Kaip gauti naudos iš grupavimo? Tarkime,
# turime vardų sąrašą tokiu formatu - Mr. Phil Collins.
# Parašykime funkciją, kuri išskaido kreipinį, vardą ir
# pavardę:

# def split_names(name):
#     pattern = re.compile(r'^([A-Z]\w{1,3}\.)\s([A-Z]\w+)\s([A-Z]\w+)$')
#     result = pattern.search(name)
#     if result:
#         print(f'Visa eilutė: {result.group(0)}')
#         print(f'Kreipinys: {result.group(1)}')
#         print(f'Vardas: {result.group(2)}')
#         print(f'Pavardė: {result.group(3)}')
#         print('----------------------------------')
#         print(result.group())
#         print(result.groups())
#     else:
#         print('Įvestis neatitinka šablono')
#
# split_names('Mr. Clint Eastwood')

# jeigu norime, grupėms galime suteikti savo pavadinimus,
# naudodami tokią sintaksę:

# pattern = re.compile(r'^([A-Z]\w{1,3}\.)\s([A-Z]\w+)\s([A-Z]\w+)$')
# print(f'Kreipinys: {result.group("kreipinys")}')

# card_number = "card1: 0452 6544 0004 4456, card2: 1234 4567 8910 1112"
# pattern = re.compile(r'\b\d{4}\s\d{4}\s\d{4}\s\d{4}\b')
# res = pattern.sub('**** **** **** ****', card_number)
# print(res)
#
# card_number = "card1: 0452 6544 0004 4456, card2: 1234 4567 8910 1112"
# pattern = re.compile(r'\b(\d{4})\s\d{4}\s\d{4}\s\d{4}\b')
# res = pattern.sub('\g<1> **** **** ****', card_number)
# print(res)

# galime naudoti flags.
# re.IGNORECASE arba re.I - padaro jūsų užklausą case insensitive.
# t.y. nekreipia dėmesio, į didžiąsias - mažąsias raides.
# re.MULTILINE arba re.M - elgiasi su jūsų tekstu kaip su daug
# eilučių turinčia struktūra, o ne žiūri kaip į vieną eilutę.
# *re.VERBOSE arba re.X - leidžia jums suformuoti regex užklausą per
# kelias eilutes su komentarais. Prideda užklausoms skaitomumo.

# tekstas = '''Trumpas tekstas
# apie beleką'''
# pattern = re.compile(r't\w+', re.I)
# res = pattern.findall(tekstas)
# print(res)

# re.MULTILINE:
# tekstas = '''Trumpas tekstas
# apie beleką'''
#
# pattern = re.compile(r'^\w+')
# res = pattern.findall(tekstas)
#
# pattern2 = re.compile(r'^\w+', re.M)
# res2 = pattern2.findall(tekstas)
#
# print(res)
# print(res2)

# re.VERBOSE:

# tekstas = 'Jonas Jonaitis +370 622 01234'
# pattern = re.compile(r'''
#                     [A-Z]\w+              # vardas
#                     \s                    # tarpas
#                     [a-z]\w+              # pavardė
#                     \s                    # tarpas
#                     \+370\s6\d{2}\s\d{5}  # telefono numeris
#                     ''', re.X | re.I)
# res = pattern.findall(tekstas)
# print(res)
