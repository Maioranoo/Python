
a=int(input("Valor de lado a:"))
b=int(input("Valor do lado b:"))
c=int(input("Valor do lado C:"))
if (a<b+c) and (b<c+a) and (c<a+b):
    if (a==b) and (b==c):
        print("Triangulo equilatero")
    elif (a==b) or (b==c) or (c==a):
        print("Triangulo isosceles")
    else:
        print("Triangulo escaleno")
else:
    print("Não é triangulo")