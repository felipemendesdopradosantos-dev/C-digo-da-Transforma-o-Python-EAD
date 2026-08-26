# Script completo e unificado (sem precisar de arquivos separados)

import datetime
from faker import Faker

fake = Faker('pt_BR')

# Funções de utilidades embutidas
def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Erro: Divisão por zero"
    return a / b

def divisao_inteira(a, b):
    if b == 0:
        return "Erro: Divisão por zero"
    return a // b

def resto_divisao(a, b):
    if b == 0:
        return "Erro: Divisão por zero"
    return a % b

def potencia(base, exp):
    return base ** exp

# Execução do programa
print('**Dados Criados - Prova de Matemática**')
print(f'Nome: {fake.name()}')
print(f'E-Mail: {fake.email()}')
print(f'Telefone: {fake.phone_number()}')

print('Dados da Prova *')
agora = datetime.datetime.now()
print(f'Data e hora: {agora.strftime("%H:%M %d/%m/%Y")}')

num1, num2 = 10, 5

print('⚙️ Teste de Utilidades ⚙️')
print(f'Números: {num1} e {num2}')
print(f'Adição: {somar(num1, num2)}')
print(f'Subtração: {subtrair(num1, num2)}')
print(f'Multiplicação: {multiplicar(num1, num2)}')
print(f'Divisão: {dividir(num1, num2)}')
print(f'Divisão Inteira: {divisao_inteira(num1, num2)}')
print(f'Resto: {resto_divisao(num1, num2)}')
print(f'Potenciação: {potencia(num1, num2)}')

print('\n=== TESTE DE SEGURANÇA ===')
print(f'Divisão por zero: {dividir(10, 0)}')