from time import sleep


def soma(x,y):
    print(x+y)

def media(x,y,z,k):
    mediana = round(((x+y+z+k)/4), 3)
    print("calculando media....")
    sleep(0.5)
    print(mediana)

def conversor_metro():
    print("""
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Escolha a unidade atual e depois desejada:
    
    -milimetro(1)
    -centimetro(2)
    -decimetro(3)
    -metro(4)
    -decametro(5)
    -hectometro(6)
    -kilometro(7)
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    """)
    unidade_inicial = int(input("-> "))
    unidade_final = int(input("-> "))
    sleep(1)
    print("""
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            codando codando e codando
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        """)
    sleep(1)
    print("""
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        Agora escreva o número desejado:
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    """)
    n = float(input("-> "))

    if unidade_inicial == 1:
        if unidade_final == 2:
            x = (n / 10)
            print("{}mm são {}cm".format(n, x))
        elif unidade_final == 3:
            x = (n / 100)
            print("{}mm são {}dm".format(n, x))
        elif unidade_final == 4:
            x = (n / 1000)
            print("{}mm são {}m".format(n, x))
        elif unidade_final == 5:
            x = (n / 10000)
            print("{}mm são {}dam".format(n, x))
        elif unidade_final == 6:
            x = (n / 100000)
            print("{}mm são {}hm".format(n, x))
        elif unidade_final == 7:
            x = (n / 1000000)
            print("{}mm são {}km".format(n, x))
        else:
            print("é impossivel transformar milimetros em milimetros")
    ##milimetros##
    elif unidade_inicial == 2:
        if unidade_final == 1:
            x = (n * 10)
            print("{}cm são {}mm".format(n, x))
        elif unidade_final == 3:
            x = (n / 10)
            print("{}cm são {}dm".format(n, x))
        elif unidade_final == 4:
            x = (n / 100)
            print("{}cm são {}m".format(n, x))
        elif unidade_final == 5:
            x = (n / 1000)
            print("{}cm são {}dam".format(n, x))
        elif unidade_final == 6:
            x = (n / 10000)
            print("{}cm são {}hm".format(n, x))
        elif unidade_final == 7:
            x = (n / 100000)
            print("{}cm são {}km".format(n, x))
        else:
            print("é impossivel transformar centimetros em centimetros")
    ##centimetros##
    elif unidade_inicial == 3:
        if unidade_final == 1:
            x = (n * 100)
            print("{}dm são {}mm".format(n, x))
        elif unidade_final == 2:
            x = (n * 10)
            print("{}dm são {}cm".format(n, x))
        elif unidade_final == 4:
            x = (n / 10)
            print("{}dm são {}m".format(n, x))
        elif unidade_final == 5:
            x = (n / 100)
            print("{}dm são {}dam".format(n, x))
        elif unidade_final == 6:
            x = (n / 1000)
            print("{}dm são {}hm".format(n, x))
        elif unidade_final == 7:
            x = (n / 10000)
            print("{}dm são {}km".format(n, x))
        else:
            print("é impossivel transformar decimetros em decimetros")
    ##metros##
    elif unidade_inicial == 4:
        if unidade_final == 1:
            x = (n * 1000)
            print("{}m são {}mm".format(n, x))
        elif unidade_final == 2:
            x = (n * 100)
            print("{}m são {}cm".format(n, x))
        elif unidade_final == 3:
            x = (n * 10)
            print("{}m são {}dm".format(n, x))
        elif unidade_final == 5:
            x = (n / 10)
            print("{}m são {}dam".format(n, x))
        elif unidade_final == 6:
            x = (n / 100)
            print("{}m são {}hm".format(n, x))
        elif unidade_final == 7:
            x = (n / 1000)
            print("{}m são {}km".format(n, x))
        else:
            print("é impossivel transformar metros em metros")
    ##decametros##
    elif unidade_inicial == 5:
        if unidade_final == 1:
            x = (n * 10000)
            print("{}dam são {}mm".format(n, x))
        elif unidade_final == 2:
            x = (n * 1000)
            print("{}dam são {}cm".format(n, x))
        elif unidade_final == 3:
            x = (n * 100)
            print("{}dam são {}dm".format(n, x))
        elif unidade_final == 4:
            x = (n * 10)
            print("{}dam são {}m".format(n, x))
        elif unidade_final == 6:
            x = (n / 10)
            print("{}dam são {}hm".format(n, x))
        elif unidade_final == 7:
            x = (n / 100)
            print("{}dam são {}km".format(n, x))
        else:
            print("é impossivel transformar decametros em decametros")
    ##hectometros##
    elif unidade_inicial == 6:
        if unidade_final == 1:
            x = (n * 100000)
            print("{}hm são {}mm".format(n, x))
        elif unidade_final == 2:
            x = (n * 10000)
            print("{}hm são {}cm".format(n, x))
        elif unidade_final == 3:
            x = (n * 1000)
            print("{}hm são {}dm".format(n, x))
        elif unidade_final == 4:
            x = (n * 100)
            print("{}hm são {}m".format(n, x))
        elif unidade_final == 5:
            x = (n * 10)
            print("{}hm são {}dam".format(n, x))
        elif unidade_final == 7:
            x = (n / 10)
            print("{}hm são {}km".format(n, x))
        else:
            print("é impossivel transformar hectometros em hectometros")
    ##kilometros##
    elif unidade_inicial == 7:
        if unidade_final == 1:
            x = (n * 1000000)
            print("{}km são {}mm".format(n, x))
        elif unidade_final == 2:
            x = (n * 100000)
            print("{}km são {}cm".format(n, x))
        elif unidade_final == 3:
            x = (n * 10000)
            print("{}km são {}dm".format(n, x))
        elif unidade_final == 4:
            x = (n * 1000)
            print("{}km são {}m".format(n, x))
        elif unidade_final == 5:
            x = (n * 100)
            print("{}km são {}dam".format(n, x))
        elif unidade_final == 6:
            x = (n / 10)
            print("{}km são {}hm".format(n, x))
        else:
            print("é impossivel transformar hectometros em hectometros")
    else:
        print("voce não digitou valores validos")

class Circulo:
    def __init__(self, raio):
        self.raio = raio

    def diametro(self):
        self.diametro = (self.raio * 2)
        return self.diametro

    def calculos(self):
        self.area = 3.14 * (self.raio**2)
        self.circunferencia = (self.diametro * 3.14)











escolha = int(input("escolha um exercicio: "))

if escolha == 1:
    print("alo mundo")

elif escolha == 2:
    num_ex2 = float(input("escolha um numero: "))
    print("voce escolheu o numero {}.".format(num_ex2))

elif escolha == 3:
    num1_ex3 = float(input("digite o primeiro numero: "))
    num2_ex3 = float(input("digite o segundo numero: "))
    sleep(0.5)
    print("seu resultado sera...")
    soma(num1_ex3, num2_ex3)

elif escolha == 4:
    ######forma de resolver com função#########
    num1_ex4 = float(input("A primeira nota foi: "))
    num2_ex4 = float(input("A segunda nota foi: "))
    num3_ex4 = float(input("A terceira nota foi: "))
    num4_ex4 = float(input("A quarta nota foi: "))

    media(num1_ex4, num2_ex4, num3_ex4, num4_ex4)

    ######Forma de resolver sem funções#######
    ##resultado = 0
    ##for i in range(1,5):
        ##nota = float(input("digite a nota {}: ".format(i)))
        ##resultado += nota

    ##media = (resultado//4)
    ##print("calculando media....")
    ##sleep(0.5)
    ##print("A média será: {}".format(media))

elif escolha == 5:
    conversor_metro()


