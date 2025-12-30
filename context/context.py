from interfaces.strategy import Strategy


class Context:
    def __init__(self, strategy: Strategy, cep: str):
        self.cep = cep
        self.strategy = strategy

    def set_strategy(self, strategy: Strategy):
        self.strategy = strategy

    def execute(self):
        self.strategy.search_zip_code(self.cep)
