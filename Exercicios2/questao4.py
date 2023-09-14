# Peca ao usuario para inserir um numero e, em seguida, mostre a tabuada desse numero de 1 a 10.

print("## CALCULO DE TABUADA ##")
print(" ")

numero = input("Informe o numero a ser multiplicado: ")

while not numero.isnumeric():
        print("O numero deve ser de numeros inteiros. Tente novamente.")
        numero = input("Digite novamente o numero: ")
numero = int(numero)

contador = 0
print(" ")
print("Segue a tabuada")
while contador <= 10:
    print(numero, '*', contador,'=', numero * contador)
    contador += 1