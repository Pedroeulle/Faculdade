
#6
print("6 - Uma empresa decide dar um aumento de 30% aos funcionários com salários inferiores a R$ 500,00. Faça um programa que receba o salário do funcionário e mostre o valor do salário reajustado ou uma mensagem caso ele não tenha direito ao aumento. \n \n")

s6alari = float(input("Digite o salario: "))

if s6alari <= 500:
  s6alariR = s6alari + s6alari * (30/100)
  print(f"Seu salario agora é de R${s6alariR}")
else:
  print("Valor acima da margem para reajuste \n \n")
