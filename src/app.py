from bigquery_client import BigQueryClient


B1 = BigQueryClient()
B1.create_dataset("opex_dashboard","US")
B1.create_table("secure-proxy-308710.opex_dashboard.cost_table")
