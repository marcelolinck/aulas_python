# Crie um programa que solicite ao usuario tres notas e calcule a media. Com base na media, informe
# se o aluno foi aprovado ou reprovado (considerando a media 7 como criterio de aprovacao).

print("## CALCULO DE MEDIA ##")
print(" ")

contador = 0
nota = 0
acumulador = 0
while contador < 3:
    nota = input(f" Informe a nota { contador + 1 }: ")
    
    while not nota.isnumeric():
        print("A sua nota deve ser de numeros. Tente novamente.")
        nota = input(f" Informe novamente a nota { contador + 1 }: ")
    
    acumulador += float(nota)
    contador += 1
    
media = acumulador / contador

print("A sua nota final eh ", round(media,2))

if media > 7 :
    print("Voce foi Aprovado")
else:
    print("Voce foi Reprovado")
