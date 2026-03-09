htrabalho=int(input("digite o valor da hora de trabalho: "))
horas=int(input("digite a quantidade de horas trabalhada: "))
print()

salario_bruto= htrabalho*horas
print("+ salario bruto: R$ %.2f" % salario_bruto)

imposto_renda= salario_bruto*(11/100)
print("- IR (11%%): R$ %.2f" %imposto_renda)

inss= salario_bruto* (8/100)
print("-INSS (8%%): R$ %.2f" %inss)

sindicato= salario_bruto*(5/100)
print("- sindicato (5%%): R$ %.2f" % sindicato)

salario_liquido=salario_bruto-imposto_renda-inss-sindicato
print("+salario liquido: R$ %.2f" %salario_liquido)
