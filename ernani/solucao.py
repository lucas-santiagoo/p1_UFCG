def organiza_pedido(lista):
    for i in range(len(lista) - 1):
        for j in range(len(lista) - i - 1):
            if lista[j + 1] < lista[j]:
                lista[j + 1], lista[j] = lista[j], lista[j + 1]       
    
    return lista
  