import os, re
from pathlib import Path

def avaliaReact(pastaBase, nomeArquivo):
    print(f'Nome do Arquivo: {nomeArquivo}')
    
    nomeArquivoCompleto = os.path.join(foldername, filename)

    arquivo = open(nomeArquivoCompleto)
    texto = arquivo.read()
    #print(texto)

    # Filtragem do Texto Inicial
    regexSeta = re.compile(r"=>")
    texto = regexSeta.sub("", texto)

    matchesOriginal = []
    matchesGerado = []
    
    regexTags = re.compile(r'(<[^>]*>)')
    for groups in regexTags.findall(texto):
        #print(groups)
        matchesOriginal.append(groups)

    matchesGerado = matchesOriginal.copy()
    # Remoção das duplicatas
    for elemento in matchesOriginal:
        if "/>" in elemento:
            continue
        regexNomeTag = re.compile(r"<(\s*)(\w*)")
        nomeTag = regexNomeTag.search(elemento).group(2)
        print(nomeTag)

        for indice, elementoReverso in reversed(list(enumerate(matchesOriginal))):
            regexNomeTagReverso = re.compile(r"<(\s*)/(\w*)(\s*)>")
            nomeTagReverso = ''
            if regexNomeTagReverso.search(elementoReverso) is not None:
                nomeTagReverso = regexNomeTagReverso.search(elementoReverso).group(2)
            else:
                regexNomeTagReverso = re.compile(r"<(\s*)(\w*)(\s*)/>")
                if regexNomeTagReverso.search(elementoReverso) is not None:
                    nomeTagReverso = regexNomeTagReverso.search(elementoReverso).group(2)
                else:
                    continue
            if nomeTag == nomeTagReverso:
                matchesOriginal.pop(indice)
                break



    print("Original")
    print("\n".join(matchesGerado))
    print("Cortado")
    print("\n".join(matchesOriginal))    
        #matchesOriginal.reverse().remove()

    

    
    arquivo.close()

    


def avaliaVueJS(arquivo):
    print(arquivo)

def avaliaAngular(arquivo):
    print(arquivo)

arquivoEntrada = open("/home/administrador/Documentos/Python/automate/mestrado/Lista.txt", "r", newline='')
numero = 0

for linha in arquivoEntrada:
    linhaSplit = linha.split(";")
    
    nomeProjeto = linhaSplit[ 0 ]
    linguagem = linhaSplit[ 1 ]
    caminhoPadraoOrigem = linhaSplit[ 2 ]
    caminhoPadraoGerado = linhaSplit[ 3 ]
    while linha.strip() != ";;;;":
        linha = arquivoEntrada.readline().strip()
        print(linha)
        pasta = str(Path(caminhoPadraoOrigem, linha))

        for foldername, subfolders, filenames in os.walk(pasta):
            for filename in filenames:
                #nomeArquivo = os.path.join(foldername, filename)

                if ( linguagem == "React" and (filename.endswith(".js") or filename.endswith(".jsx") ) ):
                    avaliaReact(foldername, filename)


arquivoEntrada.close()




"""
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
    [a-zA-Z0-9._%+-]+      # username
    @                      # @ symbol
    [a-zA-Z0-9.-]+         # domain name
    (\.[a-zA-Z]{2,4})      # dot-something
    )''', re.VERBOSE)

text = str(pyperclip.paste())
matches = []

for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
         phoneNum += ' x' + groups[8]
    matches.append(phoneNum)

for groups in emailRegex.findall(text):
    matches.append(groups[0])

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')
"""