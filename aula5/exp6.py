contador = 0
soma = 0

# Laço que continua pedindo números até o 0 ser digitado
while True:
    numero = int(input("Digite um número (ou 0 para parar): "))
    
    if numero == 0:
        break
    
    contador=contador+1
    soma=numero +soma

# Verifica se algum número foi digitado antes de calcular a média
media = soma / contador
print(f"Quantidade de números digitados: {contador}")
print(f"Soma dos números: {soma}")
print(f"Média aritmética: {media}")
