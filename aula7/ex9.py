def data(dia,mes,ano):
    if dia*mes==ano%100:
        return True
    else:
         return False
for ano in range(1901,2001):
    for mes in range(1,13):
        for dia in range(1,32):
            if data(dia,mes,ano)==True:
                print(f"A data{dia}/{mes}/{ano} é magica")
