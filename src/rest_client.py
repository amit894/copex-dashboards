import requests

class RestClient():
    def __init__(self):
        pass

    @staticmethod
    def get_api(request_url,pms):
        response=requests.get(request_url,params=pms)
        if response.status_code != 200:
            print(response.status_code)
            return "Error in Get call"
        else:
            return response.json()

    @staticmethod
    def post_api(request_url,request_data,headers):
        response=requests.post(request_url,data=request_data,headers=headers)
        if response.status_code != 200:
            print(response.content)
            return "Error in Post call"
        else:
            return response.json()

    @staticmethod
    def post_api_without_headers(request_url,request_data):
        response=requests.post(request_url,data=request_data)
        if response.status_code != 200:
            print(response.content)
            return "Error in Post call"
        else:
            return response.json()
