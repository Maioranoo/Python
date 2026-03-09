def exponencial(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    b = 2
    while True:
        k = 0
        resultado = 1
        while resultado < n:
            resultado = b ** k
            k += 1
        
        if resultado == n:
            print(f"{b}^{k-1} = {n}")
            break
        else:
            b += 1

print(exponencial(0))
print(exponencial(1))
print(exponencial(2))
print(exponencial(10))
print(exponencial(16))
