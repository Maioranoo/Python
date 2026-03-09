atual=int(input("digite o ano atual:"))
fabricacao=int(input("digite o ano de fabricacao do carro:"))
idade=atual-fabricacao

if idade< 3:
    print("novo")

else:
    print("velho")