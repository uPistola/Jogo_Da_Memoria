#Arthur Neumann Salerno, João Gabriel Pitol e Rafael Munhoz da Cunha Marques
import random
import time
def printa_matriz(matriz):
    print("")
    for m in range(0, len(matriz)):
        print("    %d" % (m), end="")
    print("")
    for i in range(0, len(matriz)):
        print('%d: %s' % (i, matriz[i]))
    print("")
def popula_matriz(valor, tamanho):
    matriz = []
    for i in range(0, tamanho):
        matriz.append([])
        for j in range(0, tamanho):
            matriz[i].append(valor)
    return matriz
def matriz_cont(matriz, valor):
    cont = 0
    for i in matriz:
        for j in i:
            if j == valor:
                cont += 1
    return cont
def matriz_shuffle(matriz, max_coluna, max_linha):
    copia_matriz = matriz
    # Popula a nova matriz com 0
    nova_matriz = popula_matriz(0, max_linha)
    # Para cada valor na matriz é sorteado uma nova posição na nova matriz
    for linha in copia_matriz:
        for coluna in linha:
            nova_coluna = random.randint(0, max_coluna - 1)
            nova_linha = random.randint(0, max_linha - 1)
            while nova_matriz[nova_linha][nova_coluna] != 0:
                nova_coluna = random.randint(0, max_coluna - 1)
                nova_linha = random.randint(0, max_linha - 1)
            nova_matriz[nova_linha][nova_coluna] = coluna
    return nova_matriz
# Cria o alfabeto
letras = []
for i in range(65, 91):
    letras.append(chr(i))
print('1.Fácil\n2.Médio\n3.Difícil')
dificuldade = int(input('Dificuldade: '))
if dificuldade == 1:
    tamanho = 4
elif dificuldade == 2:
    tamanho = 6
elif dificuldade == 3:
    tamanho = 10
# Popula uma matriz com todas as duplas de letras.
matriz_populada = []
letra_atual = letras[0]
cont = 0
for i in range(0, tamanho):
    matriz_populada.append([])
    for j in range(0, tamanho):
        matriz_populada[i].append(letra_atual)
        if cont == 1:
            cont = 0
            letra_atual = letras[random.randint(0, len(letras) - 1)]
        else:
            cont += 1
# Cria a matriz do jogo, aleatorizando as posições
matriz_aleatorizada = matriz_shuffle(matriz_populada, tamanho, tamanho)
# Popula uma matriz com (#)
matriz_escondida = popula_matriz('#', tamanho)
poder_cont = 2
jogando = 1
while jogando == 1:
    printa_matriz(matriz_escondida)
    opcao = int(input("1.Usar poder %d/2\n2.Desistir\n3.Escolher" % (poder_cont)))
    if opcao == 1:
        if 0 < poder_cont <= 2:
            printa_matriz(matriz_aleatorizada)
            poder_cont -= 1
            time.sleep(3)
        else:
            print("Seus poderes acabaram!!!")
    elif opcao == 2:
        print("Voce Desistiu do jogo!!!")
        jogando = 0
    else:
        # Escolhe linha e coluna e mostra o primeiro valor
        linha = int(input("Digite a linha: "))
        coluna = int(input("Digite a coluna: "))
        matriz_escondida[linha][coluna] = matriz_aleatorizada[linha][coluna]
        printa_matriz(matriz_escondida)
        # Escolhe linha e coluna e mostra o segundo valor
        linha2 = int(input("Digite a linha: "))
        coluna2 = int(input("Digite a coluna: "))
        matriz_escondida[linha2][coluna2] = matriz_aleatorizada[linha2][coluna2]
        printa_matriz(matriz_escondida)
        # Se os valores não batem, as "cartas" são escondidas
        if matriz_escondida[linha][coluna] != matriz_escondida[linha2][coluna2]:
            matriz_escondida[linha][coluna] = '#'
            matriz_escondida[linha2][coluna2] = '#'
        elif matriz_cont(matriz_escondida, '#') == 0:
            print("Você venceu o jogo!")
            jogando = 0