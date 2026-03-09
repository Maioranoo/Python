linha=int(input("N linhas:"))
coluna=int(input("N colunas:"))

for l in range(linha):
    for c in range(coluna):
        if l==0 or l==linha-1 or c==0 or c==coluna-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()