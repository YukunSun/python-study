# -*- coding: utf-8 -*-
import requests
import re

# 抓取图片

url = 'http://www.cnu.cc/inspirationPage/recent-226'
content = requests.get(url).text
# <img src="http://img.cnu.cc/uploads/images/flow/1909/12/eb682b96fefa372bae04c816d5547cd7.jpg?width=1000&amp;height=667" alt="美丽大自然 | Zack Seckler航拍作品">
pattern = re.compile(r'<img src="(.*?)" alt="(.*?)">')
results = re.findall(pattern, content)

for result in results:
    print(result[0], result[1])
