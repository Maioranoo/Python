intervalo=[0,0,0,0]
while True:
    n=float(input("Digite um numero positivo, ou um negativo para sair:"))
    if n<0:
        break
    elif 0<=n<=25:
        intervalo[0]+=1
    elif 26<=n<=50:
        intervalo[1]+=1
    elif 51<=n<=75:
        intervalo[2]+=1
    elif 76<=n<=100:
        intervalo[3]+=1
print(f"intervalo[0-25]:{intervalo[0]}")
print(f"intervalo[26-50]:{intervalo[1]}")
print(f"intervalo[51-75]:{intervalo[2]}")
print(f"intervalo[76-100]:{intervalo[3]}")
