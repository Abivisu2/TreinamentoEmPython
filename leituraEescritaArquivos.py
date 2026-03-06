with open("exemplo_de_escrita.txt", "w") as arquivo_escrita:
    #Escreve uma linha no arquivo
    arquivo_escrita.write("Programação em Python é muito divertida!\n")
    arquivo_escrita.write("Texto externo!\n")

with open("exemplo_de_escrita.txt", "r") as arquivo_leitura:
    #Leitura de informações em arquivo de texto externo
    mensagem = arquivo_leitura.read()
    print("Conteúdo do arquivo de leitura: \n", mensagem)