#entrada
defensivo = str(input())
hectare = float(input())

#calculo
herb = 0.3 * hectare         
fung = 1  
inset = 2.5 * hectare
preco_herb = herb * 100
preco_fung = fung * 320 
preco_inset = inset * 400
if defensivo == "Herbicida":
    print(f"{herb:.0f} Herbicida(s)") 
    print(f"R$ {preco_herb:.2f}")
elif defensivo == "Fungicida":
    print(f"{fung:.0f} Fungicida(s)") 
    print(f"R$ {preco_fung:.2f}")
elif defensivo == "Inseticida":
    print(f"{inset:.0f} Inseticida(s)") 
    print(f"R$ {preco_inset:.2f}")
