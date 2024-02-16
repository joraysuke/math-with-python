coluna = int(input('Insira o numero de colunas: '))
linha = int(input('Insira o numero de linhas: '))

matriz= []

for i in range(coluna, linha):
    all = coluna, linha
    matriz.append(all)

print(matriz)
