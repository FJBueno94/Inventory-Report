from inventory_report.importer.importer import Importer
from csv import DictReader


class CsvImporter(Importer):
    def import_data(cls, path):
        if path.endswith(".csv"):
            with open(path, "r", encoding='utf-8') as file:
                reader = DictReader(file, delimiter=',', quotechar='"')
            return list(reader)
        raise ValueError("Extensão de arquivo não suportada")
