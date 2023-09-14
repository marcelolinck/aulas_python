# Crie um jogo em que o programa escolha um numero aleatorio entre 1 e 100, e o usuario deve
# adivinhar qual e o numero. Dˆe dicas ao usuario sobre se o numero e maior ou menor ate que ele
# acerte.
import random

##Para nao ficar repentindo codigo, criei essa funcao junto
def obter_numero_inteiro():
    while True:
        numero = input("Informe um número inteiro: ")
        if numero.isnumeric():
            return int(numero)
        else:
            print("O número deve ser inteiro e sem pontos. Tente novamente.")

print("## ADIVINHE O NUMERO DE 1 A 100 ##")
print(" ")
acertou = False
numero_aleatorio = random.randint(1, 100)

numero_escolhido = obter_numero_inteiro()

acertou = False

while acertou == False:
    if numero_escolhido > numero_aleatorio: 
        print("O numero deve ser menor")
        numero_escolhido = obter_numero_inteiro()        
    elif numero_escolhido < numero_aleatorio:
        print("O numero deve ser maior")
        numero_escolhido = obter_numero_inteiro()
    else:
        print("Acertou")
        acertou = True
        
        
print("Fim")   