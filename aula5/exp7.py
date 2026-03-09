soma=0
for x in range(10):
    n=int(input("Digite um numero:"))
    soma=soma+n
    print(f"Numero {x+1}: {n} - soma: {soma}")
print("Soma dos numeros:", soma)