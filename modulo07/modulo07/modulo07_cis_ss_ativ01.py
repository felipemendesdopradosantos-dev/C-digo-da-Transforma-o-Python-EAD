# utilidades que e uma sistema 
# de calculos matematicos

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

def calcular_media(*args):
    if not args:
        return 0
    return sum(args) / len(args)

def e_par(*args):
    return [num % 2 == 0 for num in args]