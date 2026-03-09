codigo = {
    1: 6.00,
    2: 6.50,
    3: 5.00,
    4: 3.00,
    5: 2.50
}
produto = int(input("Digite o código do produto: "))
quantidade = int(input("Digite a quantidade do produto: "))


if produto in codigo:
    total = codigo[produto] * quantidade
    print(f"Total:R$ {total:.2f}")
else:
    print("Código inválido.")
