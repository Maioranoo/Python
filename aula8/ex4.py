L=[]
for x in range(10):
    x=float(input("Digite um valor real:"))
    L.append(x)
ind=-1
somapar=0
somaind=0
for indice in range(len(L)):
    if L[indice]%2==0:
        somapar=somapar+L[indice]
        ind=indice
    if indice%2==0:
        somaind=somaind+L[indice]


print(L)
print(f"A soma dos elementos pares sao {somapar}")
print(f"A soma dos indices pares são:{somaind}")