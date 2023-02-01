from abc import ABC

class Importer(ABC):
    def import_data(
        self, path: str, type_report: str, 
        strategy_csv: CsvImporter, 
        strategy_json: JsonImporter,
        strategy_xml: XmlImporter,
    ):
        try:
            if path.endswith(".csv"):
                return strategy_csv(path, type_report)
            elif path.endswith(".json"):
                return strategy_json(path, type_report)
            else:
                return strategy_xml(path, type_report)
            
        except ValueError:
            raise ValueError("Arquivo inválido")
