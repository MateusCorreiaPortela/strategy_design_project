import requests

from interfaces.strategy import Strategy


class ViaCepService(Strategy):
    def search_zip_code(self, cep):
        data = self.get_request_data(cep=cep)

        if not data:
            return

        print(self.format_data(data), flush=True)

    def get_request_data(self, cep):
        response = requests.get(f"http://viacep.com.br/ws/{cep}/json/")
        data = response.json()

        if not self.validate_status(response.status_code):
            return

        return data

    def validate_status(self, status: int):
        if status != 200:
            return False

        return True

    def format_data(self, data: dict):
        return (
            f'CEP: {data["cep"]}, CIDADE: {data["localidade"]}, '
            f'BAIRRO: {data["bairro"]}, RUA: {data["logradouro"]}, '
            f'ESTADO {data["estado"]}, REGIÂO {data["regiao"]}'
        )
