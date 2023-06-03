#1
print("1 - Faça um programa que receba quatro notas de um aluno, calcule e mostre a média aritmética das notas e a mensagem de aprovado ou reprovado, considerando para aprovação média maior ou igual a 7: \n \n")

n1ota1 = float(input("Digite uma nota: \n"))
n1ota2 = float(input("Digite uma nota: \n"))
n1ota3 = float(input("Digite uma nota: \n"))
n4ota4 = float(input("Digite uma nota: \n"))
m1edia = (n1ota1 + n1ota2 + n1ota3 + n4ota4) / 4
if m1edia >= 7 :
  print("aluno aprovado")
else:
  print("Aluno reprovado \n \n")
