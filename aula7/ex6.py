def raiz(x,y,z):
    resultado=x**0.5+y**0.5+z**0.5+(x+y)/2+(y+z)/2+(x+z)/2
    return resultado
print(f"{raiz(10,15,13):.2f}")
print(f"{raiz(10,11,12):.2f}")
print(f"{raiz(49,14,27):.2f}")
print(f"{raiz(14,15,13):.2f}")
print(f"{raiz(15,21,18):.2f}")