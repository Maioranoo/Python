letra=input("Digite a letra desejada:")

if letra=='a' or letra=='A' or letra=='e'  or letra=='E' or letra=='i'  or letra=='I' or letra=='o'  or letra=='O' or letra=='u' or letra=='U':
    print("Essa letra é uma vogal")
elif letra=='y' or letra=='Y':
    print("Essa letra, em algumas línguas, pode ser considerada como uma vogal e, em outras, como uma consoante.")
else:
    print("Essa letra é uma consoante.")