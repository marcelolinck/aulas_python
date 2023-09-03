# idade = 17

# if idade >= 18:
#     print (" Voce e maior de idade.")
# else:
#     print (" Voce e menor de idade.")


# nota = 91

# if nota >= 90:
#     print (" Voce tirou uma nota A.")
# elif nota >= 80:
#     print (" Voce tirou uma nota B.")
# elif nota >= 70:
#     print (" Voce tirou uma nota C.")
# else :
#     print (" Voce nao passou no exame .")



##### TRABALHANDO COM FOR #####

# frutas = [" maca ", " banana ", " laranja "]

# for fruta in frutas :
#     print ( fruta )


##### TRABALHANDO COM WHILE #####

# contador = 0

# while contador < 5:
#     print(f"Contagem :{ contador}")
#     # TEM QUE CUIDAR DA INDENTACAO
#     contador += 1


##### TRABALHANDO COM FOR E IF COLOCANDO CONDIÇÃO PARA EXECUTAR UM NUMERO #####
# numeros = [1 , 2, 3, 4, 5, 6]
# for numero in numeros :
#     if numero == 4:
#        break   
#     print ( numero )


numeros = [1 , 2, 3, 4, 5,6,7,8,9,10,11]
for numero in numeros :
    if numero % 2 == 0:
        continue
    print ( numero )
