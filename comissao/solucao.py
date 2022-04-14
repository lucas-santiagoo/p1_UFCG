nome = input("Qual é o nome do(a) vendedor(a)? ")
venda = float(input("Qual é o valor da venda? "))

output = ""

if venda <= 500.00:
    comissao = (venda * 0.05)
    output = f"O valor da comissão para o(a) vendedor(a) {nome} é R$ {comissao :.2f}."
else:
    comissao = (venda * 0.10)
    output = f"O valor da comissão para o(a) vendedor(a) {nome[0:5]} é R$ {comissao :.2f}." 
 
print(output)
