
#9
print("9 - Faça um programa que receba o preço de um produto, calcule e mostre, de acordo com as tabelas a seguir, o novo preço e a classificação do produto considerando o novo preço. \n \n")

v9alor = float(input("Digite o preço do produto: "))

if v9alor <= 50:
    a9lmen = v9alor + v9alor * (5/100)
    print(f"Novo preço: R${a9lmen}")
elif v9alor > 50 and v9alor < 100:
    a9lmen = v9alor + v9alor * (10/100)
    print(f"Novo preço: R${a9lmen}")
elif v9alor >= 100:
    a9lmen = v9alor + v9alor * (15/100)
    print(f"Novo preço: R${a9lmen}")
if v9alor <= 80:
  print("Barato")
elif v9alor > 80 and v9alor <= 120:
  print("Normal")
elif v9alor > 120 and v9alor <= 200:
  print("Caro")
elif v9alor > 200:
  print("Muito caro")
else:
    print("Valor inválido para reajuste. \n \n")