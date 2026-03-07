class pessoa:
    def __init__(self, nome):
        self.nome = nome
        def falar(self):
            pass

class coordenador(pessoa):
    def falar(self):
        return f"Olá, meu nome é {self.nome} e sou coordenador"
class gerente(pessoa):
    def falar(self):
        return f"Olá, meu nome é {self.nome} e sou gerente"
            
#Declarando os objetos da classe coordenador e gerente.
pessoa1 = coordenador(input("Digite o nome do coordenador: "))
pessoa2 = gerente(input("Digite o nome do gerente: "))

#Impressão dos métodos falar para os objetos criados.
print(pessoa1.nome)
print(pessoa1.falar())
print(pessoa2.nome)
print(pessoa2.falar())