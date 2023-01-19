from django.test import TestCase
from django.test import RequestFactory
# import requests
import json

class ViewsTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.auth_headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Key': 'Token dff6b811d3e70ac52a55f356b72e03b5566955b6'
            }
        self.save_investment_url = 'http://127.0.0.1:8000/blog/request_check'    

    def tearDown(self):
        pass   

    def setup_request(self, request):
        pass  

    # def test_wrong_http_method(self):
    #     data = {
    #         "amount": 50000,
    #         "productId":8,
    #         "FIPEndDate":"28/10/2023",
    #         "maturityAmount":55500,
    #         # This field is not required, if we use this need to make changes in function also
    #         "userName": "fceps7381d@gmail.com"
    #     }
    #     response = requests.request('GET',self.save_investment_url, headers=self.auth_headers, data=data)
    #     self.assertEquals(response.status_code, 200)


    # def test_input_invalid_data(self):
    #     data = {}
    #     response = requests.request('POST',self.save_investment_url, headers=self.auth_headers, data=data)
    #     self.assertEquals(response.status_code, 200)
    #     print("started")
    
    # def test_wrong_datatype(self):
    #     data = {
    #         "amount": 50000,
    #         "productId":"8", # This is actually need to send int but sending string
    #         "FIPEndDate":"28/10/2023",
    #         "maturityAmount":55500,
    #         # This field is not required, if we use this need to make changes in function also
    #         "userName": "fceps7381d@gmail.com"
    #     }
    #     response = requests.request('POST',self.save_investment_url, headers=self.auth_headers, data=data)
    #     self.assertEquals(response.status_code, 200)

    # def test_more_amount_than_userBalance(self):
    #     data = {
    #         "amount": 800005, # Actually user balance is 800002 but giving more than user balance like 800005
    #         "productId":8,
    #         "FIPEndDate":"28/10/2023",
    #         "maturityAmount":55500,
    #         # This field is not required, if we use this need to make changes in function also
    #         "userName": "fceps7381d@gmail.com"
    #     }
    #     response = requests.request('POST',self.save_investment_url, headers=self.auth_headers, data=data)
    #     self.assertEquals(response.status_code, 200)

    def test_input_valid_data(self):
        data = {
            "amount": 50000,
            "productId":8, 
            "FIPEndDate":"28/10/2023",
            "maturityAmount":55500,
            "userName": "fceps7381d@gmail.com" }
        data = json.dumps(data)        
        response = self.client.post('http://127.0.0.1:8000/blog/request_check',headers=self.auth_headers,data=data)
        print("response",response.__dict__)
        self.assertEquals(response.status_code, 200)    




        
