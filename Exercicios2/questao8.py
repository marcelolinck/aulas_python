# Crie um programa que peca ao usuario para inserir cinco numeros em uma lista. Em seguida,
# calcule a soma e a media desses numeros e exiba os resultados.

# Criando uma lista vazia
lista = []
total = 0
contador = 0
# Adicionando números à lista usando append()
while contador < 5:
    valor = input("Informe o valor: ")
    lista.append(float(valor))
    contador += 1    
    total += float(valor)
    
print("Media: ", contador)
print("Os numeros digitados sao: ", lista)
print("O total é: ", total)