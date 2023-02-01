from abc import ABC
import csv
from inventory_report.reports.simple_report import CompleteReport
from inventory_report.reports.complete_report import SimpleReport

class CsvImporter(ABC):

    @staticmethod
    def import_data(path: str, type_report: str):
        try:
            with open(path, mode='r', encoding="utf-8") as file:
                data = list(csv.DictReader(file))
            if type_report == "simples":
                return SimpleReport.generate(data)
            else:
                return CompleteReport.generate(data)
        
        except ValueError:
            raise ValueError("Arquivo inválido")