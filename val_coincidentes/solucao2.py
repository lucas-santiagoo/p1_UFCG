sequencia1 = input().split()
sequencia2 = input().split()

  
conta = 0

if sequencia1 < sequencia2:
    for i in range(len(sequencia1)):
        if sequencia1[i] == sequencia2[i]:
            conta += 1
            print(f"i = {i}:  {sequencia1[i]}")
elif sequencia1 > sequencia2:
    for j in range(len(sequencia1)):
        if sequencia1[j] == sequencia2[j]:
            conta += 1
            print(f"i = {j}: {sequencia1[j]}")
else:
    for k in range(len(sequencia1)):
        if sequencia1[k] == sequencia2[k]:
            conta += 1
            print(f"i = {k}: {sequencia1[k]}")

percentagem = (conta * 100)/(len(sequencia1) + len(sequencia2)) 
print(f"Valores coincidentes: {conta} ({percentagem:.0f}%)")