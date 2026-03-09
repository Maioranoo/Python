from random import randint, random

inteiros = [randint(0, 10) for _ in range(10)]
reais = [random() * 10 for _ in range(5)]
string = ["M", "A", "I", "O", "R", "A", "N", "O"]

completa = []
completa.append(inteiros)
completa.append(reais)
completa.append(string)

del inteiros
del reais
del string

print("COMPLETA:", completa)
