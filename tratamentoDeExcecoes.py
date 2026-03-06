#Exercícios para tratamento de exceções

numero_inicial = input("Digite um número inteiro de 1 a 10:")
try:
    numero_inicial = int(numero_inicial)
    resultado = 10 / numero_inicial
except ValueError as  value_error:
    print(f"Erro de valor: {value_error}")
except ZeroDivisionError as  Zero_division_error:
    print(f"Erro de divisão por zero: {Zero_division_error}")
except Exception as  Exception:
    print(f"Outros tipos de erros: {Exception}")
else:
    print(f'Resultado da divisão: {resultado}')

#Figura 67: Exemplo de implementação de situação-problema onde analisamos o tratamento de uma variável para a retirada de números.

try:
    nome = input("Digite o seu nome: ")
    for caractere in nome:
        if '0' <= caractere <= '9':
            raise ValueError("O nome não pode conter números, tenta novamente!")    
    print(f"Olá, senhor {nome}!")
except ValueError as e:
    print(f"Valor digitado inválido: {e}")
finally:
    print("Exemplo de tratamento de exceções completo, com try, raise, except e finally.")

