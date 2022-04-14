quant_num = int(input())

menor_num = 0
maior_num = 0
entre_num = 0

nums = []

for i in range(quant_num):
    nums.append(int(input()))

print('---')
sentinela_1 = int(input())
sentinela_2 = int(input())

for e in range(quant_num):
    if int(e) < sentinela_1:
        menor_num += 1
    elif int(e) > sentinela_2 :    
        maior_num += 1
    elif int(e) < sentinela_1 and int(e) > sentinela_2:
        entre_num += 1

print(f'{menor_num} antes')
print(f'{entre_num} entre') 
print(f'{maior_num} depois')   
