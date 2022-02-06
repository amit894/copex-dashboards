from rest_client import RestClient
import json
from requests.auth import HTTPBasicAuth


class ServiceNowClient():
    def __init__(self,url):
        self.url=url
        self.creds_file="../resources/opex/servicenow/creds.json"

    def autheticate(self,username,password):
        creds = HTTPBasicAuth(username,password)
        return creds


S1=ServiceNowClient("https://dev84921.service-now.com/")
