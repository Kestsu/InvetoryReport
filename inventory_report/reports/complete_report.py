# from simple_report import SimpleReport
from inventory_report.reports.simple_report import SimpleReport
from abc import ABC
import json

class CompleteReport(ABC):
    def generate(list: list[dict]):
        simple_report = SimpleReport.generate(list)

        lista_de_empresa = [
             empresas["nome_da_empresa"] 
            for empresas in list
        ]

        contagem = {}
        for item in lista_de_empresa:
            contagem[item] = contagem.get(item, 0) + 1
        
        string = "Produtos estocados por empresa:"
        for item in contagem.items():
            string += "\n" + f"- {item[0]}: {item[1]}"
        
       

        return simple_report + "\n" + string + "\n"

# with open("inventory_report/data/inventory.json") as json_file:
#     dados = json.load(json_file)

#     testss = CompleteReport.generate(
#     dados
#     )

#     print(testss)

#  ✗ python3 inventory_report/reports/complete_report.py