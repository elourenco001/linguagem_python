#Fazer um programa para ler as medidas da base e altura de um retângulo. 
# Em seguida, mostrar o valor da área, perímetro e diagonal deste retângulo, com quatro casas decimais, conforme exemplos.

import math # importar a biblioteca Matematica

base = float(input("Base do retangulo: "))
altura = float(input("Altura do Retangulo: "))

area = base * altura
perimento = 2 * (base + altura)
diagonal = math.sqrt(base ** 2 + altura ** 2)

print(f"Area = {area:.4f}")
print(f"Perimentro = {perimento:.4f}")
print(f"Diagonal = {diagonal:.4f}")

