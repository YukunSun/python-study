# -*- coding: utf-8 -*-
import requests

# get
url_1 = 'http://httpbin.org/get'
data = {'key': 'value', 'timeout': 5}
response = requests.get(url_1, data)
print(response.text)

# post
url_2 = 'http://httpbin.org/post'
data_2 = {'key': 'value'}
response2 = requests.post(url_2, data_2)
print(response2.text)
