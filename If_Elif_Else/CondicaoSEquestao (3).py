
#3
print("3 - Faça um programa que receba dois números e mostre o menor e o maior. \n \n")

n3ume1 = float(input("Digite um numero: \n"))
n3ume2 = float(input("Digite um numero: \n"))

if n3ume1> n3ume2:
  print(f" {n3ume1} (primeiro) numero maior \n")
elif n3ume2> n3ume1:
  print(f"{n3ume2} (segundo) numero maior \n")
else:
  print("Valor invalido \n \n")
