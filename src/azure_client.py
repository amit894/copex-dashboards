from azure.mgmt.resource import ResourceManagementClient
from azure.identity import AzureCliCredential
import os

class AzureClient():
    def __init__(self,subscription_id):
        self.subscription_id=subscription_id

    def authenticate(self):
        self.credential = AzureCliCredential()

    def set_resource_client(self):
        self.resource_client = ResourceManagementClient(self.credential, self.subscription_id)



    def create_resource_group(self,rg_name,location):
        rg_result = self.resource_client.resource_groups.create_or_update(
    "PythonAzureExample-rg",
    {
        "location": "centralus"
    }
)
