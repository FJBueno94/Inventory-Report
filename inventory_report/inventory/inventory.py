from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import csv
import json


class Inventory:
    def import_data(path, type):
        if path.endswith(".csv"):
            with open(path, "r") as file:
                reader = csv.DictReader(file)
                info = [row for row in reader]
        elif path.endswith(".json"):
            with open(path, "r") as file:
                info = json.load(file)

        if type == "simples":
            return SimpleReport.generate(info)
        elif type == "completo":
            return CompleteReport.generate(info)
        else:
            raise ValueError("Relatório invalido!")
