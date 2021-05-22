import requests
import json 

from decouple import config

API_URL_SANDBOX = 'https://www.billplz.com/api/'
BILLPLZ_API_KEY = config('BILLPLZ_API_KEY')

def create_bill(collection_id, mobile, amount, name, description, callback_url, redirect_url, 
    reference_1_label, reference_1, reference_2_label, reference_2):

    url = API_URL_SANDBOX + '/v3/bills'
    data_json = {
        'collection_id': collection_id,
        'mobile': mobile,
        'amount': amount,
        'name': name,
        'description': description,
        'callback_url': callback_url,
        'redirect_url': redirect_url,
        'reference_1_label': reference_1_label,
        'reference_1': reference_1,
        'reference_2_label': reference_2_label,
        'reference_2': reference_2,        
    }   
    req = requests.post(url, data=data_json, auth=(BILLPLZ_API_KEY,BILLPLZ_API_KEY))
    if req.status_code == 200:
        return json.loads(req.content)
    else:
        print(req.status_code)