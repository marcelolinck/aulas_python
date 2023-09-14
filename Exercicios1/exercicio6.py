# Peca ao usuario para inserir seu nome e sobrenome separados por espaco. Concatene-os em uma unica string e imprima.

print("## SEU CADASTRO AQUI ##")

nomeSobrenome = input("Informe seu nome e sobre nome: ")
tudoJunto = nomeSobrenome.replace(" ", "")
print("Retirando espacos fica dessa forma", tudoJunto)