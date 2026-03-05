 #Declaração de variáveis
idade = 30
altura = 1.67
nome = "Eduardo"
ativo_para_acesso = True
restricao = False

 #Impressão das variáveis
print("idade:", idade)
print("Altura:", altura)
print("Nome:", nome)
print("Ativo para acesso:", ativo_para_acesso)
print("Restrição:", restricao)


#variáveis locais E globais
variavel_global = "Abilio"

def variavel_local():
    nome_local = "Eduardo"
    print("Variável local:", nome_local)
variavel_local()

print("variável global:", variavel_global)