from random import randint
A=[]
for nlinha in range(10):
    linha=[]
    for ncoluna in range(15):
        linha.append(randint(0,100))
    A.append(linha)

print("Matriz Completa:")
for linha in range(10):
    for coluna in range(15):
        print(f'{A[linha][coluna]:4d}', end='')
    print()

print()
print("Elementos da primeira coluna")
for linha in range(10):
    print(f'{A[linha][0]:4d}', end='')
print()

