numero = input()
lista = input()
lista = lista.split(" ")

resposta = "não"

for elemento in lista:
    if numero == elemento:
        resposta = "sim"
print(resposta)

