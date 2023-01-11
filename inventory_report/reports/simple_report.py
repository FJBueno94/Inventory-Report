import datetime
from collections import Counter


class SimpleReport:
    def generate(inventory):
        fabricação_mais_antigo = min(
            [item["data_de_fabricacao"] for item in inventory]
        )

        data = datetime.date.today().strftime("%d/%m/%Y")

        validade_mais_novo = min(
            [item["data_de_validade"] for item in inventory
                if item["data_de_validade"] > data]
        )

        nome_fabrica = [empresa["nome_da_empresa"] for empresa in inventory]

        empresa_produtos, _ = Counter(nome_fabrica).most_common()[0]

        return (
            f"Data de fabricação mais antiga: {fabricação_mais_antigo}\n"
            f"Data de validade mais próxima: {validade_mais_novo}\n"
            f"Empresa com mais produtos: {empresa_produtos}"
        )
