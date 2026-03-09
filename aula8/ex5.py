numero=int(input("Digite a quantidade de numeros:"))
L=[]
for i in range(numero):
    x=float(input("Digite um valor real:"))
    L.append(x)
LR=L[ : : -1]
print(L)
print("Inverso:")
print(LR)