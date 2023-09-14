# Peca ao usuario para inserir um numero e, em seguida, determine se o numero e par ou ımpar.
# Exiba uma mensagem correspondente.

print("## PAR OU IMPAR ##")
print(" ")

numero = input("Informe o numero(inteiro): ")
while not numero.isnumeric():
    print("O numero deve ser inteiro e sem pontos. Tente novamente.")
    numero = input("Informe novamente o numero: ")
numero = int(numero)

if numero % 2 == 0:
    print('eh par')
else:
    print("Eh impar")