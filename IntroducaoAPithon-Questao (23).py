
#23
print(" Você foi contratado por uma agência bancária emergente no mercado brasileiro para escrever uma parte do algoritmo de saque dos caixas eletrônicos dela. Sua tarefa é escrever a parte do algoritmo que recebe um valor e conta quantas notas de 100, 50, 20, 10 e 5 devem ser entregues ao cliente pelo caixa eletrônico. O caixa eletrônico sempre deve entregar a menor quantidade de notas possíveis, por exemplo, se o saque for de 100 reais deve ser entregue uma nota de 100 e não duas de 50. Além disso, sempre serão digitados para saques valores possíveis de serem retirados com esse conjunto de notas, você não precisa fazer essa validação, ela será responsabilidade de outra pessoa. Veja um possível exemplo abaixo quando o cliente quer sacar o valor de 595 reais: \n")

n23um = int(input("Digite o valor da conta: "))
r23esul1 = n23um // 100
n23um = n23um % 100
print(f"Notas de 100: {r23esul1}")
r23esul2 = n23um // 50
n23um = n23um % 50
print(f"Notas de 050: {r23esul2}")
r23esul3 = n23um // 20
n23um = n23um % 20
print(f"Notas de 020: {r23esul3}")
r23esul4 = n23um // 10
n23um = n23um % 10
print(f"Notas de 010: {r23esul4}")
r23esul5 = n23um // 5
print(f"Notas de 005: {r23esul5}")
