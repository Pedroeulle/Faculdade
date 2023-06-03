
#10
print("10 - Faça um programa que receba a altura (h) em metros e o sexo de uma pessoa (M ou F) e mostre seu peso ideal, usando as fórmulas (72.7⋅h)−58 para homens e (62.1⋅h)−44.7 para mulheres. \n \n")

a10ltura = float(input("digite sua altura (Ex.. 1.97): "))
s10exo = str(input("digite seu sexo (Ex...'M' ou 'F'): "))

if s10exo == 'F':
  P10esoI = a10ltura - 44;7
  print(f"O peso ideial é:{P10esoI}")
elif s10exo == 'M':
  P10esoI = a10ltura - 58
  print(f"O peso ideial é:{P10esoI}Kg")
else:
  print("dado invalido \n \n")
