
#2
print("2 -Faça um programa que receba duas notas, calcule e mostre a média aritmética e uma mensagem de acordo com o que se encontra na tabela abaixo: \n \n")

n2ota1 = float(input("Digite uma nota: \n"))
n2ota2 = float(input("Digite uma nota: \n"))
m2edia = (n2ota1 + n2ota2) / 2

if m2edia >= 7 and m2edia < 10:
  print("aluno aprovado!")
elif m2edia > 4 and m2edia < 7:
  print("Aluno na prova final! ")
elif m2edia < 4:
  print("Aluno reprovado!")
else:
  print("Valor invalido! \n \n")
