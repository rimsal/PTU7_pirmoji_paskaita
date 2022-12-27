# 1
# import re
#
# def date_format(date):
#     pattern = re.compile(r'^(\d{2})\.(\d{2})\.(\d{4})$')
#     result = pattern.sub('\g<3> \g<2> \g<1>', date)
#     return result
import re

# 2
# import re


# text = '''Workshop & Tutorial proposals: November 21, 2019
# Notification of acceptance: December 1, 2019
# Workshop & Tutorial websites online: December 18, 2019
# Workshop papers: February 28, 2020
# Workshop paper notifications: March 27, 2020
# Workshop paper camera-ready versions: April 10, 2020
# Tutorial material due (online): April 10, 2020'''
#
# pattern = re.compile(r'\s[a-zA-Z]+\s\d{1,2},\s\d{4}$', re.M)
# res = pattern.findall(text)
# print(res)

# 3
#
# import re
#
# text = '''Workshop & Tutorial proposals: November 21, 2019
# Notification of acceptance: December 1, 2019
# Workshop & Tutorial websites online: December 18, 2019
# Workshop papers: February 28, 2020
# Workshop paper notifications: March 27, 2020
# Workshop paper camera-ready versions: April 10, 2020
# Tutorial material due (online): April 10, 2020'''
#
# for nr, line in enumerate(text.splitlines(), 1):
#
#     pattern = re.compile(r"(^[a-zA-Z]+\s[&?\s[a-zA-Z\W]+:)\s([a-zA-Z]+\s\d{1,2},\s\d{4}$)", re.M)
#     result = pattern.search(text)
#     print(nr)
#     print(f'Event: {result.group(1)}')
#     print(f'Date: {result.group(2)}')

# 4
# import re
#
# def cenzura(tekstas, *keiksmai):
#     for zodis in keiksmai:
#         pattern = re.compile(f"([a-zA-Z\wąčęėįšųūž])([a-zA-Z\wąčęėįšųūž]+)([a-zA-Z\wąčęėįšųūž])")
#         result = pattern.search(zodis)
#         zodis1 = pattern.sub("\g<1>*****\g<3>", zodis)
#         tekstas.replace(zodis1, zodis)
#         print(zodis1)
#
#
#
# cenzura('baisūs žodžiai, tokie kaip kvaraba, žaltys..', 'kvaraba', 'žaltys')
#

# 5

import re

with open("tekstas1223.html", 'r') as file:
    textas = file.read()
    pattern = re.compile(r'([a-zA-Z\wąčęėįšųūž].+)', re.M)
    res = pattern.findall(textas)

print(res)















