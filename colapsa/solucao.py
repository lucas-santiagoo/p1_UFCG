def colapsa_n_menores(N, nums):
    N = int(input())
    nums = list(input())    
    valor = 0
    for i in range(len(nums)):
        if int([i]) < int([i + 1]):
            valor.append(i)