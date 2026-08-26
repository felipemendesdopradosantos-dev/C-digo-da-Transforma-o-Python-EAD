# que é o pacot e de utilidades que
# e um sistema

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return 0
    return a / b

def em_moeda(valor):
    return f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")