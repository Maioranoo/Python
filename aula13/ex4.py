nome_arquivo=input("Digite o nome do arquivo: ")

with open(f"{nome_arquivo}.txt", "r") as arquivo:
    conteudo = arquivo.read() 

palavras = conteudo.split()
palavras=[palavra.split(",.!?\"'").lower() for palavra in palavras]
print(palavras)
   



























