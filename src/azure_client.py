from rest_client import RestClient
import json

class AzureClient():
    def __init__(self,subscription_id):
        self.subscription_id=subscription_id

    def authenticate(self):
        self.credential = AzureCliCredential()

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
        headers = {"Content-Type": "application/json","Authorization": "amit"}
        request_url="https://management.azure.com//subscriptions/8b207ff4-64b0-4488-9353-aebe1d29be77/resourceGroups/NetworkWatcherRG/providers/Microsoft.CostManagement/query?api-version=2021-10-01"
        f1 = open("../resources/cost/azure/sample.json")
        request_data = json.load(f1)
        print(RestClient.post_api(request_url,request_data,headers))
