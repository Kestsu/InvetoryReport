from inventory_report.reports.simple_report import SimpleReport
from abc import ABC


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
