# from abc import ABC
import csv
from inventory_report.importer.importer import Importer
# from inventory_report.reports.simple_report import SimpleReport
# from inventory_report.reports.complete_report import CompleteReport


class CsvImporter(Importer):

    @staticmethod
    def import_data(path: str):
        if path.endswith(".csv"):
            try:
                with open(path, mode='r', encoding="utf-8") as file:
                    data = list(csv.DictReader(file))
                    return data
            # if type_report == "simples":
            #     return SimpleReport.generate(data)
            # else:
            #     return CompleteReport.generate(data)

            except AttributeError:
                raise ValueError("Arquivo inválido")
        raise ValueError("Arquivo inválido")
