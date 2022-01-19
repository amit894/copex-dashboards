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
