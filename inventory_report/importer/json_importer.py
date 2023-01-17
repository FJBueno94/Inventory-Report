from inventory_report.importer.importer import Importer
import json


class JsonImporter(Importer):
    @classmethod
    def import_data(cls, path):
        if path.endswith(".json"):
            with open(path, "r", encoding='utf-8') as file:
                return json.load(file)
        raise ValueError("Arquivo inválido")
