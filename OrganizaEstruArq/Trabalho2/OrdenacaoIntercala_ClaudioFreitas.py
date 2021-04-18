'''
 Criado por Claudio Freitas
 Execucao do codigo de ser feita por linha de comando
 Programa iniciado na funcao "main()"
 Chamada: OrdenacaoIntercala_ClaudioFreitas.py
 Funcoes (por ordem cima-baixo em que aparecem):
 key_func(linha); juntar_ordenar(rodada, arquivo_rodada, arquivo1, arquivo2); escreve_novos_arquivos(qtd_rodada, rodada);
 escreve_novos_arquivos(qtd_rodada, rodada); separa_arquivos(); main()
'''
# Utilizada pela funcao SORTED para retornar a chave de ordenacao
# Parametros - linha: linha do arquivo
def key_func(linha):
    return linha[-10:-3]

# Juncao dos arquivos separados conforma a instrucao do exercicio
# Parametros - rodada: numero de uma das 4 rodadas necessarias para separar/juntar os arquivos
#              arquivo_rodada: numero do arquivo para aquela rodada
#              arquivo1: primeiro arquivo para juncao
#              arquivo2: segundo arquivo para juncao
def juntar_ordenar(rodada, arquivo_rodada, arquivo1, arquivo2):
    f1 = open(arquivo1, "r")
    f2 = open(arquivo2, "r")

    novo_arquivo = 'rodada_'+str(rodada)+'_ordenado_'+str(arquivo_rodada)+'.dat'
    arquivo = open(novo_arquivo, "w")
    while True:
        linha = f1.readline()
        if linha == "":
            break
        else:
            arquivo.write(linha)
    linha = ""
    while True:
        linha = f2.readline()
        if linha == "":
            break
        else:
            arquivo.write(linha)
    f1.close()
    f2.close()

# Criar os 16 arquivos da primeira rodada que separa o arquivo principal e depois os arquivos das demais rodadas
# Parametros - qtd_rodada: quantidad de arquivos para aquela rodada
#              rodada: numero de uma das 4 rodadas necessarias para separar/juntar os arquivos
def escreve_novos_arquivos(qtd_rodada, rodada):
    count = 1
    arq1 = 1
    arq2 = 1
    if rodada != 1:
        nome_arquivo = 'rodada_'+str(rodada-1)+'_ordenado_{}.dat'
    else:
        nome_arquivo = 'ordenado_{}.dat'
    while count <= qtd_rodada:
        juntar_ordenar(rodada, count, nome_arquivo.format(arq1), nome_arquivo.format(arq2*2))
        count += 1
        arq1  += 2
        arq2  += 1

# Separa o arquivo principal nas 16 partes ja ordenado
# Sem parametros
def separa_arquivos():
    arquios_menores = None
    f = open("cep.dat", "rb")
    num_linhas = sum(1 for line in f)
    linhas_por_arq = num_linhas // 16
    count = 0
    print(num_linhas)
    f.close()
    linha_ordenar = list()

    with open('cep.dat') as bigfile:
        for num_da_linha, linha in enumerate(bigfile):
            if num_da_linha % linhas_por_arq == 0:
                if arquios_menores:
                    '''ORDENAR'''
                    linha_ordenar = sorted(linha_ordenar, key = key_func) # ORDENAR
                    '''ORDENAR'''
                    for l in linha_ordenar:
                        arquios_menores.write(l)
                    linha_ordenar.clear()
                    arquios_menores.close()

                nom_arq_dividido = 'ordenado_{}.dat'.format(count+1)
                arquios_menores = open(nom_arq_dividido, "w")
                count = count + 1
            linha_ordenar.append(linha)
        if arquios_menores:
            arquios_menores.close()

# Funcao que desenvolve toda a aplicacao
# Chamada das funcoes separa_arquivos() e escreve_novos_arquivos(qtd_rodada, rodada)
def main():
    separa_arquivos()
    escreve_novos_arquivos(8, 1)
    escreve_novos_arquivos(4, 2)
    escreve_novos_arquivos(2, 3)
    escreve_novos_arquivos(1, 4)

# Inicio do programa
if __name__ == "__main__":
    main()


