A=[]
soma_impares=[0,0,0,0]
for nlinha in range(4):
    linha=[]
    for ncoluna in range(4):
        n=int(input(f'Digite o elemento[{nlinha}][{ncoluna}]:'))
        linha.append(n)
    A.append(linha)
print("Matriz:")
for linha in A:
    for elemento in linha:
        print(f'{elemento:2d}', end=' ')
    print()

print('Soma dos numeros impares:')
for linha in range(len(A)):
    for coluna in range(len(A[linha])):
        if A[linha][coluna]%2==1:
            soma_impares[linha]+=A[linha][coluna]
print(soma_impares)

