
#8
print("8 - Um banco concederá um crédito especial aos seus clientes, de acordo com o saldo médio do último ano. Faça um programa que receba o saldo médio de um cliente e calcule o valor do crédito, de acordo com a tabela a seguir. Mostre o saldo médio e o valor do crédito. \n \n")

s8ald = float(input("Digite o salario: "))

if s8ald > 400:
  c8red = s8ald + s8ald * (30/100)
  print(f"Seu credito ficou de R${c8red}")
elif s8ald < 400 and s8ald >  300:
  c8red = s8ald + s8ald * (25/100)
  print(f"Seu credito ficou de R${c8red}")
elif s8ald < 300 and s8ald >  200:
  c8red = s8ald + s8ald * (20/100)
  print(f"Seu credito ficou de R${c8red}")
elif s8ald <= 200:
  c8red = s8ald + s8ald * (10/100)
  print(f"Seu credito ficou de R${c8red}")
else:
  print("Valor acima da margem para reajuste \n \n")
