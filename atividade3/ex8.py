def ler_vetor(nome, tamanho):
    vetor = []
    print(f"Digite o {nome}:")
    while len(vetor) < tamanho:
        entrada = input()
        if entrada.replace('-', '').isnumeric():
            numero = int(entrada)
            vetor.append(numero)
        else:
            print("Erro: Por favor, digite apenas números inteiros.")
    return vetor

vetor1 = ler_vetor("vetor 1", 3)
vetor2 = ler_vetor("vetor 2", 3)

produto_escalar = 0
for i in range(3):
    produto_escalar += vetor1[i] * vetor2[i]

print(produto_escalar)