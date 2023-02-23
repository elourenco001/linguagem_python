#Fazer um programa para ler três números inteiros. Em seguida, mostrar qual o menor dentre os três números lidos. Em caso de empate, mostrar apenas uma vez.

valor1: int; valor2: int; valor3: int; menor: int

valor1 = int(input("Primeiro Valor: "))
valor2 = int(input("Segundo Valor: "))
valor3 = int(input("Terceiro Valor: "))

if valor1 < valor2 and valor1 < valor3: #Forma de declarar 'E' em Python 
     menor = valor1
elif valor2 < valor3: # Sempre manter o encadeamento posicionado abaixo dos demais !!!
     menor = valor2     
else:
     menor = valor3

print(f"Menor: ",menor) #Durante a Impressao em tela, pode ser informado com ', variavel' ou {variavel}