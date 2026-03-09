def tarifa_inicial(km):
    tarifa = 10.00
    preco_125m = 0.50
    metros = km * 1000
    custo = (metros // 125) * preco_125m
    return tarifa + custo

km = float(input("Digite a quantidade de quilômetros:"))
tarifa_total = tarifa_inicial(km)
print(f"Tarifa:{tarifa_total}")
