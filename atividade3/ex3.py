def media(nota1, nota2, nota3, tipo):
    if tipo.upper() == 'A':
        return (nota1 + nota2 + nota3) / 3
    elif tipo.upper() == 'P':
        return (nota1 * 5 + nota2 * 3 + nota3 * 2) / (5 + 3 + 2)
    else:
        return None

def nota():
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    nota3 = float(input("Digite a terceira nota: "))
    tipo = input("Digite 'A' para média aritmética ou 'P' para média ponderada: ")

    resultado = media(nota1, nota2, nota3, tipo)

    if resultado is not None:
        print(f"A média é: {resultado:.2f}")
    else:
        print("Tipo de média inválido.")


nota()
