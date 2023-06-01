
#16
print(" Faça um programa que receba o valor dos catetos de um triângulo retângulo, calcule e mostre o valor da hipotenusa. Sabe-se que h = √ a² +  b² sendo h a hipotenusa, a e b os catetos do triângulo.\n")

n16um = float (input("digite o valor de 'a': "))
n16um1 = float (input("digite o valor de 'b': "))
c16alc = ((n16um ** 2) + (n16um1 ** 2)) ** 0.5 # Quando elevamos um número a 0.5, estamos efetivamente calculando a raiz quadrada desse número.
print(f"O valor da hipotenusa é: {c16alc} \n \n")
