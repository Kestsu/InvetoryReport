from abc import ABC
import csv
import json
import xml.etree.ElementTree as ET
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory(ABC):

    def import_data(path: str, type_report: str):

        if path.endswith(".csv"):
            with open(path, mode='r', encoding="utf-8") as file:
                data = list(csv.DictReader(file))
            if type_report == "simples":
                return SimpleReport.generate(data)
            return CompleteReport.generate(data)

        elif path.endswith(".json"):
            with open("inventory_report/data/inventory.json") as json_file:
                data = json.load(json_file)
            if type_report == "simples":
                return SimpleReport.generate(data)
            return CompleteReport.generate(data)

        else:
            tree = ET.parse(path)
            root = tree.getroot()
            data = []
            for elemento in root:

                dicionario = {}
                for filho in elemento:
                    dicionario[filho.tag] = filho.text

                data.append(dicionario)

            if type_report == "simples":
                return SimpleReport.generate(data)
            return CompleteReport.generate(data)
