with open("./aula12/exemplos/pares.txt","r") as pares:
    linhas=pares.readlines()

linhas=linhas[::-1]

with open("./aula12/exemplos/invertido.txt","w") as invertidos:
    for linha in linhas:
        invertidos.write(linha)