
#22
print(" Faça um programa que receba um horário qualquer (use uma variável para a hora e outra para os minutos), calcule e mostre: \n")

n21um = int(input("Digite a hora:  "))
n21um1 = int(input("Digite os minutos: "))

print("\na) Somente a variável da hora convertida em minutos; \n ")

r21sul = n21um * 60
print(f"Hora convertida em minutos: {r21sul}min \n")

print("b) O total dos minutos, ou seja, os minutos digitados mais a soma da conversão anterior; \n")

r21sul1 = r21sul + n21um1
print(f"total dos minutos (os minutos digitados mais a soma da conversão anterior): {r21sul1}min \n")

print("c) O total dos minutos convertidos em segundos. \n")

r21sul2 = r21sul1 * 60
print(f"O total dos minutos convertidos em segundos (Totalidade): {r21sul2}seg \n")

r21sul3 = n21um1 * 60
print(f"O total dos minutos convertidos em segundos (Numero inicial) {r21sul3}seg \n \n")
