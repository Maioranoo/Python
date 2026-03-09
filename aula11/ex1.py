def procurarchaves(dicionario,valor):
    lista=[]
    for chave, val in dicionario.items():
        if val==valor:
            lista.append(chave)
    return lista

dicionario={
    'alpha':1,
    'bravo':2,
    'charlie':1,
    'delta':3,
    'echa':1,
}

print(procurarchaves(dicionario,1))
print(procurarchaves(dicionario,2))
print(procurarchaves(dicionario,3))
print(procurarchaves(dicionario,4))

