# from inventory_report.reports.colored_report import ColoredReport
# from inventory_report.reports.simple_report import SimpleReport


# def test_decorar_relatorio():

#     lista = [
#         {
#             "id": 1,
#             "nome_do_produto": "Cafe",
#             "nome_da_empresa": "Cafes Nature",
#             "data_de_fabricacao": "2020-07-04",
#             "data_de_validade": "2023-02-09",
#             "numero_de_serie": "FR48",
#             "instrucoes_de_armazenamento": "instrucao"
#         },
#         {
#             "id": 2,
#             "nome_do_produto": "Cafe",
#             "nome_da_empresa": "Cafes",
#             "data_de_fabricacao": "2020-07-04",
#             "data_de_validade": "2023-02-09",
#             "numero_de_serie": "FR48",
#             "instrucoes_de_armazenamento": "instrucao"
#         },
#         {
#             "id": 3,
#             "nome_do_produto": "Cafe",
#             "nome_da_empresa": "Cafe com leite",
#             "data_de_fabricacao": "2019-01-02",
#             "data_de_validade": "2023-02-09",
#             "numero_de_serie": "FR48",
#             "instrucoes_de_armazenamento": "instrucao"
#         }
#     ]
#     azul = "\033[32m"
#     verde = "\033[32m"
#     vermelho = "\033[31m"
#     fechar = "\033[0m"
#     frase1 =
#     frase2 =
#     frase3 = s
#     instance = ColoredReport(SimpleReport).generate(lista)

#     assert instance == (
#         verde + "Data de fabricação mais antiga:" + fechar
#         + " " + azul
#         + "2020-07-04" + fechar + "\n"
#         + verde + "Data de validade mais próxima:" + fechar
#         + " " + azul
#         + "2023-02-09" + fechar + "\n"
#         + verde + "Empresa com mais produtos:" + fechar
#         + " " + vermelho
#         + "Cafes Nature" + fechar + "\n"
#     )
