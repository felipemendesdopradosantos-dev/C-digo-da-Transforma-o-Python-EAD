import hashlib
import getpass


# ==========================================
# 1. EXCEÇÕES PERSONALIZADAS
# ==========================================

class CredenciaisInvalidasError(Exception):
    """Usuário ou senha incorretos."""
    pass


class LimiteTentativasExcedidoError(Exception):
    """Limite máximo de tentativas atingido."""
    pass


# ==========================================
# 2. SERVIÇO DE AUTENTICAÇÃO
# ==========================================

class AuthService:
    def __init__(
        self,
        usuario_valido="dev_user",
        senha_valida="pass123",
        max_tentativas=3
    ):
        self._usuario_valido = usuario_valido
        self._senha_hash = self._gerar_hash(senha_valida)
        self.max_tentativas = max_tentativas
        self.tentativas_atuais = 0

    @staticmethod
    def _gerar_hash(senha):
        """Cria um hash da senha."""
        return hashlib.sha256(
            senha.encode("utf-8")
        ).hexdigest()

    def autenticar(self, usuario, senha):
        """Valida as credenciais do usuário."""

        if self.tentativas_atuais >= self.max_tentativas:
            raise LimiteTentativasExcedidoError(
                "Conta bloqueada por segurança."
            )

        senha_hash = self._gerar_hash(senha)

        usuario_valido = (
            usuario == self._usuario_valido
        )

        senha_valida = (
            senha_hash == self._senha_hash
        )

        if not usuario_valido or not senha_valida:
            self.tentativas_atuais += 1

            restantes = (
                self.max_tentativas
                - self.tentativas_atuais
            )

            if restantes == 0:
                raise LimiteTentativasExcedidoError(
                    "Acesso bloqueado! "
                    "Limite de tentativas atingido."
                )

            raise CredenciaisInvalidasError(
                "Credenciais incorretas. "
                f"Tentativas restantes: {restantes}"
            )

        self.tentativas_atuais = 0
        return True


# ==========================================
# 3. INTERFACE DE TERMINAL
# ==========================================

def executar_interface_login():
    """Executa a interface de login."""

    auth_system = AuthService(
        usuario_valido="dev_user",
        senha_valida="pass123",
        max_tentativas=3
    )

    print("=" * 42)
    print("       SISTEMA DE AUTENTICAÇÃO")
    print("=" * 42)

    while True:
        try:
            print("\nDigite suas credenciais:")

            usuario = input("Usuário: ")
            senha = getpass.getpass("Senha: ")

            if auth_system.autenticar(usuario, senha):
                print("\n[OK] Login realizado com sucesso!")
                print(f"[OK] Bem-vindo, {usuario}!")
                print("[OK] Acesso ao painel autorizado.")
                break

        except CredenciaisInvalidasError as erro:
            print(f"\n[ERRO] {erro}")

        except LimiteTentativasExcedidoError as erro:
            print(f"\n[BLOQUEADO] {erro}")
            print("[SISTEMA] Encerrando a sessão...")
            break

        except KeyboardInterrupt:
            print("\n\n[SISTEMA] Operação cancelada.")
            break


# ==========================================
# 4. EXECUÇÃO
# ==========================================

if __name__ == "__main__":
    executar_interface_login()
