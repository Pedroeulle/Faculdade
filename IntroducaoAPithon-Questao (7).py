#7
print(" 7 - Um funcionário recebe um salário fixo mais 4% de comissão sobre vendas. Faça um programaque receba o salário fixo do funcionário e o valor de suas vendas, calcule e mostre o valor da comissão e do seu salário final. \n")

N7um = float(input("digite seu salario: "))
Vend = float(input("digite o total em vendas: "))
Comiss = Vend * (4/100)
SalF = N7um + Comiss
print(f"O Salario final do funcionario é {SalF} \n \n")