tamanho=int(input("N linhas:"))

for l in range(tamanho):
    for c in range(tamanho):
        if l%2==0:
            if c%2==0:
                print("$", end=" ")
            else:
                print("&", end=" ")
        else:
            if c%2==0:
                print("%", end=" ")
            else:
                print("#", end=" ")
        
    print()