
x: int; y: int; soma: int

print("Digite um valor: ")
x = int(input())
y = int(input())

if x > y:        #Logica para efetuar troca de valores entre variaveis.
    troca = x
    x = y
    y = troca
    
soma = 0

for i in range(x+1, y): #Validando se os valores sao impares.
    if i % 2 !=0:
        soma = soma + i
        
        print("SOMA DOS IMPARES: ", soma)    



