
#7
print("7 - Faça um programa que receba o salário de um funcionário, calcule e mostre o salário reajustado. O percentual de aumento encontra-se na tabela a seguir. \n \n")

s7alari = float(input("Digite o salario: "))

if s7alari <= 300:
  s7alariR = s7alari + s7alari * (35/100)
  print(f"Seu salario agora é de R${s7alariR}")
elif s6alari > 300:
  s7alariR = s7alari + s7alari * (15/100)
  print(f"Seu salario agora é de R${s7alariR}")
else:
  print("Valor acima da margem para reajuste")
