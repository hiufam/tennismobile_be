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

"""Testing verification"""

with open('test1.jpg', 'rb') as f:
    im_bytes = f.read()        

im_b64 = base64.b64encode(im_bytes).decode("utf8")

user_profile = {
    'phone_number': '1212231114',
    'full_name': 'Hieu Pham',
    'date_of_birth': '01/01/2000',
    'gender': 'MALE',
    'singles_skill': 1,
    'doubles_skill': 10,
    'avatar': im_b64,
}

response = requests.post(BASE + '/api/verification/user-profile',  json=user_profile)

print(response.json())