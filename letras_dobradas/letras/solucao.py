
entrada = int(input())
palavras = []
palavras_repetidas = []
palavras_normais = []

for i in range(entrada):
    palavra = input()
    palavras.append(palavra)

for palavra in palavras:
    status = False
    for i in range(len(palavra)-1):
        if palavra[i] == palavra[i + 1]:
            status = True
            break
    
    if status:
        palavras_repetidas.append(palavra)
    else:
        palavras_normais.append(palavra)

print(f'{len(palavras_repetidas)} palavra(s) com letras dobradas:')
for plr in palavras_repetidas:
    print(plr)
print('---')
print(f'{len(palavras_normais)} palavra(s) sem letras dobradas:')
for pln in palavras_normais:
    print(pln)
