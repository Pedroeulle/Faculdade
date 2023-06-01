#4
print(" 4 - Faça um programa que receba dois inteiros, armazene o primeiro em uma variável chamada a e o segundo em uma variável chamada b. Depois troque o valor das variáveis, ou seja, a deverá ter o valor de b e vice-versa. Imprima a e b para mostrar que a troca foi realmente feita.\n")

A = int(input("Digite um numero inteiro: "))
B = int(input("Digite um numero inteiro: "))
print("Valor de A: ", A ,"Valor de B: ", B)
A1 = A ; B1 = B
A = B1 ; B = A1
print("Valor de A: ", A ,"Valor de B: ", B ,"\n \n")
