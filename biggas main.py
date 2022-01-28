import random
from time import sleep

jogar = input("deseja jogar?(sim / não)")
jogar = jogar.lower()
inimigos = []
life_player = 300
dano = 10
jogando = True

if (jogar == "sim"):

    while jogando:

        inimigos_quant = random.randint(3,5)

        print("vamos acabar com sua raça")
        sleep(1)
        print("você terá que enfrentar {0} jottas, você se fudeu".format(inimigos_quant))

        for i in range(1, inimigos_quant + 1):
            inimigos.append([i,30])

        arma = int(input("escolha sua arma: Espada do Rei(1), Maça de Guerra(2), bastão necessariamente grande(3)"))
        sleep(1)
        
        batalhando = True

        while batalhando:

            ##jogada jogador
            escolha = int(input("agora escolha sua ação: atacar(1), curar(2)"))
            sleep(0.9)

            if (escolha == 1):
                player_atk = random.randint(1,3)

            if (player_atk >= 3):
                selecionado = random.choice(inimigos)
                selecionado[1] -= dano
                print("o inimigo", selecionado[0], "tem", selecionado[1], "de vida e sofreu 10 de dano")
                sleep(1.25)

                elogio = random.randint(1,3)
                if (elogio == 1):
                    print("bom golpe de", arma)
                elif (elogio == 2):
                    print("você possui maestria de", arma)
                elif (elogio == 3):
                    print ("me ensine a usar", arma, "dessa forma")

            else:
                print("voce errou o ataque, se concentre mais na próxima")

            ###ataque inimigo
            inimigo_atacante = random.choice(inimigos_quant)
            inimigo_dano = random.randint(14,20)
            print:("você sofreu", inimigo_dano, "de dano, o jottas te atacou")
            


