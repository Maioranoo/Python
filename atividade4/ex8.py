N = int(input("Digite a ordem da matriz: "))

if 0 <= N <= 15:
    M = []
    for i in range(N):
        linha = []
        for j in range(N):
            linha.append(2 ** (i + j))  
        M.append(linha)
for linha in M:
        for elemento in linha:
            print(f"{elemento:4d}", end="")  
        print()
