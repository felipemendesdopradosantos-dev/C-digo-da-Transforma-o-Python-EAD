# Este código demonstra o conceito de herança em Programação Orientada a Objetos em Python.
# Ele cria uma classe base Carro e uma classe filha CarroEletrico com atributos e métodos próprios.

class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def exibir_info(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}"

class CarroEletrico(Carro):
    def __init__(self, marca, modelo, autonomia_bateria):
        super().__init__(marca, modelo)
        self.autonomia = autonomia_bateria

    def exibir_info(self):
        info_base = super().exibir_info()
        return f"{info_base} | Autonomia da Bateria: {self.autonomia} km"

meu_carro = CarroEletrico("BYD", "Dolphin", 600)
print(meu_carro.exibir_info())
