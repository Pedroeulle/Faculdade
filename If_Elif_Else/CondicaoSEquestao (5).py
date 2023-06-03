
#5
print("5 - Faça um programa que receba dois números e execute as operações listadas a seguir, de acordo com a escolha do usuário, mostrando o resultado ao final. Se for digitada uma opção inválida, mostre uma mensagem de erro e termine a execução do programa. \n \n")

n5ume1 = float(input("Digite um numero: "))
n5ume2 = float(input("Digite um numero: "))
#media
m5dia = (n5ume1 + n5ume2) / 2
print(f"media entre os dois numeros é: {m5dia}\n")
#produto
p5rodu = n5ume1 * n5ume2
print(f"Produto entre os números digitados é: {p5rodu}\n")
#divisão
d5vis = n5ume1 / n5ume2
print(f"divisão entre os números digitados é: {d5vis}\n")
#elevado
e5lev = n5ume1 ** n5ume2
print(f"primeiro numero elevado ao segundo é: {e5lev}")
#raiz
r5aiz1 = n5ume1 * 0.5 ; r5aiz2 = n5ume2 * 0.5
print(f"raiz de {n5ume1} é {r5aiz1}\nraiz de {n5ume2} é {r5aiz2}")
#cubica
r5aizc1 = n5ume1 ** (1/3); r5aizc2 = n5ume2 ** (1/3)
print(f"raiz cubica de {n5ume1} é {r5aizc1}\nraiz cubica de {n5ume2} é {r5aizc2}")

if n5ume1 > n5ume2:
  d5ifer = n5ume1 - n5ume2
  print(f"diferença entre({n5ume1}) e {n5ume2} é: {d5ifer}\n")
elif n5ume2 > n5ume1:
  d5ifer = n5ume2 - n5ume1
  print(f"diferença entre({n5ume2}) e {n5ume1} é: {d5ifer}\n")
else:
  print("Os números são iguais. \n \n")
