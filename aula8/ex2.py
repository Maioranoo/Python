T=[11,7,2,4,1]

menor=float("inf")
for elemento in T:
    if menor>elemento:
        menor=elemento

print(f"O menor valor dessa lista é {menor}")