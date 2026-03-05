#inicialização de variáveis

idade = 25
maior_idade = 18
renda = 30000
renda_base = 25000

#Execução dos operadores lógicos

elegivel = idade >= maior_idade and renda > renda_base
print(" Saída do operador AND:", elegivel)

#atualização da renda
renda = 20000

elegivel = idade >= maior_idade or renda > renda_base
print("Saída do operador OR:", elegivel)

elegivel = idade >= maior_idade and not renda > renda_base
print("Saída do operador NOT:", elegivel)

#atualização da renda
renda = 30000

elegivel = idade >= maior_idade and not renda > renda_base
print("Saída do operador NOT:", elegivel)



