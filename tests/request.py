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

"""Testing avatar verification"""

with open('test1.jpg', 'rb') as f:
    im_bytes = f.read()        

im_b64 = base64.b64encode(im_bytes).decode("utf8")

user_avatar = {
    'phone_number': '1212231114',
    'avatar': im_b64,
}

response = requests.post(BASE + '/api/verification/avatar',  json=user_avatar)

print(response.json())

"""Testing full name verification"""

user_full_name = {
    'phone_number': '1212231114',
    'full_name': 'Hieu Pham',
}

response = requests.post(BASE + '/api/verification/full-name',  json=user_full_name)

print(response.json())

"""Testing date of birth verification"""

user_date_of_birth = {
    'phone_number': '1212231114',
    'date_of_birth': '01/01/2000',
}

response = requests.post(BASE + '/api/verification/date-of-birth',  json=user_date_of_birth)

print(response.json())

"""Testing gender verification"""

user_gender = {
    'phone_number': '1212231114',
    'gender': 'MALE',
}

response = requests.post(BASE + '/api/verification/gender',  json=user_gender)

print(response.json())

"""Testing singles skill verification"""

user_singles_skill = {
    'phone_number': '1212231114',
    'singles_skill': 1,
}

response = requests.post(BASE + '/api/verification/singles-skill',  json=user_singles_skill)

print(response.json())

"""Testing doubles skill verification"""

user_doubles_skill = {
    'phone_number': '1212231114',
    'doubles_skill': 10,
}

response = requests.post(BASE + '/api/verification/doubles-skill',  json=user_doubles_skill)

print(response.json())