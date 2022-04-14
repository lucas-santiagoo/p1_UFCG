limite = float(input())
quebra = limite / 2
saida = ''

while True:
  valores = input().split()
  if valores[0] == 'fim': break
    
  soma = 0
  for valor in valores:
    soma += int(valor)
  media = soma / len(valores)

  if media < quebra: break

  if media > limite:
    for i in valores:
      saida += i + ' '
print(saida)