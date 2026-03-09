def calcular_peso(planeta, peso_terra):
    relacao_pesos = {
        "Mercúrio": 0.37,
        "Vênus": 0.88,
        "Marte": 0.38,
        "Júpiter": 2.64,
        "Saturno": 1.15,
        "Urano": 1.17,
        "Netuno": 1.18
    }
    if planeta in relacao_pesos:
        return peso_terra * relacao_pesos[planeta]
    


planeta = input("Digite o nome do planeta desejado: ")
peso_terra = float(input("Digite o peso da pessoa na Terra em Kg: "))

peso_planeta = calcular_peso(planeta, peso_terra)

if peso_planeta is not None:
    print(f"O peso da pessoa em {planeta} é: {peso_planeta:.2f} Kg")
else:
    print("Planeta inválido. Por favor, insira um planeta válido do Sistema Solar.")
