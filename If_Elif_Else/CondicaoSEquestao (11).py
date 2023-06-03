
#11
print("11 - Faça um programa que receba o código de origem de um produto e mostre sua procedência. A procedência obedece à tabela a seguir: \n \n")

p11rod = float(input("Digite o codigo do produto: "))

if p11rod == 1:
  print("Produto do Sul")
elif p11rod == 2:
  print("Produto do Norte")
elif p11rod == 3:
  print("Produto do Leste")
elif p11rod == 4:
  print("Produto do Oeste")
elif p11rod == 5 or p11rod == 6 or p11rod >= 21 and p11rod <= 30:
  print("Produto do Nordeste")
elif p11rod == 7 or p11rod == 8 or p11rod == 9:
  print("Produto do Sudeste")
elif p11rod >= 10 and p11rod <= 20:
  print("Produto do Centro-Oeste")
else:
  print("Valor invalido \n \n")
