import re
'''
Criado por Claudio Freitas Nascimento
--
ORGANIZACAO DE ESTRUTURAS DE ARQUIVOS
LISTA DE AVALIACAO 1 - 2020.2
PROF. RENATO CAMPOS MAURO
Questao 3 - Considere agora dois arquivos no mesmo formato: candidatosA.dat e candidatosB.
dat, ambos ordenados por CPF. Faca um programa que imprima na tela o email
dos candidatos que estao no arquivo A e no arquivo B simultaneamente. Escreva de
forma efciente. Nao ha repeticao de CPF. Qual e a complexidade desse metodo?
--
Chamada: nao_enviar_lista1questao3Claudio.py
'''
separado = []# Split da linha
dicionario_candidatosA = {}# Dicionario do arquivo: key = CPF; values: linha do arquivo
dicionario_candidatosB = {}# Dicionario do arquivo: key = CPF; values: linha do arquivo

def lerArquivo(nome_arquivo):
    f1 = open(nome_arquivo, "r")
    dicionario_candidatos = {}
    while True:
        linha = f1.readline()
        linha = linha.replace('\n', '').replace('\r', '') # Remove fim da linha
        if linha == "":
            break
        else:
            separado = re.compile('[\s]{2,}').split(linha)# Split por 2 ou mais espacos
            if len(separado) == 1:
                separado = re.compile(' ').split(linha)# Split por 1 espaco
            elif len(separado) == 1:
                separado = re.compile(';').split(linha)# Split por ;
            if separado[2] in dicionario_candidatos: # Posicao 2 e o do CPF
                if separado[0] > dicionario_candidatos[separado[2]]: # Posicao 1 e o do ID
                    dicionario_candidatos[separado[2]] = linha
            else:
                dicionario_candidatos[separado[2]] = linha
    f1.close()
    return dicionario_candidatos

print('Inicio da execucao do programa.\n')

dicionario_candidatosA = lerArquivo('candidatosA.dat')
dicionario_candidatosB = lerArquivo('candidatosB.dat')

if bool(dicionario_candidatosA) & bool(dicionario_candidatosB):
    print('Comparando os dois arquivos e mostrando o e-mail: ')
    '''set1 = set(dicionario_candidatosA.items())
    set2 = set(dicionario_candidatosB.items())
    comparado = set2 - set1'''
    for key in dicionario_candidatosA:
        if key in dicionario_candidatosB:
            comparado = re.compile('[\s]{2,}').split(dicionario_candidatosB[key])
            if len(comparado) == 1:
                comparado = re.compile(' ').split(dicionario_candidatosB[key])
            elif len(comparado) == 1:
                comparado = re.compile(';').split(dicionario_candidatosB[key])
            print(comparado[5])
else:
    print('Nada lido nos arquivos.')
print('\nPrograma encerrado.')
