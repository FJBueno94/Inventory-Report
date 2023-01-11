from inventory_report.inventory.product import Product

numero_de_serie = '123456789'


def test_cria_produto():
    productMock = Product(
        1,
        'Coca-Cola',
        'Coca-Cola Company',
        '01/01/2023',
        '28/02/2033',
        '123456789',
        'em local seco e arejado'
    )

    assert productMock.id == 1
    assert productMock.nome_do_produto == 'Coca-Cola'
    assert productMock.nome_da_empresa == 'Coca-Cola Company'
    assert productMock.data_de_fabricacao == '01/01/2023'
    assert productMock.data_de_validade == '28/02/2033'
    assert productMock.numero_de_serie == '123456789'
    assert productMock.instrucoes_de_armazenamento == 'em local seco e arejado'
