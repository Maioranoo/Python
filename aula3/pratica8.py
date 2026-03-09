from math import ceil
pi=3.1415

#capturas os dados dos usuarios
raio=float(input("Raio:"))
altura=float(input("Altura:"))

#calcular a area da base
area_base= pi*(raio**2)
#print(f"A area da base é de: {area_base}")

#calcular a area lateral
area_lateral=2*pi*raio*altura
#print(f"A area lateral é: {area_lateral}")

area_total=1* area_base+area_lateral
print(f"A area total do cilindro é: {area_total:.2f}m²")

litros=area_total/3 #3 metros quadrados por litro
print(f"quantidade de litros necessario:{litros:.2f}")

#calcular qnt de latas aredondando pra cima
latas=ceil(litros/5)
print(f"Quantidade de latas:{latas:.0f}")

if latas==1:
    custo=50
if latas==2:
    custo= 48  
if latas==3:
    custo=46
if latas>3:
    custo=45
#imprimir o preço unitario e o custo
print(f"preço unitario:R$ {custo:.2f}")
print(f"custo total:R${latas*custo:.2f}")