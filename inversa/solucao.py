palavra = input()

palavra_inversa = ''
caracteres_comum = 0

for i in range(len(palavra)-1,-1, -1):
    palavra_inversa += palavra[i]


for i in range(len(palavra)):
    if palavra[i] == palavra_inversa[i]:
      caracteres_comum += 1


print(f'A palavra {palavra} contém {caracteres_comum} caractere(s) coincidente(s) com a sua inversa.')