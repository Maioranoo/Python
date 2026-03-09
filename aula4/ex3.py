altura=float(input("Digite sua altura:"))
sexo=input("Digite a inicial do seu sexo:")

if sexo=="M" or sexo=="m":
    print(f"Peso ideal {72.7*altura-58:.2f}:")
elif sexo=="F" or sexo=="f":
    print(f"Peso ideal {62.1*altura-44.7:.2f}:")

