#Leia uma quantidade indeterminada de duplas de valores inteiros X e Y. Escreva para cada X e Y uma mensagem que indique se estes valores foram digitados em ordem crescente ou decrescente. 
# O programa deve finalizar quando forem digitados dois valores iguais.

x: int; y: int
crescente: str; decrescente: str

x = int(input("Digite um numeros: "))
y = int(input("Digite outro numero: "))


if x < y:
    print("CRESCENTE")
else:
    print("DECRESCENTE")
    
    
    