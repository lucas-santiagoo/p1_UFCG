# Computação - UFCG
# Programação 1 - 2021.1e
# Lucas Santiago | Matrícula: 120210478
# letras distintas, o programa deve receber duas palavras e verificar as letras que diferem entre si, saida quantidade de letras.


primeira_palavra = input()
palavra_a_comparar = input()
letras_diferentes = 0    
diferentes = []

for letra1 in range(len(primeira_palavra)):
    status = False
    for letra2 in range(len(palavra_a_comparar)):
        if palavra_a_comparar[letra2] == primeira_palavra[letra1]:
            status = True 
    
    if status == False:
        diferentes.append(primeira_palavra[letra1])

for letra in diferentes: 
    letras_diferentes += 1
print(f'{letras_diferentes}')