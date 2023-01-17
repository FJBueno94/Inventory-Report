from inventory_report.inventory.product import Product


def test_relatorio_produto():
    product_mock = Product(
        1,
        'Coca-Cola',
        'Coca-Cola Company',
        '01/01/2023',
        '28/02/2033',
        '123456789',
        'em local seco'
    )

    assert product_mock.__repr__() == (
        "O produto Coca-Cola fabricado em 01/01/2023 por Coca-Cola Company"
        " com validade até 28/02/2033 precisa ser armazenado"
        " em local seco."
    )