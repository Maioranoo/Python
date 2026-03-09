l=[]
for i in range(10):
    x=float(input("Digite um numero real:"))
    l.append(x)
print(l)

for indice in range(2,len(l)):  
    if l[indice]>l[indice-1]+l[indice-2]:
        print(f"{l[indice]}")
