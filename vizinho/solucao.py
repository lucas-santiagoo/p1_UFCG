sequencia = input().split()
contador = 0

for i in range(len(sequencia)-1):
    for e in range(i + 1, i + 2):
        if sequencia[i] == sequencia[e]:
            contador += 1
print(contador)
