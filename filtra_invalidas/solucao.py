# Computação - UFCG
# Programação 1 - 2021.1e
# <Lucas Santiago> | Matrícula: <120210478>
# <Filtra linhas inválidas>
#Escreva um programa que leia uma sequência de linhas de números inteiros e que filtre e exiba as sequências consideradas inválidas. Uma sequência é válida se ela contém uma quantidade maior de números pares que de ímpares (e inválida, caso contrário, obviamente).

numero_linha = 0
numero_pares = 0
numero_impares = 0
numero_invalido = 0


while True:
    linha = input()
    if linha == 'fim': break
    numero_linha += 1
    sequencias = linha.split()

    for s in sequencias:
        if int(s) % 2 == 0:
            numero_pares += 1 
        if int(s) % 2 != 0:
            numero_impares += 1
    if numero_pares <= numero_impares:
        numero_invalido += 1 
        print(f'linha {numero_linha} inválida: {linha}')

    numero_pares = 0
    numero_impares = 0
    
print(f"sequências lidas: {numero_linha} (inválidas: {numero_invalido})")


    