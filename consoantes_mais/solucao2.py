contador = 0
while True:
    palavra = input()
    vogais = 0
    consoantes = 0
    for i in palavra:
        if i == 'a' or i == 'A' or i == 'e' or i == 'E' or i == 'i' or i == 'I' or i == 'o' or i == 'O' or i == 'u' or i == 'U':
             vogais += 1
        else:
            consoantes += 1
    if vogais >= consoantes:
        contador += 1
    else:
        contador += 1

        break

print(contador)