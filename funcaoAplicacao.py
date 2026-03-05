#Implementação de uma função em Python

def calcular_soma(valor1, valor2):
    resultado = valor1 + valor2
    return resultado

#Chamada da função e exibição do resultado
print("Resultado da operação de soma: ", calcular_soma(5, 6))

#Variavel Local 
def minha_funcao():
    nome = "Eduardo"
    print("Variável local:", nome)
minha_funcao()

#Variavel Global
variavel_global = 10
def minha_funcao_global():
    print("Variável global:", variavel_global)

minha_funcao_global()
print("Variável global fora da função:", variavel_global)