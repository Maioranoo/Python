l=[]
while True:
    palavra=input("Digite sua palavra:")
    if palavra=="":
        break
    else:
        if palavra not in l:
            l.append(palavra)

print("Palavras Digitadas:")
for palavra in l:
    print(palavra)
