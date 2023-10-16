"""Test requests"""

import time
import requests
import base64
import json

BASE = 'http://127.0.0.1:5000/'

"""Testing registration"""

new_phone_number = {
    'phone_number': '1212231114',
}

response = requests.post(url=BASE + 'api/registration/phone-number', json=new_phone_number)

"""Testing authentication"""

response = requests.get(url=BASE + 'api/auth/otp/create', json=new_phone_number)

print(response.json())

my_otp = {
    'phone_number': '1212231114',
    'otp_code': response.json()['user']['registration_otp']
}

# time.sleep(2)

response = requests.post(url=BASE + 'api/auth/otp/verify', json=my_otp)

print(response.json())