from typing import List #importar a lista para Vetor e Matriz

M: int
N: int

M = int(input("Quantas Linhas vai ter a matriz? "))
N = int(input("Quantas Colunas vai ter a matriz?" ))

mat: List[List[int]] = [[0 for x in range(N)]for x in range(M)] # para declarar a Matriz eh necessario adicionar List conforme declarado

for i in range(0, M):
    for j in range(0, N):
        mat[i][j] = int(input(f"Elemento [{i},{j}]: "))
print()
print("MATRIZ DIGITADA:") 
for i in range(0, M):
    for j in range(0, N): 
        print(f"{mat[i][j]} ", end="")
    print()