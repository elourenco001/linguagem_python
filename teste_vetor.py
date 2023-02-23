from typing import List # para usar Vetor é necessário importar a seguinte biblioteca para List

N: int
N = int(input("Quantos Numeros voce vai digitar? "))
vet: List[float] = [0 for x in range(N)] # declaracao correta para Vetor

for i in range(0, N):
    vet[i] = float(input("Digite um numero: "))
    
print()
print("NUMEROS DIGITADOS:")
for i in range(0, N):
    print(f"{vet[i]:.1f}")
    