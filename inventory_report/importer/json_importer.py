from abc import ABC
import json
from inventory_report.reports.simple_report import CompleteReport
from inventory_report.reports.complete_report import SimpleReport

class JsonImporter(ABC):

    @staticmethod
    def import_data(path: str, type_report: str):

        with open("inventory_report/data/inventory.json") as json_file:
            data = json.load(json_file)
        if type_report == "simples":
            return SimpleReport.generate(data)
        else:
            return CompleteReport.generate(data)

        except ValueError:
            raise ValueError("Arquivo inválido")
