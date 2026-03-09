import os

menu_inicial = {
    1: "Cadastrar usuário",
    2: "Logar",
    0: "Sair"
}

menu_logado = {
    3: "Cadastrar música",
    4: "Procurar música",
    5: "Curtir e descurtir música",
    6: "Adicionar na playlist",
    7: "Editar playlist",
    8: "Excluir playlist",
    0: "Sair da conta"
}

def main():
    while True:
        escolha = exibir_menu(menu_inicial)
        if escolha == 1:
            novo_usuario()
        elif escolha == 2:
            logar_usuario()
        elif escolha == 0:
            sair()
        else:
            print("Opção inválida.")

def exibir_menu(menu_principal):
    print("\nMenu:")
    for opcao, descricao in menu_principal.items():
        print(f"{opcao} - {descricao}")
    return int(input("Escolha uma opção: "))

def novo_usuario():
    print("Cadastrar novo usuário:")
    nome_usuario = input("Digite o nome: ")
    senha = input("Crie uma senha: ")
    with open("usuarios.txt", "a") as arquivo_usuario:
        arquivo_usuario.write(f"{nome_usuario},{senha},\n")
    print("Usuário cadastrado com sucesso!")

def logar_usuario():
    print("Login:")
    nome_logar = input("Digite o nome do usuário: ")
    senha_logar = input("Digite a senha: ")

    with open("usuarios.txt", "r") as arquivo:
        usuarios = arquivo.readlines()

    for linha in usuarios:
        nome_usuario, senha,_ = linha.strip().split(",")
        if nome_usuario == nome_logar and senha == senha_logar:
            print(f"\nBem-vindo, {nome_usuario}!")
            menu_usuario_logado(nome_usuario)
            break
    else:
        print("Usuário ou senha incorretos.")

def menu_usuario_logado(nome_usuario):
    while True:
        escolha = exibir_menu(menu_logado)
        if escolha == 3:
            nova_musica()
        elif escolha == 4:
            procurar_musica()
        elif escolha == 5:
            curtir_descurtir()
        elif escolha == 6:
            adicionar_playlist()
        elif escolha == 7:
            editar_playlist()
        elif escolha == 8:
            excluir_playlist()
        elif escolha == 0:
            print(f"{nome_usuario} saiu da conta.")
            break
        else:
            print("Opção inválida.")

def nova_musica():
    print("Cadastrar nova música:")
    nome_musica = input("Nome da música: ")
    artista = input("Nome do artista: ")
    genero = input("Gênero musical: ")
    with open("musicas.txt", "a") as arquivo_musica:
        arquivo_musica.write(f"{nome_musica},{artista},{genero}\n")
    print("Música cadastrada com sucesso!")

def procurar_musica():
    print("Procurar música:")
    nome_busca = input("Digite o nome da música: ")
    with open("musicas.txt", "r") as arquivo_musica:
        musicas = arquivo_musica.readlines()

    for linha in musicas:
        nome_musica, artista, genero = linha.strip().split(",")
        if nome_musica.lower() == nome_busca.lower():
            print(f"Nome: {nome_musica}, Artista: {artista}, Gênero: {genero}")
            break
    else:
        print("Música não encontrada.")

def curtir_descurtir():
    open ("curtidas.txt","a").close()
    print("Curtir ou descurtir música:")
    nome_musica_curtir = input("Digite o nome da música que deseja curtir ou descurtir: ")

    with open("musicas.txt", "r") as arquivo_musica:
        musicas = arquivo_musica.readlines()

    for linha in musicas:
        nome_musica, artista, genero = linha.strip().split(",")
        if nome_musica_curtir.lower() == nome_musica.lower():
            print(f"Música encontrada: Nome: {nome_musica}, Artista: {artista}, Gênero: {genero}")
            break
    else:
        print("Música não encontrada.")
        return
    with open("curtidas.txt", "r") as arquivo_curtidas:
        linhas_curtidas = [linha.strip() for linha in arquivo_curtidas.readlines()]

    if nome_musica_curtir.lower() in [musica.lower() for musica in linhas_curtidas]:
        nova_lista = [musica for musica in linhas_curtidas if musica.lower() != nome_musica_curtir.lower()]
        with open("curtidas.txt", "w") as arquivo_curtidas:
            for musica in nova_lista:
                arquivo_curtidas.write(musica + "\n")

        with open("descurtidas.txt", "a") as arquivo_descurtidas:
            arquivo_descurtidas.write(f"{nome_musica_curtir}\n")

        print("Música descurtida com sucesso!")
    else:
        with open("curtidas.txt", "a") as arquivo_curtidas:
            arquivo_curtidas.write(f"{nome_musica_curtir}\n")
        print("Música curtida com sucesso!")

             
def adicionar_playlist():
    print("Adicionar ou remover música da playlist:")

    nome_playlist = input("Digite o nome da playlist: ")
    nome_musica_playlist = input("Digite o nome da música: ")

    with open("musicas.txt", "r") as arquivo_musica:
        musicas = arquivo_musica.readlines()

    for linha in musicas:
        nome_musica, artista, genero = linha.strip().split(",")
        if nome_musica_playlist.lower() == nome_musica.lower():
            print(f"Música encontrada: Nome: {nome_musica}, Artista: {artista}, Gênero: {genero}")
            break
    else:
        print("Música não encontrada.")
        return

    nome_arquivo = f"{nome_playlist}.txt"

    if os.path.exists(nome_arquivo):
        with open(nome_arquivo, "r") as arquivo_playlist:
            linhas_playlist = [linha.strip() for linha in arquivo_playlist.readlines()]
    else:
        linhas_playlist = []

    for linha in linhas_playlist:
        nome, artista, genero = linha.split(",")
        if nome.lower() == nome_musica_playlist.lower():
            nova_playlist = [musica for musica in linhas_playlist if musica.lower() != linha.lower()]
            with open(nome_arquivo, "w") as arquivo_playlist:
                for musica in nova_playlist:
                    arquivo_playlist.write(musica + "\n")
            print(f"Música '{nome_musica_playlist}' removida da playlist '{nome_playlist}'.")
            break
    else:
        with open(nome_arquivo, "a") as arquivo_playlist:
            arquivo_playlist.write(f"{nome_musica},{artista},{genero}\n")
        print(f"Música '{nome_musica}' adicionada à playlist '{nome_playlist}' com sucesso!")



def editar_playlist():
    print("Editar nome da playlist:")
    nome_atual = input("Digite o nome atual da playlist: ")
    nome_novo = input("Digite o novo nome para a playlist: ")

    nome_arquivo_atual = f"{nome_atual}.txt"
    nome_arquivo_novo = f"{nome_novo}.txt"

    if os.path.exists(nome_arquivo_atual):
        os.rename(nome_arquivo_atual, nome_arquivo_novo)
        print(f"Playlist renomeada de '{nome_atual}' para '{nome_novo}' com sucesso!")
    else:
        print("Playlist não encontrada.")

def excluir_playlist():
    print("Excluir playlist:")
    nome_playlist = input("Digite o nome da playlist para a excluir: ")
    nome_arquivo = f"{nome_playlist}.txt"

    if os.path.exists(nome_arquivo):
        os.remove(nome_arquivo)
        print(f"Playlist '{nome_playlist}' excluída com sucesso!")
    else:
        print("Playlist não encontrada.")

def sair():
    print("Saindo...")
    exit()

if __name__ == "__main__":
    main()
