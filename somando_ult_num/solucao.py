
# Computação - UFCG
# Programação 1 - 2021.1e
# Lucas Santiago | Matrícula: 120210478

sentinela = input()
sequencia = []
somador = 0
for i in range(len(sentinela)):
    sequencia.append(int(input()))

for i in range(len(sequencia)):
    somador += sequencia[i] 
print(somador)