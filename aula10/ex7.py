from random import randint
notas=[]
for nlinha in range(10):
    aluno=[]
    for ncoluna in range(3):
        aluno.append(randint(0,10))
    notas.append(aluno)

print("Matriz:")
for aluno in notas:
    for nota in aluno:
        print(f'{nota:4d}', end='')
    print()

for aluno in nota:
    menor_nota=min(aluno)
    prova=aluno.index(menor_nota)
    print(f"Aluno{nota.index(aluno)} - Prova {prova} - Nota{nota}")

notas_transposta=[]
for j in range(3):
    prova=[]
    for i in range(10):
        prova.append

