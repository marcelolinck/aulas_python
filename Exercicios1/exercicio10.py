# Peca ao usuario para inserir sua idade como numero inteiro e sua altura como numero de ponto flutuante. Concatene esses valores em uma string e imprima.
def is_float(string):
    try:
        float(string)
        return True
    except ValueError:
        return False


print("## TESTE DE CONVERSOES ##")
print(" ")

idade = input("Informe a sua idade: ")

while not idade.isnumeric():
    print("A sua idade deve ser de numeros inteiros e sem pontos. Tente novamente.")
    idade = input("Informe novamente a sua idade: ")

idade = int(idade)
        
altura = input("Informe a sua altura: ")

while not is_float(altura):
        print("Por favor, digite uma altura válida como número de ponto flutuante.")
        altura = input("Digite sua altura (número de ponto flutuante): ")

altura = float(altura)
    
print("A sua idade é: ", idade, "e a sua altura é: ", altura)

