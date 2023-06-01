
#15
print(" João recebeu seu salário e precisa pagar duas contas atrasadas. Por causa do atraso, ele deveria pagar multa de 2% sobre o valor original de cada conta. Faça um programa que receba o salário de João e o valor original de cada uma das contas, calcule e mostre quanto restará do salário de João após pagar as duas contas. \n")

sal15 = float (input("digite o salario: \n"))
n15um = float(input("digite o valor da primeira conta : \n"))
n15um1 = float(input("digite o valor da conta da segunda conta: \n"))
c15alc = n15um + (n15um * 2/100)
c15alc1 = n15um1 + (n15um1 * 2/100)
R15esul = sal15 - (c15alc + c15alc1)
print(f"Salario apos pagamento de dividas sera de: R${R15esul} \n \n")
