
#13
print("13 - Faça um programa que receba o preço, a categoria (Limpeza, Alimentação ou Vestuário) e a situação (R ou S) de um determinado produto. A situação R significa produto que precisa de refrigeração e S que não precisa. Calcule e mostre:")
p13reco = float(input("Digite o preço do produto: "))
c13ategoria = input("Digite a categoria do produto (Limpeza, Alimentação ou Vestuário): ")
s13ituacao = input("Digite a situação do produto (R ou S): ")

a13umento = 0
if p13reco <= 25:
    if c13ategoria == "Limpeza":
        a13umento = 0.05
    elif c13ategoria == "Alimentação":
        a13umento = 0.08
    elif c13ategoria == "Vestuário":
        a13umento = 0.1
else:
    if c13ategoria == "Limpeza":
        a13umento = 0.12
    elif c13ategoria == "Alimentação":
        a13umento = 0.15
    elif c13ategoria == "Vestuário":
        a13umento = 0.18

i13mposto = 0.05 if c13ategoria == "Alimentação" or s13ituacao == "R" else 0.08

n13ovo_preco = p13reco * (1 + a13umento) * (1 + i13mposto)

c13lassificacao = ""
if n13ovo_preco <= 50:
    c13lassificacao = "Barato"
elif n13ovo_preco >= 120:
    c13lassificacao = "Caro"
else:
    c13lassificacao = "Normal"

print(f"Aumento: {a13umento*100:.2f}%")
print(f"Imposto: {i13mposto*100:.2f}%")
print(f"Novo preço: R${n13ovo_preco:.2f}")
print(f"Classificação: {c13lassificacao} \n \n")