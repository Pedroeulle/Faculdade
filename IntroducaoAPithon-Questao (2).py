#2
print(" 2-Faça um programa que receba tres numeros reais (a,b,c), calcule e mostre a subtração do primeiro numero pelo segundo e pelo terceiro (a - b - c), a soma dos tres (a + b + c), a multiplicação dos tres (a x b x c) e a divisão dos tres (a / b / c): \n")

N2umA = float(input("digite um numero: "))
N2umB = float(input("digite um numero: "))
N2umC = float(input("digite um numero: "))
Soma = N2umA + N2umB + N2umC
Subtracao = N2umA - N2umB - N2umC
Divisao = N2umA / (N2umB * N2umC)
Multiplicacao = N2umA * N2umB * N2umC
print (f"Os numeros tem como resultado: \n Soma: {Soma :.2f} \n Subtração: { Subtracao  :.2f} \n Multiplicação: {Multiplicacao  :.2f} \n Divisão: {Divisao  :.2f} \n \n")