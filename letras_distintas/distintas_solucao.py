palavra = input()
segunda_comparar = input()
letras_distintas = 0    
diferentes = []

for letra1 in range(len(palavra)):
    status = False
    for letra2 in range(len(segunda_comparar)):
        if segunda_comparar[letra2] == palavra[letra1]:
            status = True 
    
    if status == False:
        diferentes.append(palavra[letra1])

for letra in diferentes: 
    letras_distintas += 1

print(letras_distintas)