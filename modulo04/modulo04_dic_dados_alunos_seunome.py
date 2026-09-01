# ======================================================================
# 🚀 Projeto: Dados de Alunos com Dicionários
# ======================================================================

# 📋 Passo 1: Criar o Dicionário
# Este é o nosso "recipiente" para guardar as informações do aluno.
# Cada item tem uma "chave" (como 'nome') e um "valor" (como 'João').
aluno = {
    "nome": "João da Silva",
    "idade": 17,
    # As notas são guardadas em uma lista, pois são vários valores.
    "notas": [8.5, 7.0, 9.5] 
}

# ======================================================================
# 🔄 Passo 2: Mostrar os dados no console
# Vamos imprimir as informações de forma clara.

print("--- Ficha do Aluno ---")

# Acessamos cada valor do dicionário usando sua chave.
# É como pedir: "Qual o valor da chave 'nome'?"
print(f"Nome: {aluno['nome']}")
print(f"Idade: {aluno['idade']} anos")

# Calculamos a média das notas para mostrar.
# A função 'sum()' soma todos os números da lista e 'len()' conta quantos são.
media_das_notas = sum(aluno['notas']) / len(aluno['notas'])
print(f"Média das notas: {media_das_notas:.2f}") # O ': .2f' formata o número com 2 casas decimais.

# Também podemos imprimir todas as notas.
print(f"Notas: {aluno['notas']}")

print("----------------------")

# ======================================================================
# ✨ Bônus: Iterando pelo Dicionário
# Uma forma mais avançada e legal de mostrar todos os dados.
# Este 'for' percorre todas as "chaves" e "valores" do dicionário de uma vez.
print("\n--- Todos os Dados ---")
for chave, valor in aluno.items():
    print(f"{chave.capitalize()}: {valor}")

# ======================================================================
# 🏁 Fim do Programa
# ======================================================================
