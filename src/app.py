from google.cloud import bigquery
from google.oauth2 import service_account

client = bigquery.Client()

for project in client.list_projects():
        print(project.project_id)
