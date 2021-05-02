import re
'''
Criado por Claudio Freitas Nascimento
--
ORGANIZACAO DE ESTRUTURAS DE ARQUIVOS
LISTA DE AVALIACAO 1 - 2020.2
PROF. RENATO CAMPOS MAURO
Questao 2 - Considere um arquivo com registros de tamanho fixo, conforme a estrutura
definida abaixo. Considere tambem que o arquivo estao ordenado por cpf. Por uma
falha no sistema de inscricao o mesmo candidato pode se inscrever mais de uma vez.
Decidiu-se que a inscricao valida sera a ultima, ou seja, aquela com o maior numero de
id inscricao. Faca um programa que copie o arquivo "candidatos.dat" original em um
novo arquivo "candidatos2.dat", com os registros validos. Escreva de forma eficiente.
Qual e a complexidade desse metodo?
--
Chamada: lista1questao2Claudio.py
'''
f1 = open('candidatos.dat', "r")

separado = [] # Split da linha
dicionario_candidatos = {} # Dicionario do arquivo: key = CPF; values: linha do arquivo
print('Inicio da execucao do programa.\n')
while True:
    linha = f1.readline()
    linha = linha.replace('\n', '').replace('\r', '') # Remove fim da linha
    if linha == "":
        break
    else:
        separado = re.compile('[\s]{2,}').split(linha) # Split por 2 ou mais espacos
        if len(separado) == 1:
            separado = re.compile(' ').split(linha) # Split por 1 espaco
        elif len(separado) == 1:
            separado = re.compile(';').split(linha) # Split por ;
        if separado[2] in dicionario_candidatos: # Posicao 2 e o do CPF
            if separado[0] > dicionario_candidatos[separado[2]]: # Posicao 1 e o do ID
                dicionario_candidatos[separado[2]] = linha
        else:
            dicionario_candidatos[separado[2]] = linha
f1.close()

if bool(dicionario_candidatos):
    print('\nCriando arquivo candidatos2.dat')
    f2 = open('candidatos2.dat', "w")
    count = 1
    for key in sorted(dicionario_candidatos):
        linhaArq2 = dicionario_candidatos[key]
        f2.write(linhaArq2)
        if count < len(dicionario_candidatos):
            f2.write('\n')
            count += 1
    f2.close()
else:
    print('Nada lido no arquivo candidatos.dat')
print('\nPrograma encerrado.')
