import sys
import re
'''
Criado por Claudio Freitas Nascimento
--
ORGANIZACAO DE ESTRUTURAS DE ARQUIVOS
LISTA DE AVALIACAO 1 - 2020.2
PROF. RENATO CAMPOS MAURO
Questao - 1 Escreva um programa na sua linguagem de programcao de preferencia que
conte o numero de palavras e linhas de um arquivo texto, com o nome passado pelo
argumento do comando de linha.
--
Chamada: lista1questao1Claudio.py [NOME_ARQUIVO]
'''

if len(sys.argv) != 2:
    print ("CODIGO FONTE NAO RECEBEU PARAMETRO DE ENTRADA: %s [NOME_ARQUIVO]" % sys.argv[0])
    quit()

print("INICIO DO PROCESSAMENTO")
f = open(sys.argv[1],"r")
f.seek(0,2) # Vai para o fim do arquivo
fimArquivo = f.tell() #Fim do Arquivo
f.seek(0,0) # Volta ao inicio do arquivo
print("Tamanho do Arquivo "+sys.argv[1]+": " + str(fimArquivo))

linha = f.readline()
count = 0

while(linha != "" ):
    qtdPalavrasLinha = re.findall(r'\b\S+\b', linha) # Nao conta '-' como palavra
    count = count + 1
    print("Linha " + str(count) + " - '" + linha.rstrip() + "' tem " + str(len(qtdPalavrasLinha)) + " palavras.")
    linha = f.readline()

f.close()
print("FIM DO PROCESSAMENTO\n")
