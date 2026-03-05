#ESTRUTURAS DE DADOS EM PYTHON

#1 - Listas - São estruturas de dados mutáveis, ou seja, podem ser modificadas após a criação. Elas são definidas usando colchetes [] e podem conter elementos de diferentes tipos.

#Inicialização de listas
lista_numeros = [1, 2, 3, 4, 5]
lista_strings = ["Python", "Java", "C++", "JavaScript"]
lista_mista = [1, "Python", 3.14, True]
lista_vazia = []
#Implementação e execução de listas
print("Lista de números:", lista_numeros)
print("Lista de strings:", lista_strings) 
print("Lista mista:", lista_mista)
print("Lista vazia:", lista_vazia)

#2 - Tuplas - São estruturas de dados imutáveis, ou seja, não podem ser modificadas após a criação. Elas são definidas usando parênteses () e também podem conter elementos de diferentes tipos.

#Inicialização de tuplas
tupla_numeros = (1, 2, 3, 4, 5)
tupla_strings = ("Python", "Java", "C++", "JavaScript")
tupla_mista = (1, "Python", 3.14, True)
tupla_vazia = ()
#Implementação e execução de tuplas
print("Tupla de números:", tupla_numeros)
print("Tupla de strings:", tupla_strings) 
print("Tupla mista:", tupla_mista)
print("Tupla vazia:", tupla_vazia)

#3 - conjuntos - São estruturas de dados que armazenam elementos únicos e não ordenados. Eles são definidos usando chaves {} e são úteis para operações de conjunto, como união, interseção e diferença.

#Inicialização de conjuntos
conjunto_1 = {1,2,3}
conjunto_2 = set([3,4,5])
conjunto_vazio = set()
conjunto_misto = conjunto_1 | conjunto_2

#Implementação e execução de conjuntos
print("Conjunto 1:", conjunto_1)
print("Conjunto 2:", conjunto_2)
print("Conjunto vazio:", conjunto_vazio)
print("Conjunto misto:", conjunto_misto)

#4 - Dicionários - São estruturas de dados que armazenam pares de chave-valor. Eles são definidos usando chaves {} e cada chave é associada a um valor correspondente. Os dicionários são mutáveis e permitem acesso rápido aos valores com base nas chaves.

#Inicialização de dicionários

Pessoa = {
    'nome': 'Abilio',
    'idade': 30,
    'altura': 1.67,
    'telefone': '123456789',
    'ativo_para_acesso': False
}

#Implementação e execução de dicionários
print("Dicionário Pessoa:", Pessoa)
print("nome da Pessoa:", Pessoa['nome'], "\nidade:", Pessoa['idade'] )