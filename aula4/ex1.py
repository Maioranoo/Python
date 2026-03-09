codigo=int(input("Digite o codigo do produto:"))

if codigo==1:
    print("Produto do sul")
elif codigo==2:
    print("Produto do norte")
elif codigo ==3:
    print("Produto do leste")
elif codigo ==4:
    print("Produto do oeste")
elif codigo==5 or codigo==6:
    print("Produto do nordeste")
elif codigo>=7 and codigo<=9:
    print("Produto do sudeste")
elif codigo>=10 and codigo<=20:
    print("Produto do centro oeste")
elif codigo>=25 and codigo<=30:
    print("Produto nordeste pt2")
else:
    print("Produto importado")