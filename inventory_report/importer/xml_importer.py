from abc import ABC
import xml.etree.ElementTree as ET
from inventory_report.reports.simple_report import CompleteReport
from inventory_report.reports.complete_report import SimpleReport

class XmlImporter(ABC):

    @staticmethod
    def import_data(path: str, type_report: str):
        tree = ET.parse(path) #Carregar o arquivo XML
        root = tree.getroot() # Raiz do documento
        data = []
        for elemento in root: # Passar cada elemento

            dicionario = {}
            for filho in elemento:  
                dicionario[filho.tag] = filho.text # filho.tag pegar so a string E Adicionar o nome do elemento e o seu conteudo ao dicionário
                data.append(dicionario)  #Adicionar o dicionário a lista

        if type_report == "simples":
            return SimpleReport.generate(data)
        else:
            return CompleteReport.generate(data)

        except ValueError:
            raise ValueError("Arquivo inválido")