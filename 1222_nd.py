# 1
# import re
#
# def date_format(date):
#     pattern = re.compile(r'^(\d{2})\.(\d{2})\.(\d{4})$')
#     result = pattern.sub('\g<3> \g<2> \g<1>', date)
#     return result

# 2
import re

text = '''Workshop & Tutorial proposals: November 21, 2019
Notification of acceptance: December 1, 2019
Workshop & Tutorial websites online: December 18, 2019
Workshop papers: February 28, 2020
Workshop paper notifications: March 27, 2020
Workshop paper camera-ready versions: April 10, 2020
Tutorial material due (online): April 10, 2020'''

def date_format(text):
    pattern = re.compile(r'\s[a-zA-Z][\wąčęėįšųūž]+\s\d{1,2},\s\d{4}$')
    result = pattern.sub('text')
    print(result)
