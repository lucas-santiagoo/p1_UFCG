def organiza_pedido(lista):
    for c in range(len(lista) - 1):
        for i in range(len(lista) - c - 1):
            if lista[i] == 'p' and lista[i + 1] == 'd':
                lista[i], lista[i + 1] = lista[i + 1], lista[i]
            if lista[i] == 's' and lista[i + 1] == 'p':
                lista[i], lista[i + 1] = lista[i + 1], lista[i]
            if lista[i] == 's' and lista[i + 1] == 'd':
                lista[i], lista[i + 1] = lista[i + 1], lista[i]