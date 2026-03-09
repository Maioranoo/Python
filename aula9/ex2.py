voto=[0,0,0,0,0,0,0]
while True:
    n=int(input("Digite seu voto(1 a 6, 0 para sair):"))
    if n==0:
        break
    elif n==1:
        voto[0]+=1
    elif n==2:
        voto[1]+=1
    elif n==3:
        voto[2]+=1
    elif n==4:
        voto[3]+=1
    elif n==5:
        voto[4]+=1
    elif n==6:
        voto[5]+=1
    elif n==7:
        voto[6]+=1
total=sum(voto)

print(f"{'Sistema Operacional':<25}{'Votos':<8}{'%':<6}")
print(f"{'_'*20:<25}{'_'*5:<8}{'_'*3:<6}")
print(f"{'Windows Server':<25}{voto[0]:<8}{voto[0]/total*100:<6.2f}")
print(f"{'Unix':<25}{voto[1]:<8}{voto[1]/total*100:<6.2f}")
print(f"{'Linux':<25}{voto[2]:<8}{voto[2]/total*100:<6.2f}")
print(f"{'Netware':<25}{voto[3]:<8}{voto[3]/total*100:<6.2f}")
print(f"{'Mac Os':<25}{voto[4]:<8}{voto[4]/total*100:<6.2f}")
print(f"{'Outro':<25}{voto[5]:<8}{voto[5]/total*100:<6.2f}")
print(f"{'_'*20:<25}{'_'*5:<8}{'_'*3:<6}")
print(f"{'Total':<25}{total:<8}{'100%':<6}")