L=[]
for x in range(10):
    x=float(input("Digite um valor real:"))
    L.append(x)
maior=float("-inf")
ind=-1
for indice in range(len(L)):
    if L[indice]>maior:
        maior=L[indice]
        ind=indice
print(L)
print(maior)
print(f"O maior elemento é {maior} e seu indice é {ind}")
