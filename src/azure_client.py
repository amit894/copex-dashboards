from rest_client import RestClient
import json

class AzureClient():
    def __init__(self,subscription_id):
        self.subscription_id=subscription_id

    def authenticate(self):
        request_url="https://login.microsoftonline.com/8f12c261-6dbf-47c3-918f-1d15198a3b3b/oauth2/token"
        f1 = open("../resources/cost/azure/identity_grant.json")
        request_data = json.load(f1)
        response=RestClient.post_api_without_headers(request_url,request_data)
        self.access_token="Bearer "+ response["access_token"]

    def set_resource_client(self):
        self.resource_client = ResourceManagementClient(self.credential, self.subscription_id)


    def create_resource_group(self,rg_name,location):
        rg_result = self.resource_client.resource_groups.create_or_update(
                    rg_name,
                    {
                        "location": location
                    }
        )

    def get_resource_group_cost(self,resource_group):
        headers = {"Authorization": self.access_token}
        request_url="https://management.azure.com/subscriptions/8b207ff4-64b0-4488-9353-aebe1d29be77/resourceGroups/NetworkWatcherRG/providers/Microsoft.CostManagement/query?api-version=2021-10-01"
        f1 = open("../resources/cost/azure/sample.json")
        request_data = json.load(f1)
        request_data["scope"]="/subscriptions/8b207ff4-64b0-4488-9353-aebe1d29be77/resourceGroups/NetworkWatcherRG"
        print(RestClient.post_api(request_url,request_data,headers))
