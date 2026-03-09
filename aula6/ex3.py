linha=int(input("N linhas:"))
coluna=int(input("N colunas:"))

for l in range(linha):
    for c in range(coluna):
        if l%2==0:
            if c %2==0:
                print("x", end=" ")
            else:
                print("0", end=" ")
        elif l%2==1:
            if  c%2==1:
                print("x", end=" ")
            else:
                print("0", end=" ")
    print()