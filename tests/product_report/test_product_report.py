from inventory_report.inventory.product import Product


def __repr__():
    pass

def test_relatorio_produto():
    
    product_instance = Product(  
    1,
    "CADEIRA",
    "Forces of Nature",
    "2022-04-04",
    "2023-02-09",
    "FR48",
    "Conservar em local fresco",
    )

    assert product_instance == (f"O produto CADEIRA fabricado em 2022-04-04 por"
    f" Forces of Nature com validade até 2023-02-09"
    f" precisa ser armazenado Conservar em local fresco.")