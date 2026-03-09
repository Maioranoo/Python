from random import randint
dicionario={

}
for i in range(100):
    n=randint(0,20)
    if n not in dicionario:
        dicionario[n]=1
    else:
        dicionario[n] +=1

for chave, valor in dicionario.items():
    print(f'{chave:2d}:{valor:2d}')
