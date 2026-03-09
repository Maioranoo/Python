senha=int(input("Digite sua senha:"))
if senha==1234:
    print("Acesso permitido")
    
    area=input("deseja acessar area administrativa?(S para sim, N para não):")
    
    if area=="s":
        print(" Entrando na área administrativa...")
    else:
        print("Você está na área de usuário comum.")
else:
   print("Senha incorreta! Acesso negado")