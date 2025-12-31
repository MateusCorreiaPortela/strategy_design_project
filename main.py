import sys

from context.context import Context
from services.brasil_api import BrasilApiService
from services.via_cep import ViaCepService


class Client:
    def __init__(self):
        self.context = Context()
        self.brasil_api = BrasilApiService()
        self.via_cep = ViaCepService()

    def main(self) -> None:
        while True:
            print(
                "\nPor onde deseja buscar? Digite o valor referente ao serviço ou saida. Exemplo: 1\n"
                "\033[32m[ 1 ] - Brasil API \n[ 2 ] - Via CEP\033[m \n\033[31m[ 3 ] - Sair\033[m\n",
                flush=True
            )

            number = self.get_number_service()

            if number == 3:
                print("Volte sempre!", flush=True)
                sys.exit()

            self.context.set_strategy(self.get_service(number=number))
            self.context.execute(cep=str(input("CEP: ")))

    def get_number_service(self):
        while True:
            try:
                valor = int(input("Valor: "))

                if valor not in [1, 2, 3]:
                    print("Ta caindo aqui?")
                    raise ValueError("O valor deve ser válido")

                break

            except Exception as e:
                pass

        return valor

    def get_service(self, number: int):
        services = {
            1: self.brasil_api,
            2: self.via_cep,
        }

        return services[number]


if __name__ == "__main__":
    Client().main()
