somatoria=0
while True:
    entrada=int(input("Digite um numero para somar ou 0 para sair:"))
    if entrada==0:
        break
    else:
        somatoria=somatoria+entrada
print("somatoria", somatoria)