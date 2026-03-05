#inicialializações de varáveis
nota_a = 10; nota_b = 10; nome = "Eduardo"; sobrenome = " Coelho"

#expressões e condicionais
#Execucução da estrutura para impressão em tela

nome_completo = nome + " " + sobrenome
print("Qual o nome do desenvolvedor: ", nome_completo)

media = nota_a + nota_b / 2
print("Média de notas sem PEMDAS:", media)

media = (nota_a + nota_b) / 2
print("Média de notas com PEMDAS:", media)

#Estrutura condicional
nota1 = 6; nota2 = 7; nota3 = 8
notaDoAluno = (nota1 + nota2 + nota3) / 3
mediaEscolar = 7.0

if(notaDoAluno >= mediaEscolar):
    print("O aluno foi aprovado! \nMédia do aluno foi: ", notaDoAluno)
else:
    print("O aluno foi reprovado! \nMédia do aluno foi: ", notaDoAluno)
