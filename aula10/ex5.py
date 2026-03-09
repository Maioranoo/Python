from random import randint
A=[]
for nlinha in range(10):
    linha=[]
    for ncoluna in range(5):
        linha.append(randint(0,100))
    A.append(linha)

print("Matriz:")
for linha in range(10):
    for coluna in range(5):
        print(f'{A[linha][coluna]:4d}', end='')
    print()

transposta = [list(coluna) for coluna in zip(*A)]

print("Matriz transposta:")
for linha in transposta:
    print(linha)