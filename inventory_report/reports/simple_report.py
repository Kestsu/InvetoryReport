from abc import ABC, abstractmethod
from datetime import datetime, date

class SimpleReport(ABC):

    @abstractmethod
    def generate(list: list[dict]):
        today_date = str(date.today())
        
        lista_date_fab = [
            item["data_de_fabricacao"]
            for item in list
        ]

        data_mais_antiga = min(lista_date_fab) 

        lista_date_val = [
            item["data_de_validade"]
            for item in list
        ]
        
        mais_perto = []

        for data in lista_date_val:
            if today_date < data:
                mais_perto.append(data)

        data_validade_perto = min(mais_perto)
        
        lista_de_empresa = [
            item["nome_da_empresa"]
            for item in list
        ]

        contagem = {}
        for item in lista_de_empresa:
            contagem[item] = contagem.get(item, 0) + 1

        # print(contagem)
        empresa_mais_repetida = max(contagem, key=contagem.get)

        return f"""Data de fabricação mais antiga: {data_mais_antiga}
Data de validade mais próxima: {data_validade_perto}
Empresa com mais produtos: {empresa_mais_repetida}"""

# testss = SimpleReport.generate(   [
#      {
#        "id": 1,
#        "nome_do_produto": "CADEIRA",
#        "nome_da_empresa": "Forces of Nature",
#        "data_de_fabricacao": "2022-04-01",
#        "data_de_validade": "2021-02-07",
#        "numero_de_serie": "FR48",
#        "instrucoes_de_armazenamento": "Conservar em local fresco"
#      },
#           {
#        "id": 1,
#        "nome_do_produto": "CADEIRA",
#        "nome_da_empresa": "Forces of Nature",
#        "data_de_fabricacao": "2022-04-04",
#        "data_de_validade": "2023-02-03",
#        "numero_de_serie": "FR48",
#        "instrucoes_de_armazenamento": "Conservar em local fresco"
#      },
#           {
#        "id": 1,
#        "nome_do_produto": "CADEIRA",
#        "nome_da_empresa": "Forces of",
#        "data_de_fabricacao": "2022-04-02",
#        "data_de_validade": "2023-02-01",
#        "numero_de_serie": "FR48",
#        "instrucoes_de_armazenamento": "Conservar em local fresco"
#      }
#    ])

# print(testss)

