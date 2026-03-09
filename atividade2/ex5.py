numero = int(input("Digite a quantidade de linhas: "))

for i in range(1, numero + 1):
    quadrado = i**2
    cubo = i**3
    print(f"{i} {quadrado} {cubo}")