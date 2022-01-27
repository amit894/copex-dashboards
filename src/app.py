from bigquery_client import BigQueryClient
from azure_client import AzureClient
from datetime import date
from data_aggregator import DataAggregator
from google.cloud import bigquery


A1= AzureClient("8b207ff4-64b0-4488-9353-aebe1d29be77")
A1.authenticate()
daily_cost_array=A1.get_resource_group_cost("NetworkWatcherRG")
daily_cost=DataAggregator.sum(daily_cost_array)


B1 = BigQueryClient()
B1.create_dataset("opex_dashboard","US")

usage_schema = [
    bigquery.SchemaField("last_updated_time", "TIMESTAMP", mode="REQUIRED"),
    bigquery.SchemaField("si_number", "INTEGER", mode="REQUIRED"),
    bigquery.SchemaField("domain_name", "STRING", mode="REQUIRED"),
    bigquery.SchemaField("cost_value", "NUMERIC", mode="REQUIRED"),
    bigquery.SchemaField("cost_date", "DATE", mode="REQUIRED"),
]

budget_schema = [
    bigquery.SchemaField("last_updated_time", "TIMESTAMP", mode="REQUIRED"),
    bigquery.SchemaField("si_number", "INTEGER", mode="REQUIRED"),
    bigquery.SchemaField("domain_name", "STRING", mode="REQUIRED"),
    bigquery.SchemaField("monthly_budget_value", "NUMERIC", mode="REQUIRED"),
]
B1.create_table("secure-proxy-308710.opex_dashboard.usage_table",usage_schema)
B1.create_table("secure-proxy-308710.opex_dashboard.budget_table",budget_schema)


query = """
    SELECT *
    FROM `secure-proxy-308710.opex_dashboard.usage_table`
    LIMIT 10
"""
B1.client_query(query)

my_date = date(2022, 1, 20)
rows_to_insert=[( 1642662156, 1, u'Domain 1',daily_cost,my_date)]
B1.create_table_from_query(rows_to_insert,"opex_dashboard","usage_table")


query = """
    SELECT *
    FROM `secure-proxy-308710.opex_dashboard.usage_table`
    LIMIT 10
"""
B1.client_query(query)
