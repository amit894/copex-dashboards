from bigquery_client import BigQueryClient
from azure_client import AzureClient
from datetime import date



A1= AzureClient("8b207ff4-64b0-4488-9353-aebe1d29be77")
A1.authenticate()
daily_cost=A1.get_resource_group_cost("NetworkWatcherRG")


B1 = BigQueryClient()
B1.create_dataset("opex_dashboard","US")
B1.create_table("secure-proxy-308710.opex_dashboard.cost_table")

query = """
    SELECT *
    FROM `secure-proxy-308710.opex_dashboard.cost_table`
    LIMIT 10
"""
B1.client_query(query)

my_date = date(2022, 1, 20)
rows_to_insert=[( 1642662156, 1, u'Domain 1',daily_cost,my_date)]
B1.create_table_from_query(rows_to_insert,"opex_dashboard","cost_table")


query = """
    SELECT *
    FROM `secure-proxy-308710.opex_dashboard.cost_table`
    LIMIT 10
"""
B1.client_query(query)
