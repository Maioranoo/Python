from random import randint
A=[]
for nlinha in range(12):
    linha=[]
    for ncoluna in range(12):
        linha.append(randint(0,100))
    A.append(linha)

print("Matriz:")
for linha in range(12):
    for coluna in range(12):
        print(f'{A[linha][coluna]:4d}', end='')
    print()

soma=0
contador=0
for linha in range (12):
    if linha>coluna:
        soma += A[linha][coluna]
        contador += 1
operacao=input("Digitem'S' para soma ou 'M' para media:").strip().upper()
if operacao=='S':
    print(f"Soma dos elementos abaixo da diagonal é de:{soma}")
elif operacao=='M':
    if contador>0:
        media=soma/contador
    else:
        media=0
    print(f"Media dos elementos abaixo da diagonal principal é de:{media:.2f}")