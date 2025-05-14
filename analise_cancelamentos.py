import pandas as pd
import plotly.express as px

# 1- Importar base de dados
tabela = pd.read_csv("cancelamentos.csv")
# 2- Visualizar a base de dados
print(tabela.info())
# 3- Resolver problemas da base de dados
# 3-a) informações inúteis (eliminar customer_id e usuários vazios)
tabela = tabela.drop(columns="CustomerID") # Não tem relevância na análise
# 3-c) informações vazias
tabela = tabela.dropna() #Elimina informações vazias
print(tabela.info())
# Filtro para mulheres
# tabela_filtrada = tabela[tabela["sexo"] != "Male"]
# 3-b) informações no formato errado
# 4- Análise Inicial (quantos clientes cancelaram, e % de clientes)
print(tabela["cancelou"].value_counts(normalize=True).map("{:.1%}".format))
# # 5- Análise detalhada (causas de cancelamento comparadas)
# # Entender como cada coluna impacta no cancelamento do cliente (criando gráficos)
for coluna in tabela.columns:
#     #cria o gráfico
    grafico = px.histogram(tabela, x="cancelou", color=coluna, text_auto=True,histnorm="percent")
#     #exibe o gráfico
    grafico.show()
#
# # 66% das mulheres cancelaram
    # melhorar ambiente para as mulheres
# # todos os clientes acima de 50 cancelaram
#     # criar rotinas para pessoas 50+
# # todos os clientes do contrato mensal cancelaram
#     # dar desconto nos outros contratos
# # todos os clientes que ligaram > 4x cancelaram
#     # criar alerta quando o cliente ligar 3ªx
# # todos os clientes que atrasaram mais de 20 dias no pagamento, cancelaram
#     # ligar alerta pro time de cobrança qnd o cliente bater 10 dias de atraso
#
# # olhar base excluindo os dados de ligação
# tabela = tabela[tabela["ligacoes_callcenter"]<=4]
# # olhar a base excluindo os dias de atraso
# tabela = tabela[tabela["dias_atraso"]<=20]
# # olhar a tabela excluindo os contratos mensais
# tabela = tabela[tabela["duracao_contrato"]!="Monthly"]
# # olhar a tabela excluindo pessoas acima de 50 anos
# tabela = tabela[tabela["idade"]<50]
# print(tabela["cancelou"].value_counts(normalize=True))
