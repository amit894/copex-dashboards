from rest_client import RestClient
import json

class AzureClient():
    def __init__(self,subscription_id):
        self.subscription_id=subscription_id
        self.authenticate_url="https://login.microsoftonline.com/8f12c261-6dbf-47c3-918f-1d15198a3b3b/oauth2/token"
        self.creds_file="../resources/cost/azure/creds.json"
        self.management_url="https://management.azure.com/subscriptions/8b207ff4-64b0-4488-9353-aebe1d29be77/"

    def authenticate(self):
        f1 = open(self.creds_file)
        request_data = json.load(f1)
        response=RestClient.post_api_without_headers(self.authenticate_url,request_data)
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
        headers = {"Authorization": self.access_token,"Content-Type":"application/json"}
        payload = json.dumps({
          "type": "Usage",
          "timeframe": "TheLastMonth",
          "dataset": {
            "granularity": "Daily",
            "aggregation": {
              "totalCost": {
                "name": "PreTaxCost",
                "function": "Sum"
              }
            },
            "grouping": [
              {
                "type": "Dimension",
                "name": "ResourceGroup"
              }
            ]
          }
        })
        request_url=self.management_url+"/resourceGroups/"+resource_group+"/providers/Microsoft.CostManagement/query?api-version=2021-10-01"
        response=RestClient.post_api(request_url,payload,headers)
        return response["properties"]["rows"]
