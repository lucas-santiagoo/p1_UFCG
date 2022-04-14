#entrada
custo = float(input())
despesas = float(input())
lucro = float(input())
impostos = float(input())
comissoes = float(input())
descontos = float(input())
encargos = float(input())

#calculo
preco_de_venda = (custo + despesas + lucro) * 100 / (100 - impostos - comissoes - descontos - encargos)

parte_inteira = (int(preco_de_venda))
parte_fracionaria = preco_de_venda - parte_inteira

#saida

print(f"Preço de venda é R$ {preco_de_venda:.2f} (R$ {parte_inteira} + R$ {parte_fracionaria:.2f})") 
