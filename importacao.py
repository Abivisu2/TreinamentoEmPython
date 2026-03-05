#Importação de um módulo em Python
# Exemplos de implementação de cálculo de raiz quadrada com a função sqrt().

import math as matematica
#Utilização de funções do módulo importado
x = matematica.sqrt(64)
print(x)

#Importação de um função específico
from math import sqrt
a = sqrt(49)
print(a)

#Exemplo de carregamento da biblioteca math e importação de todas as suas funções.
from math import *
b = sqrt(25)
print(b)