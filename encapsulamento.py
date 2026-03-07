#Métodos Públicos
class pessoa:
    def __init__(self):
        self.idade_pessoa = 30
    def falar_publico(self):
        return f"Exemplo de método público"  
pessoa1  = pessoa()

print(pessoa1.idade_pessoa)
print(pessoa1.falar_publico())

#Métodos protegidos
print("Exemplo de método protegido")
class conta:
    def __init__(self):
        self._saldo_conta = 0

    def consulta_protegida(self):
        return f"Saldo na conta é de: {self._saldo_conta}"
#Criando um objeto da classe conta para acessar o método protegido.
consulta_banco = conta() 
print(consulta_banco._saldo_conta)
print(consulta_banco.consulta_protegida())

#Métodos privados
print("Exemplo de método privado")
class conta:
    def __init__(self):
        self._saldo_conta = 100

    def _consulta_privada(self):
        return f"Saldo na conta é de: {self._saldo_conta}"
#Criando um objeto da classe conta para acessar o método privado.
saldo = conta() 
print(saldo._consulta_privada())
