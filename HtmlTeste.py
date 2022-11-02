#! python3

import pyperclip, re

phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?                # area code
    (\s|-|\.)?                        # separator
    (\d{3})                           # first 3 digits
    (\s|-|\.)                         # separator
    (\d{4})                           # last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?    # extension
    )''', re.VERBOSE)

emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+
    @
    [a-zA-Z0-9.-]+
    (\.[a-zA-Z]{2,4})
)''', re.VERBOSE)

htmlRegex2 = re.compile(r'''<(?:"[^"]*"['"]*|'[^']*'['"]*|[^'">])+>''', re.VERBOSE)
scriptRegex = re.compile(r'''<template>.*</template>''', re.VERBOSE)
htmlRegex = re.compile(r'''(<[^>]*>)''', re.VERBOSE)

text = str(pyperclip.paste())
matches = []
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)

for groups in emailRegex.findall(text):
    matches.append(groups[0])

"""for grupos in scriptRegex.findall(text):
    for groups in htmlRegex.findall(grupos):
        matches.append(groups)"""

cinturaoRegex = re.compile(r'''=>''')
textoAlterado = cinturaoRegex.sub('', text)


for groups in htmlRegex.findall(textoAlterado):
    matches.append(groups)

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Total encontrado: ' + str(len(matches)))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')