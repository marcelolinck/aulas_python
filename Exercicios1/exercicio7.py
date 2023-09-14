# Crie uma variavel para armazenar o nome de uma cidade. Use essa variavel para criar uma mensagem formatada como ?Bem-vindo a cidade de [nome da cidade]!?


print("## MINHA CIDADE PREFERIDA ##")

cidade = input("Informe o nome da cidade: ")

while not all(caractere.isalpha() or caractere.isspace() for caractere in cidade):
    
    print("O nome da cidade deve conter somente letras.")
    cidade = input("Informe novamente o nome da cidade: ")

print ("Bem vindo a cidade de ", cidade)