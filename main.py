import random

# Tamanho do campo de batalha
largura = 20
altura = 10

# Posições iniciais dos tanques
tanque1_x = random.randint(0, largura // 2)
tanque1_y = random.randint(0, altura)
tanque2_x = random.randint(largura // 2, largura - 1)
tanque2_y = random.randint(0, altura)


# Função para desenhar o campo de batalha
def desenhar_campo():
    for y in range(altura):
        for x in range(largura):
            if x == tanque1_x and y == tanque1_y:
                print("T1", end='')
            elif x == tanque2_x and y == tanque2_y:
                print("T2", end='')
            else:
                print(".", end='')
        print()


# Loop principal do jogo
while True:
    desenhar_campo()

    # Obter ação do jogador 1
    acao1 = input("Jogador 1 - Escolha uma ação (w, a, s, d): ")
    if acao1 == "w":
        tanque1_y -= 1
    elif acao1 == "s":
        tanque1_y += 1
    elif acao1 == "a":
        tanque1_x -= 1
    elif acao1 == "d":
        tanque1_x += 1

    # Obter ação do jogador 2
    acao2 = input("Jogador 2 - Escolha uma ação (w, a, s, d): ")
    if acao2 == "w":
        tanque2_y -= 1
    elif acao2 == "s":
        tanque2_y += 1
    elif acao2 == "a":
        tanque2_x -= 1
    elif acao2 == "d":
        tanque2_x += 1

    # Verificar colisões e condições de vitória

