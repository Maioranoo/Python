def main():
    valor_compra = float(input("Digite o valor da compra: "))
    parcelas = int(input("Digite a quantidade de parcelas: "))
    
    desconto=0
    if parcelas == 1:
        desconto=desconto+(10/100)
    if parcelas==2 or parcelas==3:
        desconto=desconto+(5/100)
    if parcelas>3:
        desconto=desconto+(0/100)
    if valor_compra > 5000:
        desconto=desconto+(5/100)
    
    
    
    desconto_total = valor_compra * desconto
    valor_final = valor_compra - desconto_total
    valor_parcela = valor_final / parcelas
    
    print(f"Desconto total: {desconto_total:.2f}")
    print(f"Valor final da compra com desconto: {valor_final:.2f}")
    print(f"Cada parcela será de: {valor_parcela:.2f}")
    

main()