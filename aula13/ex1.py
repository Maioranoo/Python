texto = input("Digite um texto: ")
nova_string = ""
for letra in texto:
    if letra == "a":
        nova_string += "A"
    elif letra == "e":
        nova_string += "E"
    elif letra == "i":
        nova_string += "I"
    elif letra == "o":
        nova_string += "O"
    elif letra == "u":
        nova_string += "U"
    else:
        nova_string += letra
print(nova_string)
