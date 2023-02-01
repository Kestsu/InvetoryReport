from abc import ABC, abstractmethod


class Importer(ABC):

    @classmethod
    @abstractmethod
    def import_data(path: str):
        raise NotImplementedError("Error desconhecido")


# teste = Importer.import_data(
#     'inventory_report/data/inventory.csv', 'simples', CsvImporter)
# print(teste)
