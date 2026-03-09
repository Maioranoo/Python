dia=int(input("Digite o dia:"))
mes=int(input("Digite o mes:"))
ano=int(input("Digite o ano:"))

def data(dia,mes,ano):
    if dia*mes==ano%100:
        return True
    else:
         return False
magico=data(dia,mes,ano)
if magico:
    print(f"Data magica {dia}/{mes}/{ano}")
else:
    print("Este ano nao é magico")