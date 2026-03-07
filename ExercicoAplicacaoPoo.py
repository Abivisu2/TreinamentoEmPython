class veiculo:
    def __init__(self, marca, modelo):
        self._marca = marca
        self._modelo = modelo

    def get_informacoes(self):
        return f"Marca: {self._marca}, Modelo: {self._modelo}"


class carro(veiculo):
    def __init__(self, marca, modelo, ano):
        super().__init__(marca, modelo)
        self._ano = ano

    def get_informacoes(self):
        return f"Tipo: Carro, {super().get_informacoes()}, Ano: {self._ano}"


def exibir_informacoes_veiculo(veiculo):
    print(veiculo.get_informacoes())


carro1 = carro("Fiat", "Uno", 2020)
carro2 = carro("Chevrolet", "Onix", 2021)

exibir_informacoes_veiculo(carro1)
exibir_informacoes_veiculo(carro2)