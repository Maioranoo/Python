sexo=input("Digite o sexo da pessoa (M/F):")
peso=float(input("Digite o peso da pessoa:"))

def doacao(sexo,peso):
    if sexo =='M' and peso>=60:
        return True
    elif sexo =='F' and peso >=50:
        return True
    else:
        return False
pode=doacao(sexo,peso)
if pode:
    print("A pessoa pode doar sangue")
else:
    print("A pessoa NÃO pode doar sangue")