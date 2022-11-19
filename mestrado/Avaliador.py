import os
import re
import csv
from pathlib import Path

def calculaPortcentagem(gerado, total):
    return round((gerado / total) * 100, 2)

def calculaMedia(lista):
    return round((sum(lista) / len(lista)),2)

def avaliaReact(pastaBaseOriginal, nomeArquivoOriginal, pastaBaseGerado, nomeArquivoGerado, nomeProjeto, outputDictWriter):
    tagsOriginal = 0
    tagsOriginalFormatado = 0
    tagsGerado = 0
    tagsGeradoFormatado = 0
    porcentagemNormal = 0.0
    porcentagemFormatado = 0.0

    print(f'Nome do Arquivo: {nomeArquivoOriginal}')

    nomeArquivoCompletoOriginal = os.path.join(pastaBaseOriginal, nomeArquivoOriginal)

    arquivoOriginal = open(nomeArquivoCompletoOriginal)
    textoOriginal = arquivoOriginal.read()
    # print(texto)

    # Filtragem do Texto Inicial
    regexSeta = re.compile(r"=>")
    textoOriginal = regexSeta.sub("", textoOriginal)

    if ( linguagem == "VueJS"):
        regexVueJS = re.compile(r'<\s*template\s*>.*<\s*/\s*template\s*>', re.DOTALL)
        textoOriginal = regexVueJS.findall(textoOriginal)[ 0 ]

    matchesOriginal = []

    regexTags = re.compile(r'(<[^>]*>)')
    for groups in regexTags.findall(textoOriginal):
        # print(groups)
        matchesOriginal.append(groups)

    tagsOriginal = len(matchesOriginal)

    # Remoção das duplicatas
    regexTagsASeremRemovidas = re.compile(r'<(\s*)/([^>]*)>')
    matchesOriginal = [
        i for i in matchesOriginal if not regexTagsASeremRemovidas.match(i)]

    print("Cortado")
    print("\n".join(matchesOriginal))

    tagsOriginalFormatado = len(matchesOriginal)
    arquivoOriginal.close()

    #Fim do tratamento do arquivo original

    print(f'Nome do Arquivo: {nomeArquivoGerado}')

    nomeArquivoCompletoGerado = os.path.join(pastaBaseGerado, nomeArquivoGerado)

    arquivoGerado = open(nomeArquivoCompletoGerado)
    textoGerado = arquivoGerado.read()
    # print(texto)

    # Filtragem do Texto Inicial
    #regexSeta = re.compile(r"=>")
    textoGerado = regexSeta.sub("", textoGerado)

    if ( linguagem == "VueJS"):
        textoGerado = regexVueJS.findall(textoGerado)[ 0 ]

    matchesGerado = []

    #regexTags = re.compile(r'(<[^>]*>)')
    for groups in regexTags.findall(textoGerado):
        # print(groups)
        matchesGerado.append(groups)

    tagsGerado = len(matchesGerado)

    # Remoção das duplicatas
    #regexTagsASeremRemovidas = re.compile(r'<(\s*)/(\w*)(\s*)>')
    matchesGerado = [
        i for i in matchesGerado if not regexTagsASeremRemovidas.match(i)]

    print("Cortado")
    print("\n".join(matchesGerado))

    tagsGeradoFormatado = len(matchesGerado)
    arquivoGerado.close()

    # Calcula porcentagens
    porcentagemNormal = calculaPortcentagem(tagsGerado, tagsOriginal)
    mediaPorcentagemNormal.append(porcentagemNormal)
    porcentagemNormal = str(porcentagemNormal) + "%"

    porcentagemFormatado = calculaPortcentagem(tagsGeradoFormatado, tagsOriginalFormatado)
    mediaPorcentagemFormatado.append(porcentagemFormatado)
    porcentagemFormatado = str(porcentagemFormatado) + "%"

    # Adiciona valores
    mediaTagsOriginal.append(tagsOriginal)
    mediaTagsOriginalFormatado.append(tagsOriginalFormatado)
    mediaTagsGerado.append(tagsGerado)
    mediaTagsGeradoFormatado.append(tagsGeradoFormatado)    

    #Escreve arquivo    
    outputDictWriter.writerow({'Projeto': nomeProjeto, 'Arquivo': nomeArquivoOriginal, 'TagsOriginal': tagsOriginal, 'TagsOriginalFormatado': tagsOriginalFormatado, 'TagsGerado': tagsGerado, 'TagsGeradoFormatado': tagsGeradoFormatado, 'PorgentagemNormal': porcentagemNormal, 'PorcentagemFormatado': porcentagemFormatado })




def avaliaVueJS(arquivo):
    print(arquivo)


def avaliaAngular(arquivo):
    print(arquivo)


arquivoEntrada = open(
    "/home/administrador/Documentos/Python/automate/mestrado/Lista.txt", "r", newline='')

# Variáveis para as médias
mediaTagsOriginal = []
mediaTagsGerado = []
mediaPorcentagemNormal = []
mediaTagsOriginalFormatado = []
mediaTagsGeradoFormatado = []
mediaPorcentagemFormatado = []

outputFile = open('output.csv', 'w', newline='')
outputDictWriter = csv.DictWriter(outputFile, ['Projeto', 'Arquivo', 'TagsOriginal', 'TagsGerado', 'PorgentagemNormal', 'TagsOriginalFormatado',  'TagsGeradoFormatado', 'PorcentagemFormatado'])
outputDictWriter.writeheader()

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
                                avaliaReact(foldername, filename, foldernameGerado, filenameGer, nomeProjeto, outputDictWriter)
                            elif (linguagem == "Angular" and filename.endswith(".html")):
                                avaliaReact(foldername, filename, foldernameGerado, filenameGer, nomeProjeto, outputDictWriter)
                            elif (linguagem == "VueJS" and filename.endswith(".vue")):
                                avaliaReact(foldername, filename, foldernameGerado, filenameGer, nomeProjeto, outputDictWriter)



mediaTagsOriginal = calculaMedia(mediaTagsOriginal)
mediaTagsGerado = calculaMedia(mediaTagsGerado)
mediaTagsOriginalFormatado = calculaMedia(mediaTagsOriginalFormatado)
mediaTagsGeradoFormatado = calculaMedia(mediaTagsGeradoFormatado)
mediaPorcentagemNormal = str(calculaMedia(mediaPorcentagemNormal)) + "%"
mediaPorcentagemFormatado = str(calculaMedia(mediaPorcentagemFormatado)) + "%"

outputDictWriter.writerow({'Projeto': "Média", 'Arquivo': "Média", 'TagsOriginal': mediaTagsOriginal, 'TagsOriginalFormatado': mediaTagsOriginalFormatado, 'TagsGerado': mediaTagsGerado, 'TagsGeradoFormatado': mediaTagsGeradoFormatado, 'PorgentagemNormal': mediaPorcentagemNormal, 'PorcentagemFormatado': mediaPorcentagemFormatado })



arquivoEntrada.close()
outputFile.close()

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
