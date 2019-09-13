import requests
import json

reg_url = "https://exercise.api.rebiton.com/auth/register"
login_url = "https://exercise.api.rebiton.com/auth/login"
user_url = "https://exercise.api.rebiton.com/user"


class Helper:
    def registraion(self, data):
        try:
            # sending post request and saving response as response object
            headers = {'Content-type': 'application/json'}
            response_data = requests.post(url=reg_url, data=json.dumps(data), headers=headers)
            if response_data.status_code in range(200, 300):
                return True
            return False
        except:
            return False

    def login(self, data):
        try:
            r = requests.post(url=login_url, data=data)
            response_data = r.json()
            success_data = response_data["data"]
            return success_data["token"]
        except:
            return False

    def users(self, token):
        try:
            tok = "Bearer " + token
            response_data = requests.get(user_url, headers={'Authorization': tok})
            user_data = response_data.json()
            return user_data["data"]
        except:
            return None


"""
# api-endpoint 
URL = "http://maps.googleapis.com/maps/api/geocode/json"
  
# location given here 
location = "delhi technological university"
  
# defining a params dict for the parameters to be sent to the API 
PARAMS = {'address':location} 
  
# sending get request and saving the response as response object 
r = requests.get(url = URL, params = PARAMS) 
  
# extracting data in json format 
data = r.json() 


"""
