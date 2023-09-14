# Crie um programa que permita ao usuario calcular juros simples. Peca ao usuario para inserir o
# valor principal, a taxa de juros anual e o perıodo de tempo em anos. Calcule e exiba o valor total
# apos o perıodo especificado.


valor = float(input("Informe o valor inicial R$:"))
taxa  = float(input("Informe a taxa anual a ser aplicada de 0 % a 100% :"))
tempo = float(input("Informe o tempo em anos:"))

juros_simples = valor * (taxa / 100) * tempo

print("O valor final é de", juros_simples)