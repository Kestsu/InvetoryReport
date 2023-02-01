# from abc import ABC, abstractmethod
import xml.etree.ElementTree as ET
from inventory_report.importer.importer import Importer
# from inventory_report.reports.simple_report import SimpleReport
# from inventory_report.reports.complete_report import CompleteReport


class XmlImporter(Importer):

    @staticmethod
    def import_data(path: str):
        if path.endswith(".xml"):
            try:
                # Carregar o arquivo XML
                tree = ET.parse(path)
                # Raiz do documento
                root = tree.getroot()
                data = []
                # Passar cada elemento
                for elemento in root:

                    dicionario = {}
                    for filho in elemento:
                        # filho.tag pegar so a string E Adicionar o nome do
                        # elemento e o seu conteudo ao dicionário
                        dicionario[filho.tag] = filho.text
                        # Adicionar o dicionário a lista

                    data.append(dicionario)

            # if type_report == "simples":
            #     return SimpleReport.generate(data)
            # else:
            #     return CompleteReport.generate(data)
                return data

            except AttributeError:
                raise ValueError("Arquivo inválido")
        raise ValueError("Arquivo inválido")
