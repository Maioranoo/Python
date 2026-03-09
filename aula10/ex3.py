A=[]
for nlinha in range(3):
    linha=[]
    for ncoluna in range(3):
        coluna=[]
        n=int(input(f'Digite o elemento[{nlinha}][{ncoluna}]:'))
        linha.append(n)
    A.append(linha)
print("Matriz:")
for linha in A:
    for elemento in linha:
        print(f'{elemento:2d}', end=' ')
    print()

soma_diagonal=0
for i in range (3):
    soma_diagonal += A[i][i]
print(f'Soma da diagonal:{soma_diagonal}')
