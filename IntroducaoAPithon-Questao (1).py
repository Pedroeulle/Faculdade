#1
print(" 1-Faça um programa para calcular as seguintes expressões aritmeticas (tente tambem calcula-las na mão para verificar a importancia da precedencia dos operadores): \n")

print("a) 10 + 20 X 30 (reescrever como sintaxe Python)")
ANum1 = 10
ANum2 = 20
ANum3 = 30
AResul = ANum1 + ANum2 * ANum3
print (f"resultado do calculo é {AResul} \n \n")

print("b) 4^2 / 30 (reescrever como sintaxe Python)")
BNum1 = 4
BResul = BNum1 ** 2 / 30
print (f"resultado do calculo é {BResul :.2f} \n \n")

print("c)(9^4 + 2) x 6 - 1 (reescrever como sintaxe Python)")
CResul = (9 ** 4 + 2) * 6 - 1
print (f"resultado do calculo é {CResul :.2f} \n \n")

print("d)10 % 3 * 10^2 + 2 + 1 - 10 * 4 / 2 (reescrever como sintaxe Python)")
DResul = (10 % 3) * (10 ** 2) + 2 + 1 - (10 * 4) / 2
print (f"resultado do calculo é {DResul :.2f} \n \n")