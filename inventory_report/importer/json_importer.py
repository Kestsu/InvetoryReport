# from abc import ABC, abstractmethod
import json
from inventory_report.importer.importer import Importer
# from inventory_report.reports.simple_report import SimpleReport
# from inventory_report.reports.complete_report import CompleteReport


class JsonImporter(Importer):

    @staticmethod
    def import_data(path: str):
        if path.endswith(".json"):
            try:
                with open("inventory_report/data/inventory.json") as json_file:
                    data = json.load(json_file)
                    return data
            # if type_report == "simples":
            #     return SimpleReport.generate(data)
            # else:
            #     return CompleteReport.generate(data)

            except AttributeError:
                raise ValueError("Arquivo inválido")
        raise ValueError("Arquivo inválido")
