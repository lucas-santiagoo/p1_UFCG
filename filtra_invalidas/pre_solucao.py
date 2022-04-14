numero_linha = 0
numero_pares = 0
numero_impares = 0
numero_invalido = 0
validos = 0

while True: 
    linha = input()
    if linha == 'fim': break
    numero_linha+= 1
    numeros = linha.split()

    for s  in numeros:
        if int(s) % 2 == 0:
           numero_pares += 1 
        if int(s) % 2 != 0:
            numero_impares += 1

   
    if numero_pares <= numero_impares:
        numero_invalido += 1 
        print(f'linha {numero_linha} inválida: {s} ')

    numero_pares = 0
    numero_impares = 0
    
print(f'sequências lidas: {numero_linha} (inválidas: {numero_invalido})')