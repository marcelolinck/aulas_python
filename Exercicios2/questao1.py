# Crie um programa que permita ao usuario realizar operacoes de adicao, subtracao, multiplicacao e
# divisao com dois numeros. Peca ao usuario para escolher a operacao desejada e exiba o resultado.


print ("### Calculadora ###")

numero1 = float(input ("Informe o numero: "))
operador = (input ("Escolha a Operação: (+ - * /): "))
numero2 = float(input ("Informe o 2 numero: "))

if  operador == '+': 
   resultado = numero1 + numero2
elif operador == '-': 
    resultado = numero1 - numero2
elif operador == '*': 
    resultado = numero1 * numero2
else:
    resultado = numero1 / numero2

    
print(resultado)