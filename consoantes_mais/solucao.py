contador = 0
while True:
    palavra = input()
    vogais = 0
    consoantes = 0
    for i in palavra:
        if i in 'AEIOUaeiou':
            vogais += 1
        else:
            consoantes += 1
    if vogais >= consoantes:
        contador += 1
    else:
        contador += 1

        break

print(contador)