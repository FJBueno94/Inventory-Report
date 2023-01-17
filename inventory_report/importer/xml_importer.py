from inventory_report.importer.importer import Importer
import xml.etree.ElementTree as ET
# https://docs.python.org/3/library/xml.etree.elementtree.html


class XmlImporter(Importer):
    def import_data(cls, path):
        if path.endswith(".xml"):
            with open(path, "r", encoding='utf-8') as file:
                products_list = list()
                tree = ET.parse(file)
                root = tree.getroot()
                for product in root:
                    products = {
                        element.tag: element.text for element in product
                    }
                    products_list.append(products)
                return products_list
        raise ValueError("Extensão de arquivo não suportada")
