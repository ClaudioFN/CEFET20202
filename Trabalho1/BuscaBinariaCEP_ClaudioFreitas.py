import re
import sys

# Criado por Claudio Freitas
# Execu��o do c�digo de ser feita por linha de comando
# Chamada: BuscaBinariaCEP_ClaudioFreitas.py CEP_PARA_PESQUISA

if len(sys.argv) != 2:
	print ("CODIGO FONTE NAO RECEBEU PARAMETRO DE ENTRADA: %s [CEP]" % sys.argv[0])
	quit()

print("INICIO DO PROCESSAMENTO\n")
f = open("cep_ordenado.dat","rb")
f.seek(0,2)
'''
seek(offset, from_what) 
offet = movimentacao para frente 
from_what = ponto de referencia no arquivo 0 - inicio / 1 - meio / 2 - fim 
'''
inicioArquivo = 0     #Inicio do Arquivo
fimArquivo = f.tell() #Fim do Arquivo
counter = 0  # Contador de leitura
achou = 0    # Encontrou o CEP pesquisado
meio = 0     # Etapa de meio do arquivo em questao de leitura
print("Tamanho do Arquivo cep_ordenado.dat: %d" % fimArquivo)
while(inicioArquivo <= fimArquivo):
    meio = int((inicioArquivo + fimArquivo)//2)
    f.seek(meio,0)
    linha = f.readline()
    formatado = str(linha)
    counter += 1
    if(re.search(sys.argv[1], formatado[-12:-3])):
        achou = 1
        break
    elif int(formatado[-12:-3]) < int(sys.argv[1]):
        inicioArquivo = meio + 1
    else:
        fimArquivo = meio - 1



if achou == 1:
   print("TELL -> %d " % f.tell())
   print("Linha: ", linha)
   print("Total de Registros Lidos: %d" % counter)
else:
	print("\nNenhum registro encontrado para o valor " + sys.argv[1])
	print("Total de Registros Lidos: %d" % counter)

print("\nFIM DO PROCESSAMENTO")
f.close()