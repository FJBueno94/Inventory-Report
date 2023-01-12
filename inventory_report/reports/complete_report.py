from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    def generate(inventory):
        simple_report = SimpleReport.generate(inventory)

        qtd = {}

        for item in inventory:
            if item["nome_da_empresa"] not in qtd:

                qtd[item["nome_da_empresa"]] = 1
            else:
                qtd[item["nome_da_empresa"]] += 1

            relatorio_empresa = ''

            for empresa, quantidade in qtd.items():
                relatorio_empresa += f"- {empresa}: {quantidade}\n"

        return (
            f"{simple_report}\n"
            f"Produtos estocados por empresa:\n"
            f"{relatorio_empresa}"
        )
