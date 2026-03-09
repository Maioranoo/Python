I=int(input("Digite 1, 2 ou 3:"))
x=float(input("Digite um valor real:"))
y=float(input("Digite um valor real:"))
z=float(input("Digite um valor real:"))

def maior(x,y,z):
    if x>y and x>z:
        return x
    elif y>x and y>z:
        return y
    else:
        return z
    
def menor(x,y,z):
    if x<y and x<y:
        return x
    elif y<x and y<z:
        return y
    else:
        return z

def intermedio(x,y,z):
    if x>y and x <z or x<y and x>z:
        return x
    if y>x and y<z or y<x and y>z:
        return y
    else:
        return z
    
def ordem(I,x,y,z):
    if I==1:
        print(menor (x,y,z), intermedio(x,y,z), maior(x,y,z))
    elif I==2:
        print(maior (x,y,z), intermedio(x,y,z), menor(x,y,z))
    elif I==3:
        print(intermedio (x,y,z), maior(x,y,z), menor(x,y,z))
    else:
        print("Valor invalido!")

ordem(I,x,y,z)