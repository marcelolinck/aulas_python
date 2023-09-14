# 1. Crie duas variáveis: nome e idade. Atribua seu nome a nome e sua idade a idade. Imprima uma
# mensagem usando essas vari´aveis.

print ("### Informacoes de ###")

nome = input ("Informe o seu nome: ")
idade = input("Informe a sua idade: ")

while not idade.isnumeric():
    print("A sua idade deve ser de numeros inteiros e sem pontos. Tente novamente.")
    idade = input("Informe novamente a sua idade: ")

idade = int(idade)

print("Meu nome eh",nome ,"e minha idade eh ", idade,".")