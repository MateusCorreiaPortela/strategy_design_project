from abc import ABC, abstractmethod


class Strategy(ABC):
    @abstractmethod
    def search_zip_code(self, cep):
        pass
