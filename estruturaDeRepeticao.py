#Os loopings do tipo “For” podem ser utilizados para a iteração de informações e principalmente sobre uma sequência criada, como por exemplo, em uma lista, tupla e etc. Ao se implementá-lo sobre um bloco de código, o looping será executado até que sejam finalizadas as iterações baseadas nos itens da estrutura selecionada. 

#Inicializaç]ão da lista para aplicação do looping do tipo “For”

nomes = ["Abilio", "Eduardo", "Maria", "João"]

#execução do looping do tipo “For” para iteração sobre a lista de nomes

for nome in nomes:
    print(nome)

#Função do tipo “Range” para aplicação do looping do tipo “For” para iteração sobre uma sequência de números
for numero in range(1, 11, 2):
    print(numero)

# No caso dos loopings do tipo “While”, assim como a leitura de sua tradução literal “Enquanto”, o looping será executado até que uma condição seja finalizada.

#Inicialização da variável para aplicação do looping do tipo “While”

contador = 0

while contador < 6:
    print("Contador incrementando:", contador)
    contador += 1

contador = 5
while contador > 0:
    print("Contador em decremento:", contador)
    contador -= 1