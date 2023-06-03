
#4
print("4 - Faça um programa que receba três números e mostre o menor e o maior. \n \n")

n4ume1 = float(input("Digite um numero: "))
n4ume2 = float(input("Digite um numero: "))
n4ume3 = float(input("Digite um numero: "))

if n4ume1> n4ume2 and n4ume1> n4ume3:
  print(f"\n1º numero ({n4ume1}) é o numero maior\n")
elif n4ume2 > n4ume1 and n4ume2 > n4ume3:
  print(f"\n2º numero ({n4ume2}) é o numero maior\n")
elif n4ume3 > n4ume1 and n4ume3 > n4ume2:
  print(f"\n3º numero ({n4ume3}) é o numero maior\n")

if n4ume1 < n4ume2 and n4ume1 < n4ume3:
  print(f"1º numero ({n4ume1}) é o numero menor\n")
elif n4ume2 < n4ume1 and n4ume2 < n4ume3:
  print(f"2º numero ({n4ume2}) é o numero menor\n")
elif n4ume3 < n4ume1 and n4ume3 < n4ume2:
  print(f"3º numero ({n4ume3}) é o numero menor\n")
  
else:
  print("valor invalido \n \n")
