class pessoa:
    #criação de atributos para pessoa.
    nome_pessoa = ""
    idade_pessoa = 0
    #método para mostrar os dados da pessoa.
    def falar_pessoa(self, falar_nome, falar_idade):
        self.falar_nome = self.nome_pessoa
        self.falar_idade = self.idade_pessoa

class veiculo:
    #criação de atributos para veiculo.
    nome_veiculo = ""
    marca_veiculo = ""
    #método para mostrar os dados do veiculo.
    def falar_veiculo(self, falar_nome, falar_marca):
        self.falar_nome = self.nome_veiculo
        self.falar_marca = self.marca_veiculo

class animal:
    #criação de atributos para animal.
    nome_animal = ""
    especie_animal = ""
    #método para mostrar os dados do animal.
    def falar_animal(self, falar_nome, falar_especie):
        self.falar_nome = self.nome_animal
        self.falar_especie = self.especie_animal

#instanciando a classe pessoa, ou seja, criando um objeto da classe pessoa.
pessoa1 = pessoa()      
pessoa1.nome_pessoa = "João"
pessoa1.idade_pessoa = 30       

#instanciando a classe veiculo, ou seja, criando um objeto da classe veiculo.
veiculo1 = veiculo()
veiculo1.nome_veiculo = "Fiat"
veiculo1.marca_veiculo = "Uno"

#instanciando a classe animal, ou seja, criando um objeto da classe animal.
animal1 = animal()
animal1.nome_animal = "Rex"
animal1.especie_animal = "Cachorro"

print("Dados da pessoa: {pessoa1.nome_pessoa} - {pessoa1.idade_pessoa}".format(pessoa1=pessoa1))
print("Dados do veiculo: {veiculo1.nome_veiculo} - {veiculo1.marca_veiculo}".format(veiculo1=veiculo1))
print("Dados do animal: {animal1.nome_animal} - {animal1.especie_animal}".format(animal1=animal1))