A=[]
for nlinha in range(2):
    linha=[]
    for ncoluna in range(2):
        n=int(input(f'Digite o elemento da linha {nlinha} e coluna {ncoluna}:'))
        linha.append(n)
    A.append(linha)

maior_elemento = max(max(linha) for linha in A)

resultante = []
for linha in A:
    linha_resultante = [elemento * maior_elemento for elemento in linha]
    resultante.append(linha_resultante)

print("Matriz resultante")
for linha in resultante:
    for elemento in linha:
        print(f'{elemento:3d}', end=' ')
    print()


