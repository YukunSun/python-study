# -*- coding: utf-8 -*-
from urllib import request

# 查看网页内容
url = "http://baidu.com"
response = request.urlopen(url, timeout=2)
content = response.read().decode('utf-8')
print(content)

from urllib import parse

# post
data = bytes(parse.urlencode({'world': 'hello'}), encoding='utf8')
response2 = request.urlopen('http://httpbin.org/post', data=data, timeout=3)
content2 = response2.read().decode('utf-8')
print(content2)
