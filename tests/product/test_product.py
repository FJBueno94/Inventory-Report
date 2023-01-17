from inventory_report.inventory.product import Product


def test_cria_produto():
    product_mock = Product(
        1,
        'Coca-Cola',
        'Coca-Cola Company',
        '01/01/2023',
        '28/02/2033',
        '123456789',
        'em local seco e arejado'
    )

    assert product_mock.id == 1
    assert product_mock.nome_do_produto == 'Coca-Cola'
    assert product_mock.nome_da_empresa == 'Coca-Cola Company'
    assert product_mock.data_de_fabricacao == '01/01/2023'
    assert product_mock.data_de_validade == '28/02/2033'
    assert product_mock.numero_de_serie == '123456789'
    assert product_mock.instrucoes_de_armazenamento == 'local seco e arejado'
