import os
import re
from pathlib import Path

def avaliaReact(pastaBaseOriginal, nomeArquivoOriginal, pastaBaseGerado, nomeArquivoGerado):
    print(f'Nome do Arquivo: {nomeArquivoOriginal}')

    nomeArquivoCompletoOriginal = os.path.join(pastaBaseOriginal, filename)

    arquivoOriginal = open(nomeArquivoCompletoOriginal)
    textoOriginal = arquivoOriginal.read()
    # print(texto)

    # Filtragem do Texto Inicial
    regexSeta = re.compile(r"=>")
    textoOriginal = regexSeta.sub("", textoOriginal)

    matchesOriginal = []

    regexTags = re.compile(r'(<[^>]*>)')
    for groups in regexTags.findall(textoOriginal):
        # print(groups)
        matchesOriginal.append(groups)

    # Remoção das duplicatas
    regexTagsASeremRemovidas = re.compile(r'<(\s*)/(\w*)(\s*)>')
    matchesOriginal = [
        i for i in matchesOriginal if not regexTagsASeremRemovidas.match(i)]

    print("Cortado")
    print("\n".join(matchesOriginal))

    arquivoOriginal.close()


def avaliaVueJS(arquivo):
    print(arquivo)


def avaliaAngular(arquivo):
    print(arquivo)


arquivoEntrada = open(
    "/home/administrador/Documentos/Python/automate/mestrado/Lista.txt", "r", newline='')
numero = 0

for linha in arquivoEntrada:
    linhaSplit = linha.split(";")

    nomeProjeto = linhaSplit[0]
    linguagem = linhaSplit[1]
    caminhoPadraoOrigem = linhaSplit[2]
    caminhoPadraoGerado = linhaSplit[3].strip()
    while linha.strip() != ";;;;":
        linha = arquivoEntrada.readline().strip()
        print(linha)
        pastaOriginal = str(Path(caminhoPadraoOrigem, linha))
        pastaGerado = str(Path(caminhoPadraoGerado, linha))

        for foldername, subfolders, filenames in os.walk(pastaOriginal):
            for filename in filenames:
                for foldernameGerado, subfoldersGerado, filenamesGerado in os.walk(pastaGerado):
                    for filenameGer in filenamesGerado:
                        nomeOrigem = Path(os.path.join(foldername, filename))
                        nomeGerado = Path(os.path.join(foldernameGerado, filenameGer))
                        if nomeOrigem.stem.lower() == nomeGerado.stem.lower():
                            if (linguagem == "React" and (filename.endswith(".js") or filename.endswith(".jsx"))):
                                avaliaReact(foldername, filename, foldernameGerado, filenameGer)


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
