#UFCG - prog_1
#lucas santiago 06/12/21
#fli_flai

num_1 = int(input())
num_2 = int(input())
num_3 = int(input())


if num_1 % 10 == 0 or num_2 % 10 == 0 or num_3 % 10 == 0:
    print("Tumba")

else:

    if num_1 % 2  == 0:
        print("Fli")
    if num_2 % 3 == 0:
        print("Flai")
    if num_3 % 5 == 0:
        print("Flu")

