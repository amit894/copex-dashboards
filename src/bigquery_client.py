from google.cloud import bigquery
from google.oauth2 import service_account


class BigQueryClient():
    def __init__(self):
        pass

    def list_datasets(self,project=None):
        client = bigquery.Client(project=project)
        for dataset in client.list_datasets():
            print(dataset.dataset_id)

    def list_projects(self):
        client = bigquery.Client()
        for project in client.list_projects():
                print(project.project_id)

    def create_dataset(self,dataset_id, location, project=None):
        client = bigquery.Client(project=project)
        dataset = client.dataset(dataset_id)
        dataset.location = location
        dataset = client.create_dataset(bigquery.Dataset(dataset))

    def create_table(self,table_id,project=None):

        schema = [
            bigquery.SchemaField("last_updated_time", "TIMESTAMP", mode="REQUIRED"),
            bigquery.SchemaField("si_number", "INTEGER", mode="REQUIRED"),
            bigquery.SchemaField("domain_name", "STRING", mode="REQUIRED"),
            bigquery.SchemaField("cost_value", "NUMERIC", mode="REQUIRED"),
            bigquery.SchemaField("cost_date", "DATE", mode="REQUIRED"),
        ]
        client = bigquery.Client(project=project)
        table = bigquery.Table(table_id, schema=schema)
        table = client.create_table(table)
        print(
            "Created table {}.{}.{}".format(table.project, table.dataset_id, table.table_id)
        )
