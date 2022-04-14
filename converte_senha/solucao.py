senha = input()
lista = list(senha)
troca = 0
cripto = ''

for i in range(len(lista)):

    if i > 0 and lista[i] =='a' or i > 0 and lista[i] =='A':
        lista[i] = '4'
        troca += +1
    elif i > 0 and lista[i] == 'e' or i > 0 and lista[i] == 'E':
        lista[i] = '3'
        troca += +1
    elif i > 0 and lista[i] == 'i' or i > 0 and lista[i] == 'I':
        lista[i] = '1'
        troca += +1
    elif i > 0 and lista[i] == 'o' or i > 0 and lista[i] == 'O':
        lista[i] = '0'
        troca += +1
for letra in lista:
    cripto += letra
print(f"{cripto} ({troca} troca(s))")

