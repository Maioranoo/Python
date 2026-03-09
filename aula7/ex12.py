# Exercício 12
# Escreva uma função que calcula o quociente e o resto da
# divisão inteira entre dois números. Utilize apenas as
# operações de soma e subtração para calcular o resultado.
# Dica: utilize uma estrutura de repetição para isso.
# Faça um programa principal que recebe o dividendo e o divisor
# do usuário e, depois de chamar a função, exibe o quociente e o
# resto.

def quociente_resto(dividendo, divisor): # definindo a função
    quociente = 0 # inicializando o quociente
    resto = dividendo # inicializando o resto com o dividendo
    
    while resto >= divisor: # enquanto o resto for maior ou igual ao divisor
        resto = resto - divisor # subtraindo o divisor do resto
        quociente = quociente + 1 # incrementando o quociente
        
    print(f"Quociente: {quociente}, Resto: {resto}") # imprimindo o resultado

# Exemplo de uso
quociente_resto(10, 3) # chamando a função com dividendo 10 e divisor 3
quociente_resto(20, 4) # chamando a função com dividendo 20 e divisor 4