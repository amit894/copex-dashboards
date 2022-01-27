from google.cloud import bigquery
from google.oauth2 import service_account


class BigQueryClient():
    def __init__(self,project=None):
        self.client = bigquery.Client(project=project)

    def list_datasets(self,project=None):
        for dataset in self.client.list_datasets():
            print(dataset.dataset_id)

    def list_projects(self):
        client = bigquery.Client()
        for project in self.client.list_projects():
                print(project.project_id)

    def create_dataset(self,dataset_id, location, project=None):
        dataset = self.client.dataset(dataset_id)
        dataset.location = location
        dataset = self.client.create_dataset(bigquery.Dataset(dataset))

    def create_table(self,table_id,schema,project=None):
        table = bigquery.Table(table_id, schema=schema)
        table = self.client.create_table(table)
        print(
            "Created table {}.{}.{}".format(table.project, table.dataset_id, table.table_id)
        )

    def client_query(self,query):
        query_job = self.client.query(query)

        print("The query data:")
        for row in query_job:
            print(row)


    def create_table_from_query(self,rows_to_insert,dataset_name="DATASET", table_name="TABLE"):

        dataset_ref = self.client.dataset(dataset_name)
        table_ref = dataset_ref.table(table_name)
        table = self.client.get_table(table_ref)


        errors = self.client.insert_rows(table, rows_to_insert)
        print(errors)
        #assert errors == []
