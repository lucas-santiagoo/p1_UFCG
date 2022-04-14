nome = input()
lista = ""
for n in range(len(nome)):
    if n % 2 == 0:
       lista += nome[n]  
    
print(lista)
