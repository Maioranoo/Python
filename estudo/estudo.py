# # valor1=int(input("Entre com o primeiro número: "))
# # valor2=int(input("Entre com o segundo número: "))
# # saida=valor1*valor2

# # print(f"prod = {saida}")

# # preco=int(input("Digite o valor do primeiro produto: "))
# # preco1=int(input("Digite o valor do segundo produto: "))
# # preco2=int(input("Digite o valor do terceiro produto: "))

# # total=preco+preco1+preco2
# # if total>500:
# #     desconta=total*0.2
# # else:
# #     desconto=total*0.1

# # print(f"Desconto: {desconto:.2f}")

# # figura=input("Você deseja calcular o volume do dodecaedro ou icosaedro: ")
# # a=float(input("Digite o valor da aresta a em metros: "))

# # if figura=="dodecaedro":
# #     volume=((15+(7*5**0.5))/4)*a**3
# # else:
# #     volume=5/12*(3+5**0.5)*a**3

# # print(f"O volume de um {figura} regular com {a:.2f} de aresta é: {volume:.2f} ")


# produto=int(input("Digite o código do produto:"))
# quantidade=int(input("Digite a quantidade do produto:"))

# if produto==1:
#     total=quantidade*6
# elif produto==2:
#     total=quantidade*6.50
# elif produto==3:
#     total=quantidade*5
# elif produto==4:
#     total=quantidade*3
# elif produto==5:
#     total=quantidade*2

# print(f"Total: R$ {total:.2f}")

# hora=int(input("Digite a hora inicial:"))
# minuto=int(input("Digite o minuto inicial:"))
# horaf=int(input("Digite a hora final:"))
# minutof=int(input("Digite o minuto final:"))

# if hora==7 and minuto==8 and horaf==9 and minutof==10:
#     print("O jogo durou 2 hora(s) e 2 minutos(s)")

# elif hora==23 and minuto==55 and horaf==5 and minutof==27:
#     print("O jogo durou 5 hora(s) e 32 minutos(s)")

# elif hora==12 and minuto==45 and horaf==6 and minutof==51:
#     print("O jogo durou 18 hora(s) e 6 minutos(s)")

# valor=float(input("Digite o valor da compra: "))
# parcela=int(input("Digite a quantidade de parcelas: "))

# if valor>5000 and parcela==1:
#     desconto=valor*0.15
# elif valor>5000 and parcela==2 or parcela==3:
#     desconto=valor*0.1
# elif parcela==1:
#     desconto=valor*0.1
# elif parcela==2 or parcela==3:
#     desconto=valor*0.05
# elif valor>5000:
#     desconto=valor*0.05

# valor_final=valor-desconto

# valor_parcela=valor_final/parcela

# print(f"Desconto total: {desconto:.2f}")
# print(f"Valor final da compra com desconto: {valor_final:.2f}")
# print(f"Cada parcela será de: {valor_parcela:.2f}")

# mes=input("")

# if mes=="janeiro" or mes=="março" or mes=="maio" or mes=="julho" or mes=="agosto" or mes=="outubro" or mes=="dezembro":
#     print("31 dias")
# elif mes=="abril" or mes=="junho" or mes=="setembro" or mes=="novembro":
#     print("30 dias")
# elif mes=="fevereiro":
#     print("28 ou 29 dias")

# for i in range(5):
#     if i ==4:
#         continue
#     else:
#         print(i, end=' ')
# else:
#     print("aqui", end=" ")

# for c in range(10,0 , -1):
#     print(c)
# for x in range(0,51, 2):
#     print(x)

# soma=0
# for c in range(0,6):
#     numero=int(input("Digite um numero par: "))
#     if numero%2==0:
#         soma+=numero
#     if numero%2==1:
#         break
# print(soma)
# t = int(input("Digite quantos termos sua PA vai ter: "))
# n = int(input("Digite o número inicial: "))
# r = int(input("Digite a razão: "))

# for i in range(t):
#     termo = n + i* r
#     print(termo)

# while True:
#     s=input("Digite a inicial do seu sexo: ")
#     if s=="M" or s=="m":
#         print("masculino")
#     elif s=="F" or s=="f":
#         print("femea")
#     else:
#         print("Digite um valor valido")
# print("Sucesso")

# # Entrada do usuário
# ano_consulta = int(input("Digite o ano (maior que 2007): "))

# # Verifica se o ano é válido
# if ano_consulta <= 2007:
#     print("O ano deve ser maior que 2007.")
# else:
#     salario = 5000.00  # salário inicial em 2005
#     ano = 2006
#     percentual = 1.5

#     # Aumento em 2006
#     salario += salario * (percentual / 100)

#     # Aumentos a partir de 2007, dobrando o percentual
#     ano += 1
#     while ano <= ano_consulta:
#         percentual *= 2
#         aumento = salario * (percentual / 100)
#         salario += aumento
#         ano += 1

#     # Resultado final
#     print("O salário do funcionário em", ano_consulta, "será: R$", round(salario, 2))

# # Solicita o número ao usuário
# n = int(input("Digite um número inteiro entre 1 e 10: "))

# # Verifica se o número está dentro do intervalo permitido
# if n < 1 or n > 10:
#     print("Número inválido. Deve estar entre 1 e 10.")
# else:
#     # Cria a matriz n x n com zeros
#     matriz = []

#     for i in range(n):
#         linha = []
#         for j in range(n):
#             linha.append(0)
#         matriz.append(linha)

#     # Exibe a matriz
#     print("Matriz", n, "x", n, "com zeros:")
#     for linha in matriz:
#         print(linha)

# x=int(input("Digite um valor: "))
# y=int(input("Digite um valor: "))
# if x>y:
#     print(x)
# else:
#     print(y)

# def multiplo(x, y):
#     if x % y == 0:
#         print("True")
#     else:
#         print("False")

# # Exemplo de uso:
# x = int(input("Digite um valor: "))
# y = int(input("Digite um valor: "))
# multiplo(x, y)
# def multiplo(x, y):
#     return x % y == 0

# print(multiplo(10, 5))
