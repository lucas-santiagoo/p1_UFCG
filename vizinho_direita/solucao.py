lista = input().split()
cont = 0

for i in range(len(lista)-1):
    for e in range(i + 1, i + 2):
        if lista[i] == lista[e]:
            cont += 1

print(cont)
