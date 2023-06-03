
#12
print("12 - Faça um programa que receba o código e a quantidade comprada de um determinado produto.")
print("Calcule e mostre, de acordo com as tabelas a seguir:\n")
print("a) Uma mensagem de erro caso o código digitado seja inválido; ")
print("b) O preço unitário do produto comprado, usando a Tabela I; ")
print("c) O preço total da nota, ou seja, o preço unitário multiplicado pela quantidade do produto; ")
print("d) O valor do desconto em reais. Use a Tabela II aplicando o desconto no preço total da nota; ")
print("e) O preço final da nota depois do desconto.\n")

p12cod = int(input("Digite o código do produto: "))
p12quant = int(input("Digite a quantidade do produto: "))

if p12cod < 1 or p12cod > 40:
    print("Código de produto inválido.")
else:
    if p12cod >= 1 and p12cod <= 10:
        p12preco = 10
    elif p12cod >= 11 and p12cod <= 20:
        p12preco = 15
    elif p12cod >= 21 and p12cod <= 30:
        p12preco = 20
    else:
        p12preco = 30
        
    p12total = p12preco * p12quant
    print(f"Preço unitário: R${p12preco}")
    print(f"Preço total: R${p12total}")
    
    if p12total <= 150:
        p12desc = p12total * 0.05
    elif p12total <= 500:
        p12desc = p12total * 0.10
    else:
        p12desc = p12total * 0.15
        
    p12final = p12total - p12desc
    print(f"Desconto: R${p12desc}")
    print(f"Preço final: R${p12final} \n \n ")

