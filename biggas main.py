import random
from time import sleep

jogar = input("deseja jogar?(sim / não)")
jogar = jogar.lower()
inimigos = []
life_player = 300
dano = 10

if (jogar == "sim"):
    print("vamos acabar com sua raça")
    inimigos_quant = random.randint(3,9)
    print("você terá que enfrentar {0} jottass, você se fudeu".format(inimigos_quant))

    for i in range(1, inimigos_quant + 1):
        inimigos.append([i,30])

    arma = int(input("escolha sua arma: Espada do Rei(1), Maça de Guerra(2), bastão necessariamente grande(3)"))
    sleep(1)

    escolha = int(input("agora escolha sua ação: atacar(1), curar(2)"))

    if (escolha == 1):
        player_atk = random.randint(1,3)

    if (player_atk >= 1):
        selecionado = random.choice(inimigos)
        selecionado[1] -= dano
        print("o inimigo {0} tem {0} de vida e sofreu 10 de dano".format(selecionado[0], selecionado[1]))

    else:
        print("voce errouuu")
