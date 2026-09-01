# ======================================================================
# 🚀 Desafio Extra: Agenda de Contatos com Dicionários
# ======================================================================

# 📋 Passo 1: A nossa "base de dados" da agenda
# Criamos um dicionário vazio que vai guardar todos os contatos.
# A chave de cada item será o nome do contato.
agenda = {}

# ======================================================================
# 🔄 Passo 2: O Loop do Menu Principal
# O programa vai rodar infinitamente até você escolher sair.
while True:
    # Mostramos as opções disponíveis.
    print("\n--- Menu da Agenda ---")
    print("1. Adicionar Contato")
    print("2. Remover Contato")
    print("3. Buscar Contato")
    print("4. Ver Todos os Contatos")
    print("5. Sair")
    
    # Pegamos a escolha do usuário.
    escolha = input("Escolha uma opção (1-5): ")

    # ======================================================================
    # 🚦 Passo 3: Lógica das Opções
    # Usamos 'if/elif/else' para controlar a ação baseada na escolha.

    # ➕ Opção 1: Adicionar Contato
    if escolha == '1':
        nome = input("Digite o nome do contato: ")
        # Verificamos se o nome já existe na agenda.
        if nome in agenda:
            print(f"❌ Erro: O contato '{nome}' já existe.")
        else:
            telefone = input("Digite o telefone: ")
            email = input("Digite o email: ")
            # Criamos um novo dicionário com os detalhes e o guardamos
            # dentro da nossa 'agenda', usando o nome como chave.
            agenda[nome] = {"telefone": telefone, "email": email}
            print(f"✅ Contato '{nome}' adicionado com sucesso!")

    # ➖ Opção 2: Remover Contato
    elif escolha == '2':
        nome = input("Digite o nome do contato para remover: ")
        # Verificamos se o nome existe antes de tentar remover.
        if nome in agenda:
            del agenda[nome]
            print(f"🗑️ Contato '{nome}' removido.")
        else:
            print(f"❌ Erro: O contato '{nome}' não foi encontrado.")

    # 🔎 Opção 3: Buscar Contato
    elif escolha == '3':
        nome = input("Digite o nome do contato para buscar: ")
        # Verificamos se o nome existe.
        if nome in agenda:
            # Pegamos o dicionário de detalhes do contato.
            contato = agenda[nome]
            print(f"\n--- Detalhes do Contato: {nome} ---")
            print(f"Telefone: {contato['telefone']}")
            print(f"Email: {contato['email']}")
            print("---------------------------------------")
        else:
            print(f"❌ Erro: O contato '{nome}' não foi encontrado.")
            
    # 👁️ Opção 4: Ver Todos os Contatos
    elif escolha == '4':
        if not agenda:
            print("📝 Sua agenda está vazia.")
        else:
            print("\n--- Todos os Contatos ---")
            # Percorremos a agenda para mostrar cada contato.
            for nome, detalhes in agenda.items():
                print(f"Nome: {nome}")
                print(f"  Telefone: {detalhes['telefone']}")
                print(f"  Email: {detalhes['email']}")
                print("-------------------------")
            
    # 🛑 Opção 5: Sair
    elif escolha == '5':
        print("👋 Saindo da agenda. Até mais!")
        break # Sai do loop e encerra o programa.
    
    # ❓ Opção Inválida
    else:
        print("🚫 Opção inválida. Por favor, digite um número de 1 a 5.")

# ======================================================================
# 🏁 Fim do Programa
# ======================================================================
