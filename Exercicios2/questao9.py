# Peca ao usuario para inserir um ano e determine se esse ano e bissexto ou nao. Um ano e bissexto
# se for divisıvel por 4, mas n˜ao divisıvel por 100, a menos que tambem seja divisıvel por 400.

print("## TESTE DE ANO BISSEXTO ##")
print(" ")

ano_verificar = int(input('Informe o ano a ser verificado: '))
if (ano_verificar % 4 == 0 and ano_verificar % 100 != 0) or (ano_verificar%400==0):
    print('Bissexto')
else:
    print('Não é bissexto')