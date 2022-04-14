sequencia = input()
limite = int(input())
numeros = list(sequencia)



def somalista(numeros):
   if len(numeros) == 1:
        return numeros[0]
   else:
        return numeros[0] + somalista(numeros[1:])

print(somalista)








