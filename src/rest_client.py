import requests

class RestClient():
    def __init__(self):
        pass

    def get_api(self,request_url,pms):
        response=requests.get(request_url,params=pms)
        if response.status_code != 200:
            return "Error in Get call"
        else:
            return response.content

    def post_api(self,request_url,request_data):
        response=requests.post(request_url,data=request_data)
        if response.status_code != 200:
            return "Error in Get call"
        else:
            return response.content
