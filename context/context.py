from interfaces.strategy import Strategy


class Context:
    def __init__(self):
        self.strategy = None

    def set_strategy(self, strategy: Strategy):
        self.strategy = strategy

    def execute(self, cep: str):
        if not self.strategy:
            print("❌ Erro: Nenhuma estratégia de busca foi selecionada!", flush=True)
            return None

        self.strategy.search_zip_code(cep)
