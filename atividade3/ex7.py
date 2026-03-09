negativos = []
positivos = []

while True:
    num = int(input())
    if num == 0:
        break
    if num < 0:
        negativos.append(num)
    else:
        positivos.append(num)

resultado = negativos + positivos

print(resultado)
