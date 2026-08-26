# Cadastro de veículos em Python.

class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def exibir_info(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}"

print("🚗 CADASTRO 🚗\n")
m = input("Marca: ")
mod = input("Modelo: ")
meu_carro = Carro(m, mod)
print(meu_carro.exibir_info())