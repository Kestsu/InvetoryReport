from inventory_report.inventory.product import Product

def test_cria_produto():

    product_instance = Product(  
    1,
    "CADEIRA",
    "Forces of Nature",
    "2022-04-04",
    "2023-02-09",
    "FR48",
    "Conservar em local fresco",
    )

    assert product_instance.id == 1
    assert product_instance.nome_do_produto == "CADEIRA"
    assert product_instance.nome_da_empresa == "Forces of Nature"
    assert product_instance.data_de_fabricacao == "2022-04-04"
    assert product_instance.data_de_validade == "2023-02-09"
    assert product_instance.numero_de_serie == "FR48"
    assert product_instance.instrucoes_de_armazenamento == "Conservar em local fresco"