import xml.etree.ElementTree as ET
from inventory_report.importer.importer import Importer


class XmlImporter(Importer):

    @staticmethod
    def import_data(path: str):
        if path.endswith(".xml"):
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
            return data

        raise ValueError("Arquivo inválido")
