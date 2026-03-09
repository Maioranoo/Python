#spotyfei
menu={
    1:"Novo contato",
    2:"Procurar contato",
    3:"Atualizar contato",
    4:"Apagar contato",
    0:"Sair"
}

def main():
    while True:
        print("Menu:")
        for key, value in menu.items():
            print(f"{key} - {value}")


def novo_contato():#criar usuario e criar playlist
    pass
def procurar_contato():#procurar musica
    print("Procurar contato:")
    nome_contato=input("Digite o nome procurado:")
    with open("agenda.txt")

def atualizar_contato():#curtir e descurtir
    print("Atualizar contato:")
def apagar_contato():
    pass
def sair():
    pass