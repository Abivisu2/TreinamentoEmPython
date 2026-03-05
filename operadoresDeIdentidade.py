#Criação das listas para aplicação dos operadndos de identidade
lista_1 = [1, 2, 3]
lista_2 = lista_1
lista_3 = [4, 5, 6]

#Execução dos operadores de identidade
mesmo_objeto = lista_1 is lista_2
print("Está incluído:", mesmo_objeto)

objeto_diferente = lista_1 is not lista_3
print("Está incluído:", objeto_diferente)