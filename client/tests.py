from django.test import TestCase

# Create your tests here.
import requests, pprint
response = requests.get('http://localhost/client/SysInfo?action=listUserData')
pprint.pprint(response.json())

payload = {
    'action':'addUserData',
    'data':{
        'os':'Windows-10-10.0.18362-SP0',
        'compiler': 'MSC v.1900 64 bit (AMD64)',
        'cpuArch': 'Intel64 Family 6 Model 142 Stepping 11, GenuineIntel'
    }
}

response = requests.post('http://localhost/client/SysInfo',json=payload)
pprint.pprint(response.json())

response = requests.get('http://localhost/client/SysInfo?action=listUserData')
pprint.pprint(response.json())