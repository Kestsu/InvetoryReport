from inventory_report.inventory.product import Product


def test_cria_produto():

    id = 1
    nome_do_produto = "CADEIRA"
    nome_da_empresa = "Forces of Nature"
    data_de_fabricacao = "2022-04-04"
    data_de_validade = "2023-02-09"
    numero_de_serie = "FR48"
    instrucoes = "Conservar em local fresco"

    product_instance = Product(
        id,
        nome_do_produto,
        nome_da_empresa,
        data_de_fabricacao,
        data_de_validade,
        numero_de_serie,
        instrucoes,
    )

    assert product_instance.id == id
    assert product_instance.nome_do_produto == nome_do_produto
    assert product_instance.nome_da_empresa == nome_da_empresa
    assert product_instance.data_de_fabricacao == data_de_fabricacao
    assert product_instance.data_de_validade == data_de_validade
    assert product_instance.numero_de_serie == numero_de_serie
    assert product_instance.instrucoes_de_armazenamento == instrucoes
