# Lista de clientes (convertida de JSON para formato de lista de dicionários em Python)
clientes = [
    {
        "Nome completo": "Ivan Silva",
        "idade": "40 anos",
        "CEP": "02899-000",
        "ResgMatr": "947541",
        "E-Mail": "ivanpaulino@mail.com"
    },
    {
        "Nome completo": "Beatriz Vitoria",
        "idade": "30 anos",
        "CEP": "057193-000",
        "ResgMatr": "978786",
        "E-Mail": "beavitoria@mail.com"
    },
    {
        "Nome completo": "Eric Renan",
        "idade": "17 anos",
        "CEP": "089880-100",
        "ResgMatr": "98799",
        "E-Mail": "ericrenan@gmail.com"
    }
]

# Sistema de Lista de Compras
compras = []

while True:
    print("\n--- LISTA DE COMPRAS ---")
    print(f"Itens atuais: {compras}")
    print("1. Adicionar item")
    print("2. Remover item")
    print("3. Sair")
    
    opcao = input("Escolha uma opção: ")
    
    if opcao == "1":
        item = input("Digite o item para adicionar: ")
        compras.append(item)
        print(f"'{item}' foi adicionado.")
    elif opcao == "2":
        item = input("Digite o item para remover: ")
        if item in compras:
            compras.remove(item)
            print(f"'{item}' foi removido.")
        else:
            print("Item não encontrado na lista.")
    elif opcao == "3":
        print("Saindo...")
        break
    else:
        print("Opção inválida.")