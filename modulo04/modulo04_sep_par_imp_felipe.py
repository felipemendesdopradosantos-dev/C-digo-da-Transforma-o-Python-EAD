# ======================================================================
# 🚀 Projeto: Separador de Pares e Ímpares
# ======================================================================

# 📋 Passo 1: A nossa lista de números
# Criamos uma lista com alguns números para testar.
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Criamos listas vazias para guardar os números que serão separados.
pares = []
impares = []

# ======================================================================
# 🔄 Passo 2: O Loop para verificar cada número
# O 'for' vai pegar cada número da nossa lista 'numeros'.
print("--- Verificando os números... ---")
for numero in numeros:
    # A verificação mágica:
    # O sinal '%' (módulo) dá o resto de uma divisão.
    # Se o resto da divisão do número por 2 for IGUAL a 0, ele é PAR.
    if numero % 2 == 0:
        # Se for par, adicionamos na lista de pares.
        print(f"O número {numero} é PAR.")
        pares.append(numero)
    else:
        # Se não for par, ele é ÍMPAR.
        print(f"O número {numero} é ÍMPAR.")
        impares.append(numero)

# ======================================================================
# 👁️ Passo 3: Exibir os resultados
# Depois que o loop termina, mostramos o resultado final.

print("\n--- Resultado Final ---")
print(f"Números Pares: {pares}")
print(f"Números Ímpares: {impares}")

# ======================================================================
# 🏁 Fim do Programa
# ======================================================================
