# Crie um programa que permita ao usuario converter temperaturas de Celsius para Fahrenheit. A
# formula utilizada deve ser: (temp celsius * 9 / 5) + 32

def is_float(string):
    try:
        float(string)
        return True
    except ValueError:
        return False

print("## CONVERSAO DE TEMPERATURA DE CELSIUS PARA  FAHRENHEIT ##")

tc = input("Digite a temperatura em º Celsius: ")

while not is_float(tc):
        print("Por favor, digite uma temperatura válida com numeros.")
        tc = input("Digite a temperatura novamente: ")
conversaoParaFr = ((float(tc) * 9) / 5) + 32

print("A temperatura de",tc,"ºC convertida para",conversaoParaFr,"ºF")